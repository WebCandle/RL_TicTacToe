from environment import environment
from agent import agent
import numpy as np

agent_o = agent('agent_o','O')
agent_o.load_policy()
print(len(agent_o.Q))