"use client";

import { useEffect } from "react";

// Fires a umami event for every click on a link, button, role=button, or
// submit/button input — no manual tagging needed. Event name is the element's
// readable label (e.g. "link: Resume"); full details go into event properties.
declare global {
  interface Window {
    umami?: { track: (name: string, data?: Record<string, unknown>) => void };
  }
}

const SELECTOR = 'a, button, [role="button"], input[type="submit"], input[type="button"]';

function labelFor(el: HTMLElement, isLink: boolean): string {
  const raw =
    el.getAttribute("aria-label") ||
    el.innerText ||
    (el as HTMLInputElement).value ||
    el.getAttribute("title") ||
    (isLink ? el.getAttribute("href") || "" : "") ||
    el.tagName.toLowerCase();
  return raw.replace(/\s+/g, " ").trim().slice(0, 40);
}

export function UmamiEvents() {
  useEffect(() => {
    function onClick(e: MouseEvent) {
      const target = e.target as HTMLElement | null;
      const el = target?.closest(SELECTOR) as HTMLElement | null;
      if (!el || !window.umami) return;

      const isLink = el.tagName === "A";
      const label = labelFor(el, isLink);
      const name = `${isLink ? "link" : "button"}: ${label}`.slice(0, 50);

      window.umami.track(name, {
        type: isLink ? "link" : "button",
        text: (el.innerText || (el as HTMLInputElement).value || "").replace(/\s+/g, " ").trim().slice(0, 200),
        href: isLink ? (el as HTMLAnchorElement).href : undefined,
        id: el.id || undefined,
        aria: el.getAttribute("aria-label") || undefined,
        path: window.location.pathname,
      });
    }

    // capture phase so we still record clicks that call stopPropagation
    document.addEventListener("click", onClick, true);
    return () => document.removeEventListener("click", onClick, true);
  }, []);

  return null;
}
