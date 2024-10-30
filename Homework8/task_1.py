input_word = input("Please enter word: ")

check_word = ""
input_word_without_symbols = ""
counter = 0

while counter < len(input_word):
    counter += 1
    if input_word[counter - 1].isupper() or input_word[-counter].isupper:
        input_word = input_word.lower()
    if input_word[-counter].isalpha():
        check_word += input_word[-counter]
    if input_word[counter - 1].isalpha():
        input_word_without_symbols += input_word[counter - 1]
    

if(input_word_without_symbols == check_word):
    print("is palindrome")
else:
    print("is not palindrome")
