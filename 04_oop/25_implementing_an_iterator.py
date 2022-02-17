class MyList:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    # making it subscriptable
    def __getitem__(self, index):
        return self.__items[index]

    # add item assignment support:
    def __setitem__(self, index, value):
        self.__items[index] = value

    # add del item support:
    def __delitem__(self, index):
        del self.__items[index]

    # iterator protocol:
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f"{self.__class__.__name__} ({self.__items})"

    # optional:
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    list1 = MyList()
    list1.add("Joaquim")
    list1.add("Maria")

    # for value in list1:
    #     print(value)

    # print(next(list1))
    # print(next(list1))

    list1[0] = "Gregorio"

    print(list1[0])
    print(list1[1])

    del list1[0]

    # now list1 isn't an iterator anymore
    list1 = list(list1)
