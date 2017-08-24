# mutscraper

Dependencies:
bs4 (pip install bs4)

To invoke from command line, use the following syntax:

python mutscraper.py <b>xbox-one|playstation-4|all</b> <i>list of team names, comma separated, no spaces (use <b>all</b> instead for all teams)</i> minimum_overall maximum_overall

Example, to see all team silvers for Xbox for the Giants and Patriots with ovr 60-64:

python mutscraper.py xbox-one giants,patriots 60 64
