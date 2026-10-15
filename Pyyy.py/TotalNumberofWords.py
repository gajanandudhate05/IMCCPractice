f = open("Pyyy.py/input.txt", "r")
content = f.read()
f.close()

words = content.split()

print("Total number of words:", len(words))

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique words:", unique_words)