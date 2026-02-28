"""
Main Web Routes
---------------
Handles:

- Home page
- SEO injection
- Structured data
- Feature flag exposure
- Sitemap
- robots.txt
- ads.txt
"""

from flask import Blueprint, render_template, current_app, Response
from datetime import datetime
import json

web_main_bp = Blueprint("web_main", __name__)


# =====================================================
# 🏠 HOME PAGE
# =====================================================

@web_main_bp.route("/")
def home():
    config = current_app.config

    # ---------------- SEO ----------------
    seo_data = {
        "title": "EMI Calculator – Advanced Loan EMI & Prepayment Tool",
        "description": config.get("DEFAULT_META_DESCRIPTION"),
        "url": config.get("SITE_URL"),
    }

    # ---------------- Structured Data ----------------
    structured_data = {
        "@context": "https://schema.org",
        "@type": "FinancialProduct",
        "name": "EMI Calculator Pro",
        "description": config.get("DEFAULT_META_DESCRIPTION"),
        "url": config.get("SITE_URL"),
        "provider": {
            "@type": "Organization",
            "name": config.get("SITE_NAME")
        }
    }

    # ---------------- Feature Flags ----------------
    features = {
        "pdf": config.get("ENABLE_PDF_EXPORT", False),
        "comparison": config.get("ENABLE_LOAN_COMPARISON", False),
        "prepayment": config.get("ENABLE_PREPAYMENT_SIMULATOR", False),
        "currency": config.get("ENABLE_CURRENCY_CONVERSION", False),
        "ads": config.get("ENABLE_ADS", False)
    }

    return render_template(
        "index.html",
        seo=seo_data,
        structured_json=json.dumps(structured_data),
        features=features,
        adsense_client=config.get("ADSENSE_CLIENT_ID")
    )


# =====================================================
# 🗺️ SITEMAP.XML
# =====================================================

@web_main_bp.route("/sitemap.xml", methods=["GET"])
def sitemap():

    base_url = current_app.config.get(
        "SITE_URL",
        "https://smart-emi-hub-pro.onrender.com"
    ).rstrip("/")

    today = datetime.utcnow().strftime("%Y-%m-%d")

    pages = []

    # -------- Static URLs --------
    static_urls = [
        ("", "daily", "1.0"),
        ("/calculator/", "weekly", "0.9"),
        ("/calculator/home-loan-emi-calculator", "weekly", "0.8"),
        ("/calculator/car-loan-emi-calculator", "weekly", "0.8"),
        ("/calculator/personal-loan-emi-calculator", "weekly", "0.8"),
        ("/calculator/sip-calculator", "weekly", "0.8"),
        ("/calculator/fd-calculator", "weekly", "0.8"),
        ("/calculator/rd-calculator", "weekly", "0.8"),
        ("/calculator/gst-calculator", "weekly", "0.8"),
        ("/calculator/retirement-calculator", "weekly", "0.8"),
        ("/about", "monthly", "0.5"),
        ("/contact", "monthly", "0.5"),
        ("/privacy", "yearly", "0.3"),
        ("/terms", "yearly", "0.3"),
        ("/disclaimer", "yearly", "0.3"),
    ]

    for path, changefreq, priority in static_urls:
        pages.append({
            "loc": f"{base_url}{path}",
            "lastmod": today,
            "changefreq": changefreq,
            "priority": priority
        })

    sitemap_xml = render_template("sitemap.xml", pages=pages)

    return Response(sitemap_xml, mimetype="application/xml")


# =====================================================
# 🤖 ROBOTS.TXT
# =====================================================

@web_main_bp.route("/robots.txt")
def robots():

    base_url = current_app.config.get(
        "SITE_URL",
        "https://smart-emi-hub-pro.onrender.com"
    ).rstrip("/")

    content = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

    return Response(content, mimetype="text/plain")


# =====================================================
# 📢 ADS.TXT
# =====================================================

@web_main_bp.route("/ads.txt")
def ads_txt():
    return Response(
        "google.com, pub-2031854006818432, DIRECT, f08c47fec0942fa0",
        mimetype="text/plain"
    )