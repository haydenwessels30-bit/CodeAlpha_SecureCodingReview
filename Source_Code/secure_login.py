# CodeAlpha Secure Coding Review - Improved Login Example
# This version demonstrates safer coding practices for a basic login system.

import hashlib
import hmac
import getpass

# Passwords are stored as SHA-256 hashes for demonstration purposes.
# In real applications, use bcrypt, Argon2, or PBKDF2 with a unique salt per user.
users = {
    "admin": hashlib.sha256("StrongAdminPassword!2026".encode()).hexdigest(),
    "hayden": hashlib.sha256("SecurePassword!2026".encode()).hexdigest()
}

MAX_ATTEMPTS = 3

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_username(username: str) -> bool:
    return username.isalnum() and 3 <= len(username) <= 20

print("=== Secure Login System ===")

for attempt in range(1, MAX_ATTEMPTS + 1):
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if not is_valid_username(username):
        print("Invalid username format.")
        continue

    stored_hash = users.get(username)
    entered_hash = hash_password(password)

    if stored_hash and hmac.compare_digest(stored_hash, entered_hash):
        print("Login successful.")
        break
    else:
        print("Invalid login details.")

    if attempt == MAX_ATTEMPTS:
        print("Too many failed login attempts. Account temporarily locked.")
