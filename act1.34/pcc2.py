numberlist=[]
a=int(input("Please enter the number of numbers for the list: "))
for i in range(0,a):
    num=int(input("Please a number: "))
    numberlist.append(num)
print("Number list before sorting:")
print(numberlist)
for i in range(1,len(numberlist)):
    temp=numberlist[i]
    j=i-1
    while j>=0:
          if temp<numberlist[j]:
             numberlist[j+1]=numberlist[j]
             numberlist[j]=temp
          j=j-1
print("Number list after sorting:")
print(numberlist)
