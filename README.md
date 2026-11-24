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

## Case study funnels (Bill, Samantha, Jay)

`case-studies/<name>/` holds a 3-step funnel for each of Sophie's three case-study clients. The pages use the same colors, fonts and footer as the masterclass page.

| Step | File | What it is |
|---|---|---|
| 1 | `landing.html` | A "Client Testimonial" eyebrow, a headline about the client's marriage transformation, their case-study video (Voomly), a **Book a Call With My Team** button, the Featured In logos and a wall of client message screenshots with a second button |
| 2 | `booking.html` | The Calendly booking widget (Relationship Reset Call), what happens on the call, and a quote from the client |
| 3 | `confirmation.html` | Same layout as the VSL funnel confirmation page: "Your Call Is Scheduled" with a check-your-inbox note, Sophie's confirmation video (Wistia), client stories (the other two case studies, short client videos and the screenshot wall), About Sophie and the podcast. Each page leaves out its own client. |

Publish each page in GoHighLevel the same way as the masterclass page: one Custom Code element per funnel step.

### Before they go live
- **Link the steps.** Links between steps must be full live URLs; plain filenames like `booking.html` break inside GHL.
  - **Bill (done):** landing https://connect.sophieorozco.com/bill-landing-page → booking https://connect.sophieorozco.com/bill-call-booking → confirmation https://connect.sophieorozco.com/bill-confirmation
  - **Samantha and Jay (still to do):** their landing buttons still point to `booking.html` (marked `BOOKING_PAGE_URL`) and their booking pages to `confirmation.html` (`CONFIRMATION_PAGE_URL`). Send their live step URLs and they'll be wired the same way.
- **Calendly redirect.** The booking page sends people to the confirmation page itself once they book, so each funnel gets its own thank-you page. If the Calendly event type has its own "redirect after booking" setting turned on, turn it off. Bookings are tagged `utm_campaign=bill`, `samantha` or `jay`, so you can see in Calendly which funnel each one came from.
- **Confirmation video.** Sophie's confirmation video ("Sophie VSL v1") is the Wistia media `isodmrwjhc` on all 3 confirmation pages. To change the video, replace that ID in the 2 places it appears on each page (the `<head>` script and the `<wistia-player>` tag).
- **Tracking pixels.** Use the slot in each `<head>`. Fire the Schedule conversion on the confirmation pages.
- **Headline options.** The comment at the top of each landing page lists alternative headlines.
- **Permissions.** Each client must give written permission for their story and quotes to be used. All quotes come from machine transcripts (Bill: Ep 12, Samantha: YT-22, Jay: Ep 21), so check them against the audio.

