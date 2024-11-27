def getting_friendships():
    friendships = {}
    while True:
        names_input = input("Please enter names: ")
        if names_input == "FINISH":
            break
        name1, name2 = names_input.split("-")
        if name1 not in friendships:
            friendships[name1] = []
        if name2 not in friendships:
            friendships[name2] = []
        friendships[name1].append(name2)
        friendships[name2].append(name1)
    return friendships
    

def printing_final_output(friendships):
    for person in friendships:
        print(f"{person} -", end= " ")
        for i in range(len(friendships[person])):
            print(f"{friendships[person][i]} ", end= "")
        print()


def main():
    friendships = getting_friendships()
    printing_final_output(friendships)


if __name__ == "__main__":
    main()