from __future__ import division

full_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
beg_weeks = [1, 2, 3, 4, 5, 6, 7, 8]
end_weeks = [9, 10, 11, 12, 13, 14, 15, 16]

def calc_plyr_weeks(games):
    'Generates a list of weeks played from a list of games'

    return [game.week for game in games]
