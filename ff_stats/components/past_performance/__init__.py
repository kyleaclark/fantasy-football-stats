import sys

from nfl_stats import NflStats
from ff_stats.position import Position
from ff_stats.position_configs import qb_config, rb_config, wr_config, te_config
from ff_stats.common.stats_communicator import StatsCommunicator


def init(nfl_year_param):
    print(sys.argv)
    nfl_year = int(sys.argv[1]) if len(sys.argv) > 1 else nfl_year_param
    output_year = nfl_year + 1

    nfl_stats = NflStats()

    # Generate and export qb stats
    qb_position = Position(qb_config)
    qb_stats_generator = StatsCommunicator(nfl_stats, qb_position, output_year)
    qb_stats_generator.generate_stats()
    qb_stats_generator.export_stats()

    # Generate and export rb stats
    rb_position = Position(rb_config)
    rb_stats_generator = StatsCommunicator(nfl_stats, rb_position, output_year)
    rb_stats_generator.generate_stats()
    rb_stats_generator.export_stats()

    # Generate and export wr stats
    wr_position = Position(wr_config)
    wr_stats_generator = StatsCommunicator(nfl_stats, wr_position, output_year)
    wr_stats_generator.generate_stats()
    wr_stats_generator.export_stats()

    # Generate and export te stats
    te_position = Position(te_config)
    te_stats_generator = StatsCommunicator(nfl_stats, te_position, output_year)
    te_stats_generator.generate_stats()
    te_stats_generator.export_stats()


if __name__ == "__main__":
    init(nfl_year_param=2009)
