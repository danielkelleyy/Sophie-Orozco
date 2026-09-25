# Sophie Orozco

Funnel assets for Sophie Orozco Coaching.

## Masterclass registration page

`landing-page/landing.html` is the registration page for the free masterclass, "How to Become the Person Your Spouse Comes Back To."

It's a single self-contained HTML file (inline CSS, no build step). Sophie's hero and family photos are embedded directly in the file, so it renders on its own anywhere. The original photos are in `landing-page/images/` if you'd rather host them in the GoHighLevel Media Library and swap the `src` for faster loading.

### Publishing in GoHighLevel
1. Create a new page in your Funnel or Website and remove the default header, footer and theme.
2. Add a Custom Code / HTML element covering the full page.
3. Paste the entire contents of `landing.html` and publish.

### Before it goes live
Search the file for these and replace them:
- `REGISTRATION_FORM_ACTION_URL`: where the signup form posts. Or replace the whole `<form class="reg-form">` with your GHL form or webinar registration embed.
- Client Transformations videos are live Voomly embeds (same video IDs as Sophie's current page), so they play once the page is published. Press logos are done; white PNGs are in `landing-page/images/logos/`.
- The tracking pixel slot in `<head>`.
- Footer disclaimer text: to be replaced with the footer copy from Sophie's current landing page.
- Written releases for CJ and Bill must be on file before the page runs.
