class FlatIterator:

    def __init__(self, list_of_list):
        self.my_list = list_of_list

    def __iter__(self):
        self.main_counter = 0
        self.nested_counter = -1

        return self

    def __next__(self):

        self.nested_counter += 1
        if self.nested_counter == len(self.my_list[self.main_counter]):
            self.main_counter += 1
            self.nested_counter = 0

        if self.main_counter == len(self.my_list):
            raise StopIteration
        # return self.list[self.list_counter]
        return self.my_list[self.main_counter][self.nested_counter]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
