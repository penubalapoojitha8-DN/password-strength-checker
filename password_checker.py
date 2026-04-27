import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Lowercase check
    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    # Number check
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks.append("Add numbers.")

    # Special character check
    if re.search("[@#$%^&+=]", password):
        strength += 1
    else:
        remarks.append("Add special characters (@#$%^&+=).")

    # Final result
    if strength == 5:
        return "Strong", ["Good password 👍"]
    elif strength >= 3:
        return "Medium", remarks
    else:
        return "Weak", remarks


# Main program
password = input("Enter your password: ")
result, suggestions = check_password_strength(password)

print("\nStrength:", result)
print("Suggestions:")
for s in suggestions:
    print("-", s)
