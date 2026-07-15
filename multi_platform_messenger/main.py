from openai import OpenAI
import os
from twilio.rest import Client
import telegram
import smtplib
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
import config

# Basic config validation (add more checks as needed)
required_config = [
    'OPENAI_API_KEY', 'TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_PHONE_NUMBER',
    'TELEGRAM_BOT_TOKEN', 'EMAIL_SENDER', 'EMAIL_PASSWORD',
    'WHATSAPP_RECIPIENTS', 'SMS_RECIPIENTS', 'TELEGRAM_CHAT_IDS', 'EMAIL_RECIPIENTS'
]
for attr in required_config:
    if not hasattr(config, attr) or not getattr(config, attr):
        raise ValueError(f"Missing or empty config attribute: {attr}")

client_openai = OpenAI(api_key=config.OPENAI_API_KEY)

def generate_message(prompt):
    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You write clear, professional messages."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating message: {e}")
        return None

def send_whatsapp(message, recipient):
    try:
        twilio_client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
        twilio_client.messages.create(
            body=message,
            from_=f"whatsapp:{config.TWILIO_PHONE_NUMBER}",
            to=recipient
        )
        print(f"WhatsApp message sent to {recipient}")
    except Exception as e:
        print(f"Error sending WhatsApp to {recipient}: {e}")

def send_sms(message, recipient):
    try:
        twilio_client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
        twilio_client.messages.create(
            body=message,
            from_=config.TWILIO_PHONE_NUMBER,
            to=recipient
        )
        print(f"SMS sent to {recipient}")
    except Exception as e:
        print(f"Error sending SMS to {recipient}: {e}")

def send_telegram(message, chat_id):
    try:
        bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=chat_id, text=message)
        print(f"Telegram message sent to chat {chat_id}")
    except Exception as e:
        print(f"Error sending Telegram to {chat_id}: {e}")

def send_email(message, recipient):
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'Generated Message'
        msg['From'] = config.EMAIL_SENDER
        msg['To'] = recipient

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.sendmail(config.EMAIL_SENDER, recipient, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

def send_to_all_platforms(message):
    if not message:
        print("No message to send.")
        return
    with ThreadPoolExecutor() as executor:
        # WhatsApp
        for recipient in config.WHATSAPP_RECIPIENTS:
            executor.submit(send_whatsapp, message, recipient)
        # SMS
        for recipient in config.SMS_RECIPIENTS:
            executor.submit(send_sms, message, recipient)
        # Telegram
        for chat_id in config.TELEGRAM_CHAT_IDS:
            executor.submit(send_telegram, message, chat_id)
        # Email
        for recipient in config.EMAIL_RECIPIENTS:
            executor.submit(send_email, message, recipient)

if __name__ == "__main__":
    prompt = input("Enter the prompt for the message: ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
    else:
        generated_message = generate_message(prompt)
        if generated_message:
            print(f"Generated message: {generated_message}")
            send_to_all_platforms(generated_message)
        else:
            printP