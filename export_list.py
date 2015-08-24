import csv

qb_limit = 20
rb_limit = 40
wr_limit = 50
te_limit = 20
k_limit = 20
def_limit = 20

def export(player_list):
    with open('qbs.csv', 'w') as csvfile:
        fieldnames = ['Name', 'Avg pts per game', '+/-', '+/- replacement', '+/- median starter', 'beg +/-', 'beg +/- replacement', 'beg +/- median starter', 'health']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for index, plyr in enumerate(player_list):
            if (plyr['plus_minus'] > 0):
                writer.writerow({
                    'Name': plyr['name'],
                    'Avg pts per game': '{0:.1f}'.format(plyr['avg_pts']),
                    '+/-': '{0:.1f}'.format(plyr['plus_minus']),
                    '+/- replacement': '{0:.1f}'.format(plyr['points_above_replacement']),
                    '+/- median starter': '{0:.1f}'.format(plyr['points_above_median_starter']),
                    'beg +/-': '{0:.1f}'.format(plyr['beg_plus_minus']),
                    'beg +/- replacement': '{0:.1f}'.format(plyr['beg_points_above_replacement']),
                    'beg +/- median starter': '{0:.1f}'.format(plyr['beg_points_above_median_starter']),
                    'health': plyr['health']
                })
