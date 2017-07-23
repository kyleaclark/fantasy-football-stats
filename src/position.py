import stat_utils as util

class Position():

    def __init__(self, position_config):
        self.type = position_config['position']
        self.cost_baseline = position_config['cost_baseline']
        self.sample_size = position_config['sample_size']
        self.sample_trim = self.sample_size * .1
        self.sort_by_category = position_config['sort_by_category']

        self.weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


    # def add_player_list():



    def calc_fantasy_stats(self, plyr_dict):
        if self.position == 'QB':
            self.calc_fantasy_stats = calc_fantasy_stats
            self.generate_plyr_stats_dict = generate_plyr_stats_dict
            self.generate_plyr_default_dict = generate_plyr_default_dict


    # def generate_plyr_stats_dict(self, plyr_stats):
