# tag::importlib[]
import importlib
# end::importlib[]

__all__ = [
    'Encoder',
    'get_encoder_by_name',
]


# tag::base_encoder[]
class Encoder:
    def name(self):  # <1>
        raise NotImplementedError()

    def encode(self, game_state):  # <2>
        raise NotImplementedError()

    def encode_point(self, point):  # <3>
        raise NotImplementedError()

    def decode_point_index(self, index):  # <4>
        raise NotImplementedError()

    def num_point(self):  # <5>
        raise NotImplementedError()

# <1>
# <2>
# <3>
# <4>
# <5>
# <6>
# end::base_encoder[]

# tag::encoder_by_name[]
def get_encoder_by_name(name, board_size):  # <1>
    if isinstance(board_size, int):
        board_size = (board_size, board_size)  # <2>
    module = importlib.import_module('dlgo.encoders.' + name)
    constructor = getattr(module, 'create')  # <3>
    return constructor(board_size)

# <1>
# <2>
# <3>
# end::encoder_by_name[]