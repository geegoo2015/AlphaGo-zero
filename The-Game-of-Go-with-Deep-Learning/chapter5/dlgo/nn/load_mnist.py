# tag::encoding[]
import six.moves.cPickle as pickle
import gzip
import numpy as np


def encode_lable(j):  # <1>
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

# <1>
# end::encoding[]


# tag::shape_load[]
def shape_data(data):
    features = [np.reshape(x, (784, 1))for x in data[0]]  # <1>

    lables = [encode_lable(y) for y in data[1]]  # <2>

    return zip(features, lables)  # <3>


def load_data():
    with gzip.open('mnist.pkl.gz', 'rb') as f:
        train_data, validation_data, test_data = pickle.load(f)  # <4>

    return shape_data(train_data), shape_data(test_data)  # <5>

# <1>
# <2>
# <3>
# <4>
# <5>
# end::shape_load[]