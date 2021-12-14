def getText():
    txt = open("C:/Users/999/Desktop/hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '/.,][!@#$%^&*()-=_-*+/[]{}|':
        txt = txt.replace(ch," ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
ls = list(counts.items())
ls.sort(key = lambda x:x[1],reverse = True)
for i in range(10):
    word,count = ls[i]
    print ("{}->{}".format(word,count))

