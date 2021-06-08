from __future__ import print_function

# tag::mcts_go_cnn_simple_preprocessing[]
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D, Flatten  # <1>

np.random.seed(123)
X = np.load('../generated_games/features-200.npy')
Y = np.load('../generated_games/lables-200.npy')

samples = X.shape[0]
size = 9
input_shape = (size, size, 1)  # <2>

X = X.reshape(samples, size, size, 1)  # <3>

train_samples = 10000
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]

# <1>
# <2>
# <3>
# end::mcts_go_cnn_simple_preprocessing[]


# tag::mcts_go_cnn_simple_model[]
model = Sequential()
model.add(Conv2D(filters=32,  # <1>
                 kernel_size=(3, 3),  # <2>
                 activation='sigmiod',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='sigmoid'))  # <3>
