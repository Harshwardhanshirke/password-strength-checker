import string

password = input("Enter your password: ")


has_upper = False
has_lower = False
has_digit = False
has_special = False


if len(password) < 8:
    print("Weak (Password must be at least 8 characters long)")
else:

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True


    score = 0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 1:
        print("Weak")
    elif score == 2 or score == 3:
        print("Medium")
    else:
        print("Strong")
