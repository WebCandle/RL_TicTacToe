import numpy as np
import pickle
import Config

class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            inp = input ("Input your action: ")[0]
            if inp == "1":
                row = 2
                col = 0
            elif inp == "2":
                row = 2
                col = 1
            elif inp == "3":
                row = 2
                col = 2
            elif inp == "4":
                row = 1
                col = 0
            elif inp == "5":
                row = 1
                col = 1
            elif inp == "6":
                row = 1
                col = 2
            elif inp == "7":
                row = 0
                col = 0
            elif inp == "8":
                row = 0
                col = 1
            elif inp == "9":
                row = 0
                col = 2
            else:
                row = -1
                col = -1
            #row = int(input("Input your action row:"))
            #col = int(input("Input your action col:"))
            action = (row, col)
            if action in positions:
                return action

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def setReward(self, reward):
        pass

    def reset(self):
        pass
