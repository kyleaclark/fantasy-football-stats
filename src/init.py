import sys

import advanced_stats
import configs
from nfl_stats import NflStats
import export_list

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

    # Process and export rb stats csv
    config = configs.rb()
    rb_list = nfl_stats.generate_position_stats(config)
    advanced_stats.calc_position_stats(rb_list, config['sample_size'], config['sample_trim'])
    advanced_stats.calc_plyr(rb_list, config['sample_size'], config['cost_baseline'])

    export_list.export_to_json(output_year, rb_list, 'rb')
    export_list.export_to_csv(rb_list, ('%d_rb.csv' % output_year))

    # # Process and export wr stats csv
    config = configs.wr()
    wr_list = nfl_stats.generate_position_stats(config)
    advanced_stats.calc_position_stats(wr_list, config['sample_size'], config['sample_trim'])
    advanced_stats.calc_plyr(wr_list, config['sample_size'], config['cost_baseline'])

    export_list.export_to_json(output_year, wr_list, 'wr')
    export_list.export_to_csv(wr_list, ('%d_wr.csv' % output_year))

    # # Process and export te stats csv
    config = configs.te()
    te_list = nfl_stats.generate_position_stats(config)
    advanced_stats.calc_position_stats(te_list, config['sample_size'], config['sample_trim'])
    advanced_stats.calc_plyr(te_list, config['sample_size'], config['cost_baseline'])

    export_list.export_to_json(output_year, te_list, 'te')
    export_list.export_to_csv(te_list, ('%d_te.csv' % output_year))


if __name__ == "__main__":
    init()
