from ff_stats.common.fantasy_stats import FantasyStats


class Player(object):

    def __init__(self, player_obj):
        self.id = player_obj.player_id
        self.name = player_obj.player.full_name
        self.team = player_obj.player.team


        self.fantasy_stats = FantasyStats(player_obj)
        self.fantasy_stats_segments = {}


    def add_stats(self, segment, stats_aggregrate):
        stats = stats_aggregrate[0] if stats_aggregrate else None
        if isinstance(stats, dict):
            print('debug')
        self.fantasy_stats_segments[segment] = FantasyStats(stats)


    def get_points_segment(self, segment):
        fantasy_stats = self.fantasy_stats_segments[segment]
        fantasy_stats.calc_fantasy_points()
        return fantasy_stats.compute_fantasy_points()
