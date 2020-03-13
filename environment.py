import numpy as np

class environment:
    def __init__(self, agent_O, agent_X):
        # 'O', 'X' or '-' for empty place
        #  board = ['X','-','-',
        #           'O','-','O',
        #           'X','-','-']
        self.board = ['-','-','-','-','-','-','-','-','-']
        #  action_space = [1,2,3,
        #                 4,5,6,
        #                 7,8,9]
        self.action_space = [1,2,3,4,5,6,7,8,9]
        self.agent_O = agent_O
        self.agent_X = agent_X
        self.done = False
        # state is the hash of board
        # we get the state using the function get_state()
        self.state = '---------'

        # for more developement
        # self.observation_space = [1,2,3,4,5,6,7,8,9] how manay action can the agen make by a state


    def render(self):
        # agent_O: O  agent_X: X
        for i in [0, 3, 6]:
            print('-------------')
            out = '| '
            for j in range(0, 3):
                letter = self.board[j+i] if self.board[j+i] != '-' else ' '
                out += letter + ' | '
                print(out)
        print('-------------')

    def close(self):
        pass

    def step(self, action, agent):
        self.board[action-1] = agent.symbol
        self.action_space.remove(action)
        self.state = self.get_state()
        agent.steps.append(self.state)
        info = {}
        info['winner'] = self.get_winner()
        if info['winner'] == agent.symbol:
            reward = 1
            agent.set_reward(reward)
            self.done = True
        elif info['winner'] == 0:
            reward = 0.1
            agent.set_reward(reward)
            self.done = True
        else:
            reward = None
            self.done = False
        return self.state, reward, self.done, info
    

    # environment reset
    def reset(self):
        current_state = self.get_state()
        self.board = ['-','-','-','-','-','-','-','-','-']
        self.action_space = [1,2,3,4,5,6,7,8,9]
        self.done = False
        self.state = '---------'
        self.agent_O.reset()
        self.agent_X.reset()
        return current_state

    # get unique hash of the board state
    def get_state(self,board=None):
        state = ''
        for s in self.board if board == None else board:
            state += s
        return state

    def train(self, rounds=100):
        for i in range(rounds):
            if i % 1000 == 0:
                print("Rounds {}".format(i))
            while not self.done:
                # agent_O
                action = self.agent_O.choose_action(self.action_space, self.board)
                state, reward, done, info = self.step(action,self.agent_O)
                # ended with agent_O either winner or draw
                if info['winner'] == self.agent_O.symbol:
                    # agent_O has won!
                    self.reset()
                    #print(state,reward,done,info)
                    break
                elif info['winner'] == 0:
                    # tie
                    self.reset()
                else:
                    # agent_X
                    action = self.agent_X.choose_action(self.action_space, self.board)
                    state, reward, done, info = self.step(action,self.agent_X)
                    if info['winner'] == self.agent_X.symbol:
                        self.reset()
                        #print(state,reward,done,info)
                        break
                    elif info['winner'] == 0: #tie
                        self.reset()

    def get_winner(self):
        # row
        line = self.board[1-1] + self.board[2-1]+ self.board[3-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        line = self.board[4-1] + self.board[5-1]+ self.board[6-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        line = self.board[7-1] + self.board[8-1]+ self.board[9-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'

        # col
        line = self.board[1-1] + self.board[4-1]+ self.board[7-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        line = self.board[2-1] + self.board[5-1]+ self.board[8-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        line = self.board[3-1] + self.board[6-1]+ self.board[9-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        
        # diagonal
        line = self.board[1-1] + self.board[5-1]+ self.board[9-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        line = self.board[3-1] + self.board[5-1]+ self.board[7-1]
        if line == 'OOO':
            return 'O'
        elif line == 'XXX':
            return 'X'
        
        # tie
        # no available action_space
        if len(self.action_space) == 0:
            self.done = True
            return 0
        # not end
        self.done = False
        return None

    # # play agent_O Computer with agent_X human, Computer fängt an
    # def play2(self):
    #     while not self.done:
    #         # Player 1
    #         agent_O_action = self.agent_O.choose_action(self.action_space, self.board, 'O')
    #         self.step(agent_O_action,'O')
    #         self.render()
    #         # check board status if it is end
    #         winner = self.get_winner()
    #         if winner is not None:
    #             if winner == 1:
    #                 print(self.agent_O.name, "wins!")
    #             else:
    #                 print("tie!")
    #             self.reset()
    #             break

    #         else:
    #             # Player 2
    #             agent_X_action = self.agent_X.choose_action(self.action_space)

    #             self.step(agent_X_action,'X')
    #             self.render()
    #             winner = self.get_winner()
    #             if winner is not None:
    #                 if winner == -1:
    #                     print(self.agent_X.name, "wins!")
    #                 else:
    #                     print("tie!")
    #                 self.reset()
    #                 break
    # Computer plays as agent_O with human player as agent_X, human plays first
    def play(self):
        self.render()
        while not self.done:
            # Player 2
            agent_X_action = self.agent_X.choose_action(self.action_space)
            self.step(agent_X_action,'X')
            self.render()
            # check board status if it is end
            winner = self.get_winner()
            if winner is not None:
                if winner == 1:
                    print(self.agent_X.name, "wins!")
                else:
                    print("tie!")
                self.reset()
                break

            else:
                # Player 1
                agent_O_action = self.agent_O.choose_action(self.action_space, self.board, 'O')

                self.step(agent_O_action,'O')
                self.render()
                winner = self.get_winner()
                if winner is not None:
                    if winner == -1:
                        print(self.agent_O.name, "wins!")
                    else:
                        print("tie!",winner,self.agent_O.name)
                    self.reset()
                    break


