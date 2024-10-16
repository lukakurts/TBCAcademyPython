sentence = input("please enter string: ")

for i in range(len(sentence)):
    if i % 2 != 0 or sentence[i] == 'e':
        continue
    else:
        print(sentence[i])