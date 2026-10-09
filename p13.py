#accept the name and check if its palindrome
name = input("Enter a name: ")
cleaned_name = ''.join(c.lower() for c in name if c.isalnum())
if cleaned_name == cleaned_name[::-1]:
    print(f"{name} is a palindrome.")
else:
    print(f"{name} is not a palindrome.")