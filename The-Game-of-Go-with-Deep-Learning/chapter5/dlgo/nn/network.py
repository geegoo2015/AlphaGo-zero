from __future__ import print_function
from six.moves import range
# tag::mse[]
import random
import numpy as np


class MSE:  # <1>
    def __init__(self):
        pass

    @staticmethod
    def loss_function(predictions, lables):
        diff = predictions - lables
        return 0.5 * sum(diff * diff)[0]   # <2>

    @staticmethod
    def loss_derivative(predictions, lables):
        return predictions - lables


# <>
# <>
# <>
# end::mse[]

# tag::sequentialNetwork_init[]
class SequentialNetwork:  # <1>
    def __init__(self, loss=None):
        print("Initialize Network...")
        self.layers = []
        if loss is None:
            self.loss = MSE()  # <2>

# <>
# <>
# end::sequential_init[]

# tag::add_layers[]
    def add(self, layer):  # <1>
        self.layers.append(layer)
        layer.describe()
        if len(self.layers) > 1:
            self.layers[-1].connect(self.layers[-2])

# <>
# end::add_layers[]

# tag::train[]
    def train(self, training_data, epochs, mini_batch_size,
              learning_rate, test_data=None):
        n = len(training_data)
        for epoch in range(epochs):  # <1>
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k + mini_batch_size] for
                k in range(0, n, mini_batches)  # <2>
            ]
            for mini_batch in mini_batches:
                self.train_batch(mini_batch, learning_rate)  # <3>
            if test_data:
                n_test = len(test_data)
                print("Epoch {0}: {1} / {2}"
                      .format(epoch, self.evaluate(test_data), n_test))    # <4>
            else:print("Epoch {0} complete".format(epoch))

# <1>
# <2>
# <3>
# <4>
# end::train[]

# train_batch[]
    def train_batch(self, mini_batch, learning_rate):
        self.forward_backward(mini_batch)  # <1>
        self.update(mini_batch, learning_rate)  # <2>

# <1>
# <2>
# end::train_batch[]

# tag::update_ff_bp[]
    def update(self, mini_batch, learning_rate):
        learning_rate = learning_rate / len(mini_batch)  # <1>
        for layer in self.layers:
            layer.update_params(learning_rate)  # <2>
        for layer in self.layers:
            layer.clear_delatas()  # <3>

    def forward_backward(self, mini_batch):
        for x, y in mini_batch:
            self.layers[0].input_data = x
            for layer in self.layers:
                layer.forward()  # <4>
            self.layers[-1].input_delta = \
                self.loss.loss_derivative(self.layers[-1].output_data, y)  # <5>
            for layer in reversed(self,layers):
                layer.backward()  # <6>

# <1>
# <2>
# <3>
# <4>
# <5>
# <6>
# end::update_ff_bp[]

# tag::eval[]
    def single_forward(self, x):  # <1>
        self.layers[0].input_date = x
        for layer in self.layers:
            layer.forward()
        return self.layers[-1].output_data

    def evaluate(self, test_data):  # <2>
        test_results = [(
            np.argmax(self.single_forward(x)),
            np.argmax(y)
        ) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
# <1>
# <2>
# end::eval[]