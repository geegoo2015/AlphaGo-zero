from __future__ import print_function
# tag::bot_vs_bot[]
from dlgo.agent.naive import RandomBot
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: RandomBot(),
        gotypes.Player.white: RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.3)  # <1>

        print(chr(27) + "[2J")  # <2>
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()

# <1> 将睡眠定时器设置为0.3s，以免机器人动作的输出速度太快而无法观察
# <2> 在每个落子动作之前需要清除屏幕。这样，棋盘就会始终显示在命令行上的相同位置
# end::bot_vs_bot[]