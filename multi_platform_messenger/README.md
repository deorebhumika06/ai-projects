# Multi-Platform Messenger with Generative AI

This hackathon project demonstrates a generative AI-powered messaging system that sends the same message simultaneously across multiple platforms: WhatsApp, SMS, Telegram, and Email.

## Features

- Uses OpenAI's GPT-4o-mini to generate professional messages based on user prompts.
- Sends messages concurrently to multiple recipients on different platforms.
- Supports WhatsApp, SMS (via Twilio), Telegram, and Email.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `TWILIO_ACCOUNT_SID`: Twilio Account SID.
   - `TWILIO_AUTH_TOKEN`: Twilio Auth Token.
   - `TWILIO_PHONE_NUMBER`: Your Twilio phone number (for SMS and WhatsApp).
   - `TELEGRAM_BOT_TOKEN`: Telegram bot token.
   - `EMAIL_SENDER`: Your email address.
   - `EMAIL_PASSWORD`: Your email password (use app password for Gmail).

3. Configure recipients in `config.py`:
   - Update `WHATSAPP_RECIPIENTS`, `SMS_RECIPIENTS`, `TELEGRAM_CHAT_IDS`, `EMAIL_RECIPIENTS`.

## Usage

Run the script:
```
python main.py
```

Enter a prompt when asked, and the generated message will be sent to all configured recipients on all platforms simultaneously.

## Note

- For WhatsApp, ensure your Twilio number is enabled for WhatsApp.
- For Telegram, create a bot and get chat IDs.
- For Email, use SMTP settings compatible with your provider (example uses Gmail).

## Validation

To validate the code:
```
python -m py_compile main.py
```

This checks for syntax errors.