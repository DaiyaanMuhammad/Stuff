from time import sleep
from os import system

#Control Panel
FilePath = "./color.txt"
time = 0.16
cmd = 'clear'
I = 1
J = 6
K = 2
UP = 256
DOWN = 0
Buffer = int()

#Code
while True:
    for i in range(DOWN, UP, I):
        sleep(time)
        system(cmd)
        FILE = open(FilePath, 'w')
        for j in range(DOWN, UP, J):
            for k in range(DOWN, UP, K):
                FILE.write(f"\033[48;2;{i};{j};{k}m \033[0m")
            FILE.write("\n")
        FILE.close()
        FileRead = open(FilePath, 'r')
        print(FileRead.read())
#    I = -I
#    J = -J
#    K = -K
    Buffer = UP
    UP = DOWN
    DOWN = Buffer
    i = int()
    j = int()
    k = int()

#TODO: Lines 28 to 33. Infinite rgb coloring. Didn't work the above mentioned way.

#Debug
#print(I, J, K, UP, DOWN, Buffer)
