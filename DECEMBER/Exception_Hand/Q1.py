
try:
    ini_str = "abababababab"
    sub_str = "ab"
    occurrence = ch #no given to find the occurence

except NameError as nm:
    print("Error occured",nm)
finally:
    ini_str = "abababababab"
    sub_str = "ab"
    occurrence = 3
    val = -1
    for i in range(0, occurrence):
        val = ini_str.find(sub_str, val + 1)
    print("Nth occurrence is at", val)

