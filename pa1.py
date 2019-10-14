import sys
import Queue

#4x4 board size
BOARD_WIDTH = 4

#possible goal states
goal1 = "123456789ABCDEF "
goal2 = "123456789ABCDFE "

def boardPrint(gameboard):
	a = " _ _ _ _\n"
	for i in range(BOARD_WIDTH):
		for j in range(BOARD_WIDTH):
			a += str("|")
			a += str(gameboard[i * BOARD_WIDTH + j])
			if j == 3:
				a += str("|\n")

		a += str(" - - - - \n")

	print a
	return


def up(gameboard):
	space = gameboard.index(' ')
	row = space / BOARD_WIDTH
	column = space % BOARD_WIDTH

	if row != 0:
		# print "up"

		row -= 1
		temp = gameboard[row * BOARD_WIDTH + column]
		gameboard = gameboard.replace(" ", temp)
		gameboard = gameboard.replace(temp, " ", 1)
		#gameboard[space] = temp
		#gameboard[row * BOARD_WIDTH + column] = " "
	
	
		# boardPrint(gameboard)
		return gameboard
		
	else:
		# print "wall"
		return -1

def left(gameboard):
	space = gameboard.index(' ')
	row = space / BOARD_WIDTH
	column = space % BOARD_WIDTH

	if column != 0:
		# print "left"

		column -= 1
		temp = gameboard[row * BOARD_WIDTH + column]
		gameboard = gameboard.replace(" ", temp)
		gameboard = gameboard.replace(temp, " ", 1)
		#gameboard[space] = temp
		#gameboard[row * BOARD_WIDTH + column] = " "
	
	
		# boardPrint(gameboard)

		return gameboard

	else:
		# print "wall"
		return -1

def down(gameboard):
	space = gameboard.index(' ')
	row = space / BOARD_WIDTH
	column = space % BOARD_WIDTH

	if row != 3:
		# print "down"

		row += 1
		temp = gameboard[row * BOARD_WIDTH + column]
		gameboard = gameboard.replace(temp, " ")
		gameboard = gameboard.replace(" ", temp, 1)
		#gameboard[space] = temp
		#gameboard[row * BOARD_WIDTH + column] = " "
	
	
		# boardPrint(gameboard)

		return gameboard
	else :
		# print "wall"
		return -1

def right(gameboard):
	space = gameboard.index(' ')
	row = space / BOARD_WIDTH
	column = space % BOARD_WIDTH

	if column != 3:
		# print "right"

		column += 1
		temp = gameboard[row * BOARD_WIDTH + column]
		gameboard = gameboard.replace(temp, " ")
		gameboard = gameboard.replace(" ", temp, 1)
		#gameboard[space] = temp
		#gameboard[row * BOARD_WIDTH + column] = " "
	
	
		# boardPrint(gameboard)

		return gameboard
		
	else:
		# print "wall"
		return -1

#checks if the puzzle is solved
def checkGoal(gameboard):
	return goal1 == gameboard or goal2 == gameboard

#function for expanding a node
def expand(node, h, weight = 0):
	current = node.board
	d = node.depth + 1
	count = 0
	ye = right(current)
	if ye != -1:
		node.right = Node(ye, d, h(ye) + weight, 1)
		count += 1

	ye = down(current)
	if ye != -1:
		node.down = Node(ye, d, h(ye) + weight, 1)
		count += 1

	ye = left(current)
	if ye != -1:
		node.left = Node(ye, d, h(ye) + weight, 1)
		count += 1

	ye = up(current)
	if ye != -1:
		node.up = Node(ye, d, h(ye) + weight, 1)
		count += 1

	return count

def BFS(gameboard):
#queue use
	# depth = 0
	numCreated = 1
	numExpanded = 0
	maxFringe = 1

# 	queue q
	q = Queue.Queue()
#	q.enqueue(start)
	current = Node(gameboard)
	q.put(current)
#	visited = {}
	visited = set()
	fringe = set()
	fringe.add(current.board)
# 	while q not empty
	while q.empty() == False:
#		current = q.dequeue
		current = q.get()
		numExpanded += 1
		visited.add(current.board)
		fringe.remove(current.board)
# 		q.enqueue current.right, down, left, up if not visited
		numCreated += expand(current, h0)
		ye = current.right
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.down
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.left
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.up
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		fringeSize = len(fringe)
		if fringeSize > maxFringe:
			maxFringe = fringeSize

		if checkGoal(current.board) == True:
			# depth = current.depth
			print ("%d, %d, %d, %d" %(current.depth, numCreated, numExpanded, maxFringe))
			return

	print ("-1, %d, %d, %d" %(numCreated, numExpanded, maxFringe))


def DFS(gameboard):
#stack use
	numCreated = 1
	numExpanded = 0
	maxFringe = 1
#	stack s
	s = Queue.LifoQueue()
# 	s.push(start)
	current = Node(gameboard)
	s.put(current)
# 	visited = {}
	visited = set()
	fringe = set()
	fringe.add(current.board)
# 	while s not empty
	while s.empty() == False:
# 		current = s.pop
		current = s.get()
		numExpanded += 1
		visited.add(current.board)
		fringe.remove(current.board)

		numCreated += expand(current, h0)

		ye = current.up
		if ye != None and ye.board not in visited and ye.board not in fringe:
			s.put(ye)
			fringe.add(ye.board)

		ye = current.left
		if ye != None and ye.board not in visited and ye.board not in fringe:
			s.put(ye)
			fringe.add(ye.board)

		ye = current.down
		if ye != None and ye.board not in visited and ye.board not in fringe:
			s.put(ye)
			fringe.add(ye.board)

		ye = current.right
		if ye != None and ye.board not in visited and ye.board not in fringe:
			s.put(ye)
			fringe.add(ye.board)

		fringeSize = len(fringe)
		if fringeSize > maxFringe:
			maxFringe = fringeSize

		if checkGoal(current.board) == True:
			# depth = current.depth
			print ("%d, %d, %d, %d" %(current.depth, numCreated, numExpanded, maxFringe))
			return

	print ("-1, %d, %d, %d" %(numCreated, numExpanded, maxFringe))



def GBFS(gameboard, h):
	numCreated = 1
	numExpanded = 0
	maxFringe = 1

# 	queue q
	q = Queue.PriorityQueue()
#	q.enqueue(start)
	current = Node(gameboard, 0, h(gameboard))
	q.put(current)
#	visited = {}
	visited = set()
	fringe = set()
	fringe.add(current.board)

# 	while q not empty
	while q.empty() == False:
#		current = q.dequeue
		current = q.get()
		numExpanded += 1

		visited.add(current.board)
		fringe.discard(current.board)
# 		q.enqueue current.right, down, left, up if not visited
		numCreated += expand(current, h)
		ye = current.right
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.down
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.left
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.up
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		fringeSize = len(fringe)
		if fringeSize > maxFringe:
			maxFringe = fringeSize

		if checkGoal(current.board) == True:
			print ("%d, %d, %d, %d" %(current.depth, numCreated, numExpanded, maxFringe))
			return

	print ("-1, %d, %d, %d" %(numCreated, numExpanded, maxFringe))

def AStar(gameboard, h):
	numCreated = 1
	numExpanded = 0
	maxFringe = 1

# 	queue q
	q = Queue.PriorityQueue()
#	q.enqueue(start)
	current = Node(gameboard, 0, h(gameboard))
	q.put(current)
#	visited = {}
	visited = set()
	fringe = set()
	fringe.add(current.board)

# 	while q not empty
	while q.empty() == False:
#		current = q.dequeue
		current = q.get()
		numExpanded += 1

		visited.add(current.board)
		fringe.discard(current.board)
# 		q.enqueue current.right, down, left, up if not visited
		numCreated += expand(current, h, current.weight + 1)
		ye = current.right
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.down
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.left
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		ye = current.up
		if ye != None and ye.board not in visited and ye.board not in fringe:
			q.put(ye)
			fringe.add(ye.board)

		fringeSize = len(fringe)
		if fringeSize > maxFringe:
			maxFringe = fringeSize

		if checkGoal(current.board) == True:
			print ("%d, %d, %d, %d" %(current.depth, numCreated, numExpanded, maxFringe))
			return

	print ("-1, %d, %d, %d" %(numCreated, numExpanded, maxFringe))

def DLS(gameboard, d):
	#stack use
	numCreated = 1
	numExpanded = 0
	maxFringe = 1
#	stack s
	s = Queue.LifoQueue()
# 	s.push(start)
	current = Node(gameboard)
	s.put(current)
# 	visited = {}
	visited = set()
	fringe = set()
	fringe.add(current.board)
# 	while s not empty
	while s.empty() == False:
# 		current = s.pop
		current = s.get()
		numExpanded += 1
		visited.add(current.board)

		if current.depth != d:
			fringe.remove(current.board)

			numCreated += expand(current, h0)

			ye = current.up
			if ye != None and ye.board not in visited and ye.board not in fringe:
				s.put(ye)
				fringe.add(ye.board)

			ye = current.left
			if ye != None and ye.board not in visited and ye.board not in fringe:
				s.put(ye)
				fringe.add(ye.board)

			ye = current.down
			if ye != None and ye.board not in visited and ye.board not in fringe:
				s.put(ye)
				fringe.add(ye.board)

			ye = current.right
			if ye != None and ye.board not in visited and ye.board not in fringe:
				s.put(ye)
				fringe.add(ye.board)

			fringeSize = len(fringe)
			if fringeSize > maxFringe:
				maxFringe = fringeSize

		if checkGoal(current.board) == True:
			print ("%d, %d, %d, %d" %(current.depth, numCreated, numExpanded, maxFringe))
			return

	print ("-1, %d, %d, %d" %(numCreated, numExpanded, maxFringe))

#no heuristic
def h0(gameboard):
	return 0

#number of incorrect tiles
def h1(gameboard):
	length = len(gameboard)
	count = 0
	for i in range(length):
		if gameboard[i] != goal1[i] and gameboard[i] != goal2[i]:
			count += 1
	return count

#manhattan distance of all tiles
def h2(gameboard):
	length = len(gameboard)
	count = 0
	for i in range(length):
		if gameboard[i] != goal1[i] and gameboard[i] != goal2[i]:
			count += manhattanDist(gameboard, i)
	return count

#manhattan distance of one tile from its goal state
def manhattanDist(gameboard, i):
	g1 = goal1.index(gameboard[i])
	g2 = goal2.index(gameboard[i])
	rowi = i / BOARD_WIDTH
	columni = i % BOARD_WIDTH

	rowg1 = g1 / BOARD_WIDTH
	columng1 = g1 % BOARD_WIDTH

	rowg2 = g2 / BOARD_WIDTH
	columng2 = g2 % BOARD_WIDTH
	dist = min(abs(rowi - rowg1) + abs(columni - columng1), abs(rowi - rowg2) + abs(columni - columng2))
	return dist




class Node:


	def __init__(self, gameboard, depth = 0, weight = 0, priority = 0):
		self.board = gameboard
		self.right = None
		self.down = None
		self.left = None
		self.up = None
		self.depth = depth
		self.weight = weight
		self.priority = priority #in order: root, right, down, left, up

	#used for putting nodes into a priority queue
	def __lt__(self, other):
		return (self.weight, self.depth, self.priority) < (other.weight, other.depth, other.priority)


# get user input
if len(sys.argv) > 2:
	board = sys.argv[1].upper()
	search = sys.argv[2].lower()
	options = ""
	if len(sys.argv) > 3:
		options = sys.argv[3].lower()
else :
	raise RuntimeError("missing args\nexpected: \"[initialstate]\" [searchmethod] [options]\n"
		+ "[initialstate] 16 characters: 1-9, A-F, and a space\n" 
		+ "[searchmethod]: BFS, DFS, GBFS, AStar, DLS\n"
		+ "[options]: (AStar) and (GBFS): h1, h2 (DLS): int for depth limit")

# print board
# boardPrint(board)

if sorted(list(board)) != sorted(list(goal1)) or len(board) != 16:
	raise RuntimeError("[initial state] needs to be 16 characters: 1-9, A-F, and a space")

if search == "bfs":
	BFS(board)

elif search == "dfs":
	DFS(board)

elif search == "gbfs":
	if options == "h1":
		GBFS(board, h1)

	elif options == "h2":
		GBFS(board, h2)

	else:
		raise RuntimeError("[options]: h1, h2")

elif search == "astar":
	if options == "h1":
		AStar(board, h1)

	elif options == "h2":
		AStar(board, h2)

	else:
		raise RuntimeError("[options]: h1, h2")

elif search == "dls":
	if options.isdigit():
		DLS(board, int(options))

	else:
		raise RuntimeError("[options]: int for depth limit")
else:
	raise RuntimeError("[searchmethod]: BFS, DFS, GBFS, AStar, DLS")


#below used to get results from all search methods
# BFS(board)
# DFS(board)
# GBFS(board, h1)
# GBFS(board, h2)
# AStar(board, h1)
# AStar(board, h2)
# DLS(board, 5)
