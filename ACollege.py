#number is perfect number or not
num=28
sum=0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")