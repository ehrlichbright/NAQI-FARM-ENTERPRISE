# NAQI FARM ENTERPRISE website

A fast, mobile-first static website (plain HTML/CSS/JS, no frameworks). Works on any static host.

## Pages
| File | Purpose / target search |
|---|---|
| `index.html` | Home: "Pay for the oil, not the bottle", how it works, products, who we serve, delivery, FAQs |
| `vegetable-oil.html` | Landing page for "Kings vegetable oil / vegetable oil by the litre in Lagos" (good for Google Ads) |
| `frozen-foods.html` | Landing page for "frozen fish and chicken by the carton in Lagos" |
| `about.html` | Story, CAC number, founding date, team |
| `blog/` | Blog: 3 starter guides (oil by the litre, what Olein/Kings oil is, storing frozen fish & chicken) |
| `contact.html` | Order form (opens WhatsApp with the order pre-written), phone, map |
| `404.html`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `favicon.svg` | SEO and housekeeping |

Every page has a WhatsApp button, click-to-call, a mobile sticky Call/WhatsApp bar, SEO titles and descriptions,
Open Graph share image, and Google structured data (LocalBusiness, FAQ, breadcrumbs).

## Before going live (checklist)
1. **Domain:** all canonical/sitemap URLs use `https://www.naqifarmenterprise.com`. If your domain is different,
   find and replace that text in every file (or edit `SITE` in `build.py` and run `python3 build.py .`).
2. **Facebook link:** currently a Facebook search link. Replace `FB = ...` in `build.py` (or the links in the HTML)
   with your exact page URL, e.g. `https://www.facebook.com/yourpage`.
3. **Team photos:** save square photos as
   `assets/img/team/abiodun-giwa.jpg`, `kafilat-giwa.jpg`, `yunusa-bakare.jpg`, `jubril-balogun.jpg`.
   They show automatically; until then initials are displayed.
4. **Team bios:** the bios in `about.html` are short role-based drafts. Please confirm or send the real ones.
5. **Real photos (strongly recommended):** the depot, the tanker, the meter filling a keg, frozen cartons.
   Real photos convert far better than illustrations.
6. **Tracking for paid ads:** open `assets/js/main.js` and paste your IDs into `CONFIG`
   (`ga4MeasurementId`, `googleAdsId` + `googleAdsLeadLabel`, `metaPixelId`). Every WhatsApp/phone click is then
   reported as a lead to Google Analytics, Google Ads and the Meta Pixel.
7. **Opening hours:** not shown yet. Send them and they can be added to the site and Google data.

## Adding a blog post
Posts live in `blog_posts.py`. Copy an existing entry, change the text, then run `python3 build.py .` from this folder.
The blog index, homepage teaser, sitemap and Google data update automatically.

**Next post ideas (one or two a month is enough):**
- How many litres are in a keg or a drum? Measuring oil the honest way
- Vegetable oil for restaurants: how much does a busy kitchen use a week?
- How to start an oil retail business in your market (buying at depot level)
- Croaker, mackerel, titus: choosing frozen fish for your menu (only types you actually stock)
- Frozen chicken cuts explained for caterers and party cooks
- Delivery from Mushin to [area]: what to know (one post per area you deliver to often)

## Editing
Edit the HTML files directly for small text changes. For changes to the header/footer on every page,
edit `build.py` and run `python3 build.py .` from this folder to regenerate all pages.

## Hosting with your Google domain (free options)
- **Netlify / Cloudflare Pages / GitHub Pages:** push this folder to your GitHub repo, connect it, no build command,
  publish directory = this folder. Then add the DNS records they give you in your domain's DNS settings
  (Google Domains is now Squarespace Domains).
- After launch: add the site to **Google Search Console**, submit `sitemap.xml`, and create/verify a
  **Google Business Profile** for the depot address (the biggest win for local "near me" searches).
