import requests
import smtplib
from emaillogin import *
import Adafruit_DHT as ada
TO = 'sidd.ghosh9@gmail.com'
SUBJECT = 'Temp and humidity'
humd,temp=ada.read_retry(11,4)
TEXT = 'Humidity:-'+str(humd) +'\ntemperature:-'+str(temp)

# Gmail Sign In
gmail_sender = id1
gmail_passwd = pas

server = smtplib.SMTP('smtp.gmail.com', 587) #587 is default portno of smtplib
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', str(TEXT)])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print('email sent')
    r=requests.post('https://maker.ifttt.com/trigger/email/with/key/ctIa-jIR1N1bhvYRLIR7zs')
except:
    print('error sending mail')

server.quit()
