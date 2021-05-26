list_numbers=[]
print("Enter 10 numbers")
i=1
while i <= 10:
    n=int(input("Number {} : ".format(i)))
    if n not in list_numbers:
        list_numbers.append(n)
    else:
        print("You have already entered this number, Try Another number")
        continue
    i += 1
print('List created :', list_numbers, '\n')
#-------------------------------------------------------------------------------------
print('List is sorted in ascending order')
ln=len(list_numbers)
for x in range(ln):
    for j in range(ln-1):
        if list_numbers[j] > list_numbers[j+1]:
            temp=list_numbers[j]
            list_numbers[j]=list_numbers[j+1]
            list_numbers[j+1]=temp
print(list_numbers)
f=open('ascending_numbers.txt', 'a')
for b in list_numbers:
    f.write(str(b))
    f.write('\n')
print('Created a file ascending_numbers\n')
f.close()
#-------------------------------------------------------------------------------------
print('List is sorted in descending order')
ln=len(list_numbers)
for x in range(ln):
    for j in range(ln-1):
        if list_numbers[j] < list_numbers[j+1]:
            temp=list_numbers[j]
            list_numbers[j]=list_numbers[j+1]
            list_numbers[j+1]=temp
print(list_numbers)
f=open('descending_numbers.txt', 'a')
for b in list_numbers:
    f.write(str(b))
    f.write('\n')
print('Created a file descending_numbers\n')
f.close()
#-------------------------------------------------------------------------------------
f_e=open('even_numbers.txt', 'a')
f_o=open('odd_numbers.txt', 'a')
for c in list_numbers:
    if c%2 == 0:
        f_e.write(str(c))
        f_e.write(str('\n'))
    else:
        f_o.write(str(c))
        f_o.write(str('\n'))
print('Created a file even_numbers\n')
print('Created a file odd_numbers\n')

f_o.close()
f_e.close()