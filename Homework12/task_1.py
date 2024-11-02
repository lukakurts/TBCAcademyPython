def calculating_sum(degrees: list):
    sum = 0
    length = len(degrees)
    for element in degrees:
        sum += element
    return sum, length

def calculating_average(sum_of_degrees: int, length_of_degrees: int):
    average = sum_of_degrees / length_of_degrees
    return average

def final_result_output(average_of_degrees: float):
    print("Average is:", average_of_degrees)
    

def main():
    list_of_degrees = [22, 25, 19, 23, 25, 26, 23]
    sum_of_degrees, length_of_degrees = calculating_sum(list_of_degrees)
    average_of_degrees = calculating_average(sum_of_degrees, length_of_degrees)
    final_result_output(average_of_degrees)

if __name__ == "__main__":
    main()