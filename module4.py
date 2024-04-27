def find_index_of_x(N, numbers, X):
    for i in range(N):
        if numbers[i] == X:
            return i + 1  # Indexing starts from 1
    return -1

def main():
    N = int(input("Enter the value of N (positive integer): "))
    
    numbers = []
    for i in range(N):
        num = int(input("Enter number {}: ".format(i + 1)))
        numbers.append(num)
    
    X = int(input("Enter the value of X (integer): "))
    
    index = find_index_of_x(N, numbers, X)
    
    if index == -1:
        print("-1")
    else:
        print("Index of {} is: {}".format(X, index))

if __name__ == "__main__":
    main()
