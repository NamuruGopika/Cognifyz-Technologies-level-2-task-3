import re

def evaluate_password_strength(password):
    # Initialize strength score
    strength_score = 0
    
    # Check for length (at least 8 characters)
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should contain at least one special character.")
    
    # Assess the overall strength
    if strength_score == 5:
        print("Your password is strong!")
    elif 3 <= strength_score < 5:
        print("Your password is moderate.")
    else:
        print("Your password is weak. Consider making it stronger.")
    
    return strength_score

# Example usage
password = input("Enter your password: ")
evaluate_password_strength(password)