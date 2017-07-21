class FantasyStats():

    def __init__(self, stats):
        self.passing_yds = stats.passing_yds or 0
        self.passing_tds = stats.passing_tds or 0
        self.passing_int = stats.passing_int or 0
        self.rushing_yds = stats.rushing_yds or 0
        self.rushing_tds = stats.rushing_tds or 0
        self.receiving_yds = stats.receiving_yds or 0
        self.receiving_tds = stats.receiving_tds or 0
        self.fumbles_lost = stats.fumbles_lost or 0


    def calc_fantasy_points(self):
        'Calculates fantasy points by a rb, wr, or te'

        # TODO: Make fantasy point values configurable
        self.passing_yd_pts = self.passing_yds * 25
        self.passing_td_pts = self.passing_tds * 4
        self.passing_int_pts = self.passing_int * -2
        self.rushing_yds_pts = self.rushing_yds * 10
        self.rushing_tds_pts = self.rushing_tds * 6
        self.receiving_yds_pts = self.receiving_yds * 10
        self.receiving_tds_pts = self.receiving_tds * 6
        self.fumbles_lost_pts = self.fumbles_lost * -2
