# CodeAlpha Secure Coding Review - Vulnerable Login Example
# WARNING: This file is intentionally insecure for educational review purposes.

users = {
    "admin": "admin123",
    "hayden": "password123"
}

print("=== Simple Login System ===")
username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login successful. Welcome", username)
else:
    print("Invalid login details")
