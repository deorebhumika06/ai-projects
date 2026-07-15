import os

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Twilio Credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Your Twilio phone number

# Recipients
WHATSAPP_RECIPIENTS = ["whatsapp:+1234567890"]  # List of WhatsApp numbers
SMS_RECIPIENTS = ["+1234567890"]  # List of SMS numbers

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_IDS = [123456789]  # List of chat IDs

# Email
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENTS = ["recipient@example.com"]