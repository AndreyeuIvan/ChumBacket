'''Send email's withh attchement'''
from email.message import EmailMessage
import smtplib

EMAIL = 'andreev.ivan@sunpharma.org'
PASSWORD = '$unp#@rm@'

msg = EmailMessage()

msg['Subject'] = 'Email using python'
msg['From'] = EMAIL
msg['To'] = ['ferfef@mail.ru']

message = 'This email is generated by Python'
msg.set_contest(message)

attachments = ['C:\\USers\\']

for path in attachments:
    with open(path, 'rb') as file:
        data = file.read()
        name = path.split('\\')[-1]

    msg.add_attachment(data.maintype = 'application',
                       subtype = 'octet-stream',
                       filename = name)

with smtplib.SMTP_SSL('smtp.gmail,com', 465) as smtp:
    smtp.login(EMAIL.PASSWORD)
    smtp.send_message(msg)
    
