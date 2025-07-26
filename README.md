# 🛡️ Phishing Simulation & OTP-Based Mitigation

This project demonstrates a **phishing attack simulation** using a fake login page, and a **mitigation strategy** using **Time-based One-Time Password (TOTP)** for secure authentication. Built with Python and Flask, the goal is to educate and simulate how impersonation attacks can be carried out and countered effectively.

## 📁 Project Structure

📦 phishing-simulation-otp-mitigation/
├── app_fake.py # Phishing simulation web app
├── app_real.py # Secure login system with OTP
├── static/ # CSS/JS/images used in HTML templates
├── templates/ # HTML pages for both real and fake sites
├── stolencredential.json # Captured credentials from fake site
├── database_logins.json # User credentials for real login system
├── README.md # This file
└── requirements.txt # Python dependencies


## 🧪 Features

### 🔴 `app_fake.py` – Phishing Simulation
- Mimics the look of a real login portal (e.g., eLEAP).
- Captures user credentials silently.
- Prompts user to retry login up to 3 times.
- Redirects to a safe page after 3 failed attempts.
- Stores stolen credentials in `stolencredential.json`.

### ✅ `app_real.py` – MFA Mitigation
- Validates credentials against `database_logins.json`.
- Generates a TOTP-based OTP using `pyotp`.
- Sends OTP to the registered email address.
- Verifies user access with time-sensitive OTP.
- Secure login simulation after OTP success.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Flask
- An SMTP-compatible email (for sending OTP)
- Internet connection (to send emails)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-simulation-otp.git
   cd phishing-simulation-otp

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the phishing simulation:
   ```bash
   python app_fake.py

4. Run the secure OTP login system:
   ```bash
 python app_real.py

 5. Visit the site at http://127.0.0.1:5000

You can only run one of the apps at a time on the same port.

## 📧 OTP Email Setup
To enable email delivery for OTP:

1. Get an SMTP provider or use services like Gmail, SendGrid, Bravo SMTP, etc.

2. Add the SMTP access token or credentials in app_real.py.

3. If using Gmail:

- Enable Less Secure App Access in your Gmail settings.

- Or create an App Password for Gmail with 2FA.

### ⚠️ Important: Add Your Own Email API Key

To send OTP emails, this project uses the [Brevo (formerly Sendinblue)](https://www.brevo.com/) SMTP API. The real API key has been removed for security reasons. 

To run the `app_real.py`, you must:

1. Sign up for a free Brevo account.
2. Go to your Brevo dashboard → SMTP & API → Create an API key.
3. In `app_real.py`, **replace the `BREVO_API_KEY` and `SENDER_EMAIL` placeholders** with your actual credentials:

```python
# Replace these values with your actual API key and verified sender email
BREVO_API_KEY = "your-brevo-api-key-here"
SENDER_EMAIL = "your-verified-sender@example.com"



## 📊 Testing Credentials

Use the following test data for database_logins.json:

[
  {
    "email": "showwky@gmail.com",
    "password": "Kevin#010801130411",
    "secret": "JBSWY3DPEHPK3PXP"
  }
]

For phishing test:

- Any credentials (e.g., kevin@gmail.com / Kevin1234) will be captured.

## 📚 Academic Context

This project was developed as part of the Computer Security (TMS4853) coursework at Universiti Malaysia Sarawak (UNIMAS) to demonstrate both offensive (phishing) and defensive (OTP) security mechanisms in web authentication.

## ⚠️ Disclaimer

This project is strictly for educational purposes only. Do not use this to conduct real phishing attacks or violate ethical guidelines. Always seek consent when testing security-related systems.

## 📃 License

MIT License – feel free to use and adapt with attribution.

## Author

1. Wong Guan Ting

2. Kevin Wong King You

3. Patrick Owen Kuek 

4. Rebecca Lai Yee Enn

5. Ibnu Ameerul bin Abdul Halim
