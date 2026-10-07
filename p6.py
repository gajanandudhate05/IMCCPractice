#remove the items from the list located at 2nd and 5th position
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Remove the items at 2nd and 5th position (index 1 and 4)
del numbers[1]  # Remove the item at index 1 (2nd position)
del numbers[3]  # Remove the item at index 4 (5th position, but after the previous deletion, it's now at index 3)
print("List after removing items at 2nd and 5th position:", numbers)    