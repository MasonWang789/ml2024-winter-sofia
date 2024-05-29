import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def get_input_pairs(count, data_type):
    data = []
    print(f"Please enter {count} (x, y) pairs for the {data_type} set:")
    for i in range(count):
        x = float(input(f"Enter x value for pair {i+1}: "))
        y = int(input(f"Enter y value for pair {i+1}: "))
        data.append((x, y))
    return np.array(data)

def main():
    # Read number of training pairs
    N = int(input("Enter the number of training pairs (N): "))
    train_data = get_input_pairs(N, "training")
    X_train = train_data[:, 0].reshape(-1, 1)
    y_train = train_data[:, 1]

    # Read number of test pairs
    M = int(input("Enter the number of test pairs (M): "))
    test_data = get_input_pairs(M, "test")
    X_test = test_data[:, 0].reshape(-1, 1)
    y_test = test_data[:, 1]

    # Finding the best k
    best_k = 1
    best_accuracy = 0
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy for k={k}: {accuracy:.2f}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    # Output the best k and corresponding accuracy
    print(f"The best k is {best_k} with an accuracy of {best_accuracy:.2f}")

if __name__ == "__main__":
    main()
