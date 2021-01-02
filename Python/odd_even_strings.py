t = int(input())
for i in range(0,t):
    temp = input()
    str1 = ""
    str2 = ""
    for j in range(0, len(temp)):
        if j % 2 == 0:
            str1 = str1 + temp[j]
        if j % 2 != 0:
            str2 = str2 + temp[j]
    print('{} {}'.format(str1, str2))
