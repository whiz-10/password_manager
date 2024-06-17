from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)


def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
        return key


key = load_key()
fer = Fernet(key)



def Add():
    name = input("Account name : ")
    pwd = input("Password : ")

    with open('passwords.txt', 'a') as f:
        f.write( name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')

def View():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


while True:
    
    mode = input("Type of Mode : Add or View, q for quit ").lower()

    if mode == "q":
        break

    if mode == "add":
        Add()
    elif mode == "view":
        View()
    else:
        print("Invalid Input!")
        continue