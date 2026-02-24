"""
Main Web Routes
---------------
Handles:

- Home page
- SEO injection
- Structured data
- Feature flag exposure
"""

from flask import Blueprint, render_template, current_app, request
import json

web_main_bp = Blueprint("web_main", __name__)


@web_main_bp.route("/")
def home():
    """
    Render EMI Calculator homepage.
    """

    config = current_app.config

    # ===============================
    # SEO Metadata
    # ===============================
    seo_data = {
        "title": "EMI Calculator – Advanced Loan EMI & Prepayment Tool",
        "description": config["DEFAULT_META_DESCRIPTION"],
        "url": config["SITE_URL"],
    }

    # ===============================
    # Schema.org Structured Data
    # ===============================
    structured_data = {
        "@context": "https://schema.org",
        "@type": "FinancialProduct",
        "name": "EMI Calculator Pro",
        "description": config["DEFAULT_META_DESCRIPTION"],
        "url": config["SITE_URL"],
        "provider": {
            "@type": "Organization",
            "name": config["SITE_NAME"]
        }
    }

    # ===============================
    # Feature Flags
    # ===============================
    features = {
        "pdf": config["ENABLE_PDF_EXPORT"],
        "comparison": config["ENABLE_LOAN_COMPARISON"],
        "prepayment": config["ENABLE_PREPAYMENT_SIMULATOR"],
        "currency": config["ENABLE_CURRENCY_CONVERSION"],
        "ads": config["ENABLE_ADS"]
    }

    return render_template(
        "index.html",
        seo=seo_data,
        structured_json=json.dumps(structured_data),
        features=features,
        adsense_client=config["ADSENSE_CLIENT_ID"]
    )

from flask import Blueprint, render_template, current_app, Response
from datetime import datetime

@web_main_bp.route("/sitemap.xml", methods=["GET"])
def sitemap():

    base_url = current_app.config.get("SITE_URL", "https://smart-emi-hub-pro.onrender.com")

    pages = []

    # Static Pages
    static_urls = [
        "",
        "/calculator/",
        "/calculator/home-loan-emi-calculator",
        "/calculator/car-loan-emi-calculator",
        "/calculator/personal-loan-emi-calculator",
        "/calculator/sip-calculator",
        "/calculator/fd-calculator",
        "/calculator/rd-calculator",
        "/calculator/gst-calculator",
        "/calculator/retirement-calculator",
        "/about",
        "/contact",
        "/privacy",
        "/terms",
        "/disclaimer"
    ]

    for url in static_urls:
        pages.append({
            "loc": f"{base_url}{url}",
            "lastmod": datetime.utcnow().date().isoformat()
        })

    sitemap_xml = render_template("sitemap.xml", pages=pages)

    return Response(sitemap_xml, mimetype="application/xml") 

@web_main_bp.route("/robots.txt")
def robots():

    base_url = current_app.config.get("SITE_URL", "https://smart-emi-hub-pro.onrender.com")

    content = f"""
User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

    return Response(content, mimetype="text/plain")

@web_main_bp.route("/ads.txt")
def ads_txt():
    return Response(
        "google.com, pub-2031854006818432, DIRECT, f08c47fec0942fa0",
        mimetype="text/plain"
    )  