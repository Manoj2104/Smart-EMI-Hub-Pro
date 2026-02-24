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