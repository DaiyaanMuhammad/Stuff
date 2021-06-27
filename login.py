#####################################################################
#                                                                                                  #
#                        Making a login system with multiple users                                 #
#                                                                                                  #
####################################################################################################




# First we make some users. We are going to use dictionaries for this. Creating new users is a coming soom feature.

users_with_passwords = {
        'Daiyaan':'Password',
        'Muhammad':'Password2',
        'Fardeen':'Password3',
        'Mustafiz':'PasswordM',#---------------------------------------------------------> A dictionary to store the usernames and passwords
        'Fahim':'Islam',
        'Vladmir':'Makarov',
        'Someone':'Random'
}

LogOrSign = input("Do you want to.. \n[1]Login or [2]Sign in\n--> ")#--------------------> Prompt to ask what the user wants to do

if (LogOrSign == '2'):#------------------------------------------------------------------> If the user chooses to Signup,

    new_user = str(input("Name for the new user:\n--> "))#-------------------------------> Ask user for the new user name

    new_password = str(input("Password:\n--> "))#----------------------------------------> Ask the user for new password. But this is not a database. New users are not stored within this script

    users_with_passwords[new_user]=new_password#-----------------------------------------> Add the username and the password in the dictionary

    print("Sign in successful!! Loging in as", new_user)#--------------------------------> The new user is added. Now he can login.

    client_value = str(input("Password: "))

    if (users_with_passwords[new_user] == new_password):#--------------------------------> If the given password matches of the stored password, its a login

        print("Login Successful!!")

    else:

        print('The password was wrong.')#------------------------------------------------> If they don't match, the password must be wrong.

elif (LogOrSign == '1'):#----------------------------------------------------------------> Now if the user wants to login directly.

    client_key = str(input("Username: "))#-----------------------------------------------> Ask for username

    if client_key in users_with_passwords.keys():#---------------------------------------> If the username is in the dictionary,

        client_value = str(input("Password: "))#-----------------------------------------> Ask for password.

        if (users_with_passwords[client_key] == client_value):#--------------------------> If the given password matches the stored password,

            print("Login Successful!!")#-------------------------------------------------> It's a login

        else:

            print("Wrong password")#-----------------------------------------------------> If the user is right but he typed the password wrong

    else:

        print("\"",client_key,"\"", "Was not found in the database")#--------------------> If the username was not found.

else:

    print("Please input cautiously")#----------------------------------------------------> If the user chooses to act irratinal

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


