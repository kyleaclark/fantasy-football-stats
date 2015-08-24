from __future__ import division

# Calculate regular yard points
def calc_reg_yd_pts(yds):
    return yds / 10

# Calculate regular td points
def calc_reg_td_pts(tds):
    return tds * 6

# Calculate passing yard points
def calc_pass_yd_pts(yds):
    return yds / 25

# Caulculate passing td points
def calc_pass_td_pts(tds):
    return tds * 4

# Calculate int points loss
def calc_int_pts_loss(ints):
    return ints * -2

# Calculate fumble points loss
def calc_fum_pts_loss(fums):
    return fums * -2

def fantasy_full_weeks():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def fantasy_beg_weeks():
    return [1, 2, 3, 4, 5, 6, 7, 8]

def fantasy_end_weeks():
    return [9, 10, 11, 12, 13, 14, 15, 16]
