#create a hetrogenous list of numbers and names split the list from highest number 
hetero_list = [1, "Alice", 5, "Bob", 10, "Charlie"]
numbers = [x for x in hetero_list if isinstance(x, (int, float))]
names = [x for x in hetero_list if isinstance(x, str)]
highest_number = max(numbers)
split_index = numbers.index(highest_number)
print("Numbers:", numbers)
print("Names:", names)
print("Highest number:", highest_number)