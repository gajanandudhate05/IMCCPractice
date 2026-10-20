f=open(r"C:\Users\Gajanan\ImccPractice\PythonFiles\sample.txt","r")   # Open the file --- IGNORE ---
data=f.read()
f.close()
count=len(data)
print("Total Characters:",count)