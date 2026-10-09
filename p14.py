#print the sum of digits
num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))
print("Sum of digits:", digit_sum)