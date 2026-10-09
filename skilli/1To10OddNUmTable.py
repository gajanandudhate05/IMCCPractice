#1 to 10 odd numbers table
for i in range(1, 11):
    if i % 2 != 0:
        for j in range(1, 11):
            print(i*j, end=' ')
        print("")