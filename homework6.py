import math
a = math.pi / eval(input())
b = math.pi / eval(input())
if a > 0 and b > 0:
    y = math.cos(a) + math.cos(b)
elif a > 0 and b <= 0:
    y = math.sin(a) + math.sin(b)
elif a <= 0 and b > 0:
    y = math.cos(a) + math.sin(b)
elif a <= 0 and b <= 0:
    y = math.sin(a) + math.cos(b)

print('y = {}'.format(y))