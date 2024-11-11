def midpoint(x1, y1, x2, y2):
    midpoint_tuple = ()
    x_midpoint = (x1 + x2) / 2
    y_midpoint = (y1 + y2) / 2
    midpoint_tuple += (x_midpoint, y_midpoint,)
    return midpoint_tuple


def main():
    print(midpoint(2, 4, 6, 8))
    print(midpoint(14, 25, 36, 17))
    print(midpoint(56, 78, 29, 45))
    print(midpoint(124, 345, 239, 654))


if __name__ == "__main__":
    main()