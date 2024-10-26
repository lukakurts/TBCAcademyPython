def calculating_max(*numbers):
    _max = 0
    for i in numbers:
        if _max < i:
            _max = i
    print(f"max number is {_max}")

calculating_max(3, 4, 2, 5, 6)
calculating_max(23, 44, 45, 18, 39, 45, 89)
calculating_max(123, 342, 456, 783, 186, 129)