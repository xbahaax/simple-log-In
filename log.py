import getpass
import hashlib
import os

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def save_credentials(username: str, hashed_password: str):
    with open("credentials.txt", "a") as file:  
        file.write(f"{username}:{hashed_password}\n")

def load_credentials() -> dict:
    users = {}
    if os.path.exists("credentials.txt"):  
        with open("credentials.txt", "r") as file:
            for line in file:
                username, hashed_password = line.strip().split(":")
                users[username] = hashed_password
    return users

def login(username: str, password: str, users: dict) -> bool:
    if username in users:
        if hash_password(password) == users[username]:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found.")
        return False

if __name__ == "__main__":
    users = load_credentials()
    register = input("Do you want to register a new user? (yes/no): ").strip().lower()
    if register == 'yes':
        username = input("Enter a new username: ")
        password = getpass.getpass("Enter a new password: ") 
        hashed_password = hash_password(password)
        save_credentials(username, hashed_password)
        print("User registered successfully!")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    login(username, password, users)
