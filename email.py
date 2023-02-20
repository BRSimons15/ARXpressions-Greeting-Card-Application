# import requests;
#
#
# def send_simple_message():
#     return requests.post(
#         "https://api.eu.mailgun.net/v3/sandboxec7aa5b7840c44eab6fa6e4d93af53cb.mailgun.org/messages",
#         auth=("api", "5edf54d2c089c7c8cbfe1cb0b0411df1-8d821f0c-ba6ca6e8"),
#         data={"from": "Mailgun Sandbox <postmaster@sandboxec7aa5b7840c44eab6fa6e4d93af53cb.mailgun.org>",
#               "to": "Bjorn Boi45 <ptedectyl55@gmail.com>",
#               "subject": "Hello Bjorn Boi45",
#               "text": "Congratulations Bjorn Boi45, you just sent an email with Mailgun!  You are truly awesome!"})



import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = "foo@YOUR_DOMAIN_NAME"
msg['To']      = "bar@example.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.
