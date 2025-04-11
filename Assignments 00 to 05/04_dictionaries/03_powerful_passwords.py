import hashlib

# Simulated hash_password function
def hash_password(password):
    """Simulates hashing a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Simulated stored login information (email: hashed password)
stored_logins = {
    "user@example.com": hash_password("securepassword123"),
    "test@example.com": hash_password("password456"),
}

def login(email, password_to_check):
    """Checks if the password matches the stored hash for the given email"""
    if email in stored_logins:
        # Compare the hashed input password with the stored password hash
        if stored_logins[email] == hash_password(password_to_check):
            return True  
        else:
            return False  
    else:
        return False  

# Sample test cases
print(login("user@example.com", "securepassword123"))  
print(login("user@example.com", "wrongpassword"))     
print(login("test@example.com", "password456"))       
print(login("nonexistent@example.com", "password"))   
