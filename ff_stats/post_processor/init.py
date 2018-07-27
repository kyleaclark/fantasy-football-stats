import pandas as pd

csv_column_map = {
    'Player': 'Player',
    'Total Pts': 'TotalPts',
    'Avg Pts': 'AvgPts',
    'Auction Value': 'AuctionValue',
    'Availability': 'Availability',
    '+/-': 'PlusMinus',
    '+/- median': 'PlusMinusMedian',
    '+/- top qtr': 'PlusMinusTopQtr',
    '1-8 +/-': 'FirstHalfPlusMinus',
    '1-8 +/- median': 'FirstHalfPlusMinusMedian',
    '1-8 +/- top qtr': 'FirstHalfPlusMinusTopQtr',
    '9-16 +/-': 'SecondHalfPlusMinus',
    '9-16 +/- median': 'SecondHalfPlusMinusMedian',
    '9-16 +/- top qtr': 'SecondHalfPlusMinusTopQtr'
}

column_names = [
    'Player',
    'TotalPts',
    'AvgPts',
    'AuctionValue',
    'Availability',
    'PlusMinus',
    'PlusMinusMedian',
    'PlusMinusTopQtr',
    'FirstHalfPlusMinus',
    'FirstHalfPlusMinusMedian',
    'FirstHalfPlusMinusTopQtr',
    'SecondHalfPlusMinus',
    'SecondHalfPlusMinusMedian',
    'SecondHalfPlusMinusTopQtr'
]

qb_2015 = pd.read_csv('../../output/2015/2015_qb.csv')
df_2015 = pd.DataFrame(data=None, index=None, columns=None)

for column in qb_2015:
    column_name = csv_column_map[column]
    if column_name != 'Player':
        column_name = column_name + '_2015'

    df_2015[column_name] = qb_2015[column]


qb_2016 = pd.read_csv('../../output/2016/2016_qb.csv')
df_2016 = pd.DataFrame(data=None, index=None, columns=None)

for column in qb_2016:
    column_name = csv_column_map[column]
    if column_name != 'Player':
        column_name = column_name + '_2016'

    df_2016[column_name] = qb_2016[column]

df_2016 = df_2015.merge(df_2016, on='Player', how='outer')


qb_2017 = pd.read_csv('../../output/2017/2017_qb.csv')
df_2017 = pd.DataFrame(data=None, index=None, columns=None)

for column in qb_2017:
    column_name = csv_column_map[column]
    if column_name != 'Player':
        column_name = column_name + '_2017'

    df_2017[column_name] = qb_2017[column]

output = df_2016.merge(df_2017, on='Player', how='outer')

print (output['Player'])
