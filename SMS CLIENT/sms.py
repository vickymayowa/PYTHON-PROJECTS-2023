from twilio.rest import Client

def send_sms(to, body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'
    client = Client(account_sid, auth_token) 
    try:
        message = client.messages.create(
            to=to,
            from_=twilio_phone_number,
            body=body
        )
        print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

def main():
    # Get user input for the phone number
    to_phone_number = input("Enter the recipient's phone number (+1 for USA): ")

    # Get user input for the SMS message
    sms_body = input("Enter the message you want to send: ")

    # Send SMS
    send_sms(to_phone_number, sms_body)

if __name__ == "__main__":
    main()


# kindly install pip install twilio
