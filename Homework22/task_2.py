class Queue:
    def __init__(self):
        self._list = []
    
    def insert(self, n):
        self._list.append(n)
    
    def pop(self):
        number = self._list[0]
        self._list.remove(number)
        return number
    
    # ეს მეორე ვარიანტია უბრალოდ რადგან ეს ფუნქცია უკვე არსებობს გადავწყვიტე სხვანაირად დამეწერა
    # def pop(self):
    #     return self._list.pop(0)
    
    def __str__(self):
        self._list.reverse()
        return f"{self._list}"


def main():
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(45)
    q.insert(32)
    print(q.pop())
    print(q.pop())
    print(q)

if __name__ == "__main__":
    main()
