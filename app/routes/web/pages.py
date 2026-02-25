from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/about")
def about():
    return render_template("about.html")

@pages_bp.route("/privacy-policy")
def privacy():
    return render_template("privacy.html")

from flask import request, flash, redirect, url_for
  # if using Flask-Mail

from flask import request, flash, redirect, url_for, render_template, current_app
from flask_mail import Message
from app.core.extensions import mail


@pages_bp.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message_text = request.form.get("message")

        # Debug: Check if mail config loaded
        print("MAIL USER:", current_app.config.get("MAIL_USERNAME"))
        print("MAIL SERVER:", current_app.config.get("MAIL_SERVER"))

        msg = Message(
            subject="New Contact Message - Smart EMI Hub Pro",
            recipients=[current_app.config.get("MAIL_USERNAME")],
            body=f"""
New Contact Message

Name: {name}
Email: {email}

Message:
{message_text}
"""
        )

        try:
            mail.send(msg)
            print("✅ MAIL SENT SUCCESSFULLY")
            flash("Message sent successfully!", "success")
        except Exception as e:
            print("❌ MAIL ERROR:", str(e))
            flash("Error sending message. Please try again.", "danger")

        return redirect(url_for("pages.contact"))

    return render_template("contact.html")

@pages_bp.route("/terms")
def terms():
    return render_template("terms.html")

@pages_bp.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

# ================================
# 🔥 SEO GUIDE PAGES (2000+ Words)
# ================================

# Core EMI Guides

@pages_bp.route("/guide/what-is-emi")
def what_is_emi():
    return render_template("guide/what-is-emi.html")


@pages_bp.route("/guide/how-emi-is-calculated")
def how_emi_calculated():
    return render_template("guide/how-emi-is-calculated.html")


@pages_bp.route("/guide/emi-formula-explained")
def emi_formula():
    return render_template("guide/emi-formula-explained.html")


@pages_bp.route("/guide/reducing-vs-flat-interest")
def reducing_vs_flat():
    return render_template("guide/reducing-vs-flat-interest.html")


@pages_bp.route("/guide/fixed-vs-floating-interest-rate")
def fixed_vs_floating():
    return render_template("guide/fixed-vs-floating-interest-rate.html")


@pages_bp.route("/guide/amortization-schedule-explained")
def amortization():
    return render_template("guide/amortization-schedule-explained.html")


@pages_bp.route("/guide/how-to-reduce-emi")
def reduce_emi():
    return render_template("guide/how-to-reduce-emi.html")


@pages_bp.route("/guide/emi-and-credit-score")
def emi_credit_score():
    return render_template("guide/emi-and-credit-score.html")


@pages_bp.route("/guide/prepayment-explained")
def prepayment():
    return render_template("guide/prepayment-explained.html")


@pages_bp.route("/guide/home-loan-tax-benefits")
def home_loan_tax():
    return render_template("guide/home-loan-tax-benefits.html")


@pages_bp.route("/guide/is-emi-calculator-free")
def emi_free():
    return render_template("guide/is-emi-calculator-free.html")


# Comparison / Related Topics

@pages_bp.route("/guide/emi-vs-sip")
def emi_vs_sip():
    return render_template("guide/emi-vs-sip.html")


@pages_bp.route("/guide/loan-tenure-explained")
def loan_tenure():
    return render_template("guide/loan-tenure-explained.html")


@pages_bp.route("/guide/how-banks-calculate-emi")
def banks_calculate_emi():
    return render_template("guide/how-banks-calculate-emi.html")


# ================================
# 📄 FAQ PAGE
# ================================

@pages_bp.route("/faq")
def faq():
    return render_template("faq.html")


from flask import send_from_directory

@pages_bp.route("/ads.txt")
def ads_txt():
    return send_from_directory("static", "ads.txt")