from random import randint, random, getrandbits
class WordSearch:
	def __init__(self, n, reverse):
		self.reverse = reverse
		self.n = n
		self.board_list = [ [True]*n for i in range(0,n) ]
		self.values = [[0.1202, 0.2112, 0.2924, 0.3692, 0.44229999999999997, 0.5118, 0.5746, 0.6348, 0.6940000000000001, 0.7372000000000001, 0.7770000000000001, 0.8058000000000002, 0.8329000000000002, 0.8590000000000002, 0.8820000000000002, 0.9031000000000002, 0.9240000000000003, 0.9443000000000003, 0.9625000000000002, 0.9774000000000003, 0.9885000000000003, 0.9954000000000003, 0.9971000000000003, 0.9982000000000003, 0.9992000000000003, 0.9999000000000003], ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']]
		self.board = [ [ self.randlet() for i in range(0,n)] for i in range(0,n)]
		self.wordlist = []
		self.used_coord = []
		self.f = open("nounlist.txt").readlines()

	def hide_word(self, word):
		#hides word inside board
		wl = len(word)
		if(wl > self.n):
			return None
		word = word.upper()
		coord = []
		i = 0

		reversed = False

		if(self.reverse and randint(0,2)==0):
			word = word[::-1]
			reversed = True

		margin_x = int( round((self.n - wl)*random()) )
		margin_y = int( round((self.n - wl)*random()) )

		orient = randint(0,3)

		#picks case
		o = {0:self.vert,
			1: self.horiz,
			2: self.downdiag,
			3: self.updiag,
		}

		k = 0
		while i < wl:
			if not (self.board_list[o[orient]("x",margin_x,i)][o[orient]("y",margin_y,i)] or self.board[o[orient]("x",margin_x,i)][o[orient]("y",margin_y,i)] == word[i]):
				margin_x, margin_y, orient = self.new_coord(wl)
				k+=1
				if(k > 100):
					return None
				i = 0
			else:
				i+=1

		for j in range(0,wl):
			self.board[o[orient]("x",margin_x,j)][o[orient]("y",margin_y,j)] = word[j]
			self.board_list[o[orient]("x",margin_x,j)][o[orient]("y",margin_y,j)] = False

		if reversed:
			word = word[::-1]

		self.wordlist.append(word.lower())
		coor = (margin_x, margin_y, orient, word)
		self.used_coord.append(coor)

	def new_coord(self, wl):
		orient = randint(0,3)
		if(orient == 0):
			margin_x = int( round((self.n - wl)*random()) )
			margin_y = int( round((self.n - 1)*random()) )
		elif(orient == 1):
			margin_x = int( round((self.n - 1)*random()) )
			margin_y = int( round((self.n - wl)*random()) )
		else:
			margin_x = int( round((self.n - wl)*random()) )
			margin_y = int( round((self.n - wl)*random()) )
		return margin_x, margin_y, orient

	def fill(self, n):
		for i in range(0,n):
			self.hide_word( self.f.pop(randint(0,2326-n)).rstrip() )

	#Direction word runs in WordSearch

	def vert(self, xory, margin, i):
		if(xory == "x"):
			return margin + i
		elif(xory == "y"):
			return margin

	def horiz(self, xory, margin, i):
		if(xory == "x"):
			return margin
		elif(xory == "y"):
			return margin + i

	def downdiag(self, xory, margin, i):
		if(xory == "x"):
			return margin + i
		elif(xory == "y"):
			return margin + i

	def updiag(self, xory, margin, i):
		if(xory == "x"):
			i = self.n - margin - i -1
			return i
		elif(xory == "y"):
			return margin + i

	#Printing

	def print_wordlist(self):
		for i in self.wordlist:
			print i

	def print_board(self):
		for i in self.board:
			for j in i:
				print j,
			print "\n"

	#Retrevial functions

	def get_Board(self):
		return self.board
	
	def get_wordlist(self):
		return self.wordlist

	def randlet(self):
		choice = random()
		if choice < .1202:
			return self.values[1][0]
		if choice > .9991:
			return self.values[1][25]
		for i in range(0,25):
			if self.values[0][i] < choice and choice < self.values[0][i+1]:
				return self.values[1][i]