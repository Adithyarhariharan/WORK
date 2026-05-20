text = input("Enter sentence: ").split()

for word in set(text):
    print(word, "=", text.count(word))