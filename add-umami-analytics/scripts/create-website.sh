#!/usr/bin/env bash
# Create a website in the self-hosted umami fork and print its new website ID.
# Usage: create-website.sh "<name>" "<domain>"
# Requires: vercel CLI logged in; the umami repo linked to its Vercel project.
set -euo pipefail

NAME="${1:?usage: create-website.sh <name> <domain>}"
DOMAIN="${2:?usage: create-website.sh <name> <domain>}"
UMAMI_REPO="${UMAMI_REPO:-$HOME/Developer/umami}"

[ -d "$UMAMI_REPO" ] || { echo "umami repo not found at $UMAMI_REPO (set UMAMI_REPO)" >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

( cd "$UMAMI_REPO" && vercel env pull "$TMP/db.env" --environment=production --yes >/dev/null 2>&1 ) \
  || { echo "vercel env pull failed (is the CLI logged in and the repo linked?)" >&2; exit 1; }

DIRECT="$(grep -E '^DIRECT_DATABASE_URL=|^DATABASE_URL_UNPOOLED=' "$TMP/db.env" | head -1 | cut -d= -f2- | tr -d '"')"
[ -n "$DIRECT" ] || { echo "could not resolve a direct Postgres URL from Vercel env" >&2; exit 1; }

WID="$(psql "$DIRECT" -q -t -A -v ON_ERROR_STOP=1 -v nm="$NAME" -v dm="$DOMAIN" <<'SQL'
WITH admin AS (SELECT user_id FROM "user" WHERE role = 'admin' ORDER BY created_at LIMIT 1)
INSERT INTO website (website_id, name, domain, user_id, created_by, created_at)
SELECT gen_random_uuid(), :'nm', :'dm', admin.user_id, admin.user_id, now()
FROM admin
RETURNING website_id;
SQL
)"

[ -n "$WID" ] || { echo "insert returned no id" >&2; exit 1; }
echo "$WID"
