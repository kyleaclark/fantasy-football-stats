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
        'cost_baseline': 14,
        'sortBy': 'passing_yds',
        'sample_size': 20,
        'sample_trim': 20 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_qb,
        'generate_plyr_stats_dict': fantasy_pts.generate_qb_plyr_stats_dict,
        'generate_plyr_default_dict': fantasy_pts.generate_qb_plyr_default_dict
    }

def rb():
    'Generates a base qb configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'RB',
        'cost_baseline': 16,
        'sortBy': 'rushing_yds',
        'sample_size': 30,
        'sample_trim': 30 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr,
        'generate_plyr_stats_dict': fantasy_pts.generate_pos_plyr_stats_dict,
        'generate_plyr_default_dict': fantasy_pts.generate_pos_plyr_default_dict
    }

def wr():
    'Generates a base wr configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'WR',
        'cost_baseline': 18,
        'sortBy': 'receiving_yds',
        'sample_size': 40,
        'sample_trim': 40 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr,
        'generate_plyr_stats_dict': fantasy_pts.generate_pos_plyr_stats_dict,
        'generate_plyr_default_dict': fantasy_pts.generate_pos_plyr_default_dict
    }

def te():
    'Generates a base te configuration'

    return {
        'weeks': util.fantasy_full_weeks(),
        'position': 'TE',
        'cost_baseline': 8,
        'sortBy': 'receiving_yds',
        'sample_size': 20,
        'sample_trim': 20 * trim(),
        'calc_fantasy_stats': fantasy_pts.calc_pos_plyr,
        'generate_plyr_stats_dict': fantasy_pts.generate_pos_plyr_stats_dict,
        'generate_plyr_default_dict': fantasy_pts.generate_pos_plyr_default_dict
    }
