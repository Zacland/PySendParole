#!/usr/bin/python
#-*- coding:Utf-8 -*-

import smtplib
import logging
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from bs4 import BeautifulSoup, NavigableString
import urllib

page = urllib.urlopen('http://www.paroles.net/gold/paroles-capitaine-abandonne')
strpage = page.read()

soup = BeautifulSoup(strpage)

y=''

for x in soup.find_all(class_="song-text"):
  y = y + x.encode('cp850').replace('<br>','').replace('</br>','')

#print y

msg = MIMEMultipart()
msg['From']    = 'MYGMAILADDRESS@gmail.com'
msg['To']      = 'USER@DOMAIN.XYZ'
msg['Subject'] = '[PiParoles] Paroles du jour'
msg['Content-Type'] = "text/html; charset=cp850"
message        = y
msg.attach(MIMEText(message))
mailserver     = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('MYGMAILADDRESS@gmail.com', 'MYSUPERSECRETPASSWORD')
mailserver.sendmail('FROM@gmail.com', 'TO@DOMAINE.XYZ', msg.as_string())
mailserver.quit()
