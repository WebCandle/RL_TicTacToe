import State as sta
import Player as ply



# training
p1 = ply.Player("p1")
p2 = ply.Player("p2")

st = sta.State(p1, p2)
print("training...")
rounds = 362880
rounds = 50000
st.play(rounds)
p1.savePolicy(rounds)
p2.savePolicy(rounds)


