class PlayerTimeSeries(object):

    def __init__(self, player_id, first_name, last_name, nfl_year, num_nfl_years):
        self.id = '%i_%s_%s' % (nfl_year, first_name, last_name)
        self.internal_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.year = nfl_year

        self.year_delta_stats = {}
        self.year_delta = 0

        for year_delta in range(0, num_nfl_years):
            self.add_year_delta_stats(None, year_delta)
    def add_year_delta_stats(self, player_stats, year_delta):
        year_delta = year_delta or self.year_delta

        stats = {}

        total_fantasy_pts_delta = 'delta_%i_total_fantasy_pts' % year_delta
        stats[total_fantasy_pts_delta] = player_stats.total_fantasy_pts if player_stats else None

        passing_yds_delta = 'delta_%i_passing_yds' % year_delta
        stats[passing_yds_delta] = player_stats.passing_yds if player_stats else None

        passing_tds_delta = 'delta_%i_passing_tds' % year_delta
        stats[passing_tds_delta] = player_stats.passing_tds if player_stats else None

        passing_int_delta = 'delta_%i_passing_int' % year_delta
        stats[passing_int_delta] = player_stats.passing_int if player_stats else None

        rushing_yds_delta = 'delta_%i_rushing_yds' % year_delta
        stats[rushing_yds_delta] = player_stats.rushing_yds if player_stats else None

        rushing_tds_delta = 'delta_%i_rushing_tds' % year_delta
        stats[rushing_tds_delta] = player_stats.rushing_tds if player_stats else None

        receiving_yds_delta = 'delta_%i_receiving_yds' % year_delta
        stats[receiving_yds_delta] = player_stats.receiving_yds if player_stats else None

        receiving_tds_delta = 'delta_%i_receiving_tds' % year_delta
        stats[receiving_tds_delta] = player_stats.receiving_tds if player_stats else None

        fumbles_lost_delta = 'delta_%i_fumbles_lost' % year_delta
        stats[fumbles_lost_delta] = player_stats.fumbles_lost if player_stats else None

        self.year_delta_stats[year_delta] = stats
