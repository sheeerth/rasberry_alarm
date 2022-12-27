import smtplib, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Emailer:
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    GMAIL_USERNAME = 'bartada42@gmail.com'
    GMAIL_PASSWORD = 'lgvbiwmqefplahxa'

    def sendmail(self, recipient, subject, content, image):
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = self.GMAIL_USERNAME

        #Attach our text data
        emailData.attach(MIMEText(content))

        #Create out Image Data from the defined image
        imageData = MIMEImage(open(image, 'rb').read(), 'jpg')
        imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)

        #Connect to Gmail Server
        session = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(self.GMAIL_USERNAME, self.GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(self.GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit