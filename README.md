# fantasy-football-stats
A python program to calculate player comparison fantasy football stats.

### The mean for a position group is calculated using only the middle 80% of player values (removing the top 10% and bottom 10% per standard population statistic calculations). The program exports CSV files for the position groups QB, RB, WR, TE with the following fields:

* Player name
* Total points (weeks 1-16)
* Avg points per game (weeks 1-16)
* Avg value (average of +/- above median for wks 1-16, wks 1-8, wks 9-16 scaled by availability w/ a multiplier of 10)
* Availability (percentage of number of 2014 games played)
* +/- above the position mean (weeks 1-16)
* +/- above the position median (weeks 1-16)
* +/- above the top quarter (weeks 1-16)
* +/- above the position mean (weeks 1-8)
* +/- above the position median (weeks 1-8)
* +/- above the top quarter (weeks 1-8)
* +/- above the position mean (weeks 9-16)
* +/- above the position median (weeks 9-16)
* +/- above the top quarter (weeks 9-16)

Note 1: Calculations are based on weeks 1-16 with week 17 discarded, as the last week is commonly not apart of the fantasy season or playoffs.
Note 2: The CSV file may be imported into a spreadsheet program (i.e. Google Sheets) to be converted into a user-friendly format for analysis.

### Credit:
Full credit is given to the author, BurntSushi, of nfldb located at https://github.com/BurntSushi/nfldb. The nfldb python module provides a database of NFL statistics gathered via NFL gamecenter json data and an API query to interface with the data.
