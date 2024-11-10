def text_reversal(text):
    reversed_text = ""
    for i in range(len(text)):
        reversed_text += text[(len(text) - 1) - i]
    print(reversed_text)

text_reversal("hello")
text_reversal("D: remmargorp elttil a llits ma I")
