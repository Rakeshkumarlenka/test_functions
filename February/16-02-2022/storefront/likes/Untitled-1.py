def nonDivisibleSubset(k, s):
    # Write your code here
    my_set=set()
    for x in range(len(s)):
        for y in range(x+1,len(s)):
            two_sum=s[x]+s[y]
            if two_sum%k!=0:
                my_set.add(s[x])
                my_set.add(s[y])

    print(my_set)
# nonDivisibleSubset(3,[1,7,2,4])         
nonDivisibleSubset(7,[278,576, 496, 727, 410 ,124, 338, 149, 209, 702, 282, 718, 771, 575,436])
# nonDivisibleSubset(4,[19,10,12,10,24,25,22])