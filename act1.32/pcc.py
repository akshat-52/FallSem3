def selectionSort(itemsList ):
    n=len(itemsList)
    for i in range(n-1):
        minValueIndex=i

        for j in range(i+1,n):
            if itemsList[j] < itemsList[minValueIndex]:
                minValueIndex=j

        if minValueIndex != i:
            temp=itemsList[i]
            itemsList[i]=itemsList[minValueIndex]
            itemsList[minValueIndex]=temp
    return itemsList
list_numbers=[100,25,0,-1,21,88,16,99,133,23]
print("\nList before Sorting")
print(list_numbers)

print("\nList after applying Selection Sort Technique: ")
print(selectionSort(list_numbers))

