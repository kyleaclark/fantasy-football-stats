from __future__ import division

full_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
beg_weeks = [1, 2, 3, 4, 5, 6, 7, 8]
end_weeks = [9, 10, 11, 12, 13, 14, 15, 16]

def calc_pass_yd_pts(yds):
    'Calculate passing yard points'
    return yds / 25

def calc_pass_td_pts(tds):
    'Caulculate passing td points'
    return tds * 4

def calc_reg_yd_pts(yds):
    'Calculate regular yard points'
    return yds / 10

def calc_reg_td_pts(tds):
    'Calculate regular td points'
    return tds * 6

def calc_int_pts_loss(ints):
    'Calculate int points loss'
    return ints * -2

def calc_fum_pts_loss(fums):
    'Calculate fumble points loss'
    return fums * -2

def fantasy_full_weeks():
    'Returns list of full fantasy weeks 1-16'
    return full_weeks

def fantasy_beg_weeks():
    'Returns list of beginning fantasy weeks 1-8'
    return beg_weeks

def fantasy_end_weeks():
    'Returns list of end fantasy weeks 9-16'
    return end_weeks
