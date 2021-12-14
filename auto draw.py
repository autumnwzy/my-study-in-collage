import turtle as t
t.pensize(5)
f = open('C:/Users/999/Desktop/test.txt')
data = []
for line in f:
    line.replace("\n", ',')
    data.append(list(map(eval,line.split(","))))

f.close()

for i in range(len(data)):
    t.color(data[i][3],data[i][4],data[i][5])
    t.fd(data[i][0])
    if data[i][1] == 0:
        t.right(data[i][2])
    else:
        t.left(data[i][2])
t.done()


