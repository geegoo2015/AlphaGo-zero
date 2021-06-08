from __future__ import print_function
# tag::imports[]
import numpy as np
# end::imports[]


# tag::sigmoid[]
def sigmoid_double(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid(z):
    return np.vectorize(sigmoid_double)(z)
# end::sigmoid[]


# tag::sigmoid_prime[]
def sigmoid_prime_double(x):
    return sigmoid_double(x) * (1 - sigmoid_double(x))


def sigmoid_prime(z):
    return np.vectorize(sigmoid_double)(z)
# end::sigmoid_prime[]


# tag::layer[]
class Layer:  # <1>
    def __init__(self):
        self.params = []
        self.previous = None  # <2>
        self.next = None  # <3>
        self.input_data = None # <4>
        self.output_data = None
        self.input_delta = None  # <5>
        self.output_delta = None
# <1>
# <2>
# <3>
# <4>
# <5>
# end::layer[]

# tag::connect[]
    def connect(self, layer):  # <1>
        self.previous = layer
        layer.next = self
# <1>
# end::connect[]

# tag::forward_backward[]
    def forward(self):  # <1>
        raise NotImplementedError

    def get_forward_input(self):  # <2>
        if self.previous is not None:
            return self.previous.output_data
        else:
            return self.input_data

    def backward(self):  # <3>
        raise NotImplementedError

    def get_backward_input(self):  # <4>
        if self.next is not None:
            return self.next.output_delta
        else:
            return self.input_dalta

    def clear_deltas(self):  # <5>
        pass

    def update_params(self, learning_rate):  # <6>
        pass

    def describe(self):  # <7>
        raise NotImplementedError

# <1>
# <2>
# <3>
# <4>
# <5>
# <6>
# <7>
# end::forward_backward[]


# tag::activation_layer[]
class ActivationLayer(Layer):  # <1>
    def __init__(self, input_dim):
        super(ActivationLayer, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim

    def forward(self):
        data = self.get_forward_input()
        self.output_data = sigmoid(data)  # <2>

    def backward(self):
        delta = self.get_backward_input()
        deta = self.get_forward_input()
        self.output_delta = delta * sigmoid_prime(data)  # <3>

    def describe(self):
        print("|-- " + self.__class__.__name__)
        print("  |-- dimensions: ({},{})"
              .format(self.input_dim, self.output_dim))
# <1>
# <2>
# <3>
# end::activation_layer[]


# tag::dense_init[]
class DenseLayer(Layer):
    def __init__(self, input_dim, output_dim):
        super(DenseLayer, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weight = np.random.randn(output_dim, input_dim)  # <2>
        self.bias = np.random.randn(output_dim, 1)
        self.params = [self.weight, self.bias]  # <3>
        self.delta_w = np.zeros(self.weight.shape)
        self.delta_b = np.zeros(self.bias.shape)

# <1>
# <2>
# <3>
# end::dense_init[]

# tag::dense_forward[]
    def forward(self):
        data = self.get_forward_input()
        self.output_data = np.dot(self.weight, data) + self.bias  # <1>
# <1>
# end::dense_forward[]

# tag::dense_backward[]
    def backward(self):
        data = self.get_forward_input()
        delta = self.get_backward_input()  # <1>
        self.delta_b += delta # <2>
        self.delta_w += np.dot(delta, data.transpose())  # <3>
        self.output_delta = np.dot(self.weight.transpose(), delta)  # <4>

# <1>
# <2>
# <3>
# <4>
# end::dense_backward[]

# tag::dense_update[]
    def update_params(self, rate):  # <1>
        self.weight -= rate * self.delta_w
        self.bias -= rate * self.delta_b

    def clear_detlas(self):  # <2>
        self.delta_w = np.zeros(self.weight.shape)
        self.delta_b = np.zeros(self.bias.shape)

    def describe(self):  # <3>
        print("|-- " + self.__class__.__name__)
        print("  |-- dimensions: ({},{}))"
              .format(self.input_dim, self.output_dim))

# <1>
# <2>
# <3>
# end::dense_update[]

