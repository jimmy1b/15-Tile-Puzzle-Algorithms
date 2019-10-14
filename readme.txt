h1: misplaced tiles
h2: combined manhattan distance
Output format: [depth], [numCreated], [numExpanded], [maxFringe]
Algorithms used: breadth-first search, depth-first search, greedy best-first search(h), AStar(h), and depth-limited search

Initial State:
"1 2356749AB8DEFC"
 _ _ _ _
|1| |2|3|
 - - - - 
|5|6|7|4|
 - - - - 
|9|A|B|8|
 - - - - 
|D|E|F|C|
 - - - - 

BFS:
5, 179, 57, 66

DFS:
5, 17, 6, 6

GBFS(h1):
5, 17, 6, 6

GBFS(h2):
5, 17, 6, 6

AStar(h1):
5, 41, 13, 16

AStar(h2):
5, 38, 12, 15

DLS (depth limit = 4):
-1, 79, 56, 32

DLS (depth limit = 5):
5, 15, 6, 6



Initial State:
"123456789AFBDEC "
 _ _ _ _
|1|2|3|4|
 - - - - 
|5|6|7|8|
 - - - - 
|9|A|F|B|
 - - - - 
|D|E|C| |
 - - - - 

BFS:
4, 73, 22, 30

DFS:
60, 183, 61, 61

GBFS(h1):
4, 15, 5, 6

GBFS(h2):
4, 15, 5, 6

AStar(h1):
4, 28, 9, 11

AStar(h2):
4, 21, 7, 8

DLS (depth limit = 4):
4, 22, 12, 9

DLS (depth limit = 5):
4, 38, 22, 15



Time Complexities:
BFS: O(b^d)
DFS: O(b^m)
GBFS(h1): O(bd)
GBFS(h2): O(bd)
AStar(h1): O(bd)
AStar(h2): O(bd)
DLS (depth limit): O(b^l), l is depth limit