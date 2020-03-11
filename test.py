import pickle
#test

fr = open('policies/policy_p1_50000', 'rb')
states_value = pickle.load(fr)
fr.close()

for k in states_value:
    print('{0} => {1}'.format(k,states_value[k]))


# import numpy as np
# board = np.zeros((3, 3),dtype=int)
# print(type(board))

#print(str(board.reshape(3 * 3)))
# print(board)
# print(board.reshape(9))
# print(board.reshape((1,9)))
# print(board)

