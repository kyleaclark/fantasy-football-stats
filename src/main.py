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
export_list.export_to_json(qb_list, 'qb')
export_list.export_to_csv(qb_list, '2017_qb.csv')

# Process and export rb stats csv
rb_list = []
config = configs.rb()
core_stats.generate_position_stats(rb_list, config)
advanced_stats.calc_plyr(rb_list, config['sample_size'], config['cost_baseline'])
export_list.export_to_json(rb_list, 'rb')
export_list.export_to_csv(rb_list, '2017_rb.csv')

# # Process and export wr stats csv
wr_list = []
config = configs.wr()
core_stats.generate_position_stats(wr_list, config)
advanced_stats.calc_plyr(wr_list, config['sample_size'], config['cost_baseline'])
export_list.export_to_json(wr_list, 'wr')
export_list.export_to_csv(wr_list, '2017_wr.csv')

# # Process and export te stats csv
te_list = []
config = configs.te()
core_stats.generate_position_stats(te_list, config)
advanced_stats.calc_plyr(te_list, config['sample_size'], config['cost_baseline'])
export_list.export_to_json(te_list, 'te')
export_list.export_to_csv(te_list, '2017_te.csv')
