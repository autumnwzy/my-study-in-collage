pi = 0
for i in range(1001):
    pi = pi + (2 * (i**2))/((2 * i -1) * (2 * i + 1))

print(pi)