def Getnumber():#获得用户输入  ###错误没改
    #number = []
    n = eval(input())
    # while True :
    #     if n != "":
    #      number.append(n)
    #      n = eval(input())
    # return number
    ls = list(n)
    return ls
#print(ls)



# try:
#     Getnumber()
# except :
#     print ("error")

def average(number):#平均数
    sum = 0.0
    for n in number:
        sum = sum + n
    ave = sum/len(number)
    return ave

def mid(number):#中位数
    number.sort()
    size = len(number)
    if size % 2 != 0 :
        mid = number[size//2]
    else:
        mid = (number[size//2-1] + number[size//2+1])/2
    return mid
#
def dev(number,ave):#计算方差
    sum = 0
    for n in number:
        sum = sum + pow(ave-n,2)
    size = len(number)
    dev = sum/size
    return dev
n = Getnumber()
mean = mid(n)
print("平均数：{:.2f}，中位数：{:.2f},方差:{:.2f}".format(average(n),mid(n),dev(n,mean)))
# m = average(n)
# print("平均数：{:.2f}".format(m))

# def getNum():       #获取用户不定长度的输入
#     s = input()
#     ls = list(eval(s))
#     return ls
#
# def mean(numbers):  #计算平均值
#     s = 0.0
#     for num in numbers:
#         s = s + num
#     return s / len(numbers)
#
# def dev(numbers, mean): #计算标准差
#     sdev = 0.0
#     for num in numbers:
#         sdev = sdev + (num - mean)**2
#     return pow(sdev / (len(numbers)-1), 0.5)
#
# def median(numbers):    #计算中位数
#     numbers.sort()
#     size = len(numbers)
#     if size % 2 == 0:
#         med = (numbers[size//2-1] + numbers[size//2])/2
#     else:
#         med = numbers[size//2]
#     return med
#
# n =  getNum() #主体函数
# m =  mean(n)
# print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n,m),median(n)))