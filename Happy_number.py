

#             ░█░█░█▀█░█▀█░█▀█░█░█░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄░█▀▀
#             ░█▀█░█▀█░█▀▀░█▀▀░░█░░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄░▀▀█
#             ░▀░▀░▀░▀░▀░░░▀░░░░▀░░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀

  # Happy numbers are numbers where each element of the number can be squared added. 
  # The added sum is a new number where if each element of The sum is squared and added together,
  # If the result is 1, it is a happy nubmer 🤩

  #     ⢺  ⢉⡹ -------\   ⡔⠁ ⢺  2  _|_  ⢉⡹ 2 ⠈⢢   ⣀⣀   ⢺  ⣎⣵    ⡔⠁ ⢺ 2 _|_ ⣎⣵ 2⠈⢢   ⣀⣀  ⢺ 
  #     ⠼⠄ ⠤⠜ -------/   ⠣⡀ ⠼⠄     |   ⠤⠜   ⢀⠜   ⠒⠒   ⠼⠄ ⠫⠜,   ⠣⡀ ⠼⠄   |  ⠫⠜  ⢀⠜   ⠒⠒  ⠼⠄

number = int(input("Please insert your happy number 😊:\n👉 "))  #---> Prompt
str_number = str(number)                                         #---> Making it a string
list0 = []                                                       #---> Empty list to do something


for i in str_number:                                             #---> Making the input number into a list. Using the empty list before
    int_elmnt = int(i)
    list0.append(int_elmnt)

SUM0 = 0                                                         #---> Null variable to do a sum

for j in list0:
    SUM0 = SUM0 + (j ** 2)                                       #---> Each element of the number is squared and totaled into the Null variable

str_SUM0 = str(SUM0)                                             #---> Making the SUM0 string again to do another sum of elements

SUM1 = 0                                                         #---> Null variable to do a sum

for i in str_SUM0:                                               #---> making each element of the first SUM0 an integer
    int_elmnt1 = int(i)
    SUM1 = SUM1 + (int_elmnt1 ** 2)                              #---> Squaring each elements of the SUM0 and adding them to SUM1.

if ( SUM1 == 1):                                                 #---> According to the principle, if the SUM1 is 1, it is Happy
    print(number, 'is a happy number!!😄')
else:                                                            #---> Otherwise unhappy.
    print("Sorry. But", number, 'is not a happy number 😭')


