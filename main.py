#   P)ppppp          ##
#   P)    pp
#   P)ppppp   r)RRR  i)  m)MM MMM  e)EEEEE
#   P)       r)   RR i) m)  MM  MM e)EEEE
#   P)       r)      i) m)  MM  MM e)
#   P)       r)      i) m)      MM  e)EEEE
############################################

#   N)n   nn                    b)
#   N)nn  nn                    b)
#   N) nn nn u)   UU  m)MM MMM  b)BBBB  e)EEEEE  r)RRR
#   N)  nnnn u)   UU m)  MM  MM b)   BB e)EEEE  r)   RR
#   N)   nnn u)   UU m)  MM  MM b)   BB e)      r)
#   N)    nn  u)UUU  m)      MM b)BBBB   e)EEEE r)
#########################################################


#   n = 100
#
#   for i in range(2, n+1):
#
#       prime = True                # First let's ASSUME that every number is a prime number like a vola-vala baccha.
#
#       for j in range(2, i):       # Eikhane i er maan always 1 kom
#
#           if (i % j) == 0:        # Jodi 2 theke (i-1) porjonto kono number diye vaag jay, then number ta Prime na.
#
#               prime = False       # So prime false hoye jabe
#
#               break               # Break use kora hoilo karon jodi 2 diye vaag gelei prime false hoye jay, tahole baki number diye vaag deoar dorkar ki?
#
#       if prime == True:
#
#           print(i)
#


#   T)tttttt                                            l)L
#      T)                                                l)
#      T)     r)RRR  u)   UU e)EEEEE     c)CCCC  o)OOO   l)   o)OOO   r)RRR
#      T)    r)   RR u)   UU e)EEEE     c)      o)   OO  l)  o)   OO r)   RR
#      T)    r)      u)   UU e)         c)      o)   OO  l)  o)   OO r)
#      T)    r)       u)UUU   e)EEEE     c)CCCC  o)OOO  l)LL  o)OOO  r)
#############################################################################


steps = 16      # Smaller the steps, the longer the strip.

print("\n", end="")

for j in range(0, 255, 16):
    for i in range(0, 255+1, steps):
        print(f"\033[48;2;255;000;{i}m ", end="")   # Red to pink

    for i in range(255,0, -steps):
        print(f"\033[48;2;{i};000;255m ", end="")   # Pink to blue

    for i in range(0, 255+1, steps):
        print(f"\033[48;2;000;{i};255m ", end="")   # Blue to cyan

    for i in range(255,0, -steps):
        print(f"\033[48;2;000;255;{i}m ", end="")   # Cyan to green

    for i in range(0, 255+1, steps):
        print(f"\033[48;2;{i};255;000m ", end="")   # Green to yellow

    for i in range(255,0, -steps):
        print(f"\033[48;2;255;{i};000m ", end="")   # Yellow to red

    print("\n", end="")
