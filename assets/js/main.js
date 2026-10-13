/* NAQI FARM ENTERPRISE — site behaviour
   Tracking IDs live here so they are set in one place for every page. */
(function () {
  "use strict";

  var CONFIG = {
    whatsappNumber: "2349068431502",
    // Paste your IDs to switch tracking on. Leave empty to keep it off.
    ga4MeasurementId: "", // e.g. "G-XXXXXXXXXX" (Google Analytics 4)
    googleAdsId: "", // e.g. "AW-XXXXXXXXXX" (Google Ads conversion tracking)
    googleAdsLeadLabel: "", // conversion label for WhatsApp/phone leads
    metaPixelId: "" // e.g. "123456789012345" (Facebook / Instagram ads)
  };

  document.documentElement.classList.remove("no-js");

  /* ---------- Analytics loaders ---------- */
  function loadScript(src) {
    var s = document.createElement("script");
    s.async = true;
    s.src = src;
    document.head.appendChild(s);
  }

  var gtagId = CONFIG.ga4MeasurementId || CONFIG.googleAdsId;
  if (gtagId) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    if (CONFIG.ga4MeasurementId) window.gtag("config", CONFIG.ga4MeasurementId);
    if (CONFIG.googleAdsId) window.gtag("config", CONFIG.googleAdsId);
    loadScript("https://www.googletagmanager.com/gtag/js?id=" + gtagId);
  }

  if (CONFIG.metaPixelId) {
    /* Standard Meta Pixel bootstrap */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("init", CONFIG.metaPixelId);
    window.fbq("track", "PageView");
  }

  // One call reports a lead to every tracker that is switched on.
  function trackLead(channel, label) {
    var params = { channel: channel, placement: label || "", page: location.pathname };
    if (window.gtag) {
      window.gtag("event", "generate_lead", params);
      if (CONFIG.googleAdsId && CONFIG.googleAdsLeadLabel) {
        window.gtag("event", "conversion", { send_to: CONFIG.googleAdsId + "/" + CONFIG.googleAdsLeadLabel });
      }
    }
    if (window.fbq) window.fbq("track", channel === "whatsapp" ? "Contact" : "Lead", params);
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("wa.me") !== -1) trackLead("whatsapp", a.getAttribute("data-track"));
    else if (href.indexOf("tel:") === 0) trackLead("phone", a.getAttribute("data-track"));
  });

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Footer year ---------- */
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  /* ---------- Reveal on scroll ---------- */
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -60px 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Order form -> WhatsApp message ---------- */
  var form = document.getElementById("order-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var lines = [
        "Hello NAQI FARM ENTERPRISE, I'd like to place an order / get a price.",
        "",
        "Name: " + (d.get("name") || ""),
        "Phone: " + (d.get("phone") || ""),
        "Business type: " + (d.get("business") || ""),
        "Product: " + (d.get("product") || ""),
        "Quantity: " + (d.get("quantity") || ""),
        "Pickup or delivery: " + (d.get("fulfilment") || ""),
        "Location: " + (d.get("location") || "")
      ];
      var note = (d.get("message") || "").toString().trim();
      if (note) lines.push("Note: " + note);
      var url = "https://wa.me/" + CONFIG.whatsappNumber + "?text=" + encodeURIComponent(lines.join("\n"));
      trackLead("whatsapp", "order-form");
      window.open(url, "_blank", "noopener");
    });
  }
})();
