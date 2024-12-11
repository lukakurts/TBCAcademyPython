class Insert:
    def __init__(self):
        self._list = []
    
    def insert(self, n):
        if n not in self._list:
            self._list.append(n)
    
    def member(self, n):
        if n in self._list:
            return True
        else:
            return False
    
    def remove(self, n):
        if n in self._list:
            self._list.remove(n)
        else:
            raise ValueError(f"couldn't find number: {n}")    
    
    def __str__(self):
        self._list.sort()
        return f"list in sorted {self._list}"


def main():
    _list = Insert()
    _list.insert(9)
    _list.insert(11)
    _list.insert(7)
    _list.remove(9)
    _list.insert(8)
    _list.insert(12)
    _list.insert(1)  
    _list.insert(8)
    _list.insert(9)
    print(_list.member(4))
    print(_list.member(8))
    print(_list)
    _list.remove(4)


if __name__ == "__main__":
    main()