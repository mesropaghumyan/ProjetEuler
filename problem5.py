def resolve(i, n):
    j = 2
    while i <= n:
        if j % i != 0:
            i = 1
            j += 1
        else:
            i += 1
            ppcm = j
    return ppcm

# resolve(1, 20) it's good but the execution is too long ...

# other solution :

# let's start by finding the numbers from 1 to 20 not being prime
def not_prime(i, n):
    not_prime = []
    for x in range(i+1, n+1):
        for y in range(i+1, x-1):
            if x % y == 0 and x not in not_prime:
                not_prime.append(x)
    return not_prime

# now let's decompose the not primes numbers
def decomposite(numbers):
    res = {}
    decomposite = []
    i = 2
    for x in numbers:
        c = x
        while x > 1:
            if(x%i==0):
                q = x / i
                x = q
                decomposite.append(i)
            else:
                i += 1
        res[int(c)] = decomposite
        decomposite = []
            
        i = 2
    return res

a = not_prime(1, 20)
d = decomposite(a)

# ppcm(1, 20)
x = 1
i = 0
max = 0
c = 0
while x <= 20:
    for i in d:
        print(i)
        for j in range(0, len(d[i])):
            if d[j] == x:
