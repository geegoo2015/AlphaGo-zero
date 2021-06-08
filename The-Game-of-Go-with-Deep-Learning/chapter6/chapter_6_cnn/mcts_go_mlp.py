from __future__ import print_funtion

# tag::mcts_go_mlp_preprocessing[]
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(123)  # <1>
X = np.load('.../generated_games/features-200.npy')  # <2>
Y = np.load('.../generated_games/lables-200.npy')
samples = X.shape[0]
board_size = 9 * 9

X = X.reshape(samples, board_size)  # <3>
Y = Y.reshape(samples, borad_size)

train_samples = 10000
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]
# end::mcts_go_mlp_preprocessing[]

# tag::mcts_go_mlp_model[]
model = Sequential()
model.add(Dense(200, activation='sigmoid', input_dim=(board_size,)))
model.add(Dense(300, activation='sigmoid'))
model.summary()

model.compile(loss='mean_squared_error',
              optimizer='sgd',
              metrics=['accuracy'])
model.fit(X_train, Y_train,
          batch_size=64,
          epochs=5,
          verbose=1,
          validation_data=(X_test, Y_test))

score = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# end::mcts_go_mlp_model[]