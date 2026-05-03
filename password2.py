import random
import string
def check_strength(password):
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 12 and strength == 4:
        return "Strong 💪"
    elif len(password) >= 8:
        return "Medium ⚡"
    else:
        return "Weak ⚠️"
def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if characters == "":
        return None
    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    while len(password) < length:
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)
print("🔐 Advanced Password Generator")
while True:
    try:
        length = int(input("\nEnter password length (min 4): "))
        if length < 4:
            print("⚠️ Length should be at least 4")
            continue
    except:
        print("⚠️ Enter a valid number")
        continue
    use_letters = input("Include letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"
    password = generate_password(length, use_letters, use_digits, use_symbols)
    if password is None:
        print("⚠️ Please select at least one character type!")
        continue
    print("\nGenerated Password:", password)
    print("Strength:", check_strength(password))
    again = input("\nGenerate another password? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye 👋")
        break