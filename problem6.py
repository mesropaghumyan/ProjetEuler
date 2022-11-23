# the sum of the square of the first one hundred natural numbers
i = 1
a = 0
while i <= 100:
    a = a + i**2
    i+=1

# the square of the sum of the first one hundred natural numbers
i = 1
b = 0
while i<=100:
    b = b + i
    i+=1
b = b**2

# the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
sum = b - a
print("b = " + str(b) + " ; a = " + str(a) + " ; sum = " + str(sum))