from __future__ import division


class FantasyStats():

    def __init__(self, stats):
        self.stats = stats


    def calc_fantasy_points(self):
        'Calculates fantasy points by a rb, wr, or te'

        # TODO: Make fantasy point values configurable
        if self.stats != None:
            self.passing_yds_pts = self.stats.passing_yds / 25
            self.passing_tds_pts = self.stats.passing_tds * 4
            self.passing_int_pts = self.stats.passing_int * -2
            self.rushing_yds_pts = self.stats.rushing_yds / 10
            self.rushing_tds_pts = self.stats.rushing_tds * 6
            self.receiving_yds_pts = self.stats.receiving_yds / 10
            self.receiving_tds_pts = self.stats.receiving_tds * 6
            self.fumbles_lost_pts = self.stats.fumbles_lost * -2
        else:
            self.passing_yds_pts = 0
            self.passing_tds_pts = 0
            self.passing_int_pts = 0
            self.rushing_yds_pts = 0
            self.rushing_tds_pts = 0
            self.receiving_yds_pts = 0
            self.receiving_tds_pts = 0
            self.fumbles_lost_pts = 0


    def get_fantasy_points(self):
        return (self.passing_yds_pts +
               self.passing_tds_pts +
               self.passing_int_pts +
               self.rushing_yds_pts +
               self.rushing_tds_pts +
               self.receiving_yds_pts +
               self.receiving_tds_pts +
               self.fumbles_lost_pts)
