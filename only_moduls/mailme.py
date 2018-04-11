#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:06:38 2018
Emailing the captured image
@author: stark
"""
#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
def mail(): 
    fromaddr = "ayushstarksharma@gmail.com"
    toaddr = "ayushstarksharma@gmail.com"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ALERT! Bro there is a Robbrey!"
     
    body = "ALERT!! Intruder Here!! call PewDiePie"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "img.jpg"
    attachment = open("/home/pi/img.jpg", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "imiml33t")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return True