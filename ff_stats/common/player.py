from ff_stats.common.fantasy_stats import FantasyStats


class Player(object):

    def __init__(self, player_obj):
        self.id = player_obj.player_id
        self.name = player_obj.player.full_name
        self.team = player_obj.player.team
        self.stats = {}

    def compute_stats(self, player_obj, nfl_year):
        if nfl_year not in self.stats:
            self.stats[nfl_year] = FantasyStats(player_obj)

    def add_stats(self, segment, stats_aggregrate):
        stats = stats_aggregrate[0] if stats_aggregrate else None
        if isinstance(stats, dict):
            print('debug')
        self.fantasy_stats_segments[segment] = FantasyStats(stats)

    def get_points_segment(self, segment):
        fantasy_stats = self.fantasy_stats_segments[segment]
        fantasy_stats.calc_fantasy_points()
        return fantasy_stats.compute_fantasy_points()

    # def generate_position_stats(self, position, nfl_year):
    #     """Generates a list of player objects by position"""
    #
    #     stats = self.query.aggregrate_position_stats(position.type,
    #                                                  position.sample_size,
    #                                                  position.sort_by_category,
    #                                                  nfl_year,
    #                                                  util.full_weeks)
    #
    #     plyr_list = []
    #     for plyr in stats:
    #         plyr_info = self._generate_plyr_info(plyr,
    #                                              position.sample_size,
    #                                              position.sort_by_category,
    #                                              nfl_year)
    #         plyr_list.append(plyr_info)
    #
    #     return plyr_list
