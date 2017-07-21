from __future__ import division
import core_stats

def calc_position_stats(plyr_list, sample_size, sample_trim):
    'Calculates averages for a list of players'

    global position_full_avg
    global position_beg_avg
    global position_end_avg

    position_full_avg_sum = 0
    position_beg_avg_sum = 0
    position_end_avg_sum = 0

    for index, player in enumerate(plyr_list):
        if (index >= sample_trim and index < sample_size - sample_trim):
            position_full_avg_sum += player['avg_pts']
            position_beg_avg_sum += player['beg_avg_pts']
            position_end_avg_sum += player['end_avg_pts']

    divisible = (sample_size - (sample_trim * 2))
    position_full_avg = position_full_avg_sum / divisible
    position_beg_avg = position_beg_avg_sum / divisible
    position_end_avg = position_end_avg_sum / divisible

def calc_plyr(plyr_list, sample_size, cost_baseline):
    'Calculate the comparison stats for a list of players'

    median_plyr = (sample_size // 2) - 1
    top_qtr_plyr = (sample_size // 4) - 1

    plyr_list.sort(key=lambda p: p['avg_pts'], reverse=True)
    median_pts = plyr_list[median_plyr]['avg_pts']
    top_qtr_pts = plyr_list[top_qtr_plyr]['avg_pts']

    plyr_list.sort(key=lambda p: p['beg_avg_pts'], reverse=True)
    beg_median_pts = plyr_list[median_plyr]['beg_avg_pts']
    beg_top_qtr_pts = plyr_list[top_qtr_plyr]['beg_avg_pts']

    plyr_list.sort(key=lambda p: p['end_avg_pts'], reverse=True)
    end_median_pts = plyr_list[median_plyr]['end_avg_pts']
    end_top_qtr_pts = plyr_list[top_qtr_plyr]['end_avg_pts']

    for plyr in plyr_list:
        plyr['plus_minus'] = plyr['avg_pts'] - position_full_avg
        plyr['relative_avg_value'] = plyr['avg_pts'] / position_full_avg
        plyr['points_above_median'] = plyr['avg_pts'] - median_pts
        plyr['relative_median_value'] = plyr['avg_pts'] / median_pts
        plyr['points_above_top_qtr'] = plyr['avg_pts'] - top_qtr_pts
        plyr['relative_top_qtr_value'] = plyr['avg_pts'] / top_qtr_pts
        plyr['beg_plus_minus'] = plyr['beg_avg_pts'] - position_beg_avg
        plyr['beg_points_above_median'] = plyr['beg_avg_pts'] - beg_median_pts
        plyr['beg_points_above_top_qtr'] = plyr['beg_avg_pts'] - beg_top_qtr_pts
        plyr['end_plus_minus'] = plyr['end_avg_pts'] - position_end_avg
        plyr['end_points_above_median'] = plyr['end_avg_pts'] - end_median_pts
        plyr['end_points_above_top_qtr'] = plyr['end_avg_pts'] - end_top_qtr_pts
        plyr['auction_value'] = calc_plyr_auction_value(plyr, cost_baseline)

    plyr_list.sort(key=lambda p: p['auction_value'], reverse=True)

def calc_plyr_auction_value(plyr, cost_baseline):
    'Calculates the hypothetical auction value for a player'

    relative_total_value = (plyr['relative_median_value']) ** 2
    auction_value = (cost_baseline * relative_total_value) * plyr['availability']

    return auction_value if auction_value > 0 else 0
