from environment import environment
from agent import agent

agent_o = agent('agent_o','O',exp_rate=0.3)
agent_x = agent('agent_x','X',exp_rate=0.3)

env = environment(agent_o,agent_x)

#rounds = 9*8*7*6*5*4*3*2*1 * 10
rounds = 9
print(len(agent_o.Q))
env.train(agent_x,rounds)
print(len(agent_o.Q))
env.close()
