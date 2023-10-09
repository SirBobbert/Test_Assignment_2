import unittest
from Game import Game

class BowlingGameTest(unittest.TestCase):

    #Initializes the Game class
    def setUp(self):
        self.g = Game()

    #Helper method to roll the ball
    def rollMany(self, n, pins):
        for i in range(n):
            self.g.roll(pins)

    def testGutterGame(self):
        self.rollMany(20, 0)
        self.assertEqual(0, self.g.score())

    def testAllOnes(self):
        self.rollMany(20, 1)
        self.assertEqual(20, self.g.score())

    def testOneSpare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17, 0)
        self.assertEqual(16, self.g.score())

    def testOneStrike(self):
        self.rollStrike()
        self.g.roll(3)  
        self.g.roll(4)  
        self.rollMany(16, 0)
        self.assertEqual(24, self.g.score())

    def testPerfectGame(self):
        self.rollMany(12, 10)
        self.assertEqual(300, self.g.score())

    def rollStrike(self):
        self.g.roll(10)

    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5) 
   

if __name__ == '__main__':
    unittest.main()
