from __future__ import division


class FantasyStats(object):

    def __init__(self, nfldb_player):
        # TODO: Add functionality to make fantasy point values configurable
        self._compute_fantasy_stats(nfldb_player)
        self._compute_fantasy_points()

    def _compute_fantasy_stats(self, nfldb_player):
        self.passing_yds = nfldb_player.passing_yds
        self.passing_tds = nfldb_player.passing_tds
        self.passing_int = nfldb_player.passing_int
        self.rushing_yds = nfldb_player.rushing_yds
        self.rushing_tds = nfldb_player.rushing_tds
        self.receiving_yds = nfldb_player.receiving_yds
        self.receiving_tds = nfldb_player.receiving_tds
        self.fumbles_lost = nfldb_player.fumbles_lost

    def _compute_fantasy_points(self):
        """Calculates fantasy points by a rb, wr, or te"""

        self.passing_yds_pts = self.passing_yds / 25
        self.passing_tds_pts = self.passing_tds * 4
        self.passing_int_pts = self.passing_int * -2
        self.rushing_yds_pts = self.rushing_yds / 10
        self.rushing_tds_pts = self.rushing_tds * 6
        self.receiving_yds_pts = self.receiving_yds / 10
        self.receiving_tds_pts = self.receiving_tds * 6
        self.fumbles_lost_pts = self.fumbles_lost * -2

        self.total_fantasy_points = (self.passing_yds_pts +
                                     self.passing_tds_pts +
                                     self.passing_int_pts +
                                     self.rushing_yds_pts +
                                     self.rushing_tds_pts +
                                     self.receiving_yds_pts +
                                     self.receiving_tds_pts +
                                     self.fumbles_lost_pts)