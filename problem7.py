# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(nb:int):

    if nb < 2: return False

    for k in range (2, nb):
        if nb % k == 0: return False

    return True

i = 1
j = 1

while i <= 10001:

    if i == 10001 and is_prime(j) == True:
        print(j)

    if is_prime(j) == True:
        i += 1
        j += 1
    else:
        j += 1