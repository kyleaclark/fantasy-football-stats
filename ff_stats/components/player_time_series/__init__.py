import sys

import pandas as pd

from ff_stats.common.nfldb_client import NfldbClient
from ff_stats.common.players import Players
from ff_stats.common.player_time_series import PlayerTimeSeries


def init():
    print(sys.argv)
    nfl_years = [2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009]
    num_nfl_years = len(nfl_years)
    stat_categories = ['passing_yds', 'rushing_yds', 'receiving_yds']
    weeks = list(range(1, 17))
    sample_size = 50
    nfldb_client = NfldbClient()
    players = Players(nfldb_client)

    for year_idx, nfl_year in enumerate(nfl_years):
        for stat_category in stat_categories:
            players.compute_player_time_series_stats_by_category(sample_size, stat_category, nfl_year, weeks, year_idx)

    historical_data_list = []
    time_series_players = []
    for player_key, player in players.container.items():
        for nfl_year_delta in range(0, 9):
            if nfl_year_delta in player.stats:
                nfl_year_entry = 2017 - nfl_year_delta
                player_time_series = PlayerTimeSeries(player.id, player.first_name, player.last_name, nfl_year_entry, num_nfl_years)

                for nfl_year_idx, (nfl_year, player_stats) in enumerate(player.stats.iteritems()):
                    nfl_year_entry = nfl_year - nfl_year_delta
                    player_time_series.add_year_delta_stats(player_stats, nfl_year_entry)

                time_series_players.append(player_time_series)

    for player_time_series in time_series_players:
        player_data = {'id': player_time_series.id,
                       'first_name': player_time_series.first_name,
                       'last_name': player_time_series.last_name,
                       'year': player_time_series.year}

        for year_delta_key, year_delta_stats in player_time_series.year_delta_stats.iteritems():
            player_data.update(year_delta_stats)

        historical_data_list.append(player_data)

    historical_stats_df = pd.DataFrame(data=historical_data_list)
    historical_stats_df.sort_values(by=['id'], inplace=True)
    historical_stats_df = historical_stats_df.set_index('id').reset_index()
    #mid = df['Mid']
    #df.drop(labels=['Mid'], axis=1, inplace=True)
    #df.insert(0, 'Mid', mid)

    # historical_stats_df.reset_index(drop=True, inplace=True)
    print('debug')
    historical_stats_df.to_csv('output.csv', index=False)


    # Generate Top 50 passing yards by year
    # Generate Top 50 rushing yards by year
    # Generate Top 50 receiving yards by year


if __name__ == "__main__":
    init()
