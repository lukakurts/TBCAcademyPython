word = input("Please enter word: ")

for i in range(len(word)):
    match word[i]:
        case "a":
            continue
        case "e":
            continue
        case "i":
            continue
        case "o":
            continue
        case "u":
            continue
        case _:
            print(word[i])
