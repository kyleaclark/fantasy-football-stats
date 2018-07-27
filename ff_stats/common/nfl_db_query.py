import nfldb


class NflDbQuery(object):

    def __init__(self):
        """Initialize nfldb connection"""

        self.db = nfldb.connect()

    def aggregrate_category_stats(self, sample_size, sort_by_category, nfl_year, weeks):
        """Aggregates a query of stats by category"""

        query = self._generate_query(nfl_year, weeks)
        return query.sort(sort_by_category).limit(sample_size).as_aggregate()

    def aggregrate_position_stats(self, position_type, sample_size, sort_by_category, nfl_year, weeks):
        """Aggregates a query of stats by category and position"""

        query = self._generate_query(nfl_year, weeks)
        return query.sort(sort_by_category).player(position=position_type).limit(sample_size).as_aggregate()

    def aggregate_plyr_games(self, plyr_id, nfl_year, weeks):
        """Aggregrates a query of games by player"""

        query = self._generate_query(nfl_year, weeks)
        return query.sort('week').player(player_id=plyr_id).as_games()

    def aggregate_plyr_stats(self, plyr_id, sample_size, sort_by_category, nfl_year, weeks):
        """Aggregrates a query of stats by player"""

        query = self._generate_query(nfl_year, weeks)
        return query.sort(sort_by_category).player(player_id=plyr_id).limit(sample_size).as_aggregate()

    def _generate_query(self, nfl_year, weeks, season_type='Regular'):
        """Generate a base query to the NFLDB"""

        query = nfldb.Query(self.db)
        query.game(season_year=nfl_year, season_type=season_type, week=weeks)

        return query
