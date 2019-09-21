# !/usr/bin/python
# -*- coding:Utf-8 -*-

import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib.request
import urllib.error


def create_config():
    config = configparser.ConfigParser()
    config['SMTP'] = {
        'Host': 'smtp.gmail.com',
        'Email': 'toto@toto.com',
        'Password': '123456'
    }
    config['Sender'] = {
        'From': 'titi@tutu.com'
    }
    config['Receiver'] = {
        'To': 'lolo@gege.com'
    }
    with open('config.ini', 'w') as config_file:
        config.write(config_file)


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


# -----
# MAIN
# -----
if __name__ == "__main__":
    page = urllib.request.urlopen('http://www.paroles.net/gold/paroles-capitaine-abandonne')
    str_page = page.read()

    soup = BeautifulSoup(str_page, 'html.parser')

    y = ''

    for x in soup.find_all(class_="song-text"):
        y = x.get_text()
        # y += x.encode('cp850').replace('<br>', '').replace('</br>', '')

    y = y.replace('\n\n', '\n')
    y = y.replace('\t', '')
    y = y.replace('  ', '')

    y = y.splitlines()

    sortie = ''
    for ligne in y:
        if ligne[:3] == 'eva':
            pass
        else:
            sortie += ligne + '\n'

    print(sortie)

    msg = MIMEMultipart()
    msg['From'] = 'MYGMAILADDRESS@gmail.com'
    msg['To'] = 'USER@DOMAIN.XYZ'
    msg['Subject'] = '[PiParoles] Paroles du jour'
    msg['Content-Type'] = "text/html; charset=cp850"
    message = sortie
    msg.attach(MIMEText(message))

    # mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    # mail_server.ehlo()
    # mail_server.starttls()
    # mail_server.ehlo()
    # mail_server.login('MYGMAILADDRESS@gmail.com', 'MYSUPERSECRETPASSWORD')
    # mail_server.sendmail('FROM@gmail.com', 'TO@DOMAINE.XYZ', msg.as_string())
    # mail_server.quit()
