def creating_list():
    words = ["rame", "ra", "me", "Tus", "vaa", "ise"]
    return words


def filtring_list(words):
    filterd_list = [elements for elements in words if len(elements) <= 3]
    return filterd_list


def printing_filtered_list_in_upper_cases(filtered_list):
    filtered_list_in_upper_case = list(map(lambda a : a.upper(), filtered_list))
    print(filtered_list_in_upper_case)


def main():
    words = creating_list()
    filtered_list = filtring_list(words)
    printing_filtered_list_in_upper_cases(filtered_list)

if __name__ == "__main__":
    main()