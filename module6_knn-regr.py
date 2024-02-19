import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.data = None

    def train(self, X, Y):
        self.data = np.column_stack((X, Y))

    def predict(self, x):
        distances = np.linalg.norm(self.data[:, 0] - x, axis=1)
        indices = np.argsort(distances)[:self.k]
        nearest_neighbors = self.data[indices]
        prediction = np.mean(nearest_neighbors[:, 1])
        return prediction

def main():
    # Get user input for N and k
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the value of k for k-NN Regression: "))

    # Initialize the k-NN Regression model
    knn_model = KNNRegression(k)

    # Read N (x, y) points from the user
    X = np.zeros(N)
    Y = np.zeros(N)
    for i in range(N):
        X[i] = float(input(f"Enter x value for point {i + 1}: "))
        Y[i] = float(input(f"Enter y value for point {i + 1}: "))

    # Train the k-NN Regression model
    knn_model.train(X, Y)

    # Get user input for the test point
    test_point = float(input("Enter the x value for the test point: "))

    # Predict Y using k-NN Regression
    if k <= N:
        prediction = knn_model.predict(test_point)
        print(f"The predicted Y value for x={test_point} using {k}-NN Regression: {prediction}")
    else:
        print("Error: k should be less than or equal to the number of data points (N).")

if __name__ == "__main__":
    main()
