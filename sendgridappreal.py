# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:23:41 2019

@author: Davis
"""
import json
import os
import urllib.request
from sendgrid.helpers.mail import *
from sendgrid import *
import os 
from flask import Flask, render_template, request
import flask
app = Flask(__name__)


@app.route("/")
@app.route("/email")
def email():
    return render_template("send_email.html")

@app.route("/send", methods=['POST'])
def send():
    sg = sendgrid.SendGridAPIClient('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')
    mail= format(request.form['email'])
    from_email = Email("up785062@myport.ac.uk")
    subject = "subject"
    to_email = Email(mail)
    cc_email = Email("up785062@myport.ac.uk")
    p = Personalization()
    p.add_to(to_email)
    p.add_cc(cc_email)
    content = Content("text/plain", "and easy to do anywhere, even with Python Test")
    mail = Mail(from_email, subject, to_email, content)
    mail.add_personalization(p)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return render_template("finished.html")

if __name__ == "__main__":
    app.run(debug = False, threaded = False)
    