
import smtplib
import config
from email.mime.text import MIMEText


server =smtplib.SMTP(config.server_address, config.port)

server.starttls()

server.login(config.sender_mail, config.password)

msg = MIMEText(config.message)
msg['Subject'] = config.subject
msg['From'] = config.sender_mail
msg['To'] = config.to_mail

server.sendmail(config.sender_mail, config.to_mail, msg.as_string())

print("Mail Sent")
server.close()

