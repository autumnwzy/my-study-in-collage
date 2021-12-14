import jieba
txt = open("threekingdoms.txt", "r",encoding = "utf-8").read()
words = jieba.lcut(txt)
count = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word,0)+1
ls = list(count.items())
ls.sort(key = lambda x:x[1],reverse=True)
for i in range(15):
    word,count = ls[i]
    print("{}->{}".format(word,count))
