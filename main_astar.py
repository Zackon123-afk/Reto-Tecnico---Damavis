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

MAX_SIZE = 1000
MIN_SIZE = 3

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
        if not (MIN_SIZE <= rows <= MAX_SIZE and MIN_SIZE <= cols <= MAX_SIZE):
            raise NotPermitedSizeError("Values of the labyrinth not accepted")
    
    def fill_dict(rows, cols):

        temp_dict = {}
        x = 0
        while x < rows:
            y = 0

            while y < cols:
                cell = (x,y,HORIZONTAL)
                cell2 = (x,y,VERTICAL)
                temp_dict[cell] = float('inf')
                temp_dict[cell2] = float('inf')
                y = y + 1

            x = x + 1
        
        return temp_dict

    
    def can_move(x, y, direction):
        if 0 <= x < rows and 0 <= y < cols and maze[x][y] == ".":
            if direction == HORIZONTAL:
                return (
                    0 <= y+1 < cols 
                    and 0 <= y-1 < cols 
                    and maze[x][y+1] != "#"
                    and maze[x][y-1] != "#"
                    )
            else:
                return (
                    0 <= x+1 < rows 
                    and 0 <= x-1 < rows 
                    and maze[x+1][y] != "#"
                    and maze[x-1][y] != "#"
                    )
            
    def can_rotate(x,y):
        return (
            1 <= x < rows-1 and 1 <= y < cols-1 
            and maze[x][y] != "#" and maze[x+1][y] != "#" and maze[x-1][y] != "#" 
            and maze[x][y+1] != "#" and maze[x][y-1] != "#" and maze[x+1][y+1] != "#" 
            and maze[x-1][y-1] != "#" and maze[x+1][y-1] != "#" and maze[x-1][y+1] != "#"
            )
    
    def rotate_direction(direction):

        if direction == VERTICAL:
            return HORIZONTAL
        else:
            return VERTICAL
    
    def is_goal(curr_cell, goal1, goal2):
        return (
                (curr_cell[0] == goal1[0]
                and  curr_cell[1] == goal1[1]
                and curr_cell[2] == goal1[2])
                or 
                (curr_cell[0] == goal2[0]
                and  curr_cell[1] == goal2[1]
                and curr_cell[2] == goal2[2])
                )

    def heuristic(node, goal1, goal2):
        h_goal1 = abs(node[0] - goal1[0]) + abs(node[1] - goal1[1])
        h_goal2 = abs(node[0] - goal2[0]) + abs(node[1] - goal2[1])

        if h_goal1 <= h_goal2:
            return h_goal1
        else:
            return h_goal2

    rows = len(maze)
    cols = len(maze[0])

    is_size_correct(rows,cols)

    start = (0, 1, HORIZONTAL)
    goal1 = (rows-2, cols-1, VERTICAL)
    goal2 = (rows-1, cols-2, HORIZONTAL)

    g_score = fill_dict(rows,cols)
    g_score[start] = 0

    f_score = fill_dict(rows,cols)
    f_score[start] = heuristic(start, goal1, goal2)
    

    open_list = PriorityQueue()
    open_list.put(((heuristic(start, goal1, goal2)),start))
    a_path = {}

    while not open_list.empty():

        curr_cell=open_list.get()[1]
        if is_goal(curr_cell, goal1, goal2):
            break

        new_rotation = rotate_direction(curr_cell[2])

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
            elif can_rotate(curr_cell[0],curr_cell[1]):
                if move == EAST_ROTATED:
                        child_cell = (curr_cell[0],curr_cell[1]+1,new_rotation)
                elif move == SOUTH_ROTATED:
                        child_cell = (curr_cell[0]+1,curr_cell[1],new_rotation)
                elif move == NORTH_ROTATED:
                        child_cell = (curr_cell[0]-1,curr_cell[1],new_rotation)
                elif move == WEST_ROTATED:
                        child_cell = (curr_cell[0],curr_cell[1]-1,new_rotation)
                has_rotated = True

            else:
                continue
                      
            if can_move(child_cell[0],child_cell[1],child_cell[2]):
                temp_g_score = g_score[curr_cell]+1
                if has_rotated == True:
                    temp_g_score = temp_g_score + 1
                temp_f_score = temp_g_score+heuristic(child_cell,goal1,goal2)

                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open_list.put((temp_f_score,child_cell))                
                    a_path[child_cell]=(curr_cell,has_rotated)
    

    if goal1 in a_path :
        cell_goal1 = goal1
    else:
        cell_goal1 = None

    if goal2 in a_path:
        cell_goal2 = goal2
    else:
        cell_goal2 = None
    
    if cell_goal1 == None and cell_goal2 == None:
        return -1

    steps_1 = 0
    while cell_goal1!=start and cell_goal1!= None:

        value_a_path = a_path[cell_goal1]
        if value_a_path[1] == False:
            steps_1 = steps_1 + 1
        else:
            steps_1 = steps_1 + 2

        cell_goal1 = value_a_path[0]
    
    steps_2 = 0
    while cell_goal2!=start and cell_goal2!= None:

        value_a_path = a_path[cell_goal2]
        if value_a_path[1] == False:
            steps_2 = steps_2 + 1
        else:
            steps_2 = steps_2 + 2

        cell_goal2 = value_a_path[0]
    
    if (steps_1 < steps_2) or steps_2==0:
        return steps_1
    else:
        return steps_2

def main():
    maze=labyrinth4

    steps = solve_maze(maze)
    print(steps)


if __name__ == "__main__":
    main()
