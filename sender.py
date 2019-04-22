import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import logging
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

my_email = "pythoninsta1@gmail.com"
to_email = "kamek1999@gmail.com"
password = "dvdromkamek1"
mail = smtplib.SMTP('smtp.gmail.com', 587)
suffix = ".log"

def send_it(name, suffix):
    try:
        sub = suffix + " | " + datetime.datetime.now().strftime("%B %d %H:%M")
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = to_email
        msg['Subject'] = sub
        body = "chart - " + sub
        msg.attach(MIMEText(body, 'plain'))
        filename = name + suffix
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        text = msg.as_string()
        mail.starttls()
        mail.ehlo()
        mail.login(my_email, password)
        mail.sendmail(my_email, to_email, text)
        mail.close()
        logging.info("Logs sent")
        print("Sent | " + name + suffix)
    except Exception as e:
        print("Couldn't sent | " + name + suffix)
        logging.error("Couldn't sent | " + name + suffix + " | ERROR | " + str(e))
