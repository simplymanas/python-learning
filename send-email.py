import email, smtplib, ssl, socket

senderEmail = "manas.dash@tesco.com"
receiverEmail = "manas.dash@tesco.com"
password = ""

print("sending email")
smtpDtl = smtplib.SMTP('smtp.office365.com', 587)
smtpDtl.starttls()
smtpDtl.login(senderEmail, password)
smtpDtl.sendmail(receiverEmail, senderEmail, 'Subject: kuch nahi re bhai')
print("sent")
