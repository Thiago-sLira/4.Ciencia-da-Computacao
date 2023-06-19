class Conjunto:
    def __init__(self):
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

    def __str__(self):
        string = "{"

        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string

    def __contains__(self, item):
        return self.set[item]

    def union(self, other):
        new_set = Conjunto()

        for i in range(1001):
            if self.set[i] or other.set[i]:
                new_set.add(i)
        return new_set

    def intersection(self, other):
        new_set = Conjunto()

        for i in range(1001):
            if self.set[i] and other.set[i]:
                new_set.add(i)
        return new_set

    def difference(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and not conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def issubset(self, conjunto_b):
        for index in range(1001):
            if self.set[index] and not conjunto_b.set[index]:
                return False

        return True

    def issuperset(self, conjunto_b):
        for index in range(1001):
            if conjunto_b.set[index] and not self.set[index]:
                return False

        return True


if __name__ == "__main__":
    # conj = Conjunto()
    # for i in [1, 2, 3]:
    #     conj.add(i)
    # print(conj)
    # print(1 in conj)
    # print(0 in conj)

    # conj2 = Conjunto()
    # for i in [1, 2, 3]:
    #     conj2.add(i)
    # print(conj2)

    # conj3 = Conjunto()
    # for i in [7, 2, 10]:
    #     conj3.add(i)
    # print(conj3)

    # conj4 = Conjunto()
    # print(conj4)
    # conj1 = Conjunto()
    # for i in range(1, 11):
    #     conj1.add(i)

    # conj2 = Conjunto()
    # for i in range(10, 21):
    #     conj2.add(i)

    # conj3 = conj1.union(conj2)
    # print(conj3)
    conj1 = Conjunto()
    for i in [1, 2, 3]:
        conj1.add(i)

    conj2 = Conjunto()
    for i in [7, 2, 10]:
        conj2.add(i)

    conj3 = conj1.intersection(conj2)
    print(conj3)
