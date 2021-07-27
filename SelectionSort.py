

###   ,d88~~\           888                     d8   ,e,                   
###   8888     e88~~8e  888  e88~~8e   e88~~\ _d88__  "   e88~-_  888-~88e 
###   `Y88b   d888  88b 888 d888  88b d888     888   888 d888   i 888  888 
###    `Y88b, 8888__888 888 8888__888 8888     888   888 8888   | 888  888 
###      8888 Y888    , 888 Y888    , Y888     888   888 Y888   ' 888  888 
###   \__88P'  "88___/  888  "88___/   "88__/  "88_/ 888  "88_-~  888  888 
###                                                                        
###   ,d88~~\                   d8   
###   8888     e88~-_  888-~\ _d88__ 
###   `Y88b   d888   i 888     888   
###    `Y88b, 8888   | 888     888   
###      8888 Y888   ' 888     888   
###   \__88P'  "88_-~  888     "88_/


# A randomly generated list. Totally unsorted mess
list1 = [2,5,3,2,6,7,5,4,77,88,4,22,1,2,44,5,4,6,6,64,564,563,434,5,456,34,535,34,3543,4,567,457,34,3,56,2346,34,52,63,6,2436,45,3,45,246,324,2345,24,62,5,236,324,6]

# Where we will place the selected values
result = []

# Going through a loop
while True:
    # MIN is the minimum value of list1. Select it.
    MIN = min(list1)
    # Put the selected value in another array
    result.append(MIN)
    print(result)
    # Remove the Minimum value from the list. In the next iteration, the new minimum value will be the second minimum value and so on
    list1.remove(MIN)
    if len(list1) == 0:
        # If the old list is empty, break the loop and you got the sorted list in the new array.
        break
