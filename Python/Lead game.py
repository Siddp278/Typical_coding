# cook your dish here
def finding():
    lists = []
    count = int(input())
    # player 1 is + and player 2 is -
    while count > 0:
        (a,b) = map(int, input().split(' '))
        diff = a - b
        count = count - 1
        lists.append(diff)
    ma = max(lists)
    mi = min(lists)
    if ma > abs(mi):
        print("1" + " " + str(ma))
    else:
        print("2" + " " + str(abs(mi)))
        
        
finding()