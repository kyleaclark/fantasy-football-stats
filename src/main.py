import configs
import query
import core_stats
import advanced_stats
import export_list

# Initialize connection to NFLBB
query.init()

# Process and export qb stats csv
qb_list = []
config = configs.qb()
core_stats.generate_position_stats(qb_list, config)
advanced_stats.calc_plyr(qb_list, config['sample_size'], config['cost_baseline'])
export_list.export(qb_list, 'QB.csv')

# Process and export rb stats csv
rb_list = []
config = configs.rb()
core_stats.generate_position_stats(rb_list, config)
advanced_stats.calc_plyr(rb_list, config['sample_size'], config['cost_baseline'])
export_list.export(rb_list, 'RB.csv')

# # Process and export wr stats csv
wr_list = []
config = configs.wr()
core_stats.generate_position_stats(wr_list, config)
advanced_stats.calc_plyr(wr_list, config['sample_size'], config['cost_baseline'])
export_list.export(wr_list, 'WR.csv')

# # Process and export te stats csv
te_list = []
config = configs.te()
core_stats.generate_position_stats(te_list, config)
advanced_stats.calc_plyr(te_list, config['sample_size'], config['cost_baseline'])
export_list.export(te_list, 'TE.csv')
