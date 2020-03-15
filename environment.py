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
        # loads policy
        self.agent_O.load_policy()
        self.agent_X.load_policy()
        self.done = False
        # state is the hash of board
        # we get the state using the function get_state()
        self.state = '---------'

        # for more developement
        # self.observation_space = [1,2,3,4,5,6,7,8,9] how manay action can the agen make by a state


    def render(self, board = None):
        if board == None:
            board = self.board
        out = '-------------\n'
        out += '| ' + ( board[0] if board[0] != '-' else ' ') + ' | ' + ( board[1] if board[1] != '-' else ' ') + ' | ' + ( board[2] if board[2] != '-' else ' ') + ' |\n'
        out += '| ' + ( board[3] if board[3] != '-' else ' ') + ' | ' + ( board[4] if board[4] != '-' else ' ') + ' | ' + ( board[5] if board[5] != '-' else ' ') + ' |\n'
        out += '| ' + ( board[6] if board[6] != '-' else ' ') + ' | ' + ( board[7] if board[7] != '-' else ' ') + ' | ' + ( board[8] if board[8] != '-' else ' ') + ' |\n'
        out +='-------------'
        print(out)

    def close(self):
        self.agent_O.save_policy()
        self.agent_X.save_policy()

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

    def train(self, first_player = None, rounds=100):
        for i in range(rounds):
            if i % 1000 == 0:
                print("Rounds {}".format(i))
            self.play(first_player, False)

    def play(self, first_player = None, render = True):
        if first_player == None or first_player.symbol == 'O':
            player1 = self.agent_O
            player2 = self.agent_X
        else:
            player1 = self.agent_X
            player2 = self.agent_O
        while not self.done:
            # player1
            action = player1.choose_action(self.action_space, self.board)
            state, reward, done, info = self.step(action,player1)
            if render == True:
                self.render()
            if info['winner'] == player1.symbol and render == True:
                # player1 has won!
                print(player1.name+' won!')
            elif info['winner'] == 0 and render == True:
                # tie
                print('Draw!')
            else:
                # player2
                action = player2.choose_action(self.action_space, self.board)
                state, reward, done, info = self.step(action,player2)
                if render == True:
                    self.render()
                if info['winner'] == player2.symbol and render == True:
                    print(player2.name+' won!')
                elif info['winner'] == 0 and render == True:
                    #tie
                    print('Draw!')
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