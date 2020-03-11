import environment
import agent

agent_o = agent.agent('player1','O')
agent_x = agent.agent('player2','X')

env = environment.environment(agent_o,agent_x)
env.train(3)
print('Q-Table of agent O')
print(agent_o.Q)
print('Q-Table of agent X')
print(agent_x.Q)