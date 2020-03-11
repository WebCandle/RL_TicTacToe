import numpy as np
import pickle

class Environment:
    def __init__(self, Agent_O, Agent_X):
        self.board = np.zeros((3, 3),dtype=int)
        self.Agent_O = Agent_O
        self.Agent_X = Agent_X
        self.isEnd = False
        self.boardHash = None
        # init Agent_O plays first
        self.playerSymbol = 1

    # get unique hash of current board state
    def getBoardHash(self):
        self.boardHash = str(self.board.reshape(3 * 3))
        return self.boardHash

    def getWinner(self):
        # row
        for i in range(3):
            if sum(self.board[i, :]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.isEnd = True
                return -1
        # col
        for i in range(3):
            if sum(self.board[:, i]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.isEnd = True
                return -1
        # diagonal
        diag_sum1 = sum([self.board[i, i] for i in range(3)])
        diag_sum2 = sum([self.board[i, 3 - i - 1] for i in range(3)])
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            self.isEnd = True
            if diag_sum1 == 3 or diag_sum2 == 3:
                return 1
            else:
                return -1

        # tie
        # no available actions
        if len(self.availableActions()) == 0:
            self.isEnd = True
            return 0
        # not end
        self.isEnd = False
        return None

    def availableActions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    actions.append((i, j))  # need to be tuple
        return actions

    def updateState(self, action):
        self.board[action] = self.playerSymbol
        # switch to another player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1

    # only when game ends
    def setReward(self):
        result = self.getWinner()
        # backpropagate reward
        if result == 1:
            self.Agent_O.setReward(1)
            self.Agent_X.setReward(0)
        elif result == -1:
            self.Agent_O.setReward(0)
            self.Agent_X.setReward(1)
        else:
            self.Agent_O.setReward(0.1)
            self.Agent_X.setReward(0.5)

    # board reset
    def reset(self):
        self.board = np.zeros((3, 3),dtype=int)
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    def play(self, rounds=100):
        for i in range(rounds):
            if i % 1000 == 0:
                print("Rounds {}".format(i))
            while not self.isEnd:
                # Player 1
                actions = self.availableActions()
                Agent_O_action = self.Agent_O.chooseAction(actions, self.board, self.playerSymbol)
                # take action and upate board state
                self.updateState(Agent_O_action)
                board_hash = self.getBoardHash()
                self.Agent_O.addState(board_hash)
                # check board status if it is end

                winner = self.getWinner()
                if winner is not None:
                    # self.Render()
                    # ended with Agent_O either winner or draw
                    self.setReward()
                    self.Agent_O.reset()
                    self.Agent_X.reset()
                    self.reset()
                    break

                else:
                    # Player 2
                    actions = self.availableActions()
                    Agent_X_action = self.Agent_X.chooseAction(actions, self.board, self.playerSymbol)
                    self.updateState(Agent_X_action)
                    board_hash = self.getBoardHash()
                    self.Agent_X.addState(board_hash)

                    winner = self.getWinner()
                    if winner is not None:
                        # self.Render()
                        # ended with Agent_X either winner or draw
                        self.setReward()
                        self.Agent_O.reset()
                        self.Agent_X.reset()
                        self.reset()
                        break
    # play Agent_O Computer with Agent_X human, Computer fängt an
    def play2(self):
        while not self.isEnd:
            # Player 1
            actions = self.availableActions()
            Agent_O_action = self.Agent_O.chooseAction(actions, self.board, self.playerSymbol)
            # take action and upate board state
            self.updateState(Agent_O_action)
            self.Render()
            # check board status if it is end
            winner = self.getWinner()
            if winner is not None:
                if winner == 1:
                    print(self.Agent_O.name, "wins!")
                else:
                    print("tie!")
                self.reset()
                break

            else:
                # Player 2
                actions = self.availableActions()
                Agent_X_action = self.Agent_X.chooseAction(actions)

                self.updateState(Agent_X_action)
                self.Render()
                winner = self.getWinner()
                if winner is not None:
                    if winner == -1:
                        print(self.Agent_X.name, "wins!")
                    else:
                        print("tie!")
                    self.reset()
                    break
    # play Agent_O Computer with Agent_X human, Human fängt an
    def play3(self):
        self.Render()
        while not self.isEnd:
            # Player 2
            actions = self.availableActions()
            Agent_X_action = self.Agent_X.chooseAction(actions)
            # take action and upate board state
            self.updateState(Agent_X_action)
            self.Render()
            # check board status if it is end
            winner = self.getWinner()
            if winner is not None:
                if winner == 1:
                    print(self.Agent_X.name, "wins!")
                else:
                    print("tie!")
                self.reset()
                break

            else:
                # Player 1
                actions = self.availableActions()
                Agent_O_action = self.Agent_O.chooseAction(actions, self.board, self.playerSymbol)

                self.updateState(Agent_O_action)
                self.Render()
                winner = self.getWinner()
                if winner is not None:
                    if winner == -1:
                        print(self.Agent_O.name, "wins!")
                    else:
                        print("tie!",win,self.Agent_O.name)
                    self.reset()
                    break

    def Render(self):
        # Agent_O: x  Agent_X: o
        for i in range(0, 3):
            print('-------------')
            out = '| '
            for j in range(0, 3):
                if self.board[i, j] == 1:
                    token = 'x'
                if self.board[i, j] == -1:
                    token = 'o'
                if self.board[i, j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('-------------')
