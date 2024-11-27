def getting_text():
    text = input("Please enter text: ")
    return text


def counting_letters(text):
    letters = []
    for letter in text:
        if letter not in letters:
            letters.append(letter)
    amount = []
    for letter1 in letters:
        letter_counter = 0
        for letter in text:
            if letter1 == letter:
                letter_counter += 1
        amount.append(letter_counter)
    return letters, amount


def printing_final_output(letters, amount):
    result = {}
    for letter, count in zip(letters, amount):
        result[letter] = count
    for k, v in result.items():
        print(f"{k} - {v}")


def main():
    text = getting_text()
    letters, amount = counting_letters(text)
    printing_final_output(letters, amount)
    

if __name__ == "__main__":
    main()