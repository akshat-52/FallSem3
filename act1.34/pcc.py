numberlist=[]
a=int(input("Enter number of numbers for the list : "))
for i in range(1,a+1):
    num=int(input("Enter {} number : ".format(i)))
    numberlist.append(num)
print("List before sorting : ",numberlist)
for i in range(1,len(numberlist)):
    temp=numberlist[i]
    j=i-1
    while j>=0:
        if temp<numberlist[j]:
            numberlist[j+1]=numberlist[j]
            numberlist[j]=temp
        j=j-1
print("List after sorting : ",numberlist)