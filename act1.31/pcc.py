print("\n**********************************")
nlist=[100,-2,2,0,21,34,66,8,1]
print("\nFirst list of numbers - Before Sorting")
print(nlist)
for i in range(8):
    for j in range(8):
        if nlist[j]>nlist[j+1]:
            temp=nlist[j]
            nlist[j]=nlist[j+1]
            nlist[j+1]=temp
print("\n")
print("First list of numbers - After sorting")
print(nlist)
print("\n**********************************")
nlist=[14,46,43,27,57,41,45,21,70]
print("\nSecond list of numbers - Before Sorting")
print(nlist)
for i in range(8):
    for j in range(8):
        if nlist[j]>nlist[j+1]:
            temp=nlist[j]
            nlist[j]=nlist[j+1]
            nlist[j+1]=temp
print("\nSecond list of numbers - After Sorting")
print(nlist)
