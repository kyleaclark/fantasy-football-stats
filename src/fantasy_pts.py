import stat_utils as util

def calc_qb(plyr_dict):
    'Calculates fantasy points by a qb'

    rushing_yds_pts = util.calc_reg_yd_pts(plyr_dict['rushing_yds'])
    rushing_tds_pts = util.calc_reg_td_pts(plyr_dict['rushing_tds'])
    passing_yds_pts = util.calc_pass_yd_pts(plyr_dict['passing_yds'])
    passing_tds_pts = util.calc_pass_td_pts(plyr_dict['passing_tds'])
    passing_int_pts = util.calc_int_pts_loss(plyr_dict['passing_int'])
    fumbles_lost_pts = util.calc_fum_pts_loss(plyr_dict['fumbles_lost'])

    return rushing_yds_pts + rushing_tds_pts + passing_yds_pts + passing_tds_pts + fumbles_lost_pts + passing_int_pts

def generate_qb_plyr_stats_dict(plyr_stats):
    return {
        'rushing_yds': plyr_stats.rushing_yds or 0,
        'rushing_tds': plyr_stats.rushing_tds or 0,
        'passing_yds': plyr_stats.passing_yds or 0,
        'passing_tds': plyr_stats.passing_tds or 0,
        'passing_int': plyr_stats.passing_int or 0,
        'fumbles_lost': plyr_stats.receiving_tds or 0
    }

def generate_qb_plyr_default_dict():
    return {
        'rushing_yds': 0,
        'rushing_tds': 0,
        'passing_yds': 0,
        'passing_tds': 0,
        'passing_int': 0,
        'fumbles_lost': 0
    }

def calc_pos_plyr(plyr_dict):
    'Calculates fantasy points by a rb, wr, or te'

    rushing_yds_pts = util.calc_reg_yd_pts(plyr_dict['rushing_yds'])
    rushing_tds_pts = util.calc_reg_td_pts(plyr_dict['rushing_tds'])
    receiving_yds_pts = util.calc_reg_yd_pts(plyr_dict['receiving_yds'])
    receiving_tds_pts = util.calc_reg_td_pts(plyr_dict['receiving_tds'])
    fumbles_lost_pts = util.calc_fum_pts_loss(plyr_dict['fumbles_lost'])

    return rushing_yds_pts + rushing_tds_pts + receiving_yds_pts + receiving_tds_pts + fumbles_lost_pts

# TODO: consolidate all of these dict keys to be dynamic
def generate_pos_plyr_stats_dict(plyr_stats):
    return {
        'rushing_yds': plyr_stats.rushing_yds or 0,
        'rushing_tds': plyr_stats.rushing_tds or 0,
        'receiving_yds': plyr_stats.receiving_yds or 0,
        'receiving_tds': plyr_stats.receiving_tds or 0,
        'fumbles_lost': plyr_stats.receiving_tds or 0
    }

def generate_pos_plyr_default_dict():
    return {
        'rushing_yds': 0,
        'rushing_tds': 0,
        'receiving_yds': 0,
        'receiving_tds': 0,
        'fumbles_lost': 0
    }
