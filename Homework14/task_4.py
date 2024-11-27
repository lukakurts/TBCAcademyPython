def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        sliced_data = []
        sliced_data += data[i: i + chunk_size]
        yield sliced_data


def main():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8]
    sliced_data = chunk_data(data_list, 5)
    for i in sliced_data:
        print(i)

    data_list_2 = (12, 23, 34, 56, 78, 23, 123, 233)
    sliced_data_2 = chunk_data(data_list_2, 4)
    for i in sliced_data_2:
        print(i)


if __name__ == "__main__":
    main()