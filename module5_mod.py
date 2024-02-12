class NumberProcessor:
    def __init__(self):
        self.n = 0
        self.numbers = []

    def read_n(self):
        while True:
            try:
                self.n = int(input("Enter a positive integer N: "))
                if self.n > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def read_numbers(self):
        print("Enter {} numbers:".format(self.n))
        for i in range(self.n):
            while True:
                try:
                    num = int(input("Enter number {}: ".format(i + 1)))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

    def search_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
