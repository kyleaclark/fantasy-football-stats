from fantasy_stats import FantasyStats

class Player():

    def __init__(self, plyr_id, plyr_name):
        self.id = plyr_id
        self.name = plyr_name

        self.fantasy_stats_dict = {}
        self.fantasy_points_dict = {}


    def add_stats(self, segment, stats_aggregrate):
        stats = stats_aggregrate[0] if stats else {}
        fantasy_stats = FantasyStats(stats)
        self.fantasy_stats_dict[segment] = fantasy_stats
        self.fantasy_points_dict[segment] = fantasy_stats.calc_fantasy_points()


    def get_points_segment(self, segment):
        return self.fantasy_points_dict[segment]
