---
name: add-umami-analytics
description: Add umami analytics plus automatic click/event tracking (every link and button) to any website. Creates a umami website project, injects the tracking script, and wires detailed event tracking that logs who clicks what. Defaults to Umami Cloud; targets a self-hosted instance via environment variables. Use when the user wants to add analytics, tracking, page-view stats, or per-element click/event logging to a site.
---

# Add Umami Analytics + Event Tracking

Adds privacy-focused [umami](https://umami.is) analytics to any website and layers on **automatic event tracking for every `<a>`, `<button>`, `role="button"`, and submit/button input** — no manual tagging. Event name is the element's readable label (e.g. `link: Resume`, `button: Contact`); `href`, `id`, text, and page path are stored as event properties.

## Configuration (environment)

The skill targets **Umami Cloud by default**. Point it at a self-hosted instance purely through environment variables — no specific server or website ID is baked into these files.

- **`UMAMI_SCRIPT_URL`** — the tracking script URL injected into pages. Defaults to `https://cloud.umami.is/script.js`. Set to your own instance's `/script.js` to self-host.
- **`UMAMI_REPO`** — *(self-hosted website creation)* path to a umami repo linked to its host (e.g. Vercel). When set, `create-website.sh` creates the website directly via the instance's Postgres DB.
- **`UMAMI_API_KEY`** / **`UMAMI_API_URL`** — *(cloud website creation)* Umami Cloud API key; `UMAMI_API_URL` defaults to `https://api.umami.is/v1`.

Resolve the script URL in shell as:
```bash
SCRIPT_URL="${UMAMI_SCRIPT_URL:-https://cloud.umami.is/script.js}"
```

## Fork protection (important)

Never hardcode a website ID directly into public source in a way that a fork keeps sending data to the original owner's analytics. Apply BOTH:

1. **`data-domains` guard** — add `data-domains="prod-hostname[,other-host]"` to the script tag. umami's tracker then only sends from those hostnames, so a clone deployed elsewhere sends nothing. This is the primary guard and works everywhere (including pure static sites).
2. **Website ID from an env var** — for projects with a build/env (Next.js, Vite, Astro…), read the ID from a public env var (e.g. `NEXT_PUBLIC_UMAMI_WEBSITE_ID`, `VITE_UMAMI_WEBSITE_ID`) rather than inlining it. A fork without that env var set collects nothing.

## Procedure

### 1. Get a website ID

- **If the site already has a umami snippet** (grep for `data-website-id`), reuse that ID to preserve historical continuity — only change the `src` to `$SCRIPT_URL`.
- **Otherwise create a website** and capture the printed UUID:
  ```bash
  bash scripts/create-website.sh "<name>" "<domain>"
  ```
  The script auto-selects a mode from the environment: self-hosted DB insert (`UMAMI_REPO` set), Umami Cloud API (`UMAMI_API_KEY` set), or — if neither — it prints instructions to create the website in the dashboard and copy its ID.

Store the ID in the project's env (see Fork protection), not inline, wherever the framework supports it.

### 2. Detect the project type

- **Next.js App Router** — `src/app/layout.tsx` (or `app/layout.tsx`)
- **Next.js Pages Router** — `pages/_app.tsx` / `pages/_document.tsx`
- **Vite / CRA / plain SPA** — root `index.html` (+ env via `import.meta.env`)
- **Static site / GitHub Pages** — each `index.html` (and other `*.html`)
- **Astro / SvelteKit / Nuxt** — the framework's root layout template

### 3. Inject tracking

**A. React / Next.js** (one listener survives SPA navigation):
1. Copy `assets/umami-events.tsx` into the components dir (match the import alias).
2. Add the umami script to the root layout `<head>` (Next.js: `next/script`, `strategy="afterInteractive"`), reading the ID from env and guarding by domain:
   ```tsx
   {process.env.NEXT_PUBLIC_UMAMI_WEBSITE_ID && (
     <Script
       src={process.env.NEXT_PUBLIC_UMAMI_SCRIPT_URL ?? "https://cloud.umami.is/script.js"}
       data-website-id={process.env.NEXT_PUBLIC_UMAMI_WEBSITE_ID}
       data-domains="PROD_HOSTNAME"
       strategy="afterInteractive"
     />
   )}
   ```
   Set `NEXT_PUBLIC_UMAMI_WEBSITE_ID` (and optionally `NEXT_PUBLIC_UMAMI_SCRIPT_URL`) in the host's env + local `.env`.
3. Import and mount `<UmamiEvents />` once in the layout body.

**B. Static HTML / non-React** — inject the block from `assets/umami-tracker.html` before `</head>` in every HTML entry file. Set `src` to `$SCRIPT_URL`, replace `WEBSITE_ID`, and set `data-domains` to the production hostname(s). (Pure static sites can't read env vars, so `data-domains` is the fork guard here.)

For Astro/Svelte/Nuxt, adapt the same two pieces (guarded script tag + inline IIFE listener) into the layout template, reading the ID from the framework's public env.

### 4. Verify (optional)

Send a synthetic event to the instance's `/api/send` (base = `$SCRIPT_URL`'s origin) and check for `200`:
```bash
BASE="$(dirname "${UMAMI_SCRIPT_URL:-https://cloud.umami.is/script.js}")"
curl -s -X POST "$BASE/api/send" -H 'Content-Type: application/json' -H 'User-Agent: Mozilla/5.0' \
  -d '{"type":"event","payload":{"website":"WEBSITE_ID","hostname":"DOMAIN","url":"/","title":"test","name":"button: verify","data":{"type":"button"}}}'
```
(Test rows — delete afterward if verifying against a real site.)

### 5. Commit

Follow the user's git workflow. Commit the injected files. **Only push if the user asked you to** — confirm push scope per repo.

## Notes

- Event names are truncated to 50 chars (umami's `event_name` limit); full text/href live in properties.
- The listener uses capture phase so clicks that call `stopPropagation` are still recorded.
- One umami "website" can span multiple hostnames; list them all in `data-domains`.
- View data by logging into your umami instance → the website → Events tab.
