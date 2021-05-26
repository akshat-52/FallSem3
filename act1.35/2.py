#store numbers into list and perform binary search for finding the number in the list
lim=int(input("Enter limit for list : "))
list_numbers=[]
for i in range(1,lim+1):
    num=int(input("Enter number {} : ".format(i)))
    list_numbers.append(num)
list_numbers.sort()
print("List of sorted numbers : ",list_numbers)
number_to_be_searched=int(input("Enter a number to search in the list : "))
min=0
max=len(list_numbers)-1
mid=0
count=0
value="False"
while min<=max:
    count+=1
    mid=(min+max)//2
    if list_numbers[mid]<number_to_be_searched:
        min=mid+1
    elif list_numbers[mid]>number_to_be_searched:
        max=mid-1
    else:
        mid=mid
        value="True"
        break
if value=="True":
    print("The element",number_to_be_searched,"is present in the",list_numbers)
else:
    print("The element",number_to_be_searched,"is not present in the",list_numbers)
print("The number of comparisons done are : ",count)