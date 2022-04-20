import random
import numpy as np

# # Figure 18-1 on page 396
def roll_die():
    return random.choice([1,2,3,4,5,6])

class Craps_game(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0
        self.big6_wins, self.big6_losses = 0, 0

    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
            self.big6_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            self.big6_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            point = throw
            rolled6 = False
            if point == 6:
                rolled6 = True
            while True:
                throw = roll_die() + roll_die()
                if throw == 6:
                    rolled6 = True
                if throw == point:
                    self.pass_wins += 1
                    self.dp_losses += 1
                    break
                elif throw == 7:
                    self.pass_losses += 1
                    self.dp_wins += 1
                    if rolled6:
                        self.big6_wins += 1
                    else:
                        self.big6_losses += 1
                    break

    # def pass_results(self):
    #     return (self.pass_wins, self.pass_losses)

    # def dp_results(self):
    #     return (self.dp_wins, self.dp_losses, self.dp_pushes)

    def big6_results(self):
        return (self.big6_wins, self.big6_losses)
  
def craps_sim(hands_per_game, num_games):
    """Assumes hands_per_game and num_games are ints > 0
       Play num_games games of hands_per_game hands; print results"""
    games = []

    #Play num_games games
    for t in range(num_games):
        c = Craps_game()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)
        
    #Produce statistics for each game
    #p_ROI_per_game, dp_ROI_per_game = [], []
    big6_ROI_per_game = []
    for g in games:
        #wins, losses = g.pass_results()
        #p_ROI_per_game.append((wins - losses)/float(hands_per_game))
        #wins, losses, pushes = g.dp_results()
        #dp_ROI_per_game.append((wins - losses)/float(hands_per_game))
        wins, losses = g.big6_results()
        big6_ROI_per_game.append((wins - losses)/float(hands_per_game))
        
    #Produce and print summary statistics
    # mean_ROI = str(round((100*sum(p_ROI_per_game)/num_games), 4)) + '%'
    # sigma = str(round(100*np.std(p_ROI_per_game), 4)) + '%'
    # print('Pass:', 'Mean ROI =', mean_ROI, 'Std. Dev. =', sigma)
    # mean_ROI = str(round((100*sum(dp_ROI_per_game)/num_games), 4)) +'%'
    # sigma = str(round(100*np.std(dp_ROI_per_game), 4)) + '%'
    # print('Don\'t pass:','Mean ROI =', mean_ROI, 'Std Dev =', sigma)
    mean_ROI = str(round((sum(big6_ROI_per_game)/num_games), 4)) # + '%'
    sigma = str(round(np.std(big6_ROI_per_game), 4)) # + '%'
    # print('Big 6:', 'Mean ROI =', mean_ROI, 'Std. Dev. =', sigma)
    return mean_ROI, sigma

mean_ROI, sigma = craps_sim(100000, 10)
print(mean_ROI, sigma)

big6_cost_per_hour = round(30*5*float(mean_ROI),2)
big6_stdev = round(30*5*float(sigma),2)

print("Big 6 cost per hour = $", big6_cost_per_hour)
print("Big 6 standard deviation = $", big6_stdev)