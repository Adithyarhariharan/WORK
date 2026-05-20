text = input("Enter text: ")

count = 0
for i in text.lower():
    if i in "aeiou":
        count += 1

print("Vowels =", count)