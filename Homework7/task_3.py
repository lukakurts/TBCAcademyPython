word = input("Please enter word: ")
i = 0
print(word)

while i < 5:
    if len(word) % 2 != 0:
        print("First symbol is " + word[0])
        print("middle symbol is " + word[(len(word) - 1) // 2])
        print("Last symbol is " + word[len(word) - 1])
    else:
        print("First middle symbol is " + word[len(word) // 2 - 1] )
        print("Second middle symbol is " + word[len(word) // 2])
    i += 1