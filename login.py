##################################################################################
#                                                                                                  #
#                        Making a login system with multiple users                                 #
#                                                                                                  #
####################################################################################################




# First we make some users. We are going to use dictionaries for this. Creating new users is a coming soom feature.

users_with_passwords = {
        'Daiyaan':'Password',
        'Muhammad':'Password2',
        'Fardeen':'Password3',
        'Mustafiz':'PasswordM',
        'Fahim':'Islam',
        'Vladmir':'Makarov',
        'Someone':'Random'
}

# Right now we have 3 users. Although we can edit this .py file manually to add users and passwords. But it would be a security flow that will alow some users to see each others credentials.

print('Type "login" or "sign up"')
login_or_signup = str(input())

if (login_or_signup == "login"):
    login_username = str(input("Username: ")) #We ask for the Username 
    for i in users_with_passwords.keys(): 
        if (login_username == i):    #I initially tried to do if (login_password == "Username: " + i), but it was not the way. Although jupyter notebook showed me otherwise.
            login_password = str(input("Password: ")) #We ask for the password.

            #Now the if the login_username is true, that variable should be a valid key of the dictionary. So we just index the value of the key by using the variable, not a constant value.

            if (login_password == users_with_passwords[login_username]):   
                print("Login successful!!")   #Login is a success. You can add other stuff after this.
                break
            else:
                print("Username and password not same.")
        elif (login_username != i):
            continue
        # The two upper lines (The elif one) contains some trial, failure and success codes.
        # They are there because if the username is correct on the for loops first try, then it works perfectly.
        # But if the username not the first one, the for loop goes through the keys and sees the input username is != to the keys.
        # So from logic, for loops prints the 'Wrong username' everytime it encounters a wrong username. But the input username is also true, so it also asks for password which it should not do.
        # So we use somethings called break and continue.
        # If the login is successful, the loops breaks and doesn't check if the other 'i' values are matching or not
        # If the input username is not matching with the first username in the users_with_passwords.keys(),
        else:
            print("Wrong username!")
            break
elif (login_or_signup == "sign up"):
    print("We're sorry. This feature is coming soon!") #TODO
else:
    print("This is not debuging. Stop fooling around.")

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

#  Now if you give a wrong usename at the start, it will not show the "Wrong username" logic


