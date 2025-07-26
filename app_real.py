from flask import Flask, request, session, render_template
from datetime import datetime
import json
import pyotp
import requests
import secrets
import smtplib

app = Flask(__name__)

app.secret_key = secrets.token_hex(32)

@app.route('/', methods=['GET'])
def index():
    return render_template('real.html')


@app.route('/login', methods=['POST'])
def login():
    # Support JSON request
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

    # Check if the username and password are correct
    found = False
    with open("database_logins.json", "r", encoding="utf-8") as f:
        records = json.load(f)
        for record in records:
            if record.get("username") == username and record.get("password") == password:
                found = True
                break

    if not found:
        return "Username or Password is incorrect"

    # generate OTP code
    sending_otp()

     # Redirect to the next page
    return render_template('otp.html')


# Replace with your actual Brevo (Sendinblue) API Key and verified email
BREVO_API_KEY = "your-brevo-api-key-here"  # <-- Insert your actual API key here
SENDER_EMAIL = "your-verified-sender@example.com"  # <-- Must match your verified sender

# To send OTP to email
def send_otp_email(to_email, otp_code):
    url = "https://api.brevo.com/v3/smtp/email"
    payload = {
        "sender": {
            "name": "UNIMAS Login",
            "email": SENDER_EMAIL
        },
        "to": [{
            "email": to_email,
            "name": to_email
        }],
        "subject": "🔐 Your OTP Code",
        "htmlContent": f"<h3>Your OTP is: <strong>{otp_code}</strong></h3>"
    }
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    res = requests.post(url, json=payload, headers=headers)
    print("✅ Status:", res.status_code, res.text)
    return res.ok

# to generate OTP
def sending_otp():
    # Try to get email from form data first, then from JSON
    #email = request.form.get("username")

    email = "YOUR EMAIL"
    '''
    if not email:
        data = request.get_json(silent=True)
        if data:
            email = data.get("username")
    if not email or "@" not in email:
        return "Invalid email address", 400
    '''
    # generate base32 private key
    secret = pyotp.random_base32()

    # initalise TOTP (private key, time interval) with 1 min session
    totp = pyotp.TOTP(secret, interval=60)

    # generate otp
    otp = totp.now()

    session["otp"] = otp
    session["email"] = email
    session["otp_time"] = datetime.now().isoformat() # 記錄OTP發送時間

    # send otp to user's email
    send_otp_email(email, otp)

    return "OTP sent successfully"


@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    # Support J0SON request
    if request.is_json:
        data = request.get_json()
        user_otp = data.get("otp")
    else:
        user_otp = request.form.get("otp")

    # Check if OTP is correct
    if user_otp != session.get("otp"):
        return "❌ OTP is wrong"

    return render_template('login_success.html')


if __name__ == '__main__':
    app.run(debug=True)

