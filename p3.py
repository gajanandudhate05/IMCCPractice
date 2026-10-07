text = " welcome to IMCC "
text=text.strip()
print("capitalize first letter",text.capitalize())
#count occurrences of a substring in a string
print("count occurrences of a substring in a string",text.count("C"),"time in text")
#find the position of a substring in a string
print("find the position of a substring in a string",text.find("IMCC"))
#replace a substring in a string with another substring
print("replace a substring in a string with another substring",text.replace("IMCC","python magic"))
#split a string into a list of substrings based on a delimiter
print("split a string into a list of substrings based on a delimiter",text.split(" "))
#join a list of strings into a single string with a specified delimiter
print("join a list of strings into a single string with a specified delimiter","-".join(["hello", "world"]))