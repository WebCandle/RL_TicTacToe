from player import player

p = player('human','X')
action_space = [1,2,3,4,5,6,7,8,9]

while True:
    action = p.choose_action(action_space,None)
    print(action)