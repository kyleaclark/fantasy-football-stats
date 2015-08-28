from __future__ import division
import query
import stat_utils as util
import advanced_stats
import fantasy_pts

def generate_position_stats(plyr_list, config):
    'Generates a list of player objects by position'
    stats = query.aggregrate_position_stats(config)

    for plyr in stats:
        plyr_list.append(generate_plyr_obj(plyr, config))

    advanced_stats.calc_position_stats(plyr_list, config['sample_size'], config['sample_trim'])

def calc_plyr_weeks(games):
    'Generates a list of weeks played from a list of games'
    weeks = []

    for game in games:
        weeks.append(game.week)

    return weeks

def generate_plyr_obj(plyr, config):
    'Generates a player object and associated core stats'
    plyr_id = plyr.player_id

    # query player game weeks
    config['weeks'] = util.fantasy_full_weeks()
    full_games = query.aggregate_plyr_games(plyr_id, config)

    # query player stats (weeks 1-8)
    config['weeks'] = util.fantasy_beg_weeks()
    beg_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_beg_stats = query.aggregate_plyr_stats(plyr_id, config)[0]

    # query player stats (weeks 8-16)
    config['weeks'] = util.fantasy_end_weeks()
    end_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_end_stats = query.aggregate_plyr_stats(plyr_id, config)[0]

    # calculate player fantasy points
    full_pts = config['calc_fantasy_stats'](plyr)
    beg_pts = config['calc_fantasy_stats'](plyr_beg_stats)
    end_pts = config['calc_fantasy_stats'](plyr_end_stats)

    # total weeks, 1-8 weeks, 9-16 weeks played
    full_weeks = calc_plyr_weeks(full_games)
    full_weeks_played = len(full_weeks)
    beg_weeks = calc_plyr_weeks(beg_games)
    beg_weeks_played = len(beg_weeks)
    end_weeks = calc_plyr_weeks(end_games)
    end_weeks_played = len(end_weeks)

    full_avg_pts = full_pts / full_weeks_played
    beg_avg_pts = beg_pts / beg_weeks_played
    end_avg_pts = end_pts / end_weeks_played
    availability = (full_weeks_played / 15)

    print 'Name: %s, Pts %d %.1f' % (plyr.player, full_pts, full_avg_pts)

    return {
        'id': plyr_id,
        'name': plyr.player,
        'weeks': full_weeks_played,
        'pts': full_pts,
        'avg_pts': full_avg_pts,
        'beg_pts': beg_pts,
        'beg_avg_pts': beg_avg_pts,
        'end_pts': end_pts,
        'end_avg_pts': end_avg_pts,
        'availability': availability
    }
