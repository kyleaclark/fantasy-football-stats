import core_stats

def calc_position_stats(plyr_list, sample_size, sample_trim):
    global position_full_avg
    global position_beg_avg

    position_full_avg_sum = 0
    position_beg_avg_sum = 0

    for index, player in enumerate(plyr_list):
        if (index > sample_trim and index < sample_size - sample_trim):
            position_full_avg_sum += player['avg_pts']
            position_beg_avg_sum += player['beg_avg_pts']

    divisible = (sample_size - (sample_trim * 2))
    position_full_avg = position_full_avg_sum / divisible
    position_beg_avg = position_beg_avg_sum / divisible

def calc_plyr(player_list):
    replacement_pts = player_list[9]['avg_pts'] - position_full_avg
    median_starter_pts = player_list[4]['avg_pts'] - position_full_avg

    beg_replacement_pts = player_list[9]['beg_avg_pts'] - position_beg_avg
    beg_median_starter_pts = player_list[4]['beg_avg_pts'] - position_beg_avg

    for plyr in player_list:
        plyr['plus_minus'] = plyr['avg_pts'] - position_full_avg
        plyr['points_above_replacement'] = plyr['plus_minus'] - replacement_pts
        plyr['points_above_median_starter'] = plyr['plus_minus'] - median_starter_pts
        plyr['beg_plus_minus'] = plyr['beg_avg_pts'] - position_beg_avg
        plyr['beg_points_above_replacement'] = plyr['beg_plus_minus'] - beg_replacement_pts
        plyr['beg_points_above_median_starter'] = plyr['beg_plus_minus'] - beg_median_starter_pts
