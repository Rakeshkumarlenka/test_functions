#compute sum of digits of a given string

class String_probs():
    def sum_digits_string(str1):
        sum_digit = 0
        str1 = "123abcd45"
        for x in str1:
            if x.isdigit() == True:
                z = int(x)
                sum_digit = sum_digit + z

        print( sum_digit)

res = String_probs()
res.sum_digits_string()