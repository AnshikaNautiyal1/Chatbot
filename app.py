from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory user storage for demonstration purposes
users = {}

@app.route('/')
def index():
    return render_template('index.html')  # Ensure your HTML file is named index.html

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if the user exists and the password is correct
    if email in users and users[email] == password:
        return jsonify({"message": "Logged in successfully!"}), 200
    else:
        return jsonify({"message": "Invalid email or password."}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    if email in users:
        return jsonify({"message": "User  already exists."}), 409

    # Store the user
    users[email] = password
    return jsonify({"message": "Signed up successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
