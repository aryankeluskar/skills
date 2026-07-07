#!/usr/bin/env bash
# Create a umami website and print its new website ID.
# Usage: create-website.sh "<name>" "<domain>"
#
# Mode is auto-selected from the environment:
#   Self-hosted : UMAMI_REPO -> path to a umami repo linked to its host (e.g. Vercel).
#                 Inserts the website directly via the instance's Postgres DB.
#   Cloud / API : UMAMI_API_KEY set. Creates the website via the umami API
#                 (UMAMI_API_URL, default https://api.umami.is/v1).
#   Neither     : prints dashboard instructions and exits 2 (create it manually).
set -euo pipefail

NAME="${1:?usage: create-website.sh <name> <domain>}"
DOMAIN="${2:?usage: create-website.sh <name> <domain>}"

# --- Self-hosted: insert via the instance's Postgres DB ---
if [ -n "${UMAMI_REPO:-}" ] && [ -d "${UMAMI_REPO}" ]; then
  TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
  ( cd "$UMAMI_REPO" && vercel env pull "$TMP/db.env" --environment=production --yes >/dev/null 2>&1 ) \
    || { echo "vercel env pull failed in $UMAMI_REPO (CLI logged in? repo linked?)" >&2; exit 1; }
  DIRECT="$(grep -E '^DIRECT_DATABASE_URL=|^DATABASE_URL_UNPOOLED=|^DATABASE_URL=' "$TMP/db.env" | head -1 | cut -d= -f2- | tr -d '"')"
  [ -n "$DIRECT" ] || { echo "no Postgres URL in $UMAMI_REPO Vercel env" >&2; exit 1; }
  psql "$DIRECT" -q -t -A -v ON_ERROR_STOP=1 -v nm="$NAME" -v dm="$DOMAIN" <<'SQL'
WITH admin AS (SELECT user_id FROM "user" WHERE role = 'admin' ORDER BY created_at LIMIT 1)
INSERT INTO website (website_id, name, domain, user_id, created_by, created_at)
SELECT gen_random_uuid(), :'nm', :'dm', admin.user_id, admin.user_id, now()
FROM admin
RETURNING website_id;
SQL
  exit 0
fi

# --- Cloud / API ---
if [ -n "${UMAMI_API_KEY:-}" ]; then
  API="${UMAMI_API_URL:-https://api.umami.is/v1}"
  curl -fsS -X POST "$API/websites" \
    -H "x-umami-api-key: $UMAMI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"$NAME\",\"domain\":\"$DOMAIN\"}" \
    | sed -n 's/.*"id":"\([0-9a-f-]\{36\}\)".*/\1/p' | head -1
  exit 0
fi

# --- Neither configured ---
cat >&2 <<'EOF'
No website-creation method configured. Either:
  - Self-hosted: export UMAMI_REPO=/path/to/umami (repo linked to its host), or
  - Cloud:       export UMAMI_API_KEY=<your umami cloud api key>
Otherwise create the website in the umami dashboard and copy its Website ID.
EOF
exit 2
