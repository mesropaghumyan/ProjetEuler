# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

import time

last = 0
curr = 1
res = 0
sum = 0

while res <= 4e6:

    #time.sleep(1)

    res = last + curr
    last = curr
    curr = res

    if res % 2 == 0:
        sum = sum + res

print(sum) # sum = 4613732