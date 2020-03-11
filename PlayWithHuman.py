import Environment as env
import Player as ply



# play with human
Agent_O = ply.Player("computer", exp_rate=0)
Agen_O.loadPolicy("policies/policy_p2_50000")

Agent_X = hu.HumanPlayer("human")

st = env.Environment(Agen_O, Agent_X )
st.play3()