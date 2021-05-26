#sorting n integers using insertion sort
numberlist=[]
lim=int(input("Enter the limit of numbers you want in the list : "))
for i in range(1,lim+1):
    num=int(input("Enter number {} : ".format(i)))
    numberlist.append(num)
print("Number List Before Sorting : ",numberlist)
print("\n")
for i in range(1,len(numberlist)):
    temp=numberlist[i]
    j=i-1
    while j>=0:
        if temp<numberlist[j]:
            numberlist[j+1]=numberlist[j]
            numberlist[j]=temp
        j=j-1
print("Number List After Sorting : ",numberlist)
print("\n")