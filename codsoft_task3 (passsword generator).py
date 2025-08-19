import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password_list = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    
    for _ in range(length - 4):
        password_list.append(random.choice(all_characters))

    random.shuffle(password_list)

    
    return "".join(password_list)

def main():
    try:
       
        length = int(input("How many characters would you like your password to be (minimum 4)? "))
        if length < 4:
            print("To ensure a strong and complex password, the length must be at least 4.")
        else:
           
            generated_password = generate_password(length)
            print("-" * 50)
            print(f"Here is your new, secure password: {generated_password}")
            print("-" * 50)

    except ValueError:
       
        print("Oops! That doesn't look like a number. Please enter a whole number.")

if __name__ == "__main__":
    main()