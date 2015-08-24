import stat_utils as util

def calc_qb(p):
    rushing_yds = util.calc_reg_yd_pts(p.rushing_yds)
    rushing_tds = util.calc_reg_td_pts(p.rushing_tds)
    passing_yds = util.calc_pass_yd_pts(p.passing_yds)
    passing_tds = util.calc_pass_td_pts(p.passing_tds)
    passing_int = util.calc_int_pts_loss(p.passing_int)
    fumbles_lost = util.calc_fum_pts_loss(p.fumbles_lost)

    return rushing_yds + rushing_tds + passing_yds + passing_tds + fumbles_lost + passing_int

def calc_pos_plyr(p):
    rushing_yds = util.calc_reg_yd_pts(p.rushing_yds)
    rushing_tds = util.calc_reg_td_pts(p.rushing_tds)
    receiving_yds = util.calc_pass_yd_pts(p.receiving_yds)
    receiving_tds = util.calc_pass_td_pts(p.receiving_tds)
    fumbles_lost = util.calc_fum_pts_loss(p.fumbles_lost)

    return rushing_yds + rushing_tds + receiving_yds + receiving_tds + fumbles_lost
