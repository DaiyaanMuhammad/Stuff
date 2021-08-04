#!/usr/bin/env python3

print("\n")
for i in range(0,4):
    for j in range(0, 8):
        print(f"\033[4{j};3{j}m","   ", end = '')
        print(f"\033[10{j};9{j}m","   ", end = '\033[40;30m   ')
    print("")
print("")
