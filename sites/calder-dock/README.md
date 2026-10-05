# Calder Dock & Marine — website

Single-page site for a dock builder (placeholder business name, phone, email — edit `src/data.ts`).

- Preview locally: `npm install && npm run dev`
- Build for hosting: `npm run build` → upload the `dist/` folder to any static host (Netlify, Vercel, Cloudflare Pages, GoDaddy, etc.).
- Quote form: set `VITE_FORM_ENDPOINT` (e.g. a Formspree URL) before building so requests are emailed to the client. Without it the form only shows a thank-you message.
- Photos: AI-generated stand-ins hosted on Higgsfield's CDN; swap for real job photos in `src/data.ts`.
