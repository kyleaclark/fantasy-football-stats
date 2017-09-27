import pandas as pd

csv_column_map = {
    'Player': 'Player',
    'Total Pts': 'TotalPts',
    'Avg Pts': 'PtsPpg',
    'Auction Value': 'AuctionValue',
    'Availability': 'Availability',
    '+/-': 'PlusMinus',
    '+/- median': None,
    '+/- top qtr': None,
    '1-8 +/-': 'FirstHalfPlusMinus',
    '1-8 +/- median': None,
    '1-8 +/- top qtr': None,
    '9-16 +/-': 'SecondHalfPlusMinus',
    '9-16 +/- median': None,
    '9-16 +/- top qtr': None
}

column_names = [
    'TotalPts',
    'PtsPpg',
    'Availability',
    'PlusMinus',
    'FirstHalfPlusMinus',
    'SecondHalfPlusMinus'
]

# player
# prior_year_auction_value
# prior_year_total_pts
# prior_year_avg_pts
# prior_year_availability
# career_mean_auction_value
# career_mean_total_pts
# career_mean_pts_ppg
# career_mean_availability

rb_2016 = pd.read_csv('../../output/2016/2016_rb.csv')
auction_rb_df = pd.DataFrame(data=None, index=None, columns=None)

for column in rb_2016:
    column_name = csv_column_map[column]
    if column_name == 'Player' or column_name == 'TotalPts':
        auction_rb_df[column_name] = rb_2016[column]

auction_rb_df['Position'] = 'rb'

# rb_2016 = pd.read_csv('../../output/2016/2016_rb.csv')
# auction_rb_df = pd.DataFrame(data=None, index=None, columns=None)
# for column in rb_2016:
#     column_name = csv_column_map[column]
#     if column_name == 'Player':
#         auction_rb_df[column_name] = rb_2016[column]
#     elif column_name == 'AuctionValue':
#         auction_rb_df[column_name] = rb_2016[column]

#auction_rb_df['Position'] = 'rb'

###########

positions = ['rb']
years = ['2015', '2014', '2013', '2012', '2011', '2010', '2009']

career_dfs = []
for position in positions:
    for year in years:
        position_year_name = position + '_' + year
        csv_df = pd.read_csv('../../output/%s/%s_%s.csv' % (year, year, position))
        pos_yr_df = pd.DataFrame(data=None, index=None, columns=None)

        for column in csv_df:
            column_name = csv_column_map[column]

            if column_name == None:
                continue

            if column_name != 'Player':
                if year == years[0]:
                    prior_year_column_name = position + '_PriorYear_' + column_name
                    pos_yr_df[prior_year_column_name] = csv_df[column]

                column_name = position + '_' + year + '_' + column_name

            pos_yr_df[column_name] = csv_df[column]

        career_dfs.append(pos_yr_df)

# rb_2015 = pd.read_csv('../../output/2015/2015_rb.csv')
# df_2015 = pd.DataFrame(data=None, index=None, columns=None)
#
# for column in rb_2015:
#     column_name = csv_column_map[column]
#
#     if column_name == None:
#         continue
#
#     if column_name != 'Player':
#         prior_year_column_name = 'PriorYear_' + column_name
#         df_2015[prior_year_column_name] = rb_2015[column]
#         column_name = '2015_' + column_name
#
#     df_2015[column_name] = rb_2015[column]
#
#
# rb_2014 = pd.read_csv('../../output/2014/2014_rb.csv')
# df_2014 = pd.DataFrame(data=None, index=None, columns=None)
#
# for column in rb_2014:
#     column_name = csv_column_map[column]
#
#     if column_name == None:
#         continue
#
#     if column_name != 'Player':
#         column_name = '2014_' + column_name
#
#     df_2014[column_name] = rb_2014[column]
#
# rb_2013 = pd.read_csv('../../output/2015/2015_rb.csv')
# df_2013 = pd.DataFrame(data=None, index=None, columns=None)
#
# for column in rb_2013:
#     column_name = csv_column_map[column]
#
#     if column_name == None:
#         continue
#
#     if column_name != 'Player':
#         column_name = '2013_' + column_name
#
#     df_2013[column_name] = rb_2013[column]
#
# df_2014 = df_2015.merge(df_2014, on='Player', how='outer')
# career_df = df_2014.merge(df_2013, on='Player', how='outer')
#
#
# print (career_df['CareerMean_TotalPts'])

output_df = career_dfs.pop(0)

for df in career_dfs:
    output_df = output_df.merge(df, on='Player', how='outer')

for column_name in column_names:
    cn_prior = 'PriorYear_' + column_name
    cn_career = 'CareerMean_' + column_name

    cn_prior_list = []
    cn_career_list = []
    for position in positions:
        cn_prior_list.append((position + '_PriorYear_' + column_name))

        for year in years:
            cn_career_list.append((position + '_' + year + '_' + column_name))

    output_df[cn_prior] = output_df[cn_prior_list].mean(axis=1)
    output_df[cn_career] = output_df[cn_career_list].mean(axis=1)

    for cn_item in cn_prior_list:
        del output_df[cn_item]

    for cn_item in cn_career_list:
        del output_df[cn_item]

#auction_df = auction_rb_df.merge(auction_rb_df, on=['Player', 'Position', 'AuctionValue'], how='outer')
auction_df = auction_rb_df
output_df = auction_df.merge(output_df, on='Player', how='outer')

# output_df = auction_df.merge(career_df, on='Player', how='outer')
# output_df = output_df[pd.notnull(output_df['AuctionValue'])]
output_df = output_df[pd.notnull(output_df['CareerMean_TotalPts'])]
output_df = output_df.fillna(value=0)

output_df.to_csv('fantasy_data3.csv', index=False)
