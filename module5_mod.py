class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_n_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def find_index_of_x(self, x):
        try:
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            return -1
