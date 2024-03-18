import string

def password_strength(password):
    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }
    
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    score = length // 4 + has_uppercase + has_lowercase + has_digit + has_special
    
    if score < 3:
        return strength[0]
    elif score < 5:
        return strength[1]
    elif score < 7:
        return strength[2]
    elif score < 9:
        return strength[3]
    else:
        return strength[4]

password = input("Enter your password: ")
print("Password strength:", password_strength(password))
