from __future__ import division
import stat_utils as util
from nfl_db_query import NflDbQuery
from player import Player

class NflStats():
    def __init__(self, nfl_year):
        self.query = NflDbQuery(nfl_year)


    def generate_position_stats(self, position):
        'Generates a list of player objects by position'
        stats = self.query.aggregrate_position_stats(position.type,
                                                     position.sample_size,
                                                     position.sort_by_category,
                                                     util.full_weeks)

        plyr_list = []
        for plyr in stats:
            plyr_info = self._generate_plyr_info(plyr,
                                                 position.sample_size,
                                                 position.sort_by_category)
            plyr_list.append(plyr_info)

        return plyr_list


    def _generate_plyr_info(self, plyr, sample_size, sort_by_category):
        'Generates a player object and associated core stats'
        player = Player(plyr.player_id, plyr.player)

        # query player game weeks
        weeks = util.full_weeks
        full_games = self.query.aggregate_plyr_games(player.id, weeks)
        plyr_full_aggregate = self.query.aggregate_plyr_stats(player.id,
                                                              sample_size,
                                                              sort_by_category,
                                                              weeks)
        player.add_stats('full', plyr_full_aggregate)

        # query player stats (weeks 1-8)
        weeks = util.beg_weeks
        beg_games = self.query.aggregate_plyr_games(player.id, weeks)
        plyr_beg_aggregate = self.query.aggregate_plyr_stats(player.id,
                                                             sample_size,
                                                             sort_by_category,
                                                             weeks)
        player.add_stats('beg', plyr_beg_aggregate)

        # query player stats (weeks 8-16)
        weeks = util.end_weeks
        end_games = self.query.aggregate_plyr_games(player.id, weeks)
        plyr_end_aggregate = self.query.aggregate_plyr_stats(player.id,
                                                             sample_size,
                                                             sort_by_category,
                                                             weeks)
        player.add_stats('end', plyr_end_aggregate)

        # calculate player fantasy points
        full_pts = player.get_points_segment('full')
        beg_pts = player.get_points_segment('beg')
        end_pts = player.get_points_segment('end')

        # total weeks, 1-8 weeks, 9-16 weeks played
        full_weeks = util.calc_plyr_weeks(full_games)
        full_weeks_played = len(full_weeks)
        beg_weeks = util.calc_plyr_weeks(beg_games)
        beg_weeks_played = len(beg_weeks)
        end_weeks = util.calc_plyr_weeks(end_games)
        end_weeks_played = len(end_weeks)

        full_avg_pts = (full_pts / full_weeks_played) if full_pts > 0 else 0
        beg_avg_pts = (beg_pts / beg_weeks_played) if beg_pts > 0 else 0
        end_avg_pts = (end_pts / end_weeks_played) if end_pts > 0 else 0
        availability = (full_weeks_played / 15) if full_weeks_played > 0 else 0

        print 'Name: %s, Pts %d %.1f' % (plyr.player, full_pts, full_avg_pts)

        return {
            'id': player.id,
            'name': player.name,
            'weeks': full_weeks_played,
            'pts': full_pts,
            'avg_pts': full_avg_pts,
            'beg_pts': beg_pts,
            'beg_avg_pts': beg_avg_pts,
            'end_pts': end_pts,
            'end_avg_pts': end_avg_pts,
            'availability': availability
        }
