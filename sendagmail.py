# This is a function, that sends a gmail.
# It relies on a credentials.yml to be next to the main

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import yaml  # To load saved login credentials from a yaml file


# Sendamail currently untested without an attachment.
def sendagmail(toaddr, attach_path, subject, body_text):
    with open("credentials.yml") as f:
        content = f.read()

    # from credentials.yml import user name and password
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)

    # Load the user name and passwd from yaml file
    fromaddr, password, attachment_shownfilename = my_credentials["user"], my_credentials["password"], my_credentials["attachment_shownfilename"]

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = body_text

    msg.attach(MIMEText(body, 'plain'))

    filename = attachment_shownfilename # This row expects a filename. Using attachpath works only if attachpath is just a filename next to the main
    attachment = open(attach_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
