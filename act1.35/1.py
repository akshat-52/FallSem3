#store numbers into list and perform linear search for finding the number in the list
lim=int(input("Enter limit for list : "))
list_numbers=[]
for i in range(1,lim+1):
    num=int(input("Enter number {} : ".format(i)))
    list_numbers.append(num)
print("List of numbers : ",list_numbers)
value="false"
count=0
number_to_be_searched=int(input("Enter the number to be searched : "))
for j in range(0,10):
    count+=1
    if number_to_be_searched == list_numbers[j]:
        value="true"
        break
if value=="true":
    print("The element",number_to_be_searched,"is present in the",list_numbers)
else:
    print("The element",number_to_be_searched,"is not present in the",list_numbers)
print("The number of comparisons done are : ",count)
