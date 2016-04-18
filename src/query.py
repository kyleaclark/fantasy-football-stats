import nfldb

def init():
    'Initialize nfldb connection'

    global db

    db = nfldb.connect()

def generate_query(opts):
    'Generate a base query to the NFLDB'

    weeks = opts.get('weeks', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    season_year = opts.get('season_year', 2015)
    season_type = opts.get('season_type', 'Regular')

    query = nfldb.Query(db)
    query.game(season_year=season_year, season_type=season_type, week=weeks)

    return query

def aggregrate_position_stats(params):
    'Aggregates a query of stats by position'

    query = generate_query(params)

    return query.sort(params['sortBy']).player(position=params['position']).limit(params['sample_size']).as_aggregate()

def aggregate_plyr_games(plyr_id, params):
    'Aggregrates a query of games by player'

    query = generate_query(params)

    return query.sort('week').player(player_id=plyr_id).as_games()

def aggregate_plyr_stats(plyr_id, params):
    'Aggregrates a query of stats by player'

    query = generate_query(params)

    return query.sort(params['sortBy']).player(player_id=plyr_id).limit(params['sample_size']).as_aggregate()
