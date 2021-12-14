A1 = eval(input())####还没改
B1 = eval(input())
A2 = eval(input())
B2 = eval(input())
C1 = eval(input())
C2 = eval(input())
for x in range(100):
    for y in range(100):

        if A1 * x +B1 * y == C1 and A2 * x +B1 * y == C2:
                    print("x = {},y = {}".format(x,y))
