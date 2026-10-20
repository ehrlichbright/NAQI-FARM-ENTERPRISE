"""Generates the NAQI FARM ENTERPRISE HTML pages with a shared header/footer."""
import json
import pathlib
import re
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from blog_posts import POSTS  # noqa: E402

OUT = pathlib.Path(sys.argv[1])
SITE = "https://www.naqifarmenterprise.com"  # replace with the real domain
PHONE_DISPLAY = "+234 906 843 1502"
PHONE_TEL = "+2349068431502"
WA = "2349068431502"
ADDRESS = "104, Ishaga Road, Idi-Araba, Mushin, Lagos"
IG = "https://www.instagram.com/naqifarmenterprise/"
FB = "https://www.facebook.com/search/top?q=NAQI%20FARM%20Enterprise"
CAC = "9353141"


def wa(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"


WA_GENERAL = wa("Hello NAQI FARM ENTERPRISE, I'd like today's price for Original Olein oil / frozen foods.")
WA_OIL = wa("Hello NAQI FARM ENTERPRISE, I'd like today's price per litre for Original Olein oil. My container size is: ")
WA_FROZEN = wa("Hello NAQI FARM ENTERPRISE, which frozen fish and chicken cartons do you have today, and at what price?")
WA_DELIVERY = wa("Hello NAQI FARM ENTERPRISE, I'd like to arrange delivery. My location is: ")

# ---------- Icons (inline SVG, stroke = currentColor) ----------
def icon(paths, fill=False):
    attrs = 'fill="currentColor"' if fill else 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg viewBox="0 0 24 24" {attrs} aria-hidden="true">{paths}</svg>'

I = {
    "wa": icon('<path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5h-.01a9.4 9.4 0 0 1-4.8-1.32l-.34-.2-3.57.94.95-3.48-.22-.36a9.38 9.38 0 0 1-1.44-5.02c0-5.2 4.23-9.43 9.44-9.43a9.37 9.37 0 0 1 6.67 2.77 9.37 9.37 0 0 1 2.76 6.67c0 5.2-4.24 9.43-9.44 9.43zm8.03-17.46A11.27 11.27 0 0 0 12.04.72C5.79.72.7 5.8.7 12.06c0 2 .52 3.95 1.52 5.67L.6 23.6l6.01-1.58a11.32 11.32 0 0 0 5.42 1.38h.01c6.25 0 11.34-5.09 11.34-11.34 0-3.03-1.18-5.88-3.32-8.02z"/>', fill=True),
    "phone": icon('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'),
    "pin": icon('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>'),
    "drop": icon('<path d="M12 2.7c-3.6 4.7-6.5 8.6-6.5 12.3a6.5 6.5 0 0 0 13 0c0-3.7-2.9-7.6-6.5-12.3z"/><path d="M9 15.5a3 3 0 0 0 3 3"/>'),
    "gauge": icon('<path d="M12 14l3.5-3.5"/><path d="M3.3 17a9 9 0 1 1 17.4 0"/><circle cx="12" cy="14" r="1.5"/>'),
    "truck": icon('<path d="M1 4h13v12H1z"/><path d="M14 9h4l4 4v3h-8z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="17.5" cy="18.5" r="2"/>'),
    "tanker": icon('<rect x="1.5" y="6" width="14" height="9" rx="4.5"/><path d="M15.5 10h3.5l3 3v2h-6.5"/><circle cx="5.5" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>'),
    "container": icon('<path d="M8 3h8v3H8z"/><path d="M6 6h12a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1z"/><path d="M5 11h14M5 16h14"/>'),
    "naira": icon('<path d="M6 20V4l12 16V4"/><path d="M3 10h18M3 14h18"/>'),
    "shield": icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    "snow": icon('<path d="M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1L19.1 4.9"/><path d="M9 4l3 2 3-2M9 20l3-2 3 2M4 9l2 3-2 3M20 9l-2 3 2 3"/>'),
    "box": icon('<path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>'),
    "store": icon('<path d="M3 9l1.5-5h15L21 9"/><path d="M3 9h18v2a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0z"/><path d="M5 13v8h14v-8"/><path d="M10 21v-5h4v5"/>'),
    "chef": icon('<path d="M6 13.9A4 4 0 0 1 7.6 6a5 5 0 0 1 8.8 0A4 4 0 0 1 18 13.9V20H6z"/><path d="M6 17h12"/>'),
    "bed": icon('<path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20"/><path d="M6 8v9"/>'),
    "cart": icon('<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>'),
    "users": icon('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>'),
    "home": icon('<path d="M3 10l9-7 9 7v11a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1z"/>'),
    "check": icon('<path d="M5 12.5l4.5 4.5L19 7.5"/>'),
    "menu": icon('<path d="M3 6h18M3 12h18M3 18h18"/>'),
    "ig": icon('<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>'),
    "fb": icon('<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8.5a.5.5 0 0 1 .5-.5z"/>'),
    "doc": icon('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    "calendar": icon('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
}

# ---------- Product illustrations ----------
ART_OIL = '''<svg viewBox="0 0 200 160" aria-hidden="true"><ellipse cx="100" cy="148" rx="70" ry="8" fill="#000" opacity=".08"/>
<rect x="52" y="34" width="96" height="112" rx="14" fill="#1a4d34"/><rect x="80" y="20" width="40" height="18" rx="5" fill="#123826"/>
<rect x="60" y="72" width="80" height="66" rx="8" fill="#f2b93b"/><rect x="60" y="72" width="80" height="12" fill="#ffd877" opacity=".8"/>
<path d="M100 92c-6 8-10 13-10 18a10 10 0 0 0 20 0c0-5-4-10-10-18z" fill="#fff7e0" opacity=".9"/>
<rect x="138" y="52" width="10" height="70" rx="5" fill="#0d2a1c" opacity=".35"/></svg>'''
ART_FISH = '''<svg viewBox="0 0 200 160" aria-hidden="true"><ellipse cx="100" cy="148" rx="74" ry="8" fill="#000" opacity=".08"/>
<rect x="34" y="70" width="132" height="74" rx="6" fill="#c9a26b"/><path d="M34 70l20-22h92l20 22z" fill="#dcbb86"/>
<rect x="34" y="96" width="132" height="10" fill="#2b6f8f" opacity=".85"/>
<path d="M60 58c14-14 46-16 66 0-20 15-52 14-66 0z" fill="#9ccde0"/><path d="M126 58l16-10v20z" fill="#7fb8cf"/><circle cx="72" cy="56" r="3" fill="#123826"/></svg>'''
ART_CHICKEN = '''<svg viewBox="0 0 200 160" aria-hidden="true"><ellipse cx="100" cy="148" rx="74" ry="8" fill="#000" opacity=".08"/>
<rect x="34" y="70" width="132" height="74" rx="6" fill="#c9a26b"/><path d="M34 70l20-22h92l20 22z" fill="#dcbb86"/>
<rect x="34" y="96" width="132" height="10" fill="#1a4d34" opacity=".85"/>
<path d="M84 64c-12-4-14-22 2-26 12-3 24 4 26 14l14 6c6-4 12 0 10 6s-8 4-10 2l-14 2c-6 6-18 0-28-4z" fill="#f2c39b"/></svg>'''

NAV = [
    ("index.html", "Home"),
    ("vegetable-oil.html", "Olein Oil"),
    ("frozen-foods.html", "Frozen Foods"),
    ("about.html", "About Us"),
    ("blog/index.html", "Blog"),
    ("contact.html", "Contact"),
]


def url_for(file):
    if file.endswith("index.html"):
        return f"{SITE}/{file[:-len('index.html')]}"
    return f"{SITE}/{file}"


def header(active):
    current = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{f}"{current if f == active else ""}>{label}</a></li>' for f, label in NAV
    )
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <span>Original, unadulterated Olein oil by the litre &middot; Frozen fish &amp; chicken by the carton</span>
  <span><span class="hide-sm">Orders: </span><a href="tel:{PHONE_TEL}" data-track="topbar">{PHONE_DISPLAY}</a></span>
</div></div>
<header class="site-header"><div class="container">
  <a class="brand" href="index.html" aria-label="NAQI FARM ENTERPRISE home">
    <img class="brand-logo" src="assets/img/logo.png" alt="NAQI FARM ENTERPRISE: Pure, fresh and healthy" width="342" height="300">
  </a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{I["menu"]}</button>
  <nav class="site-nav" id="site-nav" aria-label="Main">
    <ul>{items}</ul>
    <a class="btn btn-wa btn-sm" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="header">{I["wa"]} Order on WhatsApp</a>
  </nav>
</div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="container">
  <div class="footer-grid">
    <div>
      <a class="footer-logo" href="index.html"><img src="assets/img/logo.png" alt="NAQI FARM ENTERPRISE: Pure, fresh and healthy" width="342" height="300" loading="lazy"></a>
      <p class="tagline">Straight from the source. Measured in front of you.</p>
      <p>Original, unadulterated Olein oil without paying for the packaging, and frozen fish and chicken by the carton, for traders, kitchens and homes across Nigeria.</p>
      <div class="socials">
        <a href="{IG}" target="_blank" rel="noopener" aria-label="NAQI FARM ENTERPRISE on Instagram">{I["ig"]}</a>
        <a href="{FB}" target="_blank" rel="noopener" aria-label="NAQI FARM Enterprise on Facebook">{I["fb"]}</a>
        <a href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-track="footer-social">{I["wa"]}</a>
      </div>
    </div>
    <div><h4>Products</h4><ul>
      <li><a href="vegetable-oil.html">Original Olein oil by the litre</a></li>
      <li><a href="frozen-foods.html">Frozen fish (cartons)</a></li>
      <li><a href="frozen-foods.html">Frozen chicken (cartons)</a></li>
      <li><a href="contact.html#order">Request a price</a></li>
    </ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="about.html">Our story</a></li>
      <li><a href="about.html#team">Our team</a></li>
      <li><a href="index.html#how-it-works">How it works</a></li>
      <li><a href="index.html#faq">FAQs</a></li>
      <li><a href="blog/index.html">Blog &amp; guides</a></li>
    </ul></div>
    <div><h4>Visit &amp; order</h4><ul>
      <li>{ADDRESS}</li>
      <li><a href="tel:{PHONE_TEL}" data-track="footer">{PHONE_DISPLAY}</a></li>
      <li><a href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="footer">WhatsApp: {PHONE_DISPLAY}</a></li>
      <li>Instagram: <a href="{IG}" target="_blank" rel="noopener">@naqifarmenterprise</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <span>&copy; <span id="year">2026</span> NAQI FARM ENTERPRISE. CAC Reg. No. {CAC}.</span>
    <span>Lagos, Nigeria &middot; Serving buyers nationwide</span>
  </div>
</div></footer>
<a class="wa-float" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Order on WhatsApp" data-track="float">{I["wa"]}</a>
<div class="mobile-bar">
  <a class="btn btn-outline" href="tel:{PHONE_TEL}" data-track="mobile-bar">{I["phone"]} Call</a>
  <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="mobile-bar">{I["wa"]} WhatsApp order</a>
</div>
<script src="assets/js/main.js" defer></script>'''


BUSINESS = {
    "@type": ["LocalBusiness", "WholesaleStore"],
    "@id": SITE + "/#business",
    "name": "NAQI FARM ENTERPRISE",
    "url": SITE + "/",
    "logo": SITE + "/assets/img/logo.png",
    "image": SITE + "/assets/img/og-image.jpg",
    "description": "Lagos depot selling original, unadulterated Olein refined vegetable oil (popularly known as Kings oil) by the litre into customers' own containers through a metering system, plus frozen fish and chicken by the carton. Serving traders, restaurants, hotels, supermarkets and bulk buyers across Nigeria.",
    "telephone": PHONE_TEL,
    "foundingDate": "2023-05-13",
    "slogan": "Straight from the source. Measured in front of you.",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "104 Ishaga Road, Idi-Araba",
        "addressLocality": "Mushin",
        "addressRegion": "Lagos",
        "addressCountry": "NG",
    },
    "areaServed": {"@type": "Country", "name": "Nigeria"},
    "currenciesAccepted": "NGN",
    "founder": [{"@type": "Person", "name": "Abiodun Dehinde Giwa"}],
    "sameAs": [IG],
    "identifier": {"@type": "PropertyValue", "propertyID": "CAC Registration Number", "value": CAC},
}


def page(file, title, description, body, extra_schema=None, crumbs=None, nav_active=None, og_type="website"):
    graph = [BUSINESS, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "NAQI FARM ENTERPRISE", "publisher": {"@id": SITE + "/#business"}}]
    if crumbs:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": url_for(f)} for i, (f, n) in enumerate(crumbs)
            ],
        })
    if extra_schema:
        graph.extend(extra_schema)
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)
    canonical = url_for(file)
    html = f'''<!doctype html>
<html lang="en-NG" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#123826">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="NAQI FARM ENTERPRISE">
<meta property="og:locale" content="en_NG">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="NG-LA">
<meta name="geo.placename" content="Mushin, Lagos">
<link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=Montserrat:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<script type="application/ld+json">
{schema}
</script>
</head>
<body>
{header(nav_active or file)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    depth = file.count("/")
    if depth:
        # Pages in sub-folders: point relative links back to the site root.
        up = "../" * depth
        html = re.sub(r'(href|src)="(?!https?:|#|tel:|mailto:|/|\.\./|data:)', lambda m: f'{m.group(1)}="{up}', html)
    target = OUT / file
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def breadcrumb_html(crumbs):
    parts = []
    for i, (f, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<li aria-current="page">{n}</li>')
        else:
            parts.append(f'<li><a href="{f}">{n}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'


def faq_block(items):
    html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    schema = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items
        ],
    }
    return f'<div class="faq">{html}</div>', schema


def cta_band(heading="Ready to stop paying for packaging?", text="Send us your container size or carton quantity on WhatsApp and we will reply with today's price.", track="cta-band"):
    return f'''<section class="section"><div class="container"><div class="cta-band reveal">
  <span class="eyebrow">Get today's price</span>
  <h2>{heading}</h2>
  <p class="lead" style="color:#c4d8ca;max-width:620px;margin:0 auto">{text}</p>
  <div class="btn-row">
    <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="{track}">{I["wa"]} Chat on WhatsApp</a>
    <a class="btn btn-light" href="tel:{PHONE_TEL}" data-track="{track}">{I["phone"]} Call {PHONE_DISPLAY}</a>
  </div>
</div></div></section>'''


import datetime


def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def post_card(p):
    return f'''<article class="card post-card reveal">
  <span class="tag">{p["category"]}</span>
  <h3><a href="blog/{p["slug"]}.html">{p["title"][0].upper() + p["title"][1:]}</a></h3>
  <p>{p["excerpt"]}</p>
  <p class="post-meta"><time datetime="{p["date"]}">{nice_date(p["date"])}</time> &middot; {p["read_minutes"]} min read</p>
</article>'''


def blog_teaser():
    cards = "".join(post_card(p) for p in POSTS[:3])
    return f'''<section class="section section-alt" id="blog"><div class="container">
  <div class="section-head"><span class="eyebrow">Guides for buyers</span><h2>From the NAQI blog</h2>
  <p class="lead">Plain advice on buying oil and frozen food in Nigeria without overpaying.</p></div>
  <div class="grid grid-3">{cards}</div>
  <p style="margin-top:24px"><a class="btn btn-outline" href="blog/index.html">See all articles</a></p>
</div></section>'''


# ===================================================================
# HOME
# ===================================================================
HOME_FAQ = [
    ("What kind of vegetable oil do you sell?",
     "We sell Original Olein oil: refined Olein vegetable oil, popularly known as Kings oil. Our tanker brings it directly from the manufacturer to our depot in Lagos, with no middlemen in between."),
    ("Is your oil original and unadulterated?",
     "Yes. Our oil comes by tanker straight from the manufacturer into our depot tank and is metered directly into your container. It is never mixed, diluted or repackaged along the way, so what you take home is the same oil that left the manufacturer."),
    ("Why is your oil cheaper than bottled oil?",
     "Because you are not paying for a bottle, a label or packaging markup. You bring your own drum, keg or container, we fill it through our metering system, and you pay only for the oil."),
    ("How do I know I'm getting the exact quantity?",
     "Every fill goes through our metering system, in front of you. You see exactly how many litres go into your container, and you pay for exactly that."),
    ("Do you deliver?",
     "Yes. You can arrange your own transport, or we can arrange delivery for you on request. Delivery is charged separately from the price of the product. Send your location on WhatsApp for a delivery quote."),
    ("Do you sell outside Lagos?",
     "Yes. We are based in Lagos and serve market traders, restaurants, hotels, supermarkets and bulk buyers across Nigeria."),
    ("What frozen foods do you have?",
     "We sell frozen fish and chicken in a variety of types, packed in cartons and kept properly stored. Available types change, so message us on WhatsApp for what is in stock today."),
    ("How do I get today's price?",
     f"Prices move with the market, so we quote daily. Send a WhatsApp message or call {PHONE_DISPLAY} with your container size or carton quantity."),
]

faq_html, faq_schema = faq_block(HOME_FAQ)

home = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <div class="hero-badges">
        <span class="pill">{I["check"]} 100% original Olein</span>
        <span class="pill">{I["check"]} Unadulterated</span>
        <span class="pill">{I["check"]} Direct from manufacturer</span>
        <span class="pill">{I["check"]} Metered in front of you</span>
      </div>
      <h1>Original Olein oil.<br><em>Pay for the oil, not the bottle.</em></h1>
      <p class="lead">Pure, unadulterated Olein oil straight from the manufacturer, filled into your own drum, keg or container through our meter. Plus frozen fish and chicken by the carton. From our Lagos depot to traders, kitchens and homes across Nigeria.</p>
      <div class="btn-row">
        <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="hero">{I["wa"]} Get today's price</a>
        <a class="btn btn-light" href="#how-it-works">See how it works</a>
      </div>
      <p class="hero-note">Depot: {ADDRESS}</p>
    </div>
    <div class="hero-card reveal" aria-label="Illustration: oil metered into your container">
      <div class="meter">
        <div class="meter-label">Metered fill &middot; your container</div>
        <div class="meter-value">25.00<small>litres</small></div>
        <div class="meter-bar"><span></span></div>
      </div>
      <ul class="compare">
        <li><span>Bottle &amp; label</span><span class="no">You pay</span></li>
        <li><span>Packaging markup</span><span class="no">You pay</span></li>
        <li><span>Original Olein oil, measured exactly</span><span class="yes">You pay only this</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="trust" aria-label="Why buyers trust us">
  <div class="container">
    <div class="trust-item">{I["shield"]}<div><strong>Original &amp; unadulterated</strong><span>Never mixed or diluted</span></div></div>
    <div class="trust-item">{I["tanker"]}<div><strong>Tanker direct</strong><span>From manufacturer to depot</span></div></div>
    <div class="trust-item">{I["gauge"]}<div><strong>Metered fill</strong><span>See every litre</span></div></div>
    <div class="trust-item">{I["doc"]}<div><strong>CAC Reg. {CAC}</strong><span>Registered business</span></div></div>
  </div>
</section>

<section class="section" id="how-it-works">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">How it works</span>
      <h2>Honest measurement in three steps</h2>
      <p class="lead">No bottle, no label, no markup. Just original, unadulterated oil at a fair price.</p>
    </div>
    <div class="grid grid-3 steps">
      <div class="card step reveal"><span class="step-num">1</span><div class="icon-badge gold">{I["container"]}</div><h3>Bring your container</h3><p>Come with your own drum, keg or container, any size. Send us the size on WhatsApp first and we'll confirm today's price.</p></div>
      <div class="card step reveal"><span class="step-num">2</span><div class="icon-badge">{I["gauge"]}</div><h3>Watch the meter</h3><p>We fill it through our metering system in front of you. You see exactly how many litres you are getting.</p></div>
      <div class="card step reveal"><span class="step-num">3</span><div class="icon-badge">{I["naira"]}</div><h3>Pay for exactly that</h3><p>You pay only for the litres measured. Take it away with your own transport, or ask us to arrange delivery.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt" id="products">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What we sell</span>
      <h2>Kitchen staples, sold the fair way</h2>
      <p class="lead">One depot for your cooking oil and your frozen protein.</p>
    </div>
    <div class="grid grid-3">
      <article class="card product-card reveal">
        <div class="product-media oil">{ART_OIL}</div>
        <div class="product-body">
          <span class="tag">By the litre</span>
          <h3>Original Olein oil</h3>
          <p>Pure, unadulterated Olein oil (popularly known as Kings oil), brought by tanker straight from the manufacturer and metered into your own container. Any quantity, from a keg to a drum.</p>
          <div class="btn-row"><a class="btn btn-outline btn-sm" href="vegetable-oil.html">Learn more</a><a class="btn btn-wa btn-sm" href="{WA_OIL}" target="_blank" rel="noopener" data-track="product-oil">{I["wa"]} Price</a></div>
        </div>
      </article>
      <article class="card product-card reveal">
        <div class="product-media fish">{ART_FISH}</div>
        <div class="product-body">
          <span class="tag">By the carton</span>
          <h3>Frozen fish</h3>
          <p>A variety of fish types, packed in cartons and kept properly stored so it reaches your shop or kitchen the way it should.</p>
          <div class="btn-row"><a class="btn btn-outline btn-sm" href="frozen-foods.html">Learn more</a><a class="btn btn-wa btn-sm" href="{WA_FROZEN}" target="_blank" rel="noopener" data-track="product-fish">{I["wa"]} Price</a></div>
        </div>
      </article>
      <article class="card product-card reveal">
        <div class="product-media chicken">{ART_CHICKEN}</div>
        <div class="product-body">
          <span class="tag">By the carton</span>
          <h3>Frozen chicken</h3>
          <p>A range of chicken types in cartons, properly stored for restaurants, hotels, retailers and families buying in bulk.</p>
          <div class="btn-row"><a class="btn btn-outline btn-sm" href="frozen-foods.html">Learn more</a><a class="btn btn-wa btn-sm" href="{WA_FROZEN}" target="_blank" rel="noopener" data-track="product-chicken">{I["wa"]} Price</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Why NAQI</span>
      <p class="big-quote">Original, unadulterated Olein oil. <em>Exactly as it left the manufacturer.</em></p>
      <p class="lead">Oil that passes through many hands can be mixed, diluted or refilled before it reaches you. Ours doesn't. It comes by tanker straight from the manufacturer into our depot and is metered directly into your container, so your family, your customers and your kitchen get the original oil you paid for.</p>
      <p class="lead">And because you bring your own container, you stop paying for the bottle, the label and the packaging too.</p>
      <a class="btn btn-gold" href="about.html">Read our story</a>
    </div>
    <ul class="check-list reveal">
      <li><strong style="color:#fff">100% original Olein oil.</strong> Pure and unadulterated: never mixed, diluted or repackaged.</li>
      <li><strong style="color:#fff">No middlemen.</strong> Our tanker brings oil from the manufacturer straight to our depot.</li>
      <li><strong style="color:#fff">Nothing hidden.</strong> Every litre goes through the meter in front of you.</li>
      <li><strong style="color:#fff">No packaging markup.</strong> You bring the container; you pay for the oil.</li>
      <li><strong style="color:#fff">Properly stored frozen foods.</strong> Fish and chicken kept the way they should be.</li>
      <li><strong style="color:#fff">Flexible pickup or delivery.</strong> Your own transport, or delivery we arrange on request.</li>
    </ul>
  </div>
</section>

<section class="section" id="who-we-serve">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Who we serve</span>
      <h2>Built for people who buy food in volume</h2>
      <p class="lead">From one keg for the family to regular drums for a busy kitchen.</p>
    </div>
    <div class="grid grid-3">
      <div class="card audience reveal"><div class="icon-badge gold">{I["store"]}</div><div><h3>Market traders</h3><p>Buy at depot level, resell with a healthier margin.</p></div></div>
      <div class="card audience reveal"><div class="icon-badge">{I["chef"]}</div><div><h3>Restaurants &amp; caterers</h3><p>Steady supply of oil, fish and chicken for daily service.</p></div></div>
      <div class="card audience reveal"><div class="icon-badge ice">{I["bed"]}</div><div><h3>Hotels</h3><p>Bulk kitchen staples with honest, metered quantities.</p></div></div>
      <div class="card audience reveal"><div class="icon-badge">{I["cart"]}</div><div><h3>Supermarkets</h3><p>Frozen cartons and oil supply for your shelves and freezers.</p></div></div>
      <div class="card audience reveal"><div class="icon-badge gold">{I["users"]}</div><div><h3>Bulk buyers</h3><p>Large orders, sourced direct and measured exactly.</p></div></div>
      <div class="card audience reveal"><div class="icon-badge ice">{I["home"]}</div><div><h3>Families</h3><p>Bring your keg, stock up and stop paying for bottles.</p></div></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Pickup &amp; delivery</span>
      <h2>Wherever you are, get it there your way</h2>
      <p class="lead">Collect from our depot in Mushin, Lagos with your own transport, or ask us to arrange delivery for you.</p>
      <ul class="check-list">
        <li>Delivery is arranged on request</li>
        <li>Delivery is charged separately from the product price, so you always see both clearly</li>
        <li>Serving buyers in Lagos and across Nigeria</li>
      </ul>
      <a class="btn btn-wa" href="{WA_DELIVERY}" target="_blank" rel="noopener" data-track="delivery">{I["wa"]} Ask for a delivery quote</a>
    </div>
    <div class="card reveal">
      <div class="icon-badge gold">{I["pin"]}</div>
      <h3>Visit the depot</h3>
      <p>{ADDRESS}</p>
      <p class="muted">Call ahead to confirm stock and today's price before you set out.</p>
      <div class="btn-row">
        <a class="btn btn-outline btn-sm" href="https://www.google.com/maps/search/?api=1&amp;query={quote(ADDRESS + ', Nigeria')}" target="_blank" rel="noopener">Get directions</a>
        <a class="btn btn-outline btn-sm" href="tel:{PHONE_TEL}" data-track="depot-card">{I["phone"]} Call</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">FAQs</span>
      <h2>Questions buyers ask us</h2>
    </div>
    {faq_html}
  </div>
</section>

{blog_teaser()}

{cta_band(track="home-cta")}
'''

page(
    "index.html",
    "Original Olein Oil by the Litre & Frozen Foods, Lagos | NAQI FARM",
    "Buy original, unadulterated Olein oil (Kings oil) by the litre in Lagos, straight from the manufacturer. Bring your own container, watch it metered, pay only for the oil. Frozen fish & chicken too.",
    home,
    extra_schema=[faq_schema],
)

# ===================================================================
# VEGETABLE OIL
# ===================================================================
OIL_FAQ = [
    ("Is this the same as Kings oil?",
     "Yes. We sell Original Olein oil, the refined Olein vegetable oil popularly known as Kings oil, brought by our tanker directly from the manufacturer to our depot."),
    ("Is your Olein oil original and unadulterated?",
     "Yes. It goes from the manufacturer's tanker into our depot tank and is metered straight into your container. It is never mixed, diluted or repackaged, so you get the original oil exactly as it left the manufacturer."),
    ("What containers can I bring?",
     "Bring your own clean drum, keg or container. We fill it through our metering system so you see the exact quantity."),
    ("Is there a minimum quantity?",
     "Message us on WhatsApp with the quantity you need and we will confirm availability and price."),
    ("How much does a litre cost?",
     "Prices follow the market, so we quote daily. Send your container size on WhatsApp for today's price per litre."),
    ("Can you deliver oil to my shop or kitchen?",
     "Yes, on request. Delivery is charged separately from the oil. Share your location and quantity for a delivery quote."),
]
oil_faq_html, oil_faq_schema = faq_block(OIL_FAQ)
oil_crumbs = [("index.html", "Home"), ("vegetable-oil.html", "Original Olein Oil")]
oil = f'''
<section class="page-hero"><div class="container">
  {breadcrumb_html(oil_crumbs)}
  <h1>Original Olein oil, pure and unadulterated, by the litre in Lagos</h1>
  <p class="lead">Straight from the manufacturer, never mixed or diluted. Bring your own drum, keg or container, we fill it through our meter in front of you, and you pay for the oil, not the bottle, the label or the packaging.</p>
  <div class="btn-row" style="margin-top:24px">
    <a class="btn btn-wa" href="{WA_OIL}" target="_blank" rel="noopener" data-track="oil-hero">{I["wa"]} Get today's price per litre</a>
    <a class="btn btn-light" href="tel:{PHONE_TEL}" data-track="oil-hero">{I["phone"]} Call to order</a>
  </div>
</div></section>

<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">The product</span>
    <h2>Original Olein oil, exactly as it left the manufacturer</h2>
    <p>Our tanker brings Olein refined vegetable oil, popularly known as Kings oil, directly from the manufacturer to our depot in Mushin, Lagos. There are no middlemen in between, and no repackaging.</p>
    <p>That matters, because oil that passes through many hands can be mixed, diluted or refilled before it reaches you. Ours goes from the tanker to our tank to your container, so you get original, unadulterated oil for your family's meals and your customers' food.</p>
    <p>What you don't get is the cost of a bottle, a label and a retail markup on packaging.</p>
    <ul class="check-list">
      <li>100% original Olein oil, pure and unadulterated</li>
      <li>Delivered by tanker directly from the manufacturer</li>
      <li>Filled into your own container through a metering system</li>
      <li>You see the exact litres, and pay for exactly that</li>
      <li>Any quantity, from a family keg to drums for business</li>
    </ul>
  </div>
  <div class="card product-card reveal"><div class="product-media oil" style="aspect-ratio:4/3">{ART_OIL}</div></div>
</div></section>

<section class="section section-alt"><div class="container">
  <div class="section-head center"><span class="eyebrow">Where your money goes</span><h2>Bottled oil vs. metered oil</h2></div>
  <div class="grid grid-2">
    <div class="card reveal">
      <h3>Buying bottled at the market</h3>
      <ul class="check-list" style="opacity:.85">
        <li>Oil</li><li>Plastic bottle</li><li>Label and branding</li><li>Packaging markup through every reseller</li>
      </ul>
      <p class="muted mb-0">You pay for all of it, every time.</p>
    </div>
    <div class="card reveal" style="border-color:var(--gold-500)">
      <h3>Buying from NAQI FARM</h3>
      <ul class="check-list"><li>Original, unadulterated Olein oil</li><li>Measured exactly in front of you</li></ul>
      <p class="muted">Your container. Your quantity. Your fair price.</p>
      <a class="btn btn-wa btn-sm" href="{WA_OIL}" target="_blank" rel="noopener" data-track="oil-compare">{I["wa"]} Ask today's price</a>
    </div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Who buys our oil</span><h2>For resale, for the kitchen, for the home</h2></div>
  <div class="grid grid-4">
    <div class="card reveal"><div class="icon-badge gold">{I["store"]}</div><h3>Traders</h3><p>Buy at depot level for resale.</p></div>
    <div class="card reveal"><div class="icon-badge">{I["chef"]}</div><h3>Restaurants</h3><p>Steady supply for daily frying and cooking.</p></div>
    <div class="card reveal"><div class="icon-badge ice">{I["bed"]}</div><h3>Hotels &amp; caterers</h3><p>Bulk volumes, honestly measured.</p></div>
    <div class="card reveal"><div class="icon-badge">{I["home"]}</div><h3>Families</h3><p>Stock up with your own keg.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Vegetable oil FAQs</span><h2>Before you come to the depot</h2></div>
  {oil_faq_html}
</div></section>

{cta_band("Bring your container. We'll fill it.", "Tell us your container size on WhatsApp and we'll reply with today's price per litre.", "oil-cta")}
'''
page(
    "vegetable-oil.html",
    "Original Olein Oil (Kings Oil) by the Litre, Lagos | NAQI FARM",
    "Olein refined vegetable oil (Kings oil) direct from the manufacturer, metered into your own drum or keg at our Mushin, Lagos depot. Pay for the oil, not the packaging.",
    oil,
    extra_schema=[oil_faq_schema, {
        "@type": "Product",
        "name": "Original Olein oil (Kings oil), sold by the litre",
        "description": "Original, unadulterated Olein refined vegetable oil delivered by tanker from the manufacturer and metered into the customer's own container.",
        "category": "Vegetable oil",
        "brand": {"@type": "Brand", "name": "Kings"},
        "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "priceCurrency": "NGN", "seller": {"@id": SITE + "/#business"}, "areaServed": "NG"},
    }],
    crumbs=oil_crumbs,
)

# ===================================================================
# FROZEN FOODS
# ===================================================================
FROZEN_FAQ = [
    ("What types of fish and chicken do you have?",
     "We stock a variety of fish and chicken types. Availability changes, so message us on WhatsApp for what is in stock today."),
    ("Do you sell by the carton only?",
     "Our frozen foods are packed and sold in cartons. Tell us the quantity you need and we will confirm."),
    ("How are the frozen foods stored?",
     "Our fish and chicken are kept properly stored so they reach your shop or kitchen the way they should."),
    ("Can you deliver frozen cartons?",
     "Yes, on request. Delivery is charged separately from the product price. Share your location for a quote."),
]
frozen_faq_html, frozen_faq_schema = faq_block(FROZEN_FAQ)
frozen_crumbs = [("index.html", "Home"), ("frozen-foods.html", "Frozen Foods")]
frozen = f'''
<section class="page-hero"><div class="container">
  {breadcrumb_html(frozen_crumbs)}
  <h1>Frozen fish and chicken by the carton in Lagos</h1>
  <p class="lead">A variety of fish and chicken types, packed in cartons and kept properly stored, so it reaches your shop or kitchen the way it should.</p>
  <div class="btn-row" style="margin-top:24px">
    <a class="btn btn-wa" href="{WA_FROZEN}" target="_blank" rel="noopener" data-track="frozen-hero">{I["wa"]} See what's in stock today</a>
    <a class="btn btn-light" href="tel:{PHONE_TEL}" data-track="frozen-hero">{I["phone"]} Call to order</a>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="grid grid-2">
    <article class="card product-card reveal">
      <div class="product-media fish">{ART_FISH}</div>
      <div class="product-body">
        <span class="tag">Cartons</span>
        <h3>Frozen fish</h3>
        <p>Different fish types for homes, restaurants and retailers. Stock changes, so ask for today's list and prices.</p>
        <div class="btn-row"><a class="btn btn-wa btn-sm" href="{wa("Hello NAQI FARM ENTERPRISE, which frozen fish cartons do you have today, and at what price?")}" target="_blank" rel="noopener" data-track="frozen-fish">{I["wa"]} Ask about fish</a></div>
      </div>
    </article>
    <article class="card product-card reveal">
      <div class="product-media chicken">{ART_CHICKEN}</div>
      <div class="product-body">
        <span class="tag">Cartons</span>
        <h3>Frozen chicken</h3>
        <p>A range of chicken types for kitchens, hotels and shops buying in bulk. Ask for today's list and prices.</p>
        <div class="btn-row"><a class="btn btn-wa btn-sm" href="{wa("Hello NAQI FARM ENTERPRISE, which frozen chicken cartons do you have today, and at what price?")}" target="_blank" rel="noopener" data-track="frozen-chicken">{I["wa"]} Ask about chicken</a></div>
      </div>
    </article>
  </div>
</div></section>

<section class="section section-alt"><div class="container">
  <div class="section-head center"><span class="eyebrow">The NAQI standard</span><h2>The same honest thinking, applied to frozen food</h2></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="icon-badge ice">{I["snow"]}</div><h3>Properly stored</h3><p>Kept frozen the way it should be, from our depot until it leaves.</p></div>
    <div class="card reveal"><div class="icon-badge gold">{I["box"]}</div><h3>Packed in cartons</h3><p>Clear, countable quantities that are easy to stock and resell.</p></div>
    <div class="card reveal"><div class="icon-badge">{I["truck"]}</div><h3>Pickup or delivery</h3><p>Collect with your own transport, or ask us to arrange delivery (charged separately).</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Frozen food FAQs</span><h2>Good to know</h2></div>
  {frozen_faq_html}
</div></section>

{cta_band("Stock your freezer or your shop", "Ask on WhatsApp for today's available fish and chicken types, carton prices and delivery options.", "frozen-cta")}
'''
page(
    "frozen-foods.html",
    "Frozen Fish & Chicken by the Carton in Lagos | NAQI FARM ENTERPRISE",
    "Buy frozen fish and chicken by the carton in Mushin, Lagos. A variety of types, properly stored, for restaurants, hotels, supermarkets, traders and families. Delivery on request.",
    frozen,
    extra_schema=[frozen_faq_schema],
    crumbs=frozen_crumbs,
)

# ===================================================================
# ABOUT
# ===================================================================
TEAM = [
    ("Abiodun Dehinde Giwa", "Chief Executive Officer", "AG", "abiodun-giwa",
     "Abiodun leads NAQI FARM ENTERPRISE and sets its direction: sourcing directly from the manufacturer so customers pay for food, not packaging."),
    ("Kafilat Agbeke Giwa", "Managing Director", "KG", "kafilat-giwa",
     "Kafilat oversees day-to-day operations, making sure every customer is served with honest measurement and the care the business was built on."),
    ("Yunusa Akande Bakare", "Senior Supervisor", "YB", "yunusa-bakare",
     "Yunusa supervises depot operations, from tanker deliveries to metered filling, so every litre is measured accurately."),
    ("Jubril Abayomi Balogun", "Senior Supervisor", "JB", "jubril-balogun",
     "Jubril supervises orders and customer service, coordinating frozen food stock, pickups and delivery requests."),
]
team_cards = "".join(
    f'''<div class="card team-card reveal">
  <div class="avatar"><span>{ini}</span><img src="assets/img/team/{slug}.jpg" alt="{name}, {role}" width="128" height="128" loading="lazy" onerror="this.remove()"></div>
  <h3>{name}</h3>
  <div class="team-role">{role}</div>
  <p>{bio}</p>
</div>''' for name, role, ini, slug, bio in TEAM
)
about_crumbs = [("index.html", "Home"), ("about.html", "About Us")]
about = f'''
<section class="page-hero"><div class="container">
  {breadcrumb_html(about_crumbs)}
  <h1>Quality food shouldn't be a luxury.</h1>
  <p class="lead">And honest measurement shouldn't be a favour. That's how we do business, one litre and one carton at a time.</p>
</div></section>

<section class="section"><div class="container split" style="align-items:start">
  <div class="story reveal">
    <span class="eyebrow">Our story</span>
    <h2>It started with a simple question</h2>
    <p>Across Nigeria, a lot of what we pay for at the market isn't the food. It's the bottle, the label and the packaging.</p>
    <p>NAQI FARM ENTERPRISE started in Lagos with a simple question: what if families, traders and kitchens could get the same genuine vegetable oil without paying for the packaging around it?</p>
    <p>So we went straight to the source. Our tanker brings Olein refined vegetable oil, popularly known as Kings oil, directly from the manufacturer to our depot, with no middlemen in between. You bring your own drum, keg or container, and we fill it through our metering system. You see exactly how much you're getting, and you pay for exactly that. No bottle, no label, no markup. Just good oil at a fair price.</p>
    <p>We apply the same thinking to our frozen foods. Our fish and chicken come in a variety of types, packed in cartons and kept properly stored, so it reaches your shop or kitchen the way it should.</p>
    <p>From our base in Lagos, we serve market traders, restaurants, hotels, supermarkets and bulk buyers across Nigeria. You can arrange your own transport, or we can arrange delivery for you on request, charged separately from the price of the product. Wherever you are, we want you to be able to find a supplier you can trust.</p>
    <p>Quality food shouldn't be a luxury, and honest measurement shouldn't be a favour. That's how we do business, one litre and one carton at a time.</p>
    <p class="signature">NAQI FARM ENTERPRISE<br><span style="font-size:1rem;color:var(--muted)">Straight from the source. Measured in front of you.</span></p>
  </div>
  <div class="reveal" style="position:sticky;top:96px">
    <div class="facts" style="grid-template-columns:1fr 1fr">
      <div class="fact"><strong>13 May 2023</strong><span>Year started</span></div>
      <div class="fact"><strong>{CAC}</strong><span>CAC registration no.</span></div>
      <div class="fact"><strong>Mushin, Lagos</strong><span>Depot location</span></div>
      <div class="fact"><strong>Nationwide</strong><span>Buyers served across Nigeria</span></div>
    </div>
    <div class="card" style="margin-top:14px">
      <h3>What we stand for</h3>
      <ul class="check-list mb-0">
        <li>Original, unadulterated Olein oil, never mixed or diluted</li>
        <li>Straight from the source, no middlemen</li>
        <li>Measured in front of you</li>
        <li>Fair prices, with delivery always shown separately</li>
      </ul>
    </div>
  </div>
</div></section>

<section class="section section-alt" id="team"><div class="container">
  <div class="section-head center"><span class="eyebrow">Our team</span><h2>The people behind the meter</h2><p class="lead">A Lagos team committed to honest measurement and reliable supply.</p></div>
  <div class="grid grid-4">{team_cards}</div>
</div></section>

{cta_band("Find a supplier you can trust", "Talk to our team on WhatsApp or call. We'll help you with prices, stock and delivery.", "about-cta")}
'''
page(
    "about.html",
    "About NAQI FARM ENTERPRISE | Our Story & Team, Lagos",
    "NAQI FARM ENTERPRISE (CAC Reg. 9353141) started in Lagos in May 2023 to sell original, unadulterated Olein oil without the packaging markup. Meet our story and our team.",
    about,
    extra_schema=[{
        "@type": "AboutPage", "url": SITE + "/about.html", "name": "About NAQI FARM ENTERPRISE",
        "about": {"@id": SITE + "/#business"},
    }] + [{"@type": "Person", "name": n, "jobTitle": r, "worksFor": {"@id": SITE + "/#business"}} for n, r, *_ in TEAM],
    crumbs=about_crumbs,
)

# ===================================================================
# CONTACT
# ===================================================================
contact_crumbs = [("index.html", "Home"), ("contact.html", "Contact")]
map_q = quote(ADDRESS + ", Nigeria")
contact = f'''
<section class="page-hero"><div class="container">
  {breadcrumb_html(contact_crumbs)}
  <h1>Order, ask for a price, or visit the depot</h1>
  <p class="lead">The fastest way to reach us is WhatsApp. Fill the form below and it opens WhatsApp with your order already written.</p>
</div></section>

<section class="section" id="order"><div class="container split" style="align-items:start">
  <div class="card reveal">
    <h2 style="font-size:1.6rem">Request a price or place an order</h2>
    <form class="form" id="order-form" novalidate>
      <div class="form-row">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="f-business">I am a</label>
          <select id="f-business" name="business">
            <option>Market trader</option><option>Restaurant / caterer</option><option>Hotel</option><option>Supermarket</option><option>Bulk buyer</option><option>Family / household</option><option>Other</option>
          </select></div>
        <div class="field"><label for="f-product">Product</label>
          <select id="f-product" name="product" required>
            <option>Original Olein oil (by the litre)</option><option>Frozen fish (cartons)</option><option>Frozen chicken (cartons)</option><option>Oil and frozen foods</option>
          </select></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="f-qty">Quantity / container size</label><input id="f-qty" name="quantity" placeholder="e.g. 2 drums, 3 kegs, 5 cartons" required></div>
        <div class="field"><label for="f-ful">Pickup or delivery?</label>
          <select id="f-ful" name="fulfilment"><option>I'll pick up at the depot</option><option>Please arrange delivery (quote separately)</option></select></div>
      </div>
      <div class="field"><label for="f-loc">Your location (area, city/state)</label><input id="f-loc" name="location" placeholder="e.g. Ikeja, Lagos"></div>
      <div class="field"><label for="f-msg">Anything else?</label><textarea id="f-msg" name="message"></textarea></div>
      <button class="btn btn-wa" type="submit">{I["wa"]} Send order on WhatsApp</button>
      <p class="form-note">Nothing is stored on this website. Your details go straight into a WhatsApp chat with us.</p>
    </form>
  </div>
  <div class="reveal">
    <ul class="contact-list">
      <li><span class="icon-badge">{I["wa"]}</span><div><strong>WhatsApp orders</strong><a href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="contact-list">{PHONE_DISPLAY}</a></div></li>
      <li><span class="icon-badge">{I["phone"]}</span><div><strong>Call</strong><a href="tel:{PHONE_TEL}" data-track="contact-list">{PHONE_DISPLAY}</a></div></li>
      <li><span class="icon-badge gold">{I["pin"]}</span><div><strong>Depot</strong>{ADDRESS}<br><a href="https://www.google.com/maps/search/?api=1&amp;query={map_q}" target="_blank" rel="noopener">Get directions &rarr;</a></div></li>
      <li><span class="icon-badge">{I["ig"]}</span><div><strong>Instagram</strong><a href="{IG}" target="_blank" rel="noopener">@naqifarmenterprise</a></div></li>
      <li><span class="icon-badge">{I["fb"]}</span><div><strong>Facebook</strong><a href="{FB}" target="_blank" rel="noopener">NAQI FARM Enterprise</a></div></li>
    </ul>
    <p class="notice" style="margin-top:22px">Delivery is available on request and is charged separately from the price of the product.</p>
    <iframe class="map-embed" title="Map: NAQI FARM ENTERPRISE depot, {ADDRESS}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={map_q}&amp;output=embed"></iframe>
  </div>
</div></section>
'''
page(
    "contact.html",
    "Contact & Order | NAQI FARM ENTERPRISE, Mushin Lagos",
    f"Order vegetable oil by the litre or frozen fish and chicken by the carton. WhatsApp or call {PHONE_DISPLAY}. Depot: 104 Ishaga Road, Idi-Araba, Mushin, Lagos.",
    contact,
    extra_schema=[{"@type": "ContactPage", "url": SITE + "/contact.html", "about": {"@id": SITE + "/#business"}}],
    crumbs=contact_crumbs,
)

# ===================================================================
# 404
# ===================================================================
page(
    "404.html",
    "Page not found | NAQI FARM ENTERPRISE",
    "This page could not be found.",
    f'''<section class="section"><div class="container center">
  <span class="eyebrow">404</span><h1>This page has run dry.</h1>
  <p class="lead">The page you wanted isn't here, but the oil still is.</p>
  <div class="btn-row" style="justify-content:center;margin-top:20px">
    <a class="btn btn-outline" href="index.html">Go to homepage</a>
    <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="404">{I["wa"]} Order on WhatsApp</a>
  </div>
</div></section>''',
)

# ===================================================================
# BLOG
# ===================================================================
blog_crumbs = [("index.html", "Home"), ("blog/index.html", "Blog")]
page(
    "blog/index.html",
    "Blog: Vegetable Oil & Frozen Food Guides | NAQI FARM ENTERPRISE",
    "Practical guides for Nigerian traders, kitchens and families: buying vegetable oil by the litre, understanding Olein (Kings) oil, and storing frozen fish and chicken.",
    f'''<section class="page-hero"><div class="container">
  {breadcrumb_html(blog_crumbs)}
  <h1>Guides for smarter food buying</h1>
  <p class="lead">Plain, practical advice for traders, kitchens and families on buying vegetable oil and frozen food in Nigeria without overpaying.</p>
</div></section>
<section class="section"><div class="container"><div class="grid grid-3">{"".join(post_card(p) for p in POSTS)}</div></div></section>
{cta_band(track="blog-index-cta")}''',
    extra_schema=[{
        "@type": "Blog", "@id": SITE + "/blog/#blog", "url": SITE + "/blog/", "name": "NAQI FARM ENTERPRISE Blog",
        "publisher": {"@id": SITE + "/#business"},
        "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}.html", "datePublished": p["date"]} for p in POSTS],
    }],
    crumbs=blog_crumbs,
)

for p in POSTS:
    f = f"blog/{p['slug']}.html"
    title = p["title"][0].upper() + p["title"][1:]
    crumbs = blog_crumbs + [(f, title)]
    p_faq_html, p_faq_schema = faq_block(p["faq"])
    others = "".join(post_card(o) for o in POSTS if o is not p)[:]
    body = f'''<section class="page-hero"><div class="container">
  {breadcrumb_html(crumbs)}
  <span class="eyebrow" style="color:var(--gold-400)">{p["category"]}</span>
  <h1>{title}</h1>
  <p class="post-meta" style="color:#b9cdbf">By NAQI FARM ENTERPRISE &middot; <time datetime="{p["date"]}">{nice_date(p["date"])}</time> &middot; {p["read_minutes"]} min read</p>
</div></section>
<section class="section"><div class="container">
  <article class="prose">
    {p["body"]}
    <aside class="post-cta">
      <h3>Get today's price</h3>
      <p>Send your container size or carton quantity on WhatsApp. We reply with today's price and delivery options.</p>
      <div class="btn-row">
        <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener" data-track="post-{p["slug"]}">{I["wa"]} Chat on WhatsApp</a>
        <a class="btn btn-outline" href="tel:{PHONE_TEL}" data-track="post-{p["slug"]}">{I["phone"]} Call {PHONE_DISPLAY}</a>
      </div>
    </aside>
    <h2>Frequently asked questions</h2>
    {p_faq_html}
  </article>
</div></section>
<section class="section section-alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Keep reading</span><h2>More guides</h2></div>
  <div class="grid grid-2">{others}</div>
</div></section>'''
    page(
        f,
        p["seo_title"],
        p["description"],
        body,
        extra_schema=[p_faq_schema, {
            "@type": "BlogPosting",
            "headline": title,
            "description": p["description"],
            "datePublished": p["date"],
            "dateModified": p["date"],
            "mainEntityOfPage": f"{SITE}/{f}",
            "image": SITE + "/assets/img/og-image.jpg",
            "author": {"@id": SITE + "/#business"},
            "publisher": {"@id": SITE + "/#business"},
            "inLanguage": "en-NG",
        }],
        crumbs=crumbs,
        nav_active="blog/index.html",
        og_type="article",
    )

# ---------- robots & sitemap ----------
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
urls = "".join(
    f"  <url><loc>{url_for(f)}</loc><changefreq>{'weekly' if f == 'index.html' else 'monthly'}</changefreq><priority>{'1.0' if f == 'index.html' else '0.8'}</priority></url>\n"
    for f, _ in NAV
) + "".join(
    f"  <url><loc>{SITE}/blog/{p['slug']}.html</loc><lastmod>{p['date']}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n"
    for p in POSTS
)
(OUT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n',
    encoding="utf-8",
)
print("built", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*.html")))
