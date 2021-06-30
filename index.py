import os
import smtplib
import csv
import imghdr
from email.message import EmailMessage

body = '''Dear Sir/Madam
In response to the Internship announcement. I am writing this mail as I think I am an eligible candidate for ---.

Please find my CV attached in this email.
Thank You.

Yours Sincerely,
Rishi Raj Shrestha'''

SENDER_ADDRESS = os.environ.get('EMAIL')
SENDER_PASSWORD = os.environ.get('PASSWORD')

with open('data.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        receiver = row["name"]
        subject = row['subject']
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = SENDER_ADDRESS
        msg['To'] = receiver
        msg.set_content(body)
        files = ['Rishi Raj Shrestha_CV.pdf']
        
        for file in files:
            with open(file, 'rb') as pdf:
                read_file = pdf.read()
                file_name = pdf.name
        msg.add_alternative(read_file, maintype='application', subtype='octet-stream', filename = file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_ADDRESS, SENDER_PASSWORD)
            smtp.send_message(msg)