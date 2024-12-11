# აქ ვერ მივხვდი ერთეულის ღირებულებაზე იყო საუბარი თუ ჯამურ ღირებულებაზე და მე ჯამური ღირებულების მიხედვით დავწერე.
def main():
    with open("Homework18/data.txt", "r") as file:
        for line in file:
            if(float(line.split(",")[-1]) * float(line.split(",")[-2]) < 10):
                with open("Homework18/small.txt", "a") as file:
                    file.write(line)
            else:
                with open("Homework18/big.txt", "a") as file:
                    file.write(line)

if __name__ == "__main__":
    main()