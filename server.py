import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, url_for, request,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home-two.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file_data = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        Name = request.form['Name']
        Subject_Text= request.form['Subject']
        Email = request.form['Email']
        Message= request.form['Message']
        HTMLtext= request.form['HTML']
        contactInfo=f'Name= {Name} \nEmail= {Email} \nMessage= {Message}'
        dataDict = {"info": contactInfo, "subject": Subject_Text, "email": Email, "html": HTMLtext}
        emailbot(dataDict)
        # write_to_file(data)
        return 'Message Sent. Thankyou for Connecting.'
    else:
      return 'something went wrong. try again!'

def emailbot(dataDict):
    port = 587
    smtp_server = "smtp.gmail.com"

    subject = dataDict["subject"]
    sender_email = "............."
    receiver_email = "............."

    message = MIMEMultipart()
    message["From"] = #sender_email
    message["To"] = #receiver_email
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
        server.login("#sender_email", "#password")
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()
    print('Sent')
