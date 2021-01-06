"""
count = int(input())
dic = {}
for i in range(0, count):
    data = input()
    li = data.split(' ')
    dic[li[0]] = li[1]
    
for p in range(0, count):
    data1 = input()
    if dic.get(data1):
        print('{}={}'.format(data1, dic[data1]))
    else:
        print('Not found')
        """
n = int(input())
d = dict()

for i in range(0, n):
    name, number = input().split()
    d[name] = number


for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break
