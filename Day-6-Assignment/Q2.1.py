
def check_password(password):
    has_digit=False
    has_lower=False
    has_upper=False

    if(len(password)!=8):
        print("Not a valid password it must be 8 characters")
        return
    for ch in password:
        if ch.isdigit():
            has_digit=True
        elif ch.islower():
            has_lower=True
        elif ch.isupper():
            has_upper=True
    if has_digit and has_lower and has_upper:
        print("strong password")
    else:
        print("weak password")

password=input("Enter a strong password:")
check_password(password)
