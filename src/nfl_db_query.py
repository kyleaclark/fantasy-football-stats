import nfldb

class NflDbQuery():
    def __init__(self, nfl_year):
        'Initialize nfldb connection'

        self.nfl_year = nfl_year
        self.db = nfldb.connect()


    def _generate_query(self, weeks):
        'Generate a base query to the NFLDB'

        query = nfldb.Query(self.db)
        query.game(season_year=self.nfl_year, season_type='Regular', week=weeks)

        return query


    def aggregrate_position_stats(self, position_type, sample_size,
                                  sort_by_category, weeks):
        'Aggregates a query of stats by position'

        query = self._generate_query(weeks)
        return query.sort(sort_by_category).player(
            position=position_type).limit(sample_size).as_aggregate()


    def aggregate_plyr_games(self, plyr_id, weeks):
        'Aggregrates a query of games by player'

        query = self._generate_query(weeks)
        return query.sort('week').player(player_id=plyr_id).as_games()


    def aggregate_plyr_stats(self, plyr_id, sample_size, sort_by_category,
                             weeks):
        'Aggregrates a query of stats by player'

        query = self._generate_query(weeks)
        return query.sort(sort_by_category).player(player_id=plyr_id).limit(sample_size).as_aggregate()
