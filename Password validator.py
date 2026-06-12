# Password Checker

password = input("Enter your password: ")

score = 0

# password Length check
if len(password) >= 8:
    score += 1
else:
    print("Tip: Use at least 8 characters.")

# Uppercase check
if any(char.isupper() for char in password):
    score += 1
else:
    print("Tip: must include an uppercase letter.")

# Lowercase check
if any(char.islower() for char in password):
    score += 1
else:
    print("Tip: must include a lowercase letter.")

# Number check
if any(char.isdigit() for char in password):
    score += 1
else:
    print("Tip: must include a number.")

# Special character check
special_chars = "!@#$%^&*()_+-="
if any(char in special_chars for char in password):
    score += 1
else:
    print("Tip: must include a special character.")

# Display result
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

# Check if all requirements are met
if score == 5:
    print("Password updated successfully! Proceed to login")
else:
    print("Password does not meet all requirements. Try again.")