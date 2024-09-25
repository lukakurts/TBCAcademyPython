for i in range(1, 10):
    for l in range(1, 10):
        if(l <= i):
            print(l, " * ", end= " ")
            print(i, " = ", i * l,end=" ")
    print()