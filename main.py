import configs
import query
import core_stats
import advanced_stats
import export_list

qb_list = []

# calculate mean
# calculate standard deviation per player
#
# +/- above mean for total total_pts of all games weeks 1-16
# +/- above mean for avg total_pts per games played weeks 1-16
# positive players count & percentage: above 0
# star player point line: above mean of positive players
#

query.init()
core_stats.generate_position_stats(qb_list, configs.qb())
advanced_stats.calc_plyr(qb_list)
export_list.export(qb_list)
