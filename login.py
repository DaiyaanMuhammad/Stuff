#####################################################################
#                                                                                                  #
#                        Making a login system with multiple users                                 #
#                                                                                                  #
####################################################################################################

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
    if (users_with_passwords[new_user] == new_password):
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

####################
 #                #
 #      BUGS      #
 #                #
####################

#V1 (11/6/2021)

#  Right now the for loop causes the keys in users_with_passwords to repeat.      [                      ] 
#  So the varification continues for the other users even if login is successful. [  |---   |--- |---\   ]
#  I'm sure this can be sloved through very simple solutions.                     [  |- .   |-   |    )  ]
#  For now, this is the best I can do.                                            [  |  | X |--- |---/   ]

#V2 (13/6/2021)

#  Now if you give a wrong usename at the start, it will not show the "Wrong username" logic [Fixed]

#V3 (28/6/2021)

# There is no known bug in this code. Just missing the comments.


