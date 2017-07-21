import stat_utils as util

# TODO: Centralize qb stat categories in a separate module
qb_plyr_categories = [
    'rushing_yds',
    'rushing_tds',
    'passing_yds',
    'passing_tds',
    'passing_int',
    'fumbles_lost'
]

# TODO: Centralize qb stat categories in a separate module
pos_plyr_categories = [
    'rushing_yds',
    'rushing_tds',
    'receiving_yds',
    'receiving_tds',
    'fumbles_lost'
]

qb_plyr_stat_methods = util.qb_plyr_methods()
pos_plyr_stat_methods = util.pos_plyr_methods()

def calc_qb(plyr_dict):
    'Calculates fantasy points by a qb'

    qb_plyr_pts = {category:qb_plyr_stat_methods[category](stat) for category, stat in plyr_dict.iteritems()}

    return sum(qb_plyr_pts.itervalues())

# TODO: consolidate all of these dict keys to be dynamic (possibly move into separate module)
def generate_qb_plyr_stats_dict(plyr_stats):
    return {
        'rushing_yds': plyr_stats.rushing_yds or 0,
        'rushing_tds': plyr_stats.rushing_tds or 0,
        'passing_yds': plyr_stats.passing_yds or 0,
        'passing_tds': plyr_stats.passing_tds or 0,
        'passing_int': plyr_stats.passing_int or 0,
        'fumbles_lost': plyr_stats.receiving_tds or 0
    }

def generate_qb_plyr_default_dict():
    return {category:0 for category in qb_plyr_categories}

def calc_pos_plyr(plyr_dict):
    'Calculates fantasy points by a rb, wr, or te'

    pos_plyr_pts = {category:pos_plyr_stat_methods[category](stat) for category, stat in plyr_dict.iteritems()}

    return sum(pos_plyr_pts.itervalues())

# TODO: consolidate all of these dict keys to be dynamic (possibly move into separate module)
def generate_pos_plyr_stats_dict(plyr_stats):
    return {
        'rushing_yds': plyr_stats.rushing_yds or 0,
        'rushing_tds': plyr_stats.rushing_tds or 0,
        'receiving_yds': plyr_stats.receiving_yds or 0,
        'receiving_tds': plyr_stats.receiving_tds or 0,
        'fumbles_lost': plyr_stats.receiving_tds or 0
    }

def generate_pos_plyr_default_dict():
    return {category:0 for category in pos_plyr_categories}
