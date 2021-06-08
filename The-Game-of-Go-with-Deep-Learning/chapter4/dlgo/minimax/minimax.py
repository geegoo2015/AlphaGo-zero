import enum
import random

from dlgo.agent import Agent

__all__ = [
    'MinimaxAgent',
]


# tag::gameresult-enum[]
class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3
# end::gameresult-enum[]


def reverse_game_result(game_result):
    if game_result == GameResult.loss:
        return game_result.win
    if game_result == GameResult.win:
        return game_result.loss
    return GameResult.draw
# tag::minimax-signature[]

def best_result(game_state):
# end::minimax-signature[]
# tag::minimax-base-case[]
    if game_state.is_over:
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss
# end::minimax-base-case[]

# tag::minimax-recursive-case[]
    best_result_so_far = GameResult.loss
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(next_state)
        our_result = reverse_game_result(opponent_best_result)
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result
    return best_result_so_far
# end::minimax-recursive-case[]


# tag::minimax-agent[]
class MinimaxAgent(Agent):
    def select_move(self,game_state):
        winning_moves = []
        draw_moves = []
        losing_moves = []
        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = best_result(next_state)
            our_best_outcome = reverse_game_result(opponent_best_outcome)
            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome ==GameResult.draw:
                draw_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)
        if winning_moves:
            return random.choice(winning_moves)
        if draw_moves:
            return random.choice(draw_moves)
        return random.choice(losing_moves)
# end::minimax-agent[]