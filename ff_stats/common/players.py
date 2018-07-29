from ff_stats.common.player import Player


class Players(object):

    def __init__(self, nfldb_client):
        self.nfldb_client = nfldb_client
        self.container = {}

    def compute_player_stats_by_category(self, sample_size, stats_category, nfl_year, weeks):
        player_objs = self.nfldb_client.aggregrate_category_stats(sample_size, stats_category, nfl_year, weeks)

        for player_obj in player_objs:
            player = self.generate_player(player_obj)
            player.compute_stats(player_obj, nfl_year)

    def generate_player(self, player_obj):
        player_id = player_obj.player_id

        if player_id not in self.container:
            self.container[player_id] = Player(player_obj)

        return self.container[player_id]
