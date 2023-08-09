from queue import PriorityQueue

HORIZONTAL = 0
VERTICAL = 1

labyrinth = [[".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".",".","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]]

labyrinth2 = [[".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".","#","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]]

labyrinth3 = [[".",".","."],
            [".",".","."],
            [".",".","."]]

labyrinth4 = [[".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".","#",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".","#",".",".",".","#",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."]]

def solve_maze(maze):

    def is_size_correct(rows, cols):
        if not (3<= rows <=1000 and 3<= cols <= 1000):
            raise Exception("Values of the maze not accepted")
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == "."
    
    def rotate_direction(direction):
        return HORIZONTAL if direction == VERTICAL else VERTICAL

    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    rows = len(maze)
    cols = len(maze[0])

    is_size_correct(rows,cols)

    direction = HORIZONTAL

    start = (0, 1, direction)
    goal = (rows-2, cols-1, VERTICAL)

    
    closed_set = set()
    steps = 0
    g_score = {(pos): float('inf') for row in maze for pos in row}
    g_score[(start)] = 0
    f_score = {(pos): float('inf') for row in maze for pos in row}
    f_score[(start)] = heuristic(start, goal)

    open_list = PriorityQueue()
    open_list.put((heuristic(start,goal)),(heuristic(start,goal)),start)

    while open_list:
        
        currCell=open_list.get()[2]
        if currCell == goal:
            break
        for d in 'ESNW':
            

    return None

maze=labyrinth

solucion, num_pasos = solve_maze(maze)
if solucion:
    print(num_pasos)
else:
    print("-1")


import heapq
