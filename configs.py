import stat_utils as util
import fantasy_pts

def trim():
    'Generates a percentage to trim off a sample size from the top and bottom'

    return .1

def qb():
    'Generates a base qb configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'QB',
        'sortBy': 'passing_yds',
        'sample_size': 20,
        'sample_trim': 20 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_qb
    }

def rb():
    'Generates a base qb configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'RB',
        'sortBy': 'rushing_yds',
        'sample_size': 30,
        'sample_trim': 30 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr
    }

def wr():
    'Generates a base wr configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'WR',
        'sortBy': 'receiving_yds',
        'sample_size': 40,
        'sample_trim': 40 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr
    }

def te():
    'Generates a base te configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'TE',
        'sortBy': 'receiving_yds',
        'sample_size': 20,
        'sample_trim': 20 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr
    }
