import smtplib, ssl

port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "ww2232785@gmail.com" 
receiver_email = "aa2232786@gmail.com"  
password = "hell@LIFE786"
message = """\
Subject: Hi there

This message is sent from bot."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)