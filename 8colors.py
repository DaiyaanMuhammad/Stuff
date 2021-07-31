print("\n")
for i in range(0,8):
    for j in range(2, 8):
        result = (6*i) + j
        print(f"\033[4{i};3{j}m","{:0>3d}".format(result), end = ' ')
    print("\n")
