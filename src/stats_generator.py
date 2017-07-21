import sys

import advanced_stats
import configs
from nfl_stats import NflStats
import export_list
from position import Position

class StatsGenerator():

    def __init__(self):
        self.positions = {}


    def generate_stats(position_type, config):
        self.positions.add_position(position_type)

        position_stats = nfl_stats.generate_position_stats(config)
        advanced_stats.calc_position_stats(position_stats, config['sample_size'],
                                           config['sample_trim'])
        advanced_stats.calc_plyr(position_stats, config['sample_size'],
                                 config['cost_baseline'])

        self.positions[position_type]

def init():
    nfl_year = int(sys.argv[1])
    output_year = nfl_year + 1

    nfl_stats = NflStats(nfl_year)

    # Process and export qb stats csv
    config = configs.qb()


    qb_list = nfl_stats.generate_position_stats(config)
    advanced_stats.calc_position_stats(qb_list, config['sample_size'], config['sample_trim'])
    advanced_stats.calc_plyr(qb_list, config['sample_size'], config['cost_baseline'])

    export_list.export_to_json(output_year, qb_list, 'qb')
    export_list.export_to_csv(qb_list, ('%d_qb.csv' % output_year))
