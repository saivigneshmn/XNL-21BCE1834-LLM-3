from twilio.rest import Client

def send_sms_alert(message):
    account_sid = "AC924210xx5ba8b3d469ca"
    auth_token = "787fa04fc8xxdc603d238a99b2a"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_="+19516183447",
        to="++916303308486"
    )
    print(f"SMS Sent: {message.sid}")

if __name__ == "__main__":
    send_sms_alert("Fraudulent transaction detected!")