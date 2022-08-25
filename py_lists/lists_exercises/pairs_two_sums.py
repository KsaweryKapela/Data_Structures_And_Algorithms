from random import randint


class FindPairs:

    def __init__(self):
        self.given_number = randint(5, 20)
        self.random_list = []
        self.list_of_pairs = []

    def populate_random_list(self):
        for number in range(100):
            self.random_list.append(randint(1, 100))

    def find_pairs(self):
        for number in self.random_list:
            for item in self.random_list:
                if number + item == self.given_number:
                    if [number, item] not in self.list_of_pairs and [item, number] not in self.list_of_pairs:
                        self.list_of_pairs.append([number, item])

    def print_pairs(self):
        self.populate_random_list()
        self.find_pairs()
        print('The list', self.random_list)
        print('The number ==', self.given_number)
        print('The set of pairs is:', self.list_of_pairs)


FindPairs().print_pairs()


