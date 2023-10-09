class Game:

    #Constructor
    def __init__(self):
        self.rolls = [0] * 21
        self.currentRoll = 0

    #Method to roll the ball
    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    #Method to calculate the score
    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(10):
            if self.is_strike(frameIndex):
                score += 10 + self.strike_bonus(frameIndex)
                frameIndex += 1
            elif self.is_spare(frameIndex):
                score += 10 + self.spare_bonus(frameIndex)
                frameIndex += 2
            else:
                score += self.sum_of_balls_in_frame(frameIndex)
                frameIndex += 2
        return score

    #Helper methods
    def is_strike(self, frameIndex):
        return self.rolls[frameIndex] == 10

    def sum_of_balls_in_frame(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

    def spare_bonus(self, frameIndex):
        return self.rolls[frameIndex + 2]

    def strike_bonus(self, frameIndex):
        return self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]

    def is_spare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10
