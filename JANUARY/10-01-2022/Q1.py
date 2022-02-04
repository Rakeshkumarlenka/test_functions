from itertools import permutations

# Initialising string
ini_str = "ab"

# Printing initial string
print("Initial string", ini_str)

# Finding all permutation
permutation = [''.join(p) for p in permutations(ini_str)]
# Printing result
print("Resultant List", str(permutation))