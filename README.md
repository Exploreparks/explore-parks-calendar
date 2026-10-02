# BookDay Parks: park booking reminders (test site)

A static site for GitHub Pages. It gives you free calendar (.ics) files with reminders 1 day and 15 minutes before campsite and permit windows open at 22 national parks. It is a reminder tool only. It does not book anything. Bookings happen on Recreation.gov or the park's own page.

- Rules, dates and sources for each park live in `data/parks.json`. Dates change, so always verify on the official NPS or Recreation.gov page.
- Big Bend (`ics/big-bend.ics`) is published. It is one repeating reminder on the 1st of each month at 9:00 AM Central for Chisos Basin Campground and backcountry permit windows. The Chisos Basin release time was checked on Recreation.gov on 2026-10-01.
- The combined all-parks download is still held back until it is checked against official sources.
- Several parks use a placeholder "check the booking rules" reminder tagged [TIME UNVERIFIED]. Treat those times as placeholders.

## Sign-up forms
Both forms on `index.html` post to Formspree endpoint `xoevzrvp`. The old `YOUR_FORM_ID` placeholder is gone, but nobody has confirmed yet that `xoevzrvp` is a live form on Matt's Formspree account. To confirm, submit one test email from the live page and check that it arrives in Formspree. The hidden `list` field (`free-updates` or `paid-waitlist-15`) tells the two forms apart.
