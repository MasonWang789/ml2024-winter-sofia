import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to collect training data
def collect_data(description, n):
    print(f"Please provide {n} {description} pairs (x, y):")
    data = []
    for i in range(n):
        x = float(input(f"Enter x for pair {i+1}: "))
        y = int(input(f"Enter y for pair {i+1}: "))
        data.append((x, y))
    return np.array(data)

# Collect training data
N = int(input("Enter the number of training data points (N): "))
train_data = collect_data("training", N)

# Collect test data
M = int(input("Enter the number of test data points (M): "))
test_data = collect_data("test", M)

# Separate features and labels
X_train, y_train = train_data[:, 0].reshape(-1, 1), train_data[:, 1]
X_test, y_test = test_data[:, 0].reshape(-1, 1), test_data[:, 1]

# Initialize variables to store best k and best accuracy
best_k = 0
best_accuracy = 0

# Try different values of k and find the best one
for k in range(1, 11):
    # Train kNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)

    # Predict labels for test data
    y_pred = knn_classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Update best_k and best_accuracy if current accuracy is higher
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

# Output the best k and corresponding test accuracy
print(f"The best k for kNN Classification method is: {best_k}")
print(f"The corresponding test accuracy is: {best_accuracy:.2f}")
