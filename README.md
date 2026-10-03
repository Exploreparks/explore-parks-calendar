# Angels Landing Reservations (free)

Free page and calendar reminders for hiking Angels Landing in Zion in March 2027: permit lottery link, campsite booking windows, maps, and a mini brochure. Live page: https://exploreparks.github.io/explore-parks-calendar/zion/

A GitHub Action (`.github/workflows/angels-landing-lottery.yml`) checks the NPS page every day. When the spring 2027 lottery dates are posted or the lottery opens, it updates `zion/status.json` (which the page shows at the top) and opens a GitHub issue. It is a reminder tool only and never books anything; permits are applied for on Recreation.gov. Always verify dates on the official NPS page.

# BookDay Parks: park booking reminders (test site)

A static site for GitHub Pages. It gives you free calendar (.ics) files with reminders 1 day and 15 minutes before campsite and permit windows open at 22 national parks. It is a reminder tool only. It does not book anything. Bookings happen on Recreation.gov or the park's own page.

- Rules, dates and sources for each park live in `data/parks.json`. Dates change, so always verify on the official NPS or Recreation.gov page.
- Big Bend (`ics/big-bend.ics`) is published. It is one repeating reminder on the 1st of each month at 9:00 AM Central for Chisos Basin Campground and backcountry permit windows. The Chisos Basin release time was checked on Recreation.gov on 2026-10-01.
- The combined all-parks download is still held back until it is checked against official sources.
- Several parks use a placeholder "check the booking rules" reminder tagged [TIME UNVERIFIED]. Treat those times as placeholders.

## Sign-up forms
Both forms on `index.html` post to Formspree endpoint `xoevzrvp`. The old `YOUR_FORM_ID` placeholder is gone, but nobody has confirmed yet that `xoevzrvp` is a live form on Matt's Formspree account. To confirm, submit one test email from the live page and check that it arrives in Formspree. The hidden `list` field (`free-updates` or `paid-waitlist-15`) tells the two forms apart.
