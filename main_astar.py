from queue import PriorityQueue

HORIZONTAL = 0
VERTICAL = 1
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'
EAST_ROTATED = 'ER'
NORTH_ROTATED = 'NR'
WEST_ROTATED = 'WR'
SOUTH_ROTATED = 'SR'
MOVE_LIST = [EAST,NORTH,WEST,SOUTH,EAST_ROTATED,NORTH_ROTATED,WEST_ROTATED,SOUTH_ROTATED]

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

class NotPermitedSizeError(Exception):
    """Value of the labyrinth not accepted"""
    pass

def solve_maze(maze):

    def is_size_correct(rows, cols):
        if not (3<= rows <=1000 and 3<= cols <= 1000):
            raise NotPermitedSizeError("Values of the labyrinth not accepted")
    
    def can_move(x, y):
        if 0 <= x < rows and 0 <= y < cols and maze[x][y] == ".":
            if direction == HORIZONTAL:
                return (0 <= y+1 < cols and 0 <= y-1 < cols and maze[x][y+1] != "#"
                and maze[x][y-1] != "#")
            else:
                return (0 <= x+1 < rows and 0 <= x-1 < rows and maze[x+1][y] != "#"
                and maze[x-1][y] != "#")
            
    def can_rotate(x,y):
        return (1 <= x < rows-1 and 1 <= y < cols-1 and maze[x][y] != "#" and maze[x+1][y] != "#" and maze[x-1][y] != "#" and maze[x][y+1] != "#" 
                and maze[x][y-1] != "#" and maze[x+1][y+1] != "#" and maze[x-1][y-1] != "#" and maze[x+1][y-1] != "#" and maze[x-1][y+1] != "#")
    
    def rotate_direction(direction):
        return HORIZONTAL if direction == VERTICAL else VERTICAL
    
    def is_goal(curr_cell, goal1, goal2):
        return curr_cell == goal1 or curr_cell == goal2    

    def heuristic(node, goal1, goal2):
        h_goal1 = abs(node[0] - goal1[0]) + abs(node[1] - goal1[1])
        h_goal2 = abs(node[0] - goal2[0]) + abs(node[1] - goal2[1])

        return h_goal1 if h_goal1 >= h_goal2 else h_goal2
    
    rows = len(maze)
    cols = len(maze[0])

    is_size_correct(rows,cols)

    direction = HORIZONTAL

    start = (0, 1, direction)
    goal1 = (rows-2, cols-1, VERTICAL)
    goal2 = (rows-1, cols-2, HORIZONTAL)
    g_score = {(pos): float('inf') for row in maze for pos in row}
    g_score[(start)] = 0
    f_score = {(pos): float('inf') for row in maze for pos in row}
    f_score[(start)] = heuristic(start, goal1, goal2)
    

    open_list = PriorityQueue()
    open_list.put(((heuristic(start, goal1, goal2)),(heuristic(start, goal1, goal2)),start))
    a_path = {}

    while open_list:

        curr_cell=open_list.get()[2]
        if is_goal(curr_cell, goal1, goal2):
            break

        for move in MOVE_LIST: # Moving, and when is rotated, first we check if it can rotate
            has_rotated = False
            if move == EAST:
                child_cell = (curr_cell[0],curr_cell[1]+1,curr_cell[2])
            elif move == SOUTH:
                child_cell = (curr_cell[0]+1,curr_cell[1],curr_cell[2])
            elif move == NORTH:
                child_cell = (curr_cell[0]-1,curr_cell[1],curr_cell[2])
            elif move == WEST:
                child_cell = (curr_cell[0],curr_cell[1]-1,curr_cell[2])
            elif move == EAST_ROTATED and can_rotate(curr_cell[0],curr_cell[1]):
                    child_cell = (curr_cell[0],curr_cell[1]+1,rotate_direction(curr_cell[2]))
                    has_rotated = True
            elif move == SOUTH_ROTATED and can_rotate(curr_cell[0],curr_cell[1]):
                    child_cell = (curr_cell[0]+1,curr_cell[1],rotate_direction(curr_cell[2]))
                    has_rotated = True
            elif move == NORTH_ROTATED and can_rotate(curr_cell[0],curr_cell[1]):
                    child_cell = (curr_cell[0]-1,curr_cell[1],rotate_direction(curr_cell[2]))
                    has_rotated = True
            elif move == WEST_ROTATED and can_rotate(curr_cell[0],curr_cell[1]):
                    child_cell = (curr_cell[0],curr_cell[1]-1,rotate_direction(curr_cell[2]))
                    has_rotated = True

            if can_move(child_cell[0],child_cell[1]):
                temp_g_score = g_score[curr_cell]+1
                temp_f_score = temp_g_score+heuristic(child_cell,goal1,goal2)

                if temp_f_score < f_score[(child_cell[0],child_cell[1])]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open_list.put((temp_f_score,heuristic(child_cell,goal1,goal2),child_cell))
                    a_path[child_cell]=curr_cell

    fwd_path = {}
    cell= (0,1)
    while cell!=goal1 or cell!=goal2:
        fwd_path[a_path[cell]] = cell
        cell = a_path[cell]
    return fwd_path

def main():
    maze=labyrinth

    a_path = solve_maze(maze)
    
    print(a_path.__len__)

if __name__ == "__main__":
    main()
