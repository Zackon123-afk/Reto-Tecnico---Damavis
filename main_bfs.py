HORIZONTAL = 0
VERTICAL = 1
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'
MOVE_LIST = [EAST,NORTH,WEST,SOUTH]

WALL = '#'

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
    
    def is_valid(x, y, direction):
        if 0 <= x < rows and 0 <= y < cols and maze[x][y] == ".":
            if direction == HORIZONTAL:
                return (
                    0 <= y + 1 < cols
                    and 0 <= y - 1 < cols
                    and maze[x][y + 1] != WALL
                    and maze[x][y - 1] != WALL
                )
            else:
                return (
                    0 <= x + 1 < rows
                    and 0 <= x - 1 < rows
                    and maze[x + 1][y] != WALL
                    and maze[x - 1][y] != WALL
                )
    
    def is_goal(x, y, direction):
        return (x == rows - 2 and y == cols - 1 and direction == VERTICAL) or (
            x == rows - 1 and y == cols - 2 and direction == HORIZONTAL
        )  

    def rotate(direction):
        return HORIZONTAL if direction == VERTICAL else VERTICAL

    def can_rotate(x,y):
        return (1 <= x < rows-1 and 1 <= y < cols-1 and maze[x][y] != WALL and maze[x+1][y] != WALL and maze[x-1][y] != WALL and maze[x][y+1] != WALL 
                and maze[x][y-1] != WALL and maze[x+1][y+1] != WALL and maze[x-1][y-1] != WALL and maze[x+1][y-1] != WALL and maze[x-1][y+1] != WALL)
    
    def dfs(x, y, direction, steps):

        if not is_valid(x, y, direction):
            return False, steps
        
        if is_goal(x,y,direction):
            return True, steps

        maze[x][y] = 'X'  # Mark the cell as visited
        
        # Try moving
        for move in MOVE_LIST:
            if move == EAST:
                new_x, new_y = x, y + 1
            elif move == SOUTH:
                new_x, new_y = x + 1, y
            elif move == NORTH:
                new_x, new_y = x - 1, y
            elif move == WEST:
                new_x, new_y = x, y - 1

            result, new_steps = dfs(new_x, new_y, direction, steps + 1)
            if result:
                return result, new_steps
        
        # Now moving with the rod rotated
        for move in MOVE_LIST:
            if can_rotate(x,y):
                if move == EAST:
                    new_x, new_y = x, y + 1
                elif move == SOUTH:
                    new_x, new_y = x + 1, y
                elif move == NORTH:
                    new_x, new_y = x - 1, y
                elif move == WEST:
                    new_x, new_y = x, y - 1
                                
                new_direction = rotate(direction)
                result, new_steps = dfs(new_x, new_y, new_direction, steps + 2)
                if result:
                    return result, new_steps
            
        maze[x][y] = '.'  # Backtrack if the path doesn't lead to the destination
        return False, steps
    
    rows = len(maze)
    cols = len(maze[0])

    is_size_correct(rows,cols)

    start_direction = HORIZONTAL

    _, steps = dfs(0, 1, start_direction, 0)

    return steps if steps != 0 else -1

def main():
    maze=labyrinth

    num_pasos = solve_maze(maze)
    
    print(num_pasos)

if __name__ == "__main__":
    main()