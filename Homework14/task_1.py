def finding_max_and_min_degrees(degrees):
    max_degrees = ()
    min_degrees = ()
    for i in degrees:
        max_degrees += (max(i),)
        min_degrees += (min(i),)
    return max_degrees, min_degrees


def finding_day_average_degrees(degrees):
    average_degree = ()
    for i in degrees:
        average = 0
        _sum = 0
        for l in i:
            _sum += l
        average = round(_sum / len(i), 1)
        average_degree += (average,)
    return average_degree

    
def finding_week_average_degrees(day_average_degree):
    week_average_degree = 0
    _sum = 0
    for i in day_average_degree:
        _sum += i
    week_average_degree = _sum / 7
    return week_average_degree


def printing_final_outpit(max_degrees, min_degrees, day_average_degrees, week_average_degree):
    print(f"max degrees are {max_degrees}")
    print(f"min degrees are {min_degrees}")
    print(f"average degrees in day are {day_average_degrees}")
    print(f"average degree in week is {week_average_degree}")


def main():
    degrees = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
    max_degrees, min_degrees = finding_max_and_min_degrees(degrees)
    day_average_degree = finding_day_average_degrees(degrees)
    week_average_degree = finding_week_average_degrees(day_average_degree)
    printing_final_outpit(max_degrees, min_degrees, day_average_degree, week_average_degree)

if __name__ == "__main__":
    main()