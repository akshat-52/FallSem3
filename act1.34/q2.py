#sorting name characters and vowels
my_name=input("Enter your name : ").upper()
str2=""
list=[]
for i in my_name:
    list.append(ord(i))
print("Characters of name before Sorting",my_name)
for k in range(1,len(list)):
    temp=list[k]
    j=k-1
    while j>=0:
        if temp<list[j]:
            list[j+1]=list[j]
            list[j]=temp
        j=j-1
for x in list:
    str2=str2+str(chr(x))
print("Characters of name after Sorting",str2)
f=open("vowel_characters.txt","a")
vowel=[]
for y in list:
    a=str(chr(y))
    if (a=="A"or a=="E" or a=="I" or a=="O"or a=="U"):
        vowel.append(a)
if vowel==[]:
    f.write("No Vowels in my Name")
else:
    for z in vowel:
        f.write(z)
        f.write("\n")
f.close()



    