def getting_route(start_point, end_point, graph):
    keys_list = []
    for k in graph.keys():
        keys_list.append(k)
    if start_point in keys_list:
        if end_point in graph[start_point]:
            return True
        is_true = False
        for i in graph[start_point]:
            if i in keys_list:
                    if end_point in graph[i]:
                        is_true = True
        if is_true:
            return True
        else:
            for i in graph[start_point]:
                start_point = i
                return getting_route(start_point, end_point, graph)
    return False


def main():
    graph = {
    "A" : ["B", "C"],
    "B" : ["D"],
    "C" : ["E"],
    "D" : ["S"],
    "S" : ["K"]
}
    print(getting_route("A", "K", graph))


if __name__ == "__main__":
    main()