# vim:fileencoding=utf-8:foldmethod=marker
# 25. Write a Python program to create a Caesar encryption.

# This is going to be my most favorite one.

# Insha'Allah
# Import libraries {{{
from sys import argv
#}}}

# Provided Data {{{
usernames_and_passwords = {} # Makeshift database

print("What will be your username?")
username = input('--> ')
print("What will be your password?")
password = input('--> ')

key = 3  #Important in Caesar encryption
#}}}

# Encrypt function {{{
def encryption(password):
    list1 = []
    for i in password:
        encrypted_ascii_code = ord(i) - key # encrypted_ascii_code = (ascii code of i) - key
        list1.append(chr(encrypted_ascii_code)) # Turn that back into a character
    result = ''.join(list1)
    return result
#}}}

# Decrypt Function {{{
def decrypt_password(password):
    list2 = []
    for i in password:
        decrypted_ascii_code = ord(i) + key  # decrypted_ascii_code = (ascii code of i) + key
        list2.append(chr(decrypted_ascii_code))  # Same as line 27
    result = ''.join(list2)
    return result
#}}}

the_password_we_dont_know = encryption(password)
usernames_and_passwords[username] = the_password_we_dont_know 

print('\nAccount creation Successful! You can now login with your credentials\n')

# The Login {{{

input_usrnam = input('Username: ')
a = 0  # Count the number of tries
if input_usrnam in usernames_and_passwords.keys():
    input_psword = input('Password: ')
    # while encrypted password != stored_password AND the number of tries < 3:
    # This loop will continue until the password matches
    while encryption(input_psword) != usernames_and_passwords[input_usrnam] and a < 3: 
        input_psword = input('Wrong password. Try again: ')
        a = a + 1 
    if encryption(input_psword) == usernames_and_passwords[input_usrnam]: 
        print('Login Successful with Caesar encryption 🟢')
    else:
        print("Login failed ❌")
else:
    print("Username Not Found ❌")
#}}}

# Dubug and other info function {{{
# Have a little debugging option as well. But I don't know if it will work on colabatory. To make the debug options work, copy this and make a sample.py file and add run 'python3 sample.py debug'

if len(argv) == 1: # If there is no argument after "python3 simple.py"
    pass
elif len(argv) > 1 and str(argv[1]) == 'debug':
    print('\n\n' + '-' * 100 + '\nDEBUG')  # What is this?? Run to find out
    print(usernames_and_passwords) # gives all the usernames and passwords(encrypted)
    for i in usernames_and_passwords.values():
        print(decrypt_password(i))
    print(key)
#}}}
