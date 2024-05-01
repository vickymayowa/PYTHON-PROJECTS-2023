import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace 'smtp.example.com' with your SMTP server
    smtp_server.starttls()  # Start TLS encryption
    smtp_server.login(sender_email, sender_password)  # Login to your email account

    # Construct the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())

    # Quit the SMTP server
    smtp_server.quit()

# Example usage
sender_email = 'your email '
sender_password = 'your pasword'
recipient_email = 'favouradebanjo2@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent from Python.'

send_email(sender_email, sender_password, recipient_email, subject, message)
print("Email Sent !!")
