x = eval(input())
if x<0:
    y = 2 * x -1
elif 0 <= x <10 :
    y = 2 * x +10
elif 10 <= x <100:
    y = 2 * x +100
elif x >= 100:
    y = x**2
print(y)