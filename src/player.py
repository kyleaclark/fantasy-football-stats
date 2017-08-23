from fantasy_stats import FantasyStats

class Player():

    def __init__(self, plyr_id, plyr_name):
        self.id = plyr_id
        self.name = plyr_name

        self.fantasy_stats_segments = {}


    def add_stats(self, segment, stats_aggregrate):
        stats = stats_aggregrate[0] if stats_aggregrate else None
        self.fantasy_stats_segments[segment] = FantasyStats(stats)


    def get_points_segment(self, segment):
        fantasy_stats = self.fantasy_stats_segments[segment]
        fantasy_stats.calc_fantasy_points()
        return fantasy_stats.get_fantasy_points()
