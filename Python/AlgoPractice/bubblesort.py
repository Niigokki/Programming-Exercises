print("hello bubblesort")
numlist = [999,888,5,12121212,19834012840]
print(numlist)
end = len(numlist)-1
for i in range(len(numlist)):
    for nums in range(0,end):
        if (numlist[nums] > numlist[nums+1]):
            temp = numlist[nums]
            numlist[nums] = numlist[nums+1]
            numlist[nums+1] = temp
            print (numlist)
