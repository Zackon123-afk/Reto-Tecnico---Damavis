HORIZONTAL = 0
VERTICAL = 1
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'
MOVE_LIST = [EAST,NORTH,WEST,SOUTH]

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
        if 0 <= x < rows and 0 <= y < cols and maze[x][y] == ".":
            if direction == HORIZONTAL:
                return (0 <= y+1 < cols and 0 <= y-1 < cols and maze[x][y+1] != "#"
                and maze[x][y-1] != "#")
            else:
                return (0 <= x+1 < rows and 0 <= x-1 < rows and maze[x+1][y] != "#"
                and maze[x-1][y] != "#")
    
    def is_goal(x, y, direction):
        return ((x == rows - 2 and y == cols - 1 and direction == VERTICAL) or
                (x == rows - 1 and y == cols - 2 and direction == HORIZONTAL))     

    def rotate(direction):
        return HORIZONTAL if direction == VERTICAL else VERTICAL

    def can_rotate(x,y):
        return (1 <= x < rows-1 and 1 <= y < cols-1 and maze[x][y] != "#" and maze[x+1][y] != "#" and maze[x-1][y] != "#" and maze[x][y+1] != "#" 
                and maze[x][y-1] != "#" and maze[x+1][y+1] != "#" and maze[x-1][y-1] != "#" and maze[x+1][y-1] != "#" and maze[x-1][y+1] != "#")
    
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
            if move == EAST:
                new_x, new_y = x, y + 1
            elif move == SOUTH:
                new_x, new_y = x + 1, y
            elif move == NORTH:
                new_x, new_y = x - 1, y
            elif move == WEST:
                new_x, new_y = x, y - 1
            
            if can_rotate(new_x,new_y):
                new_direction = rotate(direction)
                result, new_steps = dfs(new_x, new_y, new_direction, steps + 2)
                if result:
                    return result, new_steps
        
        maze[x][y] = '.'  # Backtrack if the path doesn't lead to the destination
        return False, steps
    
    rows = len(maze)
    cols = len(maze[0])

    start_direction = HORIZONTAL

    _, steps = dfs(0, 1, start_direction, 0)

    return steps if steps != 0 else -1

def main():
    maze=labyrinth

    num_pasos = solve_maze(maze)
    
    print(num_pasos)

if __name__ == "__main__":
    main()