import numpy as np
from agent import agent


class player(agent):
    def __init__(self, name, symbol, gamma_discount_factor=0.9, alpha_learning_rate=0.2, exp_rate= 0.3):
        agent.__init__(self,name, symbol, gamma_discount_factor, alpha_learning_rate, exp_rate)

    def choose_action(self, action_space, board=None):
        action = input ("Input your action by pressing on Keypad as TicTacToes arrange: ")
        action_space = list(map(str, action_space))
        while action not in action_space:
            action = input ("Wrong entry or not available: ")
        return int(action)