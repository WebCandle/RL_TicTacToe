import numpy as np
import pickle
import Config


class agent:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.states = []  # record all states in current round
        self.Q = {}  # dict of all learning state -> value

    # at the end of game, backpropagate and update states value Q[state] = reward
    def set_reward(self, reward):
        for state in reversed(self.states):
            if self.Q.get(state) is None:
                self.Q[state] = 0
            gamma_discount_factor =  0.9
            alpha_learning_rate = 0.2
            self.Q[state] = self.Q[state] + alpha_learning_rate * ( reward * gamma_discount_factor - self.Q[state])

    def reset(self):
        self.states = []

    def savePolicy(self,rounds):
        fw = open('policies/policy_' + str(self.name)+'_'+str(rounds), 'wb')
        pickle.dump(self.Q, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.Q = pickle.load(fr)
        fr.close()
