from State import *
from Player import *



# training
p1 = Player("p1")
p2 = Player("p2")

st = State(p1, p2)
print("training...")
st.play(50000)
#st.play(500)
p1.savePolicy()
p2.savePolicy()


