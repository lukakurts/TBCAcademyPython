def getting_sequence(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        print(n, end=" ")
        return getting_sequence(n // 2)
    else:
        print(n, end=" ")
        return getting_sequence(n * 3 + 1)


def getting_cached_sequence(n, index, cache):
    if cache.get(index):
        return cache.get(index)
    cache[index] = []
    if n == 1:
        pass
    elif n % 2 == 0:
        getting_cached_sequence(n // 2, index, cache)
    else:
        getting_cached_sequence(n * 3 + 1, index, cache)
    cache[index].append(n)
    return cache[index]


def main():
    print(getting_sequence(3))
    sequence = getting_cached_sequence(3, 3, {})
    sequence.reverse()
    print(sequence)
    


if __name__ == "__main__":
    main()