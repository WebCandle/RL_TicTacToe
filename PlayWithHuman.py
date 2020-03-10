import State as sta
import Player as ply
import HumanPlayer as hu



# play with human
p1 = ply.Player("computer", exp_rate=0)
p1.loadPolicy("policies/policy_p2_50000")

p2 = hu.HumanPlayer("human")

st = sta.State(p1, p2)
st.play3()