f = open("C:\\Users\\Gajanan\\ImccPractice\\Pyyy.py\\input.txt", "r")
lines = f.readlines()
f.close()

print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1].rstrip("\n"))
else:
    print("2nd line does not exist.")

if len(lines) >= 4:
    print("4th line:", lines[3].rstrip("\n"))
else:
    print("4th line does not exist.")