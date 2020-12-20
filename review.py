'''
for i in range(5):
    print(i)

for i in range(5):
    if i ==3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    for j in range(5):
        print(i, j, sep="-")

def say_hello(greeting):
    print(greeting)

say_hello("Hello World")
hello = say_hello
hello("Good Morning")


def add(num1, num2):
    print(num1+num2)

add(1,2)

def add(num4, num5):
    return(num4+num5)
print(add(6,2))

def ave(num1,num2,num3):
    print((num1+num2+num3)/3)
ave(9,4,2)

class Student:

    def __init__(self,name):
        self.name = name


    def avg(self,math,english):
        print((math+english)/2)

a001 =Student("sato")
print(a001.name)
a001.avg(80,90)

class Student():
    def __init__(self, name):
        self.name = name

    def calculateAvg(self,data):
        sum = 0
        for i in data:
            sum += i
        avg = sum/len(data)
        return avg

    def judge(self, avg):
        if avg >= 80:
            result="合格"
        else:
            result="不合格"
        return result

a001 = Student("tanaka")
data = [90,80,90,90,90]
avg = a001.calculateAvg(data)
result = a001.judge(avg)
print(a001.name+"  "+result)
print(avg)


'''




