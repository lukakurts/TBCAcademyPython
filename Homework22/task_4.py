class ExtendedList(list):
    def max(self):
        try:
            _max = self[0]
            for number in self:
                if number > _max:
                    _max = number
            return _max
        except IndexError as error:
            return f"There is no number in this list"
    
    def min(self):
        try:
            _min = self[0]
            for number in self:
                if number < _min:
                    _min = number
            return _min
        except IndexError as error:
            return f"There is no number in this list"
        
# ეს ისევ მეორე მარტივი ვარიანტია უბრალოდ ისევ უკვე ჩაშენებული ფუნქციებია მხოლოდ და სხვანაირად დავწერე
    # def max(self):
    #     try:
    #         return max(self)
    #     except Exception as error:
    #         return f"There is no number in this list"
    
    # def min(self):
    #     try:
    #         return min(self)
    #     except Exception as error:
    #         return f"There is no number in this list"


def main():
    l = ExtendedList((10, 23, 43, 56, 4, 21))
    print(l.max())
    print(l.min())
    l2 = ExtendedList((2, 3, 4, 12, 35, 67, 89))
    print(l2.max())
    print(l2.min())
    l3 = ExtendedList((0, 23, 4, 89, 444, 24, 67, 127))
    print(l3.max())
    print(l3.min())
    l4 = ExtendedList()
    print(l4.max())
    print(l4.min())
    l5 = ExtendedList([4])
    print(l5.max())
    print(l5.min())


if __name__ == "__main__":
    main()