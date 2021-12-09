try:
    inp_char = input("Enter the string:")
    print(inp_char[5])
    print(inp_char[3])
    print(inp_char[2])
    print(inp_char[8])
except IndexError as In:
    print("error is occured",In)




