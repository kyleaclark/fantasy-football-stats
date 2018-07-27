from __future__ import division
from ff_stats.common.nfl_db_query import NflDbQuery
from ff_stats.player import Player


class PlayerStats(object):

    def __init__(self):
        self.query = NflDbQuery()

    def generate_player_stats_by_category(self, sample_size, stats_category, nfl_year, weeks):
        player_nfl_db_objects = self.query.aggregrate_category_stats(sample_size, stats_category, nfl_year, weeks)

        for player_obj in player_nfl_db_objects:
            player = Player(player_obj)
            print(player)

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