#Name: Becky Tseng
#StudentID: 2038591

s = input()
lst = [int(x) for x in s.split(" ") if int(x)>=0]
lst.sort()
for x in lst:
    print(x,end=" ")
