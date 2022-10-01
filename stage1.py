def solution(xs):
    # Your code here
    result=1
    counter = 0
    counter0 = 0
    slist=sorted(xs)
    if(len(slist)==1):
        return str(slist[0])
    for i in range(len(slist)):
        if(slist[i] < 0):
            counter +=1
        if(slist[i] == 0):
            counter0 +=1
    if(len(slist)==1):
        return str(slist[0])
    if(counter0 == len(slist)):
        return str(0)
    flist = [i for i in slist if i != 0]
    if(len(flist) == counter0):
        return str(0)
    if(len(flist)==1):
        return flist[0]
    for i in flist:
        if (i != 0 and i <= 1000):
            result *= i
    if result < 0:
        max_neg = max([n for n in xs if n < 0])
        result = result//max_neg
    return(str((result)))
#test cases example
# generating random list of len(str) = = 50 
import random
a[]
for i in range(50):
    a.append(random.randint(-1000,1000)

#driver
print(solution(a))
