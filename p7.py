#append  a new element in list which is half of the items in 3 rd position
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Append a new element which is half of the item in 3rd position (index 2)
new_element = numbers[2] / 2
numbers.append(new_element)
print("List after appending half of the item in 3rd position:", numbers)    