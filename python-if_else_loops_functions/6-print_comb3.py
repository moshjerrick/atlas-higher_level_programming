#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1,10):
        if i != j:
            combination = f"{i}{j}"
            print("{}".format(combination), end="")
            if combination != "89":
                    print(", ", end="")
            else:
                    print("\n", end="")
