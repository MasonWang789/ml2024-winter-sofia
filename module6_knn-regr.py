import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        distances = np.abs(self.X_train[:, np.newaxis] - X_test)
        distances_sum = np.sum(distances, axis=2)
        nearest_indices = np.argsort(distances_sum)[:self.k]
        nearest_labels = self.y_train[nearest_indices]
        return np.mean(nearest_labels, axis=0)

def main():
    try:
        N = int(input("Enter the number of points (N): "))
        k = int(input("Enter the value of k for k-NN Regression: "))
        if k > N:
            raise ValueError("k should be less than or equal to N")

        X_train = np.zeros((N, 1))
        y_train = np.zeros(N)

        print("Enter the (x, y) points:")
        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            X_train[i] = x
            y_train[i] = y

        knn_reg = KNNRegression(k)
        knn_reg.fit(X_train, y_train)

        X_test = float(input("Enter the value of X for prediction: "))
        y_pred = knn_reg.predict(np.array([[X_test]]))
        print(f"The predicted Y value for X = {X_test} is {y_pred}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
