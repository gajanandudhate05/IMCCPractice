n=7
mid=(n+1)/2
for i in range(n):
    for j in range(n):
        if i == mid - 1 or j == mid - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()