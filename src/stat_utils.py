from __future__ import division

full_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
beg_weeks = [1, 2, 3, 4, 5, 6, 7, 8]
end_weeks = [9, 10, 11, 12, 13, 14, 15, 16]

# TODO: how to make the object exportable outside of method
def qb_plyr_methods():
    return {
        'rushing_yds': calc_reg_yd_pts,
        'rushing_tds': calc_reg_td_pts,
        'passing_yds': calc_pass_yd_pts,
        'passing_tds': calc_pass_td_pts,
        'passing_int': calc_int_pts_loss,
        'fumbles_lost': calc_fum_pts_loss
    }

# TODO: how to make the object exportable outside of method
def pos_plyr_methods():
    return {
        'rushing_yds': calc_reg_yd_pts,
        'rushing_tds': calc_reg_td_pts,
        'receiving_yds': calc_reg_yd_pts,
        'receiving_tds': calc_reg_td_pts,
        'fumbles_lost': calc_fum_pts_loss
    }

def calc_plyr_weeks(games):
    'Generates a list of weeks played from a list of games'

    return [game.week for game in games]
