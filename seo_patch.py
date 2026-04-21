import re

# Read file
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. Replace <head> meta block ─────────────────────────────
old_meta = '''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Caffee\'issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435 \u0438 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435</title>
  <meta name="description" content="Caffee\'issimo \u2014 \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0441\u0435\u0442\u044c \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0438\u0445 \u043a\u0430\u0444\u0435 \u0438 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d\u043e\u0432 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435. \u0423\u0437\u043d\u0430\u0439\u0442\u0435 \u043e \u043c\u0435\u043d\u044e, \u043a\u043e\u0444\u0435 Illy, \u0444\u0438\u043b\u0438\u0430\u043b\u0430\u0445 \u0438 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0435." />
  <meta property="og:title" content="Caffee\'issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435 \u0438 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435" />
  <meta property="og:description" content="\u0418\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f, \u043a\u043e\u0444\u0435 Illy, \u0444\u0438\u043b\u0438\u0430\u043b\u044b \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435 \u0438 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0430 \u0447\u0435\u0440\u0435\u0437 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0440\u044b." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://caffeeissimo.example.com" />
  <meta property="og:image" content="https://images.unsplash.com/photo-1521017432531-fbd92d768814?auto=format&fit=crop&w=1600&q=80" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="icon" type="image/ico" href="Issimo.ico" />'''

new_meta = '''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- PRIMARY SEO -->
  <title>Caffee\u2019issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0438 \u043a\u043e\u0444\u0435\u0439\u043d\u044f \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435</title>
  <meta name="description" content="Caffee\u2019issimo \u2014 \u0441\u0435\u0442\u044c \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0438\u0445 \u043a\u0430\u0444\u0435 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435. \u0415\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0441 4:00 \u0434\u043e 12:00, \u043a\u043e\u0444\u0435 Illy, \u043f\u0430\u0441\u0442\u0430, \u043f\u0438\u0446\u0446\u0430, \u0441\u0442\u0435\u0439\u043a\u0438. 3 \u0444\u0438\u043b\u0438\u0430\u043b\u0430: \u043f\u0440. \u0410\u043c\u0438\u0440\u0430 \u0422\u0435\u043c\u0443\u0440\u0430, \u0410\u043b\u043c\u0430\u0437\u0430\u0440, \u041c\u0438\u0440\u0430\u0431\u0430\u0434. \u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430 Yandex Eats, Uzum Tezkor." />
  <meta name="keywords" content="\u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0435\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u043a\u043e\u0444\u0435\u0439\u043d\u044f \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0438\u0439 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u043a\u0430\u0444\u0435 \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u043a\u043e\u0444\u0435 Illy \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u043f\u0438\u0446\u0446\u0430 \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u043f\u0430\u0441\u0442\u0430 \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 24 \u0447\u0430\u0441\u0430 \u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d \u0410\u043c\u0438\u0440\u0430 \u0422\u0435\u043c\u0443\u0440\u0430, \u043a\u0430\u0444\u0435 \u0410\u043b\u043c\u0430\u0437\u0430\u0440, Caffeeissimo, \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0430 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0439 \u0435\u0434\u044b \u0422\u0430\u0448\u043a\u0435\u043d\u0442, italian restaurant tashkent, breakfast tashkent, coffee tashkent, european cuisine tashkent" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="author" content="Caffee\u2019issimo" />
  <link rel="canonical" href="https://issimo.uz/" />

  <!-- GEO / LOCAL SEO -->
  <meta name="geo.region" content="UZ-TO" />
  <meta name="geo.placename" content="\u0422\u0430\u0448\u043a\u0435\u043d\u0442, \u0423\u0437\u0431\u0435\u043a\u0438\u0441\u0442\u0430\u043d" />
  <meta name="geo.position" content="41.299496;69.240073" />
  <meta name="ICBM" content="41.299496, 69.240073" />
  <meta name="language" content="ru" />

  <!-- OPEN GRAPH -->
  <meta property="og:type" content="restaurant" />
  <meta property="og:site_name" content="Caffee\u2019issimo" />
  <meta property="og:title" content="Caffee\u2019issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0438 \u043a\u043e\u0444\u0435\u0439\u043d\u044f \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435" />
  <meta property="og:description" content="\u0415\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u043a\u0430\u044f \u0438 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0441 4:00, \u043a\u043e\u0444\u0435 Illy. 3 \u0444\u0438\u043b\u0438\u0430\u043b\u0430 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435. \u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430 Yandex Eats, Uzum Tezkor." />
  <meta property="og:url" content="https://issimo.uz/" />
  <meta property="og:image" content="https://issimo.uz/assets/breakfast-hero.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Caffee\u2019issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435" />
  <meta property="og:locale" content="ru_RU" />
  <meta property="business:contact_data:phone_number" content="+998712050152" />
  <meta property="business:contact_data:email" content="hello@caffeeissimo.uz" />

  <!-- TWITTER CARD -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Caffee\u2019issimo \u2014 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u0435 \u043a\u0430\u0444\u0435 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435" />
  <meta name="twitter:description" content="\u0415\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u043a\u0430\u044f \u0438 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0441 4:00, \u043a\u043e\u0444\u0435 Illy. 3 \u0444\u0438\u043b\u0438\u0430\u043b\u0430. \u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430." />
  <meta name="twitter:image" content="https://issimo.uz/assets/breakfast-hero.jpg" />

  <!-- FAVICONS -->
  <link rel="icon" type="image/svg+xml" href="Assets/logo.svg" />
  <link rel="icon" type="image/x-icon" href="Issimo.ico" />
  <link rel="apple-touch-icon" href="Assets/logo-full.png" />

  <!-- FONTS & STYLES -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />

  <!-- JSON-LD STRUCTURED DATA -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Restaurant",
        "@id": "https://issimo.uz/#organization",
        "name": "Caffee\u2019issimo",
        "alternateName": ["Caffeeissimo", "\u041a\u0430\u0444\u0435\u0438\u0441\u0441\u0438\u043c\u043e", "Issimo"],
        "description": "\u0421\u0435\u0442\u044c \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0438\u0445 \u043a\u0430\u0444\u0435 \u0432 \u0422\u0430\u0448\u043a\u0435\u043d\u0442\u0435. \u0415\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u043a\u0430\u044f \u0438 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u0430\u044f \u043a\u0443\u0445\u043d\u044f, \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u0438 \u0441 4:00 \u0434\u043e 12:00, \u043a\u043e\u0444\u0435 Illy, \u043f\u0438\u0446\u0446\u0430, \u043f\u0430\u0441\u0442\u0430, \u0441\u0442\u0435\u0439\u043a\u0438.",
        "url": "https://issimo.uz",
        "logo": "https://issimo.uz/Assets/logo-full.png",
        "image": ["https://issimo.uz/assets/breakfast-hero.jpg"],
        "telephone": "+998712050152",
        "email": "hello@caffeeissimo.uz",
        "servesCuisine": ["Italian", "European", "Mediterranean"],
        "priceRange": "$$",
        "currenciesAccepted": "UZS",
        "hasMenu": "https://issimo.uz/menu-viewer.html?type=main",
        "sameAs": [
          "https://www.instagram.com/caffeeissimo/",
          "https://www.facebook.com/CaffeeIssimo/"
        ],
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u0410\u043c\u0438\u0440\u0430 \u0422\u0435\u043c\u0443\u0440\u0430, 95\u0410",
          "addressLocality": "\u0422\u0430\u0448\u043a\u0435\u043d\u0442",
          "addressCountry": "UZ"
        },
        "geo": {"@type": "GeoCoordinates", "latitude": "41.299496", "longitude": "69.240073"},
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
          "opens": "00:00",
          "closes": "23:59"
        },
        "amenityFeature": [
          {"@type": "LocationFeatureSpecification", "name": "\u0417\u0430\u0432\u0442\u0440\u0430\u043a\u0438", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Wi-Fi", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "\u041a\u043e\u0444\u0435 Illy", "value": true}
        ]
      },
      {
        "@type": "Restaurant",
        "@id": "https://issimo.uz/#branch-amir-temur",
        "name": "Caffee\u2019issimo \u2014 \u0410\u043c\u0438\u0440\u0430 \u0422\u0435\u043c\u0443\u0440\u0430 (24/7)",
        "parentOrganization": {"@id": "https://issimo.uz/#organization"},
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u0410\u043c\u0438\u0440\u0430 \u0422\u0435\u043c\u0443\u0440\u0430, 95\u0410",
          "addressLocality": "\u0422\u0430\u0448\u043a\u0435\u043d\u0442",
          "addressCountry": "UZ"
        },
        "telephone": "+998712050152",
        "geo": {"@type": "GeoCoordinates", "latitude": "41.299496", "longitude": "69.240073"},
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
          "opens": "00:00",
          "closes": "23:59"
        },
        "servesCuisine": ["Italian", "European"],
        "hasMenu": "https://issimo.uz/menu-viewer.html?type=main"
      },
      {
        "@type": "Restaurant",
        "@id": "https://issimo.uz/#branch-almaзar",
        "name": "Caffee\u2019issimo \u2014 \u0410\u043b\u043c\u0430\u0437\u0430\u0440",
        "parentOrganization": {"@id": "https://issimo.uz/#organization"},
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "\u0443\u043b. \u0422\u0430\u043b\u0430\u0431\u0430\u043b\u0430\u0440, 52",
          "addressLocality": "\u0422\u0430\u0448\u043a\u0435\u043d\u0442",
          "addressCountry": "UZ"
        },
        "telephone": "+998712076300",
        "servesCuisine": ["Italian", "European"],
        "hasMenu": "https://issimo.uz/menu-viewer.html?type=main"
      },
      {
        "@type": "Restaurant",
        "@id": "https://issimo.uz/#branch-mirobod",
        "name": "Caffee\u2019issimo \u2014 \u041c\u0438\u0440\u0430\u0431\u0430\u0434",
        "parentOrganization": {"@id": "https://issimo.uz/#organization"},
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "\u043b. \u0421\u0430\u0440\u0430\u043a\u0443\u043b\u044c, 32/2",
          "addressLocality": "\u0422\u0430\u0448\u043a\u0435\u043d\u0442",
          "addressCountry": "UZ"
        },
        "telephone": "+998712094900",
        "servesCuisine": ["Italian", "European"],
        "hasMenu": "https://issimo.uz/menu-viewer.html?type=main"
      },
      {
        "@type": "WebSite",
        "@id": "https://issimo.uz/#website",
        "url": "https://issimo.uz/",
        "name": "Caffee\u2019issimo",
        "inLanguage": "ru",
        "publisher": {"@id": "https://issimo.uz/#organization"}
      }
    ]
  }
  </script>'''

if old_meta in html:
    html = html.replace(old_meta, new_meta)
    print("OK: meta replaced")
else:
    print("ERROR: old_meta not found, trying fuzzy")
    # Try to find the title tag and replace from there
    import re
    pattern = r'<meta charset="UTF-8" />.*?<link rel="icon" type="image/ico" href="Issimo\.ico" />'
    m = re.search(pattern, html, re.DOTALL)
    if m:
        html = html[:m.start()] + new_meta + html[m.end():]
        print("OK: regex replacement done")
    else:
        print("ERROR: regex also failed")

# ── 2. Fix duplicate h1 in breakfast slide ───────────────────
html = html.replace(
    '<h1 class="hero-breakfast__title">',
    '<p class="hero-breakfast__title">'
).replace(
    '</h1>\n            <div class="breakfast-time">',
    '</p>\n            <div class="breakfast-time">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done. index.html saved.")
