import sys

import pandas as pd

from ff_stats.common.nfldb_client import NfldbClient
from ff_stats.common.players import Players

def init():
    print(sys.argv)
    nfl_years = list(range(2009, 2018))
    stat_categories = ['passing_yds', 'rushing_yds', 'receiving_yds']
    weeks = list(range(1, 17))
    sample_size = 50
    nfldb_client = NfldbClient()
    players = Players(nfldb_client)

    historical_stats_columns = ['year',
                                'player_id',
                                'first_name',
                                'last_name',
                                'total_fantasy_pts',
                                'passing_yds',
                                'passing_tds',
                                'passing_int',
                                'rushing_yds',
                                'rushing_tds',
                                'receiving_yds',
                                'receiving_tds',
                                'fumbles_lost']

    for nfl_year in nfl_years:
        for stat_category in stat_categories:
            players.compute_player_stats_by_category(sample_size, stat_category, nfl_year, weeks)

    historical_data_list = []
    for player_key, player in players.container.items():
        for year, player_stats in player.stats.items():
            player_data = [year,
                           player.id,
                           player.first_name,
                           player.last_name,
                           player_stats.total_fantasy_pts,
                           player_stats.passing_yds,
                           player_stats.passing_tds,
                           player_stats.passing_int,
                           player_stats.rushing_yds,
                           player_stats.rushing_tds,
                           player_stats.receiving_yds,
                           player_stats.receiving_tds,
                           player_stats.fumbles_lost]
            historical_data_list.append(player_data)

    historical_stats_df = pd.DataFrame(data=historical_data_list, columns=historical_stats_columns)
    historical_stats_df.sort_values(by=['year', 'last_name', 'first_name', 'player_id'], inplace=True)
    historical_stats_df.reset_index(drop=True, inplace=True)
    print('debug')
    historical_stats_df.to_csv('output.csv', index=False)


    # Generate Top 50 passing yards by year
    # Generate Top 50 rushing yards by year
    # Generate Top 50 receiving yards by year


if __name__ == "__main__":
    init()
