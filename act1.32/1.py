def selection_sort(given_list):
    length = len(given_list)
    for x in range(length-1):
        minimum_value_holder = x
        for j in range(x + 1, length):
            if given_list[j] < given_list[minimum_value_holder]:
                minimum_value_holder = j
        if minimum_value_holder != x:
            temp = given_list[x]
            given_list[x] = given_list[minimum_value_holder]
            given_list[minimum_value_holder] = temp


def selection_sort_dec(given_list):
    length = len(given_list)
    for x in range(length-1):
        minimum_value_holder = x
        for j in range(x + 1, length):
            if given_list[j] > given_list[minimum_value_holder]:
                minimum_value_holder = j
        if minimum_value_holder != x:
            temp = given_list[x]
            given_list[x] = given_list[minimum_value_holder]
            given_list[minimum_value_holder] = temp



list_numbers = []

print("Enter 6 numbers")
i = 1
while i <= 6:
    number = int(input("Number {} :".format(i)))
    if number not in list_numbers:
        list_numbers.append(number)
    else:
        print("You have already entered this Number, Try another")
        continue
    i += 1

print('List created :', list_numbers, '\n')
# ----------------------------------------------------------------------------------------------
print('List is sorted in ascending order')
selection_sort(list_numbers)

print(list_numbers)
file_handler = open('ascending_numbers.txt', 'a')
for t in list_numbers:
    file_handler.write(str(t))
    file_handler.write('\n')

print('Created a file ascending_numbers\n')
file_handler.close()
# ------------------------------------------------------------------------------------------------
print('List is sorted in descending order')
selection_sort_dec(list_numbers)
print(list_numbers)
file_handler = open('descending_numbers.txt', 'a')
for t in list_numbers:
    file_handler.write(str(t))
    file_handler.write('\n')

print('Created a file descending_numbers\n')
file_handler.close()
# ------------------------------------------------------------------------------------------------
file_handler_even = open('even_numbers.txt', 'a')
file_handler_odd = open('odd_numbers.txt', 'a')
for z in list_numbers:
    if z % 2 == 0:
        file_handler_even.write(str(z))
        file_handler_even.write('\n')
    else:
        file_handler_odd.write(str(z))
        file_handler_odd.write('\n')

print('Created a file even_numbers\n')
print('Created a file odd_numbers\n')

file_handler_odd.close()
file_handler_even.close()