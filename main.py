HORIZONTAL = 0
VERTICAL = 1
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'
MOVE_LIST = [EAST,NORTH,WEST,SOUTH]

recently_rotated = False

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
    
    def is_valid(x, y, direction):
        global recently_rotated
        if 0 <= x < rows and 0 <= y < cols and (maze[x][y] == "." or recently_rotated == True):
            recently_rotated = False
            if direction == HORIZONTAL:
                return (0 <= y+1 < cols and 0 <= y-1 < cols and maze[x][y+1] != "#"
                and maze[x][y-1] != "#")
            else:
                return (0 <= x+1 < rows and 0 <= x-1 < rows and maze[x+1][y] != "#"
                and maze[x-1][y] != "#")
            
    def rotate(direction):
        return HORIZONTAL if direction == VERTICAL else VERTICAL

    
    def dfs(x, y, direction, steps):

        global recently_rotated

        if not is_valid(x, y, direction):
            recently_rotated = False
            return False, steps
        
        if x == rows - 2 and y == cols - 1 and direction == VERTICAL:
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
            
            recently_rotated = False
            result, new_steps = dfs(new_x, new_y, direction, steps + 1)
            if result:
                return result, new_steps
        
        # Rotate
        new_direction = rotate(direction)  # Rotate 90 degrees counterclockwise
        recently_rotated = True
        result, new_steps = dfs(x, y, new_direction, steps + 1)
        if result:
            return result, new_steps
        
        recently_rotated = False
        maze[x][y] = '.'  # Backtrack if the path doesn't lead to the destination
        return False, steps
    
    rows = len(maze)
    cols = len(maze[0])

    start_direction = HORIZONTAL

    _, steps = dfs(0, 1, start_direction, 0)
    
    return steps

def main():
    maze=labyrinth

    num_pasos = solve_maze(maze)

    print(num_pasos)

if __name__ == "__main__":
    main()