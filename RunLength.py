# 10 Run Length Data Encoder

string = 'TTyyysssssssmmmmmTTTtt'
list1 = list(string)

count = int()
char = list()
result = list()

trigger = True

while trigger == True:
    element = list1[0]   # The first character of the string
    for i in list1:
        if element == i:  # While i equals to the first character 
            char.append(i)  
        if element != i:
            list1 = list1[len(char):]   # When i is changed, the list becomes everything after the last occurrence of the first character. "aaabbbcca" becomes "bbcca"
            result.append(element+str(len(char)))  # element is the character, and len(char) is how many times it occured
            char = []
            break
        if list1.count(list1[0]) == len(list1):   # When it is the last element of the list
            result.append(list1[0]+str(list1.count(list1[0])))   # Same as line 19
            trigger = False  # Break the while loop
            break


result = ''.join(result)
print(result)

# Decoder

# numbers = list()
# chars = list()
# for i in result:
#     if result.index(i) % 2 == 0:
#         chars.append(i)
#     else:
#         numbers.append(i)
# 
# for char, num in zip(chars, numbers):
    

