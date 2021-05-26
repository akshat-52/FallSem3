string1=input("Enter your name : ")
string2=""
list=[]
for i in string1:
    list.append(ord(i))
print("Charaters of name without sorting : ",string1)
for j in range(1,len(list)):
    temp=list[j]
    l=j-1
    while l>=0:
        if temp<list[l]:
            list[l+1]=list[l]
            list[l]=temp
        l=l-1
for x in list:
    string2=string2+str(chr(x))
print("Characters of name after sorting : ",string2)
f=open("vowel_characters.txt")
vowel=[]
for y in list:
    a=str

