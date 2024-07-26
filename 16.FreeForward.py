import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.bias1 = np.zeros((1, self.hidden_size))
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        self.bias2 = np.zeros((1, self.output_size))
        
    def forward(self, inputs):
        
        self.hidden_layer_activation = np.dot(inputs, self.weights1) + self.bias1
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_activation)
        self.output_layer_activation = np.dot(self.hidden_layer_output, self.weights2) + self.bias2
        self.output = self.sigmoid(self.output_layer_activation)
        return self.output
    
    def sigmoid(self, x):
        
        return 1 / (1 + np.exp(-x))


if __name__ == "__main__":
    
    input_size = 2
    hidden_size = 3
    output_size = 1
    neural_net = NeuralNetwork(input_size, hidden_size, output_size)
    
    
    inputs = np.array([[0.5, 0.7], [0.2, 0.3]])
    predictions = neural_net.forward(inputs)
    
    print("Input:\n", inputs)
    print("\nPredictions:\n", predictions)
