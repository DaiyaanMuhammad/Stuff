users_with_passwords = {
        'Daiyaan':'Password',
        'Muhammad':'Password2',
        'Fardeen':'Password3',
        'Mustafiz':'PasswordM',
        'Fahim':'Islam',
        'Vladmir':'Makarov',
        'Someone':'Random'
}

LogOrSign = input("Do you want to.. \n[1]Login or [2]Sign in\n--> ")

if (LogOrSign == '2'):
    new_user = input("Name for the new user:\n--> ")
    new_password = input("Password:\n--> ")
    users_with_passwords[new_user]=new_password
    print("Sign in successful!! Loging in as", new_user)
    client_value = input("Password: ")
    if (users_with_passwords[new_user] == client_value):
        print("Login Successful!!")
    else:
        print('The password was wrong.')
elif (LogOrSign == '1'):
    client_key = input("Username: ")
    if client_key in users_with_passwords.keys():
        client_value = input("Password: ")
        if (users_with_passwords[client_key] == client_value):
            print("Login Successful!!")
        else:
            print("Wrong password")
    else:
        print("\"",client_key,"\"", "Was not found in the database")
else:
    print("Please input cautiously")
