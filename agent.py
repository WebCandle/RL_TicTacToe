import numpy as np
import json


class agent:
    def __init__(self, name, symbol, gamma_discount_factor=0.9, alpha_learning_rate=0.2, exp_rate= 0.3):
        self.name = name
        self.symbol = symbol
        self.steps = []  # record all board states in current round
        self.Q = {}  # dict of all learning state -> value
        self.exp_rate = exp_rate # 0.3 means that 30 % of actions will be randomly
        self.gamma_discount_factor =  gamma_discount_factor
        self.alpha_learning_rate = alpha_learning_rate

    def choose_action(self, action_space, board):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            action = self.choose_action_sample(action_space)
        else:
            value_max = -999
            for next_action in action_space:
                next_board = board.copy()
                next_board[next_action-1] = self.symbol
                next_state = self.get_state(next_board)
                value = 0 if self.Q.get(next_state) is None else self.Q.get(next_state)
                if value >= value_max:
                    value_max = value
                    action = next_action
        return action

    # returns random action
    def choose_action_sample(self, action_space):
        idx = np.random.choice(len(action_space))
        action = action_space[idx]
        return action

    # get unique hash of the board state
    def get_state(self,board):
        state = ''
        for s in board:
            state += s
        return state

    # at the end of game, backpropagate and update states value Q[state] = reward
    def set_reward(self, reward):
        for state in reversed(self.steps):
            if self.Q.get(state) is None:
                self.Q[state] = 0
            self.Q[state] = self.Q[state] + self.alpha_learning_rate * ( reward * self.gamma_discount_factor - self.Q[state])

    def reset(self):
        self.steps = []

    def save_policy(self):
        file_write = open('policy/' + str(self.name) + '.json', 'w')
        file_write.write('{\n')
        counter = 1
        length = len(self.Q)
        comma = ','
        for state in self.Q:
            if(counter == length):
                comma = ''
            file_write.write('    "' + state + '": ' + str(self.Q[state]) + comma + '\n')
            counter += 1
        file_write.write('}')
        #json.dump(self.Q, file_write)
        file_write.close()

    def load_policy(self):
        file_read = open('policy/' + str(self.name) + '.json', 'r')
        content = file_read.read()
        self.Q = json.loads(content)
        file_read.close()
