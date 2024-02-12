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

def main():
    processor = NumberProcessor()

    # Read N
    processor.read_n()

    # Read N numbers
    processor.read_numbers()

    # Read X
    while True:
        try:
            x = int(input("Enter an integer X: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Search for X in the list of numbers
    result = processor.search_number(x)

    # Output result
    if result == -1:
        print("The number {} was not among the provided numbers.".format(x))
    else:
        print("The index of {} is: {}".format(x, result))

if __name__ == "__main__":
    main()
