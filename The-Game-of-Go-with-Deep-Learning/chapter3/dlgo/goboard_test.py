import unittest

import six

from dlgo.goboard import Board, GameState, Move
from dlgo.gotypes import Player,Point


class BoardTest(unittest.TestCase):
    def test_capture(self):
