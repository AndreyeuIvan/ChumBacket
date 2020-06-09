import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('Andreev.ivan@sunpharma.org', '')
message = 'Hello World'
s.sendmail('Andreev.ivan@sunpharma.org', 'andreeviv@icloud.com', message)
s.quit()
