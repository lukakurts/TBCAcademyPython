import json

def main():
    my_dict = {}
    with open("Homework18/data.txt", "r") as file:
        max_amount = max(float(line.split(",")[-2]) for line in file) 
        
    with open("Homework18/data.txt", "r") as file:
        for line in file:
            if float(line.split(",")[-2]) == max_amount:
                name = line.split(",")[0]
    my_dict["max amount owner"] = name


    with open("Homework18/data.txt", "r") as file:
        max_cost = max(float(line.split(",")[-2]) * float(line.split(",")[-1]) for line in file) 
    
    
    with open("Homework18/data.txt", "r") as file:
         count = 0
         for line in file:
            if float(line.split(",")[-2]) * float(line.split(",")[-1]) == max_cost:
                name2 = line.split(",")[0]
            count += 1
    my_dict["max cost owner"] = name2

    
    with open("Homework18/data.txt", "r") as file:
        sum_of_costs = sum(float(line.split(",")[-2]) * float(line.split(",")[-1]) for line in file)
    

    with open("Homework18/data.txt", "r") as file:
        sum_of_lines = sum(1 for line in file)
        cost_average = sum_of_costs / sum_of_lines
    my_dict["average cost"] = cost_average


    with open("Homework18/data.txt", "r") as file:
        sum_of_prices = sum(float(line.split(",")[-1]) for line in file)
        average_price = sum_of_prices / sum_of_lines
    my_dict["average price"] = average_price


    with open("Homework18/data.txt", "r") as file:
        for line in file:
            if float(line.split(",")[-2]) == max_amount:
                most_sold_product = line.split(",")[1]
    my_dict["most sold product"] = most_sold_product


    with open("Homework18/stats.json", "w") as file:
        json.dump(my_dict, file, indent=4)


if __name__ == "__main__":
    main()