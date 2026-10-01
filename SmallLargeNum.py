arr = [10, 50, 20, 80, 30]

maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print(maximum)