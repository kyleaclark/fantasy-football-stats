import csv

def export(player_list, file_name):
    'Exports a list of player dicts into a csv file'

    with open(file_name, 'w') as csvfile:
        fieldnames = [
            'Player',
            'Total Pts',
            'Avg Pts',
            'Avg Value',
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
                'Avg Value': '{0:.1f}'.format(plyr['avg_value']),
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
