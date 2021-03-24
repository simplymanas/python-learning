# draw a 8 X 8 chess board
# each line contains 80 pixel
# each bo contain 10 X 10 matrix
import numpy as np


def display_chessboard():
	white = '0' * 10
	black = '1' * 10
	final_list = []
	sequence = 'white'

	for i in range(8):
		for j in range(8):
			if sequence.__eq__('white'):
				final_list += white
				sequence = 'black'
			else:
				final_list += black
				sequence = 'white'
		final_list = final_list * 10
		print(final_list)

outputlist = display_chessboard()
print(len(outputlist))


data = np.array( outputlist )
shape = ( 80, 10 )
data.reshape( shape )
print(data)