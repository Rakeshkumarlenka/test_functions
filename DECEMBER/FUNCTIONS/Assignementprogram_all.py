class functions_problems:

    def __init__(self):
        print("functions problems")

    def palindrome(self):
        print("")
        print("Q1.check given word is palindrome or not")
        str = input("please enter a string")
        str2 = str[::-1]
        if str == str2:
            print(f"The given string {str2} is a palindrome")
        else:
            print(f"The given string {str2} is not a palindrome")

    def even_or_add(self):
        print("")
        print("Q2.print even and odd numbers")
        num = int(input("Enter the number :"))
        if num % 2 == 0:
            print(f"{num} is even number")
        else:
            print(f"{num} is odd numbers")

    def prime_numbers(self):
        print("")
        print("Q3.CHECK FOR PRIME OR NOT")
        num = int(input("enter  number"))
        c = 0;
        for i in range(1, num + 1):
            if (num % i == 0):
                c += 1
        if (c == 2):
            print(f"the number{num} is prime number")
        else:
            print(f"the number{num} is not prime number")

    def factorial_num(self):
        print("")
        print("Q4.FACTORIAL OF A NUMBER")
        dict = {}

        def fact(n):
            if (n == 1 or n == 0):
                return 1
            else:
                return n * fact(n - 1)
        for i in range(1, 9):
            dict[i] = fact(i)
        print("factorial number from 1to 8: ", dict)

    def convert(self):
        print("")
        print("Q5.CONVERT L-T & S-L & T-S ")
        list1 = [1, 2, 3, 4]
        print( tuple(list1))
        my_set = {'ram','is','a','good','boy'}
        s = list(my_set)
        print(s)
        t = ('x', 'y', 'z')
        print(set(t))

    def square_and_cube(self):
        print("")
        print("Q6.find cube/square of a number")
        num = int(input("enter the number"))
        print(num * num)
        print(num * num * num )

    def table(self):
        print("")
        print("Q7.TABLE OF A GIVEN NUMBER")
        num = int(input('enter the number :'))
        for i in range(1, 11):
            print(num, 'x', i, '=', num * i)


    def max(self):
        print("")
        print("Q8.MAX OF THREE NUMBERS")
        self.a = int(input('enter the number a :'))
        self.b = int(input('enter the number b :'))
        self.c = int(input('enter the number c :'))
        if self.a >= self.b and self.a >= self.c:
            print('the largest is %d' % self.a)
        elif self.b >= self.a and self.b >= self.c:
            print('largest number is %d ' % self.b)
        else:
            print('largest number is %d' % self.c)


    def terms(self):
        print("")
        print("Q9.FIBONNACCI SERIES")
        n_1 = 0
        n_2 = 1
        count = 0
        n_terms = int(input("How many terms the user wants to print? "))
        if n_terms <= 0:
            print("Please enter a positive integer, the given number is not valid")
        elif n_terms == 1:
            print("The Fibonacci sequence of the numbers up to", n_terms, ": ")
            print(n_1)
        else:
            print("The fibonacci sequence of the numbers is:")
            while count < n_terms:
                print(n_1)
                nth = n_1 + n_2
                n_1 = n_2
                n_2 = nth
                count += 1

    def sum(self):
        print("")
        print("Q10.SUM OF ALL EEMENTS")
        lst=[1,4,5,6]
        total = 0
        for i in range(0, len(lst)):
            total = total + lst[i]
        print("Sum of all elements in given list: ", total)

    def product(self):
        print("")
        print("Q11.PRODUCT OF ALL ELEMENTS ")
        lst1 = [1,4,5,6]
        tot = 0
        for i in range(0, len(lst1)):
            tot = tot * lst1[i]
        print("product of all elements in given list: ", tot)

    def reverse(self):
        print("")
        print("Q12.REVERSE OF A STRING ")
        in_str ='welcome'
        out_str = in_str[::-1]
        print(out_str)

    def sequence(self):
        print("")
        print("Q13.CHECK NO IS IN RANGE OR NOT ")
        n = int(input('enter the number :'))
        if n in range(0,5):
            print('yes the number is in the range')
        else:
            print('the number is out of range')

    def string_test(self):
        print("")
        print("Q14.COUNT FOR UPPER AND LOWER CASE PRESENT")
        s=('The quick Brown Fox')
        d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
        for c in s:
            if c.isupper():
                d["UPPER_CASE"] += 1
            elif c.islower():
                d["LOWER_CASE"] += 1
            else:
                pass
        print("Original String : ", s)
        print("No. of Upper case characters : ", d["UPPER_CASE"])
        print("No. of Lower case Characters : ", d["LOWER_CASE"])


    def unique(self):
        print("")
        print("Q15.UNIQUE NUMBERS")
        list1 = [10, 20, 10, 30, 40, 40]
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        for x in unique_list:
            print(x)


    def ch_even(self):
        print("")
        print("Q16.CHECK EVEN OR NOT")
        list1 = [10, 21, 4, 45, 66, 93]
        for num in list1:
            if num % 2 == 0:
                print(num, end=" ")


    def triangle(self):
        print("")
        print("Q17.PASCAL TRIANGLE")
        n = 5
        for i in range(n):
            print(' ' * (n - i), end='')
            print(' '.join(map(str, str(11 ** i))))

    def group_of_strings(self):
        print("")
        print("Q18.DISPLAY GROUP OF STRINGS")
        lis1 = []
        i = 1
        while i:
            words = input(" enter strings :")
            i = int(input('1 for continue 0 for exit'))
            lis1.append(words)
        print(lis1)

    def panagram(self):
        print("")
        print("Q19.CHECK THE STRING IS PANAGRAM OR NOT")
        # str1='The quick brown fox jumps over the lazy dog'
        str1 = "marry had a little limb"
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for x in alphabets:
            if x not in str1.lower():
                return False
        return True

    def check_itdict(self):
        print("")
        print("Q20.MATCH TWO DICTONARY")
        x = {'key1': 1, 'key2': 3, 'key3': 2}
        y = {'key1': 1, 'key2': 2}
        for (key, value) in set(x.items()) & set(y.items()):
            print('%s: %s is present in both x and y' % (key, value))





func_obj = functions_problems()
func_obj.palindrome() #Q1
func_obj.even_or_add() #Q2
func_obj.prime_numbers() #Q3
func_obj.factorial_num() #Q4
func_obj.convert() #Q5
func_obj.square_and_cube() #Q6
func_obj.table() #Q7
func_obj.max() #Q8
func_obj.terms() #Q9
func_obj.sum() #Q10
func_obj.product() #Q11
func_obj.reverse() #Q12
func_obj.sequence() #Q13
func_obj.string_test() #Q14
func_obj.unique() #Q15
func_obj.ch_even() #Q16
func_obj.triangle() #Q17
func_obj.group_of_strings()#18
print(func_obj.panagram())#19
func_obj.check_itdict()#Q20
