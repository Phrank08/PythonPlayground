master_pwd = input("What is the master pasword: ")

def view():
    with open('password.txt', 'r') as myPwdFile:
        for line in myPwdFile.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, "\nPassword:", passwd)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('password.txt', 'a') as myPwdFile:
        myPwdFile.write(name + "|" + pwd + "\n")

        
while True:
    mode = input("Would you like to add a new password or view existing one(s).\nPress\'q\'to quit: ").lower()

    if mode == 'q':
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()