f=open("Pyyy.py/input.txt", "r")
content = f.read()
count = 0
for ch in content:
    if ch in "aeiouAEIOU":
        count += 1
print("Number of vowels:", count)
f.close()
