import enum

class GameStatus(enum.Enum):
	DRAW = 0;
	OWINS = 1;
	XWINS = 2;

class Board:
	def __init__(self):
		self.board = [['.' for j in range(7)] for i in range(4)]
		self.columnStatus = [3 for j in range(7)] 
		self.turn = 0
		self.status = GameStatus.DRAW

	def printBoard(self):
		for i in range(4):
			print(self.board[i])

	def allPositionsOccupied(self):
		return all(pos < 0 for pos in self.columnStatus)

	def checkDiagonals(self):
		# Check lower-right diagonals
		for j in range(4):
			if self.board[0][j] == self.board[1][j+1] == self.board[2][j+2] == self.board[3][j+3]:
				if self.board[0][j] == 'O':
					self.status = GameStatus.OWINS
					return True
				elif self.board[0][j] == 'X':
					self.status = GameStatus.XWINS
					return True


		# Check lower-left diagonals
		for j in range(3, 7):
			if self.board[0][j] == self.board[1][j-1] == self.board[2][j-2] == self.board[3][j-3]:
				if self.board[0][j] == 'O':
					self.status = GameStatus.OWINS
					return True
				elif self.board[0][j] == 'X':
					self.status = GameStatus.XWINS
					return True
		return False

	def checkVerticals(self):
		for j in range(7):
			if self.board[0][j] == self.board[1][j] == self.board[2][j] == self.board[3][j]:
				if self.board[0][j] == 'O':
					self.status = GameStatus.OWINS
					return True
				elif self.board[0][j] == 'X':
					self.status = GameStatus.XWINS
					return True
		return False

	def checkHorizontals(self):
		for i in range(4):
			for j in range(4):
				if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
					if self.board[i][j] == 'O':
						self.status = GameStatus.OWINS
						return True
					elif self.board[i][j] == 'X':
						self.status = GameStatus.XWINS
						return True
		return False

	def isGameOver(self):
		return self.checkDiagonals() or self.checkVerticals() or self.checkHorizontals() or self.allPositionsOccupied()

	def placeToken(self, column):
		if column < 0 or column >= 7:
			return False
		elif self.columnStatus[column] < 0:
			return False
		else:
			pos = self.columnStatus[column]
			if self.turn == 0:
				self.board[pos][column] = 'O'
			else:
				self.board[pos][column] = 'X'
			self.columnStatus[column] -= 1
			return True

	def play(self):
		print("Welcome to the game of Connect4! The first player to connect four of his or her own tokens in a horizontal, vertical, or diagonal line wins!")
		while self.isGameOver() == False:
			self.printBoard()
			if self.turn == 0:
				print("Player 1, it's your turn.")
			else:
				print("Player 2, it's your turn.")
			column = int(input("Please select a column to drop your token into: "))
			if self.placeToken(column) == True:
				self.turn += 1
				self.turn %= 2
			else:
				print("Invalid choice! Please try again.")
		
		self.printBoard()
		if self.status == GameStatus.DRAW:
			print("Draw")
		elif self.status == GameStatus.OWINS:
			print("Player 1 wins")
		else:
			print("Player 2 wins")



def main():
	gameBoard = Board()
	gameBoard.play()

	return 0

if __name__ == '__main__': main()