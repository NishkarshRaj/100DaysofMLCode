# Artificial Neural Network

Artificial Neural Networks (ANNs) or simply Neural Networks (NNs) are machine learning models inspired by biological neural networks present inside the brain.  

## A Top-Level Overview of ANNs

An ANN is based on a collection of connected nodes called neurons that relay information to each other via specific connections (or edges) resembling biological synapses. The "signal" or input values at each node is a real number and the output of each neuron is calculated by non-linear manipulation of the weighted sum of the inputs. All the edges have a random weight initially and as learning proceeds, the weights are adjusted.  
The weight of an edge determines the strength of connection between two neurons. The stronger the connection, the higher the corresponding weight. The neurons are stacked horizontally into layers, the first layer being the input layer and the last one being the output layer. Signals often travel via multiple layers before passing from the input to output layer.

## Components and Functioning of an ANN

### Neurons

ANNs are composed of artificial neurons that model how neurons in our brains function. Each individual neuron takes in some inputs and produces a single output which can then be passed onto different neurons. Any neuron can have multiple inputs but it will only produce one output value (which can then be fed into one or multiple other neurons).

![Neuron](/img/neuron.jpg)

Just like neurons in our brain, the raw output of a neuron is passed through an activation function which decides whether the raw output of the neuron was really high enough or not. Some examples of activation functions are ReLU and Sigmoid functions. They help bound the output values of neurons too to help with the computation.

### Layers, Weights, and Bias

The network consists of many connected neurons. Vertically stacking the neurons forms what are called layers. Here is an illustration of different layers of an example ANN.  

![ANN](/img/ANN_structure.jpg)

Neurons in different layers are connected via connections. The strength of these connections are represented by their weights. Weights generally vary from -1 to +1 for computational simplicity. In the above illustration, the thickness of connection is directly proportional to their weights and positive connections are shown in blue colour while negative connections are shown in black colour.

Along with all the inputs, we also have a bias neuron which is generally 1 in most cases. This bias neuron is like the y-intercept when we are dealing with Linear Regression. It helps with better fitting the data. A proper in depth characterization for bias in an ANN can be found in this [article](https://www.geeksforgeeks.org/effect-of-bias-in-neural-network/).  
In the diagram above, the bias neuron is represented as a red neuron and all the red edges have a value of +1.

### Propagation

Propagation is the process of passing the outputs of each layer to the successive layer. The propagation function is how the values are passed on starting from the input neuron to the final output neurons. 

### The Cost Function

To know how well our ANN is predicting, we devise something called the cost function. The cost function tells us how "off" we are from a "perfect" prediction. Simple cost functions may be direct cost functions like calculating the mean-squared error from predictions and actual values.

### Backpropagation

The backpropagation is just the reverse process of the propagation step.  
The backpropagation algorithm is how we train or better our ANN. Using values from the cost function, we get a gradient (or direction) in which we are off from the real predicitons. Working out backwards from the predictions to the weights of the different neurons, we slowly adjust the weights so that they perform a little better with each iteration. The algorithm can be simply visualized in the following flowchart.

![Flowchart Backprop](/img/backprop.jpg)

## The Algorithm after Creating a Neural Network

Initialization
- Initialize all weights to random values.

Training (repeat desired number of times)
- Provide input and output values from training data.
- Carry out propagation to get output from input datapoints.
- Test the output value against the real value from the data point.
- Carry out backpropagation for the data point to adjust weights.

Validation
- Use a small part of the dataset (20% in many cases) for validation.
- Provide just the input values.
- Carry out propagation to get the output values.
- Calculate a score based on how well the output compares to actual values.
- If score is good enough, Yay! Else, repeat training with more data points or change connection structure (network topology).



### References

- [Deep Learning and Neural Networks](https://www.youtube.com/watch?v=ILsA4nyG7I0&ab_channel=BrandonRohrer) - a video by Brandon Rohrer that explains the functioning of a neural network in the simplest and most intuitive way possible.