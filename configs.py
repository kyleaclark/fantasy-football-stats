import stat_utils as util
import fantasy_pts

def trim():
    return .1

def qb():
    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'QB',
        'sortBy': 'passing_yds',
        'sample_size': 20,
        'sample_trim': 20 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_qb
    }
