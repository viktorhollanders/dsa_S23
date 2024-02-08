empty_list = []
ones_list = [1]
my_list = [1, 2, 4, 5, 7, 12, 13, 15]
my_list_bad = [1, 2, 4, 5, 12, 7, 13, 15]


class Test:
    def __init__(self) -> None:
        self.size = 8
        self.ordered = True

    def check_empty(self, lis):
        if len(lis) == 0:
            print("empty")

    def check_order(self, lis) -> None:
        """Checks if the list is orderd"""
        if self.check_empty(lis):
            return None
        elif len(lis) == 1:
            self.ordered = True
            print("sucsess")

        else:
            sorted = True
            for i in range(len(lis) - 1):
                if lis[i] > lis[i + 1]:
                    sorted = False
                    break
            if sorted:
                print("sorted")
            else:
                print("not sorted")


test = Test()
# test.check_order(ones_list)
# test.check_order(empty_list)
test.check_order(my_list)
test.check_order(my_list_bad)

