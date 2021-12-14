s = open("C:/Users/999/Desktop/hamlet.txt", 'r')
#print(s.readlines(5))
#print((s.read(2)))
for line in s:
    print(line)
s.close()