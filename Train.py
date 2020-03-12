import environment
import agent
import numpy as np

agent_o = agent.agent('agent_o','O')
agent_x = agent.agent('agent_x','X')
agent_o.load_policy()
agent_x.load_policy()
env = environment.environment(agent_o,agent_x)

rounds = 9*8*7*6*5*4*3*2*1

env.train(rounds)
agent_o.save_policy()
agent_x.save_policy()
env.close()
