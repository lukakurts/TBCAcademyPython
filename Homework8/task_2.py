input_word = input("Please enter word: ")
input_word2 = input("Please enter word: ")

counter = 0
numeric_value_of_a_word = 0
numeric_value_of_a_word2 = 0

if len(input_word) != len(input_word2):
    print("No")
else:
    while counter < len(input_word):
        numeric_value_of_a_word += ord(input_word[counter])
        numeric_value_of_a_word2 += ord(input_word2[counter])
        counter += 1

    if numeric_value_of_a_word == numeric_value_of_a_word2:
        print("Yes")
    else:
        print("No") 