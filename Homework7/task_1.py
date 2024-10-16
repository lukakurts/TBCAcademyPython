word = input("please enter string: ")

for i in range(len(word)):
    if i % 2 != 0 or word[i] == 'e':
        continue
    else:
        print(word[i])