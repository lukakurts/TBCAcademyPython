def vowel_counter(word):
    counter = 0
    temp_word = word.lower()
    for i in range(len(temp_word)):
        match temp_word[i]:
            case "a":
                counter += 1
            case "e":
                counter += 1
            case "i":
                counter += 1
            case "o":
                counter += 1
            case "u":
                counter += 1
    return counter

print(f"number of vowel is {vowel_counter("hEllo")}")  
print(f"number of vowel is {vowel_counter("my nAmE is Luka")}")
print(f"number of vowel is {vowel_counter("I am littlE ProgrammEr HahA")}")
    
