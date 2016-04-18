from __future__ import division
import query
import stat_utils as util
import advanced_stats
import fantasy_pts

def generate_position_stats(plyr_list, config):
    'Generates a list of player objects by position'
    stats = query.aggregrate_position_stats(config)

    for plyr in stats:
        plyr_list.append(generate_plyr_info(plyr, config))

    advanced_stats.calc_position_stats(plyr_list, config['sample_size'], config['sample_trim'])

def calc_plyr_weeks(games):
    'Generates a list of weeks played from a list of games'
    weeks = []

    for game in games:
        weeks.append(game.week)

    return weeks

def generate_plyr_info(plyr, config):
    'Generates a player object and associated core stats'
    plyr_id = plyr.player_id

    # query player game weeks
    config['weeks'] = util.fantasy_full_weeks()
    full_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_full_aggregate = query.aggregate_plyr_stats(plyr_id, config)
    if plyr_full_aggregate:
        plyr_full_dict = config['generate_plyr_stats_dict'](plyr_full_aggregate[0])
    else:
        plyr_full_dict = config['generate_plyr_default_dict']()

    # query player stats (weeks 1-8)
    config['weeks'] = util.fantasy_beg_weeks()
    beg_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_beg_aggregate = query.aggregate_plyr_stats(plyr_id, config)
    if plyr_beg_aggregate:
        plyr_beg_dict = config['generate_plyr_stats_dict'](plyr_beg_aggregate[0])
    else:
        plyr_beg_dict = config['generate_plyr_default_dict']()

    # query player stats (weeks 8-16)
    config['weeks'] = util.fantasy_end_weeks()
    end_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_end_aggregate = query.aggregate_plyr_stats(plyr_id, config)
    if plyr_end_aggregate:
        plyr_end_dict = config['generate_plyr_stats_dict'](plyr_end_aggregate[0])
    else:
        plyr_end_dict = config['generate_plyr_default_dict']()

    # calculate player fantasy points
    # TODO: better naming convention than config to indicate dynamic methods in object
    full_pts = config['calc_fantasy_stats'](plyr_full_dict)
    beg_pts = config['calc_fantasy_stats'](plyr_beg_dict)
    end_pts = config['calc_fantasy_stats'](plyr_end_dict)

    # total weeks, 1-8 weeks, 9-16 weeks played
    full_weeks = calc_plyr_weeks(full_games)
    full_weeks_played = len(full_weeks)
    beg_weeks = calc_plyr_weeks(beg_games)
    beg_weeks_played = len(beg_weeks)
    end_weeks = calc_plyr_weeks(end_games)
    end_weeks_played = len(end_weeks)

    full_avg_pts = (full_pts / full_weeks_played) if full_pts > 0 else 0
    beg_avg_pts = (beg_pts / beg_weeks_played) if beg_pts > 0 else 0
    end_avg_pts = (end_pts / end_weeks_played) if end_pts > 0 else 0
    availability = (full_weeks_played / 15) if full_weeks_played > 0 else 0

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
