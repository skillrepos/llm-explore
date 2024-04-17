import numpy as np
 
# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
 
# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)
 
# Input dataset
inputs = np.array([[0,0,1],
                   [1,1,1],
                   [1,0,1],
                   [0,1,1]])
 
# Output dataset
expected_output = np.array([[0],
                            [1],
                            [1],
                            [0]])
 
# Seed the random number generator for reproducibility
np.random.seed(1)
 
# Initialize weights randomly with mean 0
weights = 2 * np.random.random((3, 1)) - 1
 
# Learning rate
learning_rate = 0.1
 
# Training iterations
for iteration in range(10000):
    # Forward propagation
    input_layer = inputs
    outputs = sigmoid(np.dot(input_layer, weights))
 
    # Error
    error = expected_output - outputs
 
    # Backpropagation
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments) * learning_rate
 
# Output the results
print("Output After Training:")
print(outputs)
