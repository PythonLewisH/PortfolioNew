from flask import Flask, render_template, redirect, url_for, flash, request
import os
from forms import ContactForm
import smtplib
from flask_talisman import Talisman


# Run Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "MySecretKey")

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)


@app.route('/', methods=["GET", "POST"])
def home():
    contact_form = ContactForm()
    if request.method == "GET":
        return render_template("index.html", contact_form=contact_form)
    else:
        if contact_form.validate_on_submit():
            try:
                enquiry_name = contact_form.name.data
                enquiry_email = contact_form.email.data
                enquiry_message = contact_form.message.data

                password = os.getenv("PASSWORD")
                my_email = "lewishudsonpro@outlook.com"
                subject = "ENQUIRY RECEIVED FROM WEBSITE"
                message = 'Subject: {}\n\n{}'.format(subject, f"Enquirer email: {enquiry_email} \n" + f"Enquirer name: "
                                                                                                      f"{enquiry_name} \n" +
                                                     f"Enquirer message: {enquiry_message}")
                server = smtplib.SMTP("smtp-mail.outlook.com", 587)
                server.starttls()
                server.login(my_email, password)
                server.sendmail(my_email, my_email, message)
                server.close()
                flash("Thank you for your enquiry. We will get back to you within 48 hours.")
                return render_template("index.html", contact_form=contact_form)
            except:
                flash("Something went wrong and we could not deliver your message, You can try sending an email instead.")
                print(contact_form.errors)
                return render_template("index.html", contact_form=contact_form)
        else:
            flash("Something went wrong and we could not deliver your message, try sending an email instead.")
            print(contact_form.errors)
            return render_template("index.html", contact_form=contact_form)


if __name__ == "__main__":
    app.run()