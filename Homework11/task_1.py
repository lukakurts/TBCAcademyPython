def convertation(degree):
    fahrenhate = degree * 9 / 5 + 32
    celsius = (degree - 32) * 5 / 9
    print(f"{degree} celsius to fahrenhate is {fahrenhate}")
    print(f"{degree} fahrenheit to celsius is {celsius}")

def main():
    convertation(23)
    convertation(43)
    convertation(145)

if __name__ == "__main__":
    main()