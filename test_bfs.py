import unittest
import main_bfs

class TestBFS(unittest.TestCase):

    def test_correct_maze_size(self):
        labyrinth = [[".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".",".","."],]
        
        with self.assertRaises(main_bfs.NotPermitedSizeError):
            main_bfs.solve_maze(labyrinth)

        

    def test_labyrinth1(self):
    
        labyrinth = [[".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".",".","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]]
    
        steps = main_bfs.solve_maze(labyrinth)

        self.assertEqual(steps, 11)

    def test_labyrinth2(self):
    
        labyrinth = [[".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".","#","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]]
        
        steps = main_bfs.solve_maze(labyrinth)

        self.assertEqual(steps, -1)

    def test_labyrinth3(self):
    
        labyrinth = [[".",".","."],
                    [".",".","."],
                    [".",".","."]]
        
        steps = main_bfs.solve_maze(labyrinth)

        self.assertEqual(steps, 2)

    def test_labyrinth4(self):
    
        labyrinth = [[".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".","#",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".","#",".",".",".","#",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."]]
        
        steps = main_bfs.solve_maze(labyrinth)

        self.assertEqual(steps, 16)

if __name__ == '__main__':
    unittest.main()