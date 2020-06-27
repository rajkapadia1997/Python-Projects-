import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client 

# def SMS_bot(text):
#     account_sid = ‘.…………………… ‘
#     auth_token = ‘…………………….’ 
#     client = Client(account_sid, auth_token) 
    
#     message = client.messages.create( 
#                                 from_=‘+__ ___ ___ ____’,  
#                                 body=text,      
#                                 to=‘+__ ___ ___ ____’ 
#                             ) 

def emailbot(dataDict):
    port = 587
    smtp_server = "smtp.gmail.com"

    subject = dataDict["subject"]
    sender_email = "............."
    receiver_email = "............."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # Add body to email
    body = dataDict["info"]

    # write the HTML part
    html = dataDict["html"]

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(body, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    # send your email
    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as server:
        server.ehlo()
        server.starttls()
        server.login("sender_email", "password")
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()
    print('Sent')