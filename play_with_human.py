from environment import environment
from agent import agent
from player import player


# agent plays with human player
agent_o = agent('agent_o','O')
player_x = player('player_maher_x','X')
env = environment(agent_o, player_x)
env.play()
env.close()