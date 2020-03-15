from environment import environment
from agent import agent
import numpy as np

agent_o = agent('agent_o','O')
agent_x = agent('agent_x','X')
env = environment(agent_o,agent_x)
env.render(['X','O','X','O','X','O','X','O','X'])