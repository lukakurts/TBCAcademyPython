class Stack:
    def __init__(self):
        self._list = []
    
    def push(self, element):
        self._list.append(element)
    
    def pop(self):
        number = self._list[-1]
        self._list.remove(number)
        return number
    
    def peek(self):
        return self._list[-1]
    
    def is_empty(self):
        if self._list:
            return False
        else:
            return True
    
    def size(self):
        size = 0
        for _ in self._list:
            size += 1
        return size
    
    def __str__(self):
        self._list.reverse()
        return f"{self._list}"
    

def main():
    s = Stack()
    print(f"Is empty: {s.is_empty()}")
    s.push(9)
    s.push(10)
    s.push(13)
    s.push(19)
    print(f"First element is: {s.peek()}")
    print(f"Size of stack is: {s.size()}")
    print(f"Removed element is: {s.pop()}")
    print(f"First element is: {s.peek()}")
    print(f"Size of stack is: {s.size()}")
    print(f"Removed element is: {s.pop()}")
    print(f"Is empty: {s.is_empty()}")
    print(s)


if __name__ == "__main__":
    main()