import string
def is_strong(password):
    if len(password) < 8:
        return False
    
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    return has_number and has_special
passwords = []

n = int(input("How many passwords do you want to check? "))

for i in range(n):
    pwd = input(f"Enter password {i+1}: ")
    passwords.append(pwd)
with open("strong.txt", "w") as strong_file, open("weak.txt", "w") as weak_file:
    
    for pwd in passwords:
        if is_strong(pwd):
            strong_file.write(pwd + "\n")
        else:
            weak_file.write(pwd + "\n")

print("\nPasswords have been saved:")
print("- Strong passwords → strong.txt")
print("- Weak passwords → weak.txt")