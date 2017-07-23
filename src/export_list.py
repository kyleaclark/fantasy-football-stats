import csv
import json
from collections import OrderedDict

def export_to_json(output_year, player_list, position_type):
    # TODO: Make the year configurable throughout the application
    name = '%d_%s' % (output_year, position_type)
    fileName = name + '.json'

    players = []
    for index, plyr in enumerate(player_list):
        player = dict(plyr)
        player['player'] = str(plyr['name'])
        del player['name']
        players.append(player)

    output = OrderedDict([ ('_id', name), ('year', output_year), ('position', position_type), ('data', players) ])

    with open(fileName, 'w') as outfile:
        json.dump(output, outfile)

def export_to_csv(player_list, file_name):
    'Exports a list of player dicts into a csv file'

    with open(file_name, 'w') as csvfile:
        fieldnames = [
            'Player',
            'Total Pts',
            'Avg Pts',
            'Auction Value',
            'Availability',
            '+/-',
            '+/- median',
            '+/- top qtr',
            '1-8 +/-',
            '1-8 +/- median',
            '1-8 +/- top qtr',
            '9-16 +/-',
            '9-16 +/- median',
            '9-16 +/- top qtr'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for index, plyr in enumerate(player_list):
            writer.writerow({
                'Player': plyr['name'],
                'Total Pts': '{0:.1f}'.format(plyr['pts']),
                'Avg Pts': '{0:.1f}'.format(plyr['avg_pts']),
                'Auction Value': '{0:.1f}'.format(plyr['auction_value']),
                'Availability': '{0:.1f}'.format(plyr['availability']),
                '+/-': '{0:.1f}'.format(plyr['plus_minus']),
                '+/- median': '{0:.1f}'.format(plyr['points_above_median']),
                '+/- top qtr': '{0:.1f}'.format(plyr['points_above_top_qtr']),
                '1-8 +/-': '{0:.1f}'.format(plyr['beg_plus_minus']),
                '1-8 +/- median': '{0:.1f}'.format(plyr['beg_points_above_median']),
                '1-8 +/- top qtr': '{0:.1f}'.format(plyr['beg_points_above_top_qtr']),
                '9-16 +/-': '{0:.1f}'.format(plyr['end_plus_minus']),
                '9-16 +/- median': '{0:.1f}'.format(plyr['end_points_above_median']),
                '9-16 +/- top qtr': '{0:.1f}'.format(plyr['end_points_above_top_qtr'])
            })
