---
name: add-umami-analytics
description: Add self-hosted umami analytics plus automatic click/event tracking (every link and button) to any website. Points at Aryan's umami fork (umami-psi-henna.vercel.app), creates a new website project, injects the tracking script, and wires detailed event tracking that logs who clicks what. Use when the user wants to add analytics, tracking, page-view stats, or per-element click/event logging to a site.
---

# Add Umami Analytics + Event Tracking

Adds privacy-focused analytics to any website using Aryan's **self-hosted umami fork** and layers on **automatic event tracking for every `<a>`, `<button>`, `role="button"`, and submit/button input** — no manual tagging. Event name is the element's readable label (e.g. `link: Resume`, `button: Contact`); `href`, `id`, text, and page path are stored as event properties.

## Constants

- **Umami instance:** `https://umami-psi-henna.vercel.app`
- **Script URL:** `https://umami-psi-henna.vercel.app/script.js`
- **Umami repo (for DB access):** `~/Developer/umami` (override with `UMAMI_REPO` env var)

## Procedure

### 1. Get a website ID

Every tracked site needs a umami `website-id`.

- **If the site already has a umami snippet** (grep the project for `data-website-id`), reuse that ID — this preserves historical continuity. Only change the script `src` to the instance above.
- **Otherwise create a new website** in the fork and capture the printed UUID:

  ```bash
  bash ~/.claude/skills/add-umami-analytics/scripts/create-website.sh "<name>" "<domain>"
  ```
  e.g. `create-website.sh "my-site" "my-site.github.io"` → prints a new website ID.
  (Requires the user to be logged into Vercel CLI; the script pulls the DB URL from the umami repo's Vercel project and inserts the website owned by the admin user.)

### 2. Detect the project type

Grep/inspect for how the site renders its HTML shell:

- **Next.js App Router** — `src/app/layout.tsx` (or `app/layout.tsx`)
- **Next.js Pages Router** — `pages/_app.tsx` or `pages/_document.tsx`
- **Vite / CRA / plain SPA** — root `index.html`
- **Static site / GitHub Pages / nerfies template** — each `index.html` (and other `*.html`)
- **Astro / SvelteKit / Nuxt** — the root layout template for the framework

### 3. Inject tracking

**A. React / Next.js projects** — use the client-component approach (survives SPA navigation with one listener):

1. Copy `assets/umami-events.tsx` into the project's components dir (e.g. `src/components/umami-events.tsx`). Match the project's import-alias convention.
2. Add the umami `<Script>` to the root layout `<head>` (Next.js: use `next/script` with `strategy="afterInteractive"`):
   ```tsx
   <Script src="https://umami-psi-henna.vercel.app/script.js" data-website-id="WEBSITE_ID" strategy="afterInteractive" />
   ```
3. Import and mount `<UmamiEvents />` once in the layout body.

**B. Static HTML / any non-React site** — inject the self-contained block from `assets/umami-tracker.html` (script tag + inline listener) immediately before `</head>` in every HTML entry file. Replace `WEBSITE_ID` with the ID from step 1.

For Vite/CRA where you control `index.html`, the static block works directly. For frameworks with a layout template (Astro/Svelte/Nuxt), adapt the same two pieces (script tag + the inline IIFE listener) into that template.

### 4. Verify

- Confirm the script `src` and `data-website-id` are correct.
- (Optional, proves ingestion) send a synthetic event and check it lands:
  ```bash
  curl -s -X POST https://umami-psi-henna.vercel.app/api/send \
    -H 'Content-Type: application/json' -H 'User-Agent: Mozilla/5.0' \
    -d '{"type":"event","payload":{"website":"WEBSITE_ID","hostname":"DOMAIN","url":"/","title":"test","name":"button: verify","data":{"type":"button"}}}'
  ```
  A `200` means the fork accepted it. (Remember these are test rows — delete afterward if verifying against a real site.)

### 5. Commit

Follow the user's git workflow. Commit the injected files (component + layout/HTML edits). **Only push if the user asked you to** — confirm push scope per repo.

## Notes

- Event names are truncated to 50 chars (umami's `event_name` limit); full text/href live in event properties.
- The listener uses capture phase so clicks that call `stopPropagation` are still recorded.
- One umami "website" can span multiple hostnames (umami records `hostname` per event); you don't need a separate ID per subdomain unless you want separate dashboards.
- To view data: log into `https://umami-psi-henna.vercel.app` → the website → Events tab.
