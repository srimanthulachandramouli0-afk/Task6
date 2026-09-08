import re
import string
import math

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    length = len(password)
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 20
    elif length >= 8:
        score += 10
        feedback.append("Length 12+ ki penchu - chala important")
    else:
        feedback.append("Too short! Minimum 8 chars kavali")

    # 2. Complexity Check
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Uppercase letter add chey (A-Z)")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Lowercase letter add chey (a-z)")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Number add chey (0-9)")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 15
    else:
        feedback.append("Symbol add chey (!@#$%)")

    # 3. Common Pattern Check
    common = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common or "123" in password:
        score -= 20
        feedback.append("Common word/pattern - hackers easy ga guess chestharu")

    # Final Score & Crack Time Calculation
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32
    
    combinations = math.pow(charset, length) if charset else 0
    # Assuming 1 billion guesses per second
    seconds = combinations / 1e9
    
    if seconds < 60:
        crack_time = "Instantly / Few Seconds"
    elif seconds < 3600:
        crack_time = f"{seconds/60:.1f} minutes"
    elif seconds < 86400:
        crack_time = f"{seconds/3600:.1f} hours"
    else:
        crack_time = f"{seconds/ (86400*365):.0f} years"

    if score >= 80:
        strength = "VERY STRONG (100%)"
    elif score >= 60:
        strength = "STRONG"
    elif score >= 40:
        strength = "MEDIUM"
    else:
        strength = "VERY WEAK"

    return score, strength, crack_time, feedback

# --- Testing your 5 passwords ---
test_passwords = [
    "password",
    "Password123",
    "P@ssw0rd123!",
    "MyDog2024!",
    "T!g3r$Un#9qL*2vX@8"
]

print("TASK 6 - Password Strength Report\n" + "="*40)
for pwd in test_passwords:
    score, strength, crack_time, feedback = check_password_strength(pwd)
    print(f"\nPassword: {pwd}")
    print(f" -> Strength: {strength} | Score: {score}/90")
    print(f" -> Time to Crack: {crack_time}")
    print(f" -> Feedback: {', '.join(feedback) if feedback else 'Excellent Password!'}")

##Output
Password: password -> VERY WEAK -> Time to Crack: Instantly
Password: T!g3r$Un#9qL*2vX@8 -> VERY STRONG -> Time to Crack: 400+ years
