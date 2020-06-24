import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("senter mail id", "password") 
message = ""
s.sendmail("senter mail id", "reciver mail id", message) 
s.quit() 
