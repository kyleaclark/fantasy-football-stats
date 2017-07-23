# fantasy-football-stats
A python program to calculate player comparison fantasy football stats.

The mean for a position group is calculated using only the middle 80% of player values (removing the top 10% and bottom 10% per standard population statistic calculations). The program exports CSV files for the position groups QB, RB, WR, TE with the fields noted below.

* Player name
* Total points (weeks 1-16)
* Avg points per game (weeks 1-16)
* Auction value (relative positional median value times relative positional top qtr value then squared and scaled by availability)
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

#### Breakdown of the latest auction value formula:

1. relative positional median value - a player's average points scored per game divided by the median of average points scored per game cumulative for a position

2. relative positional top quarter value - a player's average points scored per game divided by the top quarter median of average points scored per game cumulative for a position

3. multiplied value of relative positional median & top quarter value - relative positional median value multiplied by relative positional top quarter value

4. squared value of the multiplied value - squared value of the multiple of relative positional median & top quarter value

5. squared value scaled by availability - squared value of the multiple of relative positional median & top quarter value, then scaled by the percentage of games a player played in weeks 1 through 16

Note: Power Ranking has an applied floor value of 0 for a 0-100 rating system.

--

Note 1: Execute in the terminal via `python init.py 2016` in the `src` directory (requires python 2.7 and [nfldb](https://github.com/BurntSushi/nfldb) module)

Note 2: Calculations are based on weeks 1-16 with week 17 discarded, as the last week is commonly not apart of the fantasy season or playoffs.

Note 3: The CSV file may be imported into a spreadsheet program (i.e. Google Sheets) to be converted into a user-friendly format for analysis. Find the CSV files without executing the program inside the `csv` directory.

### Credit:
Full credit is given to the author, BurntSushi, of nfldb located at https://github.com/BurntSushi/nfldb. The nfldb python module provides a database of NFL statistics gathered via NFL gamecenter json data and an API query to interface with the data.
