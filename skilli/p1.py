s=['a','b','c','a','a','b','c','d','e']
arr=[0]*26
for i in s:
    arr[ord(i)-ord('a')]+=1
print(arr)