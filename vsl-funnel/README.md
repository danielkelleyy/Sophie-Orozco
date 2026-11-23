# Sophie Orozco VSL Funnel

Five pages, modeled on Josh Hudson's (Marriage Reset) funnel from the Competitors folder in Drive,
built with Sophie's brand palette, fonts and components from the masterclass page (`landing-page/landing.html`).

| # | Page | File | Josh reference |
|---|------|------|----------------|
| 1 | Opt-in (with popup form) | `optin.html` | Opt-In Page.png, Opt-In Form.png |
| 2 | Video (VSL) | `video.html` | video-page.png |
| 3 | Application (Typeform) | `application.html` | Application Page |
| 4 | Call booking | `book-call.html` | none in his folder, so it continues the application page layout |
| 5 | Confirmation | `confirmation.html` | callbookedconfirmationpage.png |

Flow: opt-in popup → video → "Book your call" → application (Typeform) → booking calendar → confirmation.

## Editing

- Edit the files in this folder. They share `funnel.css` and load photos from `landing-page/images/`, so you can open them straight in a browser to preview.
- Every placeholder is a dashed green box (`class="ph"`) or yellow highlighted text (`class="todo"`). Search for `ph"`, `todo` and `[` to find them all.
- Copy follows the intake voice and claims rules: no dashes, contractions, no outcome claims, no unverified numbers.

## Publishing in GoHighLevel

1. Run `python3 vsl-funnel/build.py`. It writes self-contained copies to `vsl-funnel/ghl-ready/` with the CSS and images inlined.
2. In GHL, create one funnel step per page, remove the default header, footer and theme, add a Custom Code / HTML element, and paste the matching `ghl-ready` file.

## Before it goes live

- **Page links:** buttons link to `video.html`, `application.html`, etc. Swap these for your GHL funnel step URLs.
- **Opt-in form:** replace `OPTIN_FORM_ACTION_URL` (or the whole `<form class="optin-form">`) with the GHL form. Set its redirect to the video page.
- **VSL:** paste the player embed into the `.video-frame` on `video.html` and delete the placeholder "Your training is playing" overlay if the player has its own.
- **Typeform (`hqoLrF3O`):** in Typeform, set "Redirect on completion" to the booking page URL. UTMs on the application page URL pass through to Typeform.
- **Calendar:** paste the GHL / Calendly / OnceHub embed into `book-call.html`. Set the confirmation redirect to the confirmation page.
- **Confirmation page:** pre-call video, meet-the-team video, pull quotes for Bill and Samantha, screenshot wall, one more FAQ. Client videos are the live Voomly embeds from the masterclass.
- **Opt-in page:** rating badge, training still photo, six client-win screenshots.
- **Everywhere:** support email in the footer, tracking pixels in `<head>`, logo if you want it instead of the text wordmark.
- Written releases must be on file for every client shown, and screenshots need names and faces redacted.
