# cook your dish here

length = int(input())
lis = []
while length > 0:
    temp = int(input())
    lis.append(temp)
    length = length - 1
        
lis.sort()    
for i in lis:
    print(i,end = '\n')

