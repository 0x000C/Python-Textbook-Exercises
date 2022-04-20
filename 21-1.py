# An investigative reporter discovered that not only was Lyndsay employing
# dubious statistical methods, she was applying them to data she had
# merely made up.151 In fact, John had defeated Lyndsay 479 times and lost
# 443 times. At what level is this difference statistically significant?

import scipy.stats

num_games = 479 + 443
lyndsay_wins = 443
outcomes = [1.0] * lyndsay_wins + [0.0] * (num_games - lyndsay_wins)
print('The p-value from a one-sample test is',
      scipy.stats.ttest_1samp(outcomes, 0.5)[1])
