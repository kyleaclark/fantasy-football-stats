from past_performance import export_list
from ff_stats.summary_stats import SummaryStats

class StatsCommunicator():

    def __init__(self, nfl_stats, position, output_year):
        self.nfl_stats = nfl_stats
        self.position = position
        self.output_year = output_year

    def generate_stats(self):
        players_stats = self.nfl_stats.generate_position_stats(self.position, self.output_year)

        self.summary_stats = SummaryStats(players_stats,
                                          self.position.cost_baseline,
                                          self.position.sample_size,
                                          self.position.sample_trim)
        self.summary_stats.calc_position_summary_stats()
        self.summary_stats.calc_players_summary_stats()


    def export_stats(self):
        players_stats = self.summary_stats.players_stats
        position_type = self.position.type.lower()

        export_list.export_to_json(self.output_year, players_stats, position_type)

        export_list.export_to_csv(players_stats, ('%d_%s.csv' % (self.output_year,
                                                                 position_type)))
