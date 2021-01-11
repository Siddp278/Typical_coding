class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    def computeDifference(self):    
        i = 0
        l = []
        while i < len(self.__elements):
            j = i + 1
            while j < len(self.__elements):
                temp = abs(self.__elements[i] - self.__elements[j])
                l.append(temp)
                j = j + 1
            i = i + 1
        # print(max(l))
        self.maximumDifference = max(l)
        return self.maximumDifference
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
