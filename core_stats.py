import query
import stat_utils as util
import advanced_stats
import fantasy_pts

def generate_position_stats(plyr_list, config):
    stats = query.aggregrate_position_stats(config)

    for plyr in stats:
        plyr_list.append(generate_plyr_obj(plyr, config))

    plyr_list.sort(key=lambda full_pts: full_pts, reverse=True)

    advanced_stats.calc_position_stats(plyr_list, config['sample_size'], config['sample_trim'])

def calc_plyr_weeks(games):
    weeks = []

    for game in games:
        weeks.append(game.week)

    return weeks

def generate_plyr_obj(plyr, config):
    plyr_id = plyr.player_id

    # query player game weeks
    full_games = query.aggregate_plyr_games(plyr_id, config)

    # query player stats (weeks 1-8)
    config['weeks'] = util.fantasy_beg_weeks()
    beg_games = query.aggregate_plyr_games(plyr_id, config)
    plyr_beg_stats = query.aggregate_plyr_stats(plyr_id, config)[0]

    # calculate player fantasy points
    full_pts = config['calc_fantasy_stats'](plyr)
    beg_pts = config['calc_fantasy_stats'](plyr_beg_stats)

    # total weeks, 1-8 weeks, 9-16 weeks played
    full_weeks = calc_plyr_weeks(full_games)
    full_weeks_played = len(full_weeks)
    beg_weeks = calc_plyr_weeks(beg_games)
    beg_weeks_played = len(beg_weeks)

    full_avg_pts = full_pts / full_weeks_played
    beg_avg_pts = beg_pts / beg_weeks_played
    health = (full_weeks_played / 15) * 100

    print 'Name: %s, Pts %d, Start Pts %d' % (plyr.player, full_pts, beg_pts)

    return {
        'id': plyr_id,
        'name': plyr.player,
        'weeks': full_weeks_played,
        'pts': full_pts,
        'avg_pts': full_avg_pts,
        'beg_pts': beg_pts,
        'beg_avg_pts': beg_avg_pts,
        'health': health
    }
