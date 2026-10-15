sentence = input("Enter a sentence: ")
words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

if words:
    print("Longest word:", longest)
else:
    print("No words entered.")