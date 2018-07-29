import sys

import pandas as pd

from ff_stats.common.nfldb_client import NfldbClient
from ff_stats.common.players import Players

def init():
    print(sys.argv)
    nfl_years = list(range(2009, 2017))
    stat_categories = ['passing_yds', 'rushing_yds', 'receiving_yds']
    weeks = list(range(1, 16))
    sample_size = 50
    nfldb_client = NfldbClient()
    players = Players(nfldb_client)

    for nfl_year in nfl_years:
        for stat_category in stat_categories:
            players.compute_player_stats_by_category(sample_size, stat_category, nfl_year, weeks)



    for player in players.container:


    print('debug')

    # Generate Top 50 passing yards by year
    # Generate Top 50 rushing yards by year
    # Generate Top 50 receiving yards by year


if __name__ == "__main__":
    init()
