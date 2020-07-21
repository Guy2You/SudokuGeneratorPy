class SudokuPuzzle:

	def __init__(self):
		self.side_length = 9
		self.sub_side_length = 3
		self.grid = [[0 for i in range(9)] for j in range(9)]
		self.number_set = set(range(1, 10))

	def get_row(self, row):
		return self.grid[row]

	def get_column(self, column):
		return [x[column] for x in self.grid]

	def set_tile(self, row, column, value):
		if value not in self.number_set:
			raise ValueError(f"{value} is not a valid value in this puzzle. Valid values are: {', '.join(str(x) for x in self.number_set)}")
		if row >= self.side_length or column >= self.side_length:
			raise ValueError(f"{row}, {column} is not a valid position in a puzzle with side length {self.side_length}")


def main():
	puzzle = SudokuPuzzle()
	print(puzzle)
	print(puzzle.side_length)
	print(puzzle.sub_side_length)
	print(puzzle.grid)
	print(puzzle.number_set)
	puzzle.set_tile(2, 1, 4)
	puzzle.set_tile(9, 9, 4)
	puzzle.set_tile(2, 8, 12)


if __name__ == "__main__": main()
