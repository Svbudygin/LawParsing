class Skeleton:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        if new_next is None or type(new_next) == Skeleton:
            self.__next = new_next


class Muscles:
    def __init__(self):
        self.top = None

    @property
    def tail1(self):
        return self.tail

    def push(self, obj):
        if self.top is None:
            self.tail = self.top = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def pop_first(self):
        data = self.top
        self.top = self.top.next
        return data

    def get_data(self):

        lst = []
        obj = self.top
        while obj is not None:
            lst.append(obj.data)
            obj = obj.next
        return lst
