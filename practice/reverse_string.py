# reverse a string
def reverse_string(str):

    reversed_str = ""
    for index, word in enumerate(str):
        reversed_str += str[len(str) - 1 - index]
    return reversed_str


class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def remove(self, index):
        self.shift(index)
        self.length -= 1

    def pop(self, index):
        del self.data[self.length]
        self.length -= 1

    def shift(self, index):
        # if the index is the last one the pop it
        if index == self.length - 1:
            del self.data[self.length - 1]
            return

        # find the index, start looping at the index
        for i in range(index, self.length - 1):
            if i < self.length - 1:
                self.data[i] = self.data[i+1]
        del self.data[self.length - 1]

    def __str__(self):
        return f"{self.data}"

array = Array()
array.append(2)
array.append(4)
array.append(6)
array.remove(1)
print(array)
