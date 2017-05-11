import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendMail(to, subject, imageFileName):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'soaplaketeam@gmail.com'
    msg['To'] = to
    with open(imageFileName, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('soaplaketeam@gmail.com','xxxxxxxx')
    s.send_message(msg)
    s.quit()