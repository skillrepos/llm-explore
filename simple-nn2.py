import numpy as np
 
# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
 
# Derivative of the sigmoid function, used in backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)
 
# Input datasets
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])
 
# Output datasets, corresponding to XOR for each input pair
expected_output = np.array([[0], [1], [1], [0]])
 
# Set the seed for reproducibility
np.random.seed(0)
 
# Initialize weights randomly with mean 0
hidden_weights = np.random.uniform(size=(2, 2))
hidden_bias =np.random.uniform(size=(1, 2))
output_weights = np.random.uniform(size=(2, 1))
output_bias = np.random.uniform(size=(1, 1))
 
# Learning rate
lr = 0.1
 
# Number of epochs for learning
epochs = 10000
 
# Training algorithm
for _ in range(epochs):
    # Forward propagation
    hidden_layer_activation = np.dot(inputs, hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)
 
    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)
 
    # Backpropagation
    error = expected_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)
   
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
 
    # Updating Weights and Biases
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
    output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
    hidden_weights += inputs.T.dot(d_hidden_layer) * lr
    hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr
 
# Print final output from training
print("Predicted output from neural network after 10,000 epochs:")
print(predicted_output)