class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is on the field and he  batting and now he hit the ball ... six!.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of the Batsman and Bowler classes
bat= Batsman()
ball = Bowler()

# Call the play() method for each object
ball.play()
bat.play()

