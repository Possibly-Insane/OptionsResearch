import numpy as np

beige_sure = [[-1, 0, 1, 1, 0,-1,-1, 1,-1,-1], [ 1, 0, 1, 1,-1, 1, 0, 1, 1, 1], [ 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [-1, 0,-1,-1, 0, 1, 1, 1,-1,-1], [ 0, 1, 1, 0,-1, 1,-1, 1, 1, 1], [ 1, 0,-1,-1, 0,-1,-1,-1,-1,-1], [-1, 0, 1, 1,-1,-1,-1, 1, 1,-1], [ 0,-1,-1, 0, 0, 1, 1, 0,-1, 1], [-1,-1,-1, 1,-1, 1, 1,-1, 1, 0], [-1,-1, 1, 1,-1, 1, 1, 1, 1, 0], [ 0,-1, 1,-1,-1,-1,-1, 0,-1, 1], [ 1,-1,-1,-1, 1,-1, 1,-1, 1,-1], [-1, 1,-1,-1, 1,-1,-1, 0,-1,-1], [-1, 1,-1, 0, 1,-1,-1, 1,-1, 0], [ 1,-1,-1, 1, 1, 1, 1,-1, 1, 1]]
beige_guess = [[-1, -0.0196, 1, 1, -0.952576, -1, -1, 1, -1, -1], [ 1, 0.4624, 1, 1, -1, 1, -0.0016, 1, 1, 1], [ 1, -0.4356, 0.8464, 0.6724, 0.0196, 1, 1, 1, 1, 1], [-1, -0.0784, -1, -1, -0.5184, 1, 1, 1, -1, -1], [ 0.0484, 1, 1, 0.3844, -1, 1, -1, 1, 1, 1], [ 0.9216, 1, -0.4356, -1, 1, 0.16, 0.7396, -1, -1, -1], [ 1, -0.0016, -1, -1, 0.7744, -1, -1, -1, -1, -1], [-1, -0.09, 1, 1, -1, -1, -1, 1, 1, -1], [ 0.0144, -1, -1, -0.0196, -0.0016, 1, 1, -0.1444, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 0.6724], [-1, -1, 1, 1, -1, 1, 1, 1, 1, -0.7056], [ 0.0484, -1, 1, -1, -1, -1, -1, 0.6084, -1, 1], [ 1, -1, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, 0.0016, -1, -1], [-1, 1, -1, -0.81, 1, -1, -1, 1, -1, 0.1296], [ 1, -1, -1, 1, 1, 1, 1, -1, 1, 1]]
beige_threshold = np.array([12, 10, 14, 12, 11, 15, 14, 13, 16, 13], dtype = int)
white_sure = [[-1, 0, 1, 1, 0,-1,-1, 1,-1,-1], [ 1, 0, 1, 1,-1, 1, 0, 1, 1, 1], [ 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [-1, 0,-1,-1, 0, 1, 1, 1,-1,-1], [ 0, 1, 1, 0,-1, 1,-1, 0, 1, 1], [ 0, 1, 0,-1, 1, 0, 0, 0,-1,-1], [ 1, 0,-1,-1, 0,-1,-1,-1,-1,-1], [-1,-1, 1, 1,-1,-1,-1, 1, 1,-1], [ 0,-1,-1, 0, 0, 1, 1,-1,-1, 1], [-1,-1,-1, 1,-1, 1, 1,-1, 1, 0], [-1,-1, 1, 1,-1, 1, 1, 1, 1, 0], [ 0,-1, 1,-1,-1,-1,-1, 0,-1, 1], [ 1, 0,-1,-1, 1,-1, 1,-1, 1,-1], [-1, 1,-1,-1, 1,-1,-1, 0,-1,-1], [-1, 1,-1, 0, 1,-1,-1, 1,-1, 0], [ 1,-1,-1, 1, 1, 1, 1,-1, 1, 1]]
white_guess = [[-1, -0.0576, 1, 1, -0.7056, -1, -1, 1, -1, -1], [ 1, 0.4096, 1, 1, -1, 1, -0.0144, 1, 1, 1], [ 1, -0.4096, 0.6084, 0.49, 0.0784, 1, 1, 1, 1, 1], [-1, -0.4096, -1, -1, -0.5184, 1, 1, 1, -1, -1], [ 0.3136, 1, 1, 0.3844, -1, 1, -1, 0.2304, 1, 1], [ 0.6724, 1, -0.5776, -1, 1, 0.0484, 0.81, -0.7056, -1, -1], [ 1, -0.01, -1, -1, 0.7056, -1, -1, -1, -1, -1], [-1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [-0.0036, -1, -1, -0.0256, 0.0196, 1, 1, -1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 0.81], [-1, -1, 1, 1, -1, 1, 1, 1, 1, -0.7396], [ 0.1156, -1, 1, -1, -1, -1, -1, 0.3844, -1, 1], [ 1, 0.1156, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, 0.0016, -1, -1], [-1, 1, -1, -0.7056, 1, -1, -1, 1, -1, 0.0784], [ 1, -1, -1, 1, 1, 1, 1, -1, 1, 1]]
white_threshold = np.array([12, 10, 14, 12, 11, 15, 14, 12, 16, 13], dtype = int)
grey_sure = [[-1, -1, 1, 1, 1, -1, -1, 1, -1, -1], [ 1, 0, 1, 1, -1, 1, -1, 1, 1, 1], [ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0, 1, 1, 1, -1, -1], [-1, 1, 1, 1, -1, 1, -1, 0, 1, 1], [ 1, 1, 0, -1, -1, 1, 0, 0, -1, -1], [ 1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [ 1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [ 1, -1, -1, -1, 0, 1, 1, 1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 1], [-1, -1, 1, 1, -1, 1, 1, 0, 1, 0], [-1, -1, 1, -1, -1, -1, -1, 1, -1, 1], [ 1, 0, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1], [ 1, 0, -1, 1, 1, 1, 1, 0, 1, 1]]
grey_guess = [[-1, -1, 1, 1, 1, -1, -1, 1, -1, -1], [ 1, 0.5776, 1, 1, -1, 1, -1, 1, 1, 1], [ 1, -0.0196, 1, 1, -0.0144, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0.0064, 1, 1, 1, -1, -1], [-1, 1, 1, 1, -1, 1, -1, 0.0196, 1, 1], [ 1, 1, 0.0324, -1, -1, 1, 0.01 , 0.0196, -1, -1], [ 1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [ 1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [ 1, -1, -1, -1, -0.0144, 1, 1, 1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 1], [-1, -1, 1, 1, -1, 1, 1, 0.5776, 1, -0.4096], [-1, -1, 1, -1, -1, -1, -1, 1, -1, 1], [ 1, -0.8464, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1], [ 1, 0.5776, -1, 1, 1, 1, 1, -0.5776, 1, 1]]
grey_threshold = np.array([16, 12, 15, 16, 13, 16, 15, 12, 16, 15], dtype = int)

input = grey_guess
abs_input = np.absolute(input)

threshold = np.zeros(10)

for n1 in range(16):
    threshold += abs_input[n1]

np.set_printoptions(linewidth=256)
print(threshold)
