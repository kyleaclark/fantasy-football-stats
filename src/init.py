import sys

from nfl_stats import NflStats
from position import Position
from position_configs import qb_config, rb_config, wr_config, te_config
from stats_generator import StatsGenerator

import export_list

def init():
    nfl_year = int(sys.argv[1])

    nfl_stats = NflStats(nfl_year)

    # Generate and export qb stats
    qb_position = Position(qb_config)
    qb_stats_generator = StatsGenerator(nfl_stats, qb_position, nfl_year)
    qb_stats_generator.generate_stats()
    qb_stats_generator.export_stats()

    # Generate and export rb stats
    rb_position = Position(rb_config)
    rb_stats_generator = StatsGenerator(nfl_stats, rb_position, nfl_year)
    rb_stats_generator.generate_stats()
    rb_stats_generator.export_stats()

    # Generate and export wr stats
    wr_position = Position(wr_config)
    wr_stats_generator = StatsGenerator(nfl_stats, wr_position, nfl_year)
    wr_stats_generator.generate_stats()
    wr_stats_generator.export_stats()

    # Generate and export te stats
    te_position = Position(te_config)
    te_stats_generator = StatsGenerator(nfl_stats, te_position, nfl_year)
    te_stats_generator.generate_stats()
    te_stats_generator.export_stats()


if __name__ == "__main__":
    init()
