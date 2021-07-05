# 25. Write a Python program to create a Caesar encryption.

# This is going to be my most favorite one.

# Insha'Allah
from sys import argv#-------------------------------------------------------------------> We import a small system library to get multiple cmd arguments

usernames_and_passwords = {}#-----------------------------------------------------------> This is where we will store all the usernames and passwords

print("What will be your username?")
username = input('--> ')
print("What will be your password?")
password = input('--> ')

key = 3#--------------------------------------------------------------------------------> This is important in any sort of encryption. The amount of shift. In Caesar encryption, the keys in 3

def encrypted_password(password):#------------------------------------------------------> We define a little function to encrypte a string.
    list1 = []
    for i in password:
        encrypted_ascii_code = ord(i) - key#--------------------------------------------> ord(i) gives us the ascii code of any given character. To encrypt that, all we have to do is just minus 3 ascii value from it
        list1.append(chr(encrypted_ascii_code))#----------------------------------------> When we have the encrypted ascii code, we turn it back to a character and then append that to an empty list
    result = ''.join(list1)#------------------------------------------------------------> We can't have lists as passwords, can we?
    return result

def decrypt_password(password):#--------------------------------------------------------> This is another function for decrypting a string
    list2 = []
    for i in password:
        decrypted_ascii_code = ord(i) + key#--------------------------------------------> For every character in the encrypted password, we turn it back to ascii code and 'ADD' the key back.
        list2.append(chr(decrypted_ascii_code))#----------------------------------------> Then just append all of them to an empty list
    result = ''.join(list2)#------------------------------------------------------------> Passwords are not lists. Remember?
    return result

the_password_we_dont_know = encrypted_password(password)

usernames_and_passwords[username] = the_password_we_dont_know#--------------------------> Add the username and the password in the dictionary.

print('\nAccount creation Successful! You can now login with your credentials\n')#------> If it is added, we have a successful account creation. 

# Now the login

input_usrnam = input('Username: ')

if input_usrnam in usernames_and_passwords.keys():#-------------------------------------> Check if the input_usrnam is in the database or not 
    input_psword = input('Password: ')#-------------------------------------------------> if it is, ask for password.
    if encrypted_password(input_psword) == usernames_and_passwords[input_usrnam]:#------> Firstly, encrypted_password the input. Then if it matched with the users password in the database,
        print('Login Successful with Caesar encryption 🟢')#----------------------------> It is a success!!
    else:
        print("Login failed ❌")#-------------------------------------------------------> If it doesn't
else:
    print("Username Not Found ❌")#-----------------------------------------------------> This is if the username is not matching any thing in the usernames_and_passwords.keys()

    


# Have a little debugging option as well. But I don't know if it will work on colabatory. To make the debug options work, copy this and make a sample.py file and add run 'python3 sample.py debug'

if len(argv) == 1:#---------------------------------------------------------------------> If there is only one argument, like "python simple.py" just pass this whole logic system
    pass
elif len(argv) > 1 and str(argv[1]) == 'debug':#----------------------------------------> But if there is more than one and the second argument 'python simple.py {second argument}' is equal to 'debug',
    print('\n\n' + '-' * 100 + '\nDEBUG')#----------------------------------------------> Then print the debuggings
    print(usernames_and_passwords)#-----------------------------------------------------> print the whole database of users and passwords
    for i in usernames_and_passwords.values():
        print(decrypt_password(i))#-----------------------------------------------------> Decrypt every encrypted password
    print(key)#-------------------------------------------------------------------------> Print the main key


