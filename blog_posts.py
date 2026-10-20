"""Blog posts for the NAQI FARM ENTERPRISE site.

Each post: slug, title (H1), seo_title, description, date, read_minutes, category,
excerpt, body (HTML, links relative to the site root), faq [(q, a)].
To add a post, append a dict to POSTS and run build.py.
"""

POSTS = [
    {
        "slug": "buy-vegetable-oil-by-the-litre-lagos",
        "title": "Buying vegetable oil by the litre in Lagos: how it saves you money",
        "seo_title": "Buy Vegetable Oil by the Litre in Lagos & Save | NAQI FARM",
        "description": "Vegetable oil prices in Lagos keep rising. Here is how buying by the litre into your own keg or drum cuts out packaging costs, and what to check before you buy.",
        "date": "2026-10-13",
        "read_minutes": 5,
        "category": "Vegetable oil",
        "excerpt": "When oil prices climb, the bottle and the label climb with them. Buying by the litre into your own container is the simplest way to stop paying for packaging.",
        "body": """
<p>Buying vegetable oil by the litre means you bring your own keg, drum or container, the seller fills it from bulk stock, and you pay only for the oil that goes in. You skip the cost of the bottle, the label and the markup that every reseller adds on top. For anyone who cooks every day or sells oil for a living, that difference adds up quickly.</p>

<h2>Why does vegetable oil keep getting more expensive in Lagos?</h2>
<p>Vegetable oil prices in Lagos move with input costs and supply, and in 2026 they have mostly moved up. A May 2026 survey of Lagos markets reported by <a href="https://nm-stag.nairametrics.com/?p=840" target="_blank" rel="noopener">Nairametrics</a> found the 25-litre gallon of local vegetable oil rising from about N53,000 to N62,000, with traders pointing to input costs and tight supply.</p>
<p>You can't control the market price of oil. But you can control how much extra you pay on top of it, and that is where packaging comes in.</p>

<h2>What are you actually paying for in a bottle of oil?</h2>
<p>When you buy a sealed bottle or a branded gallon, the price covers more than the oil inside. It also pays for:</p>
<ul>
  <li><strong>The container</strong> itself, which you often throw away or reuse for something else.</li>
  <li><strong>The label and printing</strong> on the outside.</li>
  <li><strong>Handling at every step</strong>, because each distributor, wholesaler and retailer between the factory and you adds a margin.</li>
</ul>
<p>None of those things go into your stew. So when you buy oil in bulk and bring your own container, you keep that money instead.</p>

<h2>How does buying oil by the litre work?</h2>
<p>At NAQI FARM ENTERPRISE, it works in three steps:</p>
<ol>
  <li><strong>Bring your container.</strong> A keg, a drum, or any clean container with a good lid.</li>
  <li><strong>Watch the meter.</strong> We fill it through our metering system in front of you, so you can see each litre as it goes in.</li>
  <li><strong>Pay for exactly that.</strong> The meter reading is what you pay for. Nothing more.</li>
</ol>
<p>Our oil is Original Olein oil, popularly known as Kings oil, and our tanker brings it straight from the manufacturer to our depot in Mushin. There is no middleman between the factory and our tank, so the oil is never mixed, diluted or repackaged, and that is also why the price stays fair. If you want to know more about the oil itself, read <a href="blog/what-is-olein-oil-kings-oil.html">our plain guide to Olein oil</a>.</p>

<h2>Who benefits most from buying oil in bulk?</h2>
<p>Anyone who uses a lot of oil, regularly, gets the most from buying by the litre:</p>
<ul>
  <li><strong>Market traders</strong> who buy at depot level and resell in smaller quantities, so their margin grows.</li>
  <li><strong>Restaurants, bukas and caterers</strong> who fry every day and go through oil fast.</li>
  <li><strong>Hotels</strong> that need a steady supply for their kitchens.</li>
  <li><strong>Families</strong> who would rather fill one keg every few weeks than buy small bottles at shop prices.</li>
</ul>

<h2>What should you check before buying oil by the litre?</h2>
<p>Buying loose oil only saves you money if the oil is genuine and the measurement is honest, so check these four things wherever you buy:</p>
<ol>
  <li><strong>Can you see the measurement?</strong> A meter you can watch is better than "trust me, it's full".</li>
  <li><strong>Where does the oil come from?</strong> Ask whether it comes directly from the manufacturer or has passed through several hands.</li>
  <li><strong>Is your container clean and dry?</strong> Water or old residue in a keg spoils good oil. Wash, dry and cover it before you come.</li>
  <li><strong>Is delivery priced separately?</strong> A clear oil price plus a clear delivery charge is easier to compare than one mixed-up figure.</li>
</ol>

<h2>How do you get today's price?</h2>
<p>Because the market moves, we quote fresh prices every day. Send your container size on WhatsApp and we'll reply with today's price per litre. You can collect from our depot at 104 Ishaga Road, Idi-Araba, Mushin, Lagos, or ask us to arrange delivery, which is charged separately.</p>
<p>Want the full details first? See <a href="vegetable-oil.html">how we sell vegetable oil by the litre</a>.</p>
""",
        "faq": [
            ("Is buying vegetable oil by the litre cheaper than buying bottles?",
             "Usually, yes, because you are not paying for the bottle, the label or the markups added at each step of resale. You pay only for the oil measured into your own container."),
            ("What container should I bring to buy oil by the litre?",
             "Bring a clean, dry keg, drum or container with a lid that closes well. Any size works, because you pay for the litres measured, not the size of the container."),
            ("How do I know I'm getting the right quantity?",
             "Buy from a seller who fills through a meter you can watch. At NAQI FARM ENTERPRISE every fill goes through our metering system in front of you."),
            ("Where can I buy vegetable oil by the litre in Lagos?",
             "NAQI FARM ENTERPRISE sells original, unadulterated Olein oil (Kings oil) by the litre at 104 Ishaga Road, Idi-Araba, Mushin, Lagos. Message +234 906 843 1502 on WhatsApp for today's price."),
        ],
    },
    {
        "slug": "what-is-olein-oil-kings-oil",
        "title": "What is Olein oil? A plain guide to the oil Lagos calls \"Kings oil\"",
        "seo_title": "What Is Olein Oil? A Plain Guide to Kings Oil | NAQI FARM",
        "description": "Olein refined vegetable oil is the liquid part of palm oil, refined for cooking. Here is what it is, why it stays liquid, and how to buy it at a fair price in Lagos.",
        "date": "2026-10-13",
        "read_minutes": 4,
        "category": "Vegetable oil",
        "excerpt": "Many Nigerians call it Kings oil. On the label it says Olein. Here is what that word means and why it matters in your kitchen.",
        "body": """
<p>Olein oil is the liquid part of palm oil, separated out and refined into a clear, light cooking oil. In many Nigerian markets people simply call it "Kings oil", after one of the best-known brands. It is the golden vegetable oil you see in most kitchens, bukas and fast-food fryers across Lagos.</p>

<h2>Where does Olein oil come from?</h2>
<p>Olein comes from palm oil, which is pressed from the fruit of the oil palm tree. Raw palm oil is a mix of a liquid part and a more solid part. Refiners cool the oil under controlled temperatures so the solid part forms crystals, then filter those crystals out. The liquid that remains is <strong>palm olein</strong>, and the solid part is called palm stearin. This process is known as fractionation.</p>
<p>After fractionation, the olein is refined so that it is clear, light in colour and mild in smell. That is the oil that ends up in your kitchen.</p>

<h2>Is Olein oil the same as red palm oil?</h2>
<p>No. Both come from the oil palm fruit, but they are very different in the pot. Red palm oil is unrefined, deep red, and has the strong taste that makes banga soup and ofada stew what they are. Olein refined vegetable oil is pale gold and almost neutral in taste, so it suits frying, baking and everyday cooking where you don't want the oil to change the flavour of the food.</p>

<h2>Why does Olein oil stay liquid?</h2>
<p>It stays liquid because the more solid part of the palm oil has already been taken out during fractionation. That's what gives you a pourable oil at normal Lagos temperatures. In cold weather or air-conditioned storage it can look slightly cloudy, which is normal for palm-based oils and clears again when it warms up.</p>

<h2>What is Olein oil good for?</h2>
<p>Olein refined vegetable oil is an everyday, all-round cooking oil. People use it for:</p>
<ul>
  <li><strong>Deep frying</strong> dodo, puff-puff, akara, chicken, fish and chips.</li>
  <li><strong>Stews and sauces</strong> where you want a neutral oil.</li>
  <li><strong>Baking and snacks</strong> like chin chin and meat pie.</li>
  <li><strong>Commercial kitchens</strong> in restaurants and hotels that go through oil quickly.</li>
</ul>

<h2>How can you buy Olein oil at a fair price?</h2>
<p>The safest and fairest way is to buy it close to the source, where it can't be mixed or diluted along the way, and pay only for the oil. At NAQI FARM ENTERPRISE our tanker brings Original Olein oil directly from the manufacturer to our depot in Mushin, Lagos. You bring your own keg or drum, we fill it through our meter in front of you, and you pay for exactly the litres you get.</p>
<p>Read <a href="blog/buy-vegetable-oil-by-the-litre-lagos.html">how buying by the litre saves you money</a>, or go straight to <a href="vegetable-oil.html">our vegetable oil page</a> for today's price.</p>
""",
        "faq": [
            ("What is Olein oil?",
             "Olein oil is the liquid part of palm oil, separated by fractionation and then refined into a clear, light cooking oil. In Nigeria it is often called Kings oil."),
            ("Is Olein oil the same as red palm oil?",
             "No. Red palm oil is unrefined and strongly flavoured. Olein refined vegetable oil is pale gold and nearly neutral in taste, which makes it suitable for frying and everyday cooking."),
            ("Why does my vegetable oil look cloudy?",
             "Palm-based oils like olein can turn slightly cloudy in cool or air-conditioned places. It normally clears again once the oil warms up."),
            ("Where can I buy Olein (Kings) oil in Lagos?",
             "NAQI FARM ENTERPRISE sells original, unadulterated Olein oil by the litre at 104 Ishaga Road, Idi-Araba, Mushin, Lagos, filled into your own container through a meter."),
        ],
    },
    {
        "slug": "how-to-store-frozen-fish-and-chicken",
        "title": "How to store frozen fish and chicken after you buy a carton",
        "seo_title": "How to Store Frozen Fish & Chicken (Even When NEPA Takes Light)",
        "description": "Simple, safe ways to store a carton of frozen fish or chicken at home or in your shop: freezer temperature, safe thawing, refreezing, and what to do during power cuts.",
        "date": "2026-10-13",
        "read_minutes": 6,
        "category": "Frozen foods",
        "excerpt": "A carton is a big buy. Here is how to keep every piece of fish and chicken safe, from the drive home to the day you cook it, even when the power goes off.",
        "body": """
<p>To store frozen fish and chicken safely, get them into a freezer at 0&deg;F (-18&deg;C) or colder as soon as possible, keep the freezer door shut, and thaw only what you need, in the fridge rather than on the counter. Those three habits protect most of what you paid for. The rest of this guide covers the details, including what to do when the power goes off.</p>

<h2>How fast should you get frozen food into the freezer?</h2>
<p>Get it into the freezer as soon as you can. Frozen fish and chicken start to warm up the moment they leave a cold room, and Lagos heat and traffic speed that up. A few simple habits help on the way home:</p>
<ul>
  <li>Make the depot or market your <strong>last stop</strong>, not your first.</li>
  <li>Keep the carton <strong>closed</strong> and out of direct sun. A cooler box or an insulated bag helps on longer trips.</li>
  <li>If you are buying several cartons, <strong>stack them together</strong>. Frozen cartons keep each other cold.</li>
</ul>

<h2>What temperature should your freezer be?</h2>
<p>Your freezer should be at 0&deg;F (-18&deg;C) or colder. At that temperature, the germs that spoil food stop growing. If your freezer has a dial rather than a display, an inexpensive freezer thermometer will tell you where it really sits.</p>

<h2>Should you break the carton down before freezing?</h2>
<p>Yes, if you won't use the whole carton at once. Split the fish or chicken into portions for one meal or one day of business, wrap each portion tightly or bag it with as little air as possible, and write the date on it. That way you only ever take out what you'll cook, and the rest stays frozen. Tight wrapping also prevents freezer burn, the dry, pale patches that make meat tough.</p>

<h2>What is the safest way to thaw frozen chicken and fish?</h2>
<p>The safest way is in the fridge. Move what you need from the freezer to the fridge the night before. If you need it faster, you can thaw it in a sealed bag in cold water, changing the water every 30 minutes, or in the microwave, but then cook it straight away.</p>
<p>What you should not do is leave frozen meat on the kitchen counter or soak it in warm water. According to <a href="https://food.unl.edu/safety/safe-to-refreeze" target="_blank" rel="noopener">USDA guidance</a>, bacteria multiply quickly at room temperature, so the outside of the meat can become unsafe while the inside is still frozen.</p>

<h2>Can you refreeze fish and chicken after thawing?</h2>
<p>It depends on how you thawed it. USDA guidance says:</p>
<ul>
  <li><strong>Thawed in the fridge:</strong> you can refreeze it without cooking, although it may lose some quality.</li>
  <li><strong>Thawed in cold water or the microwave:</strong> cook it first, then you can freeze the cooked food.</li>
  <li><strong>Left out for more than 2 hours</strong> (or more than 1 hour in very hot conditions): do not refreeze it.</li>
</ul>
<p>Once fish or chicken has thawed in the fridge, cook it within one to two days.</p>

<h2>What should you do when NEPA takes light?</h2>
<p>Keep the freezer door closed. That is the single most useful thing you can do during a power cut. A full freezer that stays shut can hold its temperature for about 48 hours, and a half-full one for about 24 hours, according to US food safety guidance. Every time you open the door, you lose cold air and shorten that time.</p>
<p>A few more tips that help with Nigeria's power supply:</p>
<ul>
  <li><strong>Keep the freezer full.</strong> Frozen food holds cold better than empty space. If you have room, fill gaps with bottles of frozen water.</li>
  <li><strong>Run the generator or inverter on a schedule</strong> if outages are long, rather than waiting until everything has started to soften.</li>
  <li><strong>Check before you cook.</strong> If food still has ice crystals or feels fridge-cold, it is generally safe to refreeze. If it has been warm for hours, or smells off, throw it away.</li>
</ul>

<h2>Where can you buy properly stored frozen fish and chicken in Lagos?</h2>
<p>Good storage starts before you buy. At NAQI FARM ENTERPRISE our fish and chicken come in a variety of types, packed in cartons and kept properly stored at our depot in Mushin, so they reach your kitchen or shop the way they should. You can collect with your own transport, or ask us to arrange delivery, which is charged separately.</p>
<p>See <a href="frozen-foods.html">our frozen fish and chicken</a> or message us on WhatsApp for today's stock.</p>
""",
        "faq": [
            ("What temperature should a freezer be for fish and chicken?",
             "Keep your freezer at 0°F (-18°C) or colder. At that temperature, the bacteria that spoil food stop growing."),
            ("Can I refreeze chicken after it has thawed?",
             "If it thawed in the fridge, you can refreeze it, though quality may drop a little. If it thawed in cold water or the microwave, cook it before freezing. Don't refreeze food left out for more than two hours."),
            ("How long will frozen food last during a power cut?",
             "A full freezer kept closed holds its temperature for about 48 hours, and a half-full freezer for about 24 hours. Keep the door shut as much as possible."),
            ("Is it safe to thaw chicken on the kitchen counter?",
             "No. Bacteria grow quickly at room temperature. Thaw chicken and fish in the fridge, or in a sealed bag in cold water if you will cook it right away."),
        ],
    },
]
