factor = []
i = 1

while i < (int(600851475143)**0.5)+1:
    if 600851475143 % i == 0:
        factor.append(i)
        
    i += 1

k = 0

for z in factor:

    for j in range(1, z-1):
        if z % j == 0:
            factor.pop(k)
    k +=1

t = len(factor)
max = 0

for i in range (0, t):
    if factor[i] > max:
        max = factor[i]

print(max)