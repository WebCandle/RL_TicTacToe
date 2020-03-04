from State import *
from Player import *
from HumanPlayer import *



# play with human
p1 = Player("computer", exp_rate=0)
p1.loadPolicy("policy_p1_50000")

p2 = HumanPlayer("human")

st = State(p1, p2)
st.play2()