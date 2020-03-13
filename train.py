from environment import environment
from agent import agent
import numpy as np

agent_o = agent('agent_o','O',exp_rate=0.3)
agent_x = agent('agent_x','X',exp_rate=0.3)
agent_o.load_policy()
agent_x.load_policy()
env = environment(agent_o,agent_x)

rounds = 9*8*7*6*5*4*3*2*1 * 1

env.train(rounds)
agent_o.save_policy()
agent_x.save_policy()
env.close()
