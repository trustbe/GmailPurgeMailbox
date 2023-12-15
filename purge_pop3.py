import poplib
import email

#This script is designed to delete emails from a Gmail account using the POP3 protocol. 

def delete_emails(user, password):
	mail = poplib.POP3_SSL('pop.gmail.com')
	mail.user(user)
	mail.pass_(password)

	num_messages = len(mail.list()[1])
	for i in range(num_messages):
		print (i)
		mail.retr(i+1)
		mail.dele(i+1)

	mail.quit()

# Replace with your Gmail email and password
email = "XXX"
password = "XXX"

delete_emails(email, password)
