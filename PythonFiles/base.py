#odd number
def countOddNumbers(n, array):
    # Count numbers that are not divisible by 2
    return sum(1 for num in array if num % 2 != 0)