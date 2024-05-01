#!/usr/bin/python3
for i in range(97, 122):
    char = chr(i)
    if char not in ['q', 'e']:
        print("{}".format(chr(i)), end="")
