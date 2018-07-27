import sys

from ff_stats.common.player_stats import PlayerStats


def init(nfl_year_param):
    print(sys.argv)
    nfl_year = int(sys.argv[1]) if len(sys.argv) > 1 else nfl_year_param
    output_year = nfl_year + 1

    player_stats = PlayerStats()
    sample_size = 50
    nfl_year = 2017
    weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    stats_category = 'passing_yds'
    stats = player_stats.generate_player_stats_by_category(sample_size, stats_category, nfl_year, weeks)

    # Generate Top 50 passing yards by year
    # Generate Top 50 rushing yards by year
    # Generate Top 50 receiving yards by year

if __name__ == "__main__":
    init(nfl_year_param=2009)
