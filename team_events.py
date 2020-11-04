import pandas as pd
import time
import itertools
from event_info import Full_Seeds_Pools_Info, Full_Bracket_Info, Soup_Objects, accumulate, defaultdict, Counter
from standings_parser import Full_Standings

class Team_Events:
    def __init__(self):
        self.teams = Full_Seeds_Pools_Info().event_teams()
        self.seeds = Full_Seeds_Pools_Info().full_seeds()
        self.standings = Full_Standings().standings_dicts()
        self.event_names = Soup_Objects.event_names
        self.event_years = Soup_Objects.event_years
        self.pool_wins = Full_Seeds_Pools_Info().team_pool_wins_ordered()
        self.pool_losses = Full_Seeds_Pools_Info().team_pool_losses_ordered()
        self.bracket_winners = Full_Bracket_Info().full_bracket_winners()
        self.bracket_losers = Full_Bracket_Info().full_bracket_losers()
        self.spirit = pd.read_excel(r'C:\Users\hunte\Desktop\bookends_stats_club\Club_Spirit_Scores.xlsx', sheet_name='Sheet1', header=0)
        self.full_wins = [4, 5, 5, 5, 5, 4, 7, 6, 2, 4, 1, 0, 4, 4, 1, 3, 7, 8, 5, 4, 5, 4, 5, 3, 3, 2, 4, 1, 2, 3, 2, 1, 6, 8, 5, 6, 4, 5, 4, 4, 4, 4, 3, 3, 1, 2, 1, 1, 5, 5, 4, 5, 5, 4, 7, 6, 5, 3, 3, 3, 1, 2, 1, 2, 8, 7, 4, 4, 5, 5, 3, 3, 3, 1, 4, 5, 2, 4, 1, 2, 7, 7, 7, 4, 4, 3, 4, 3, 3, 5, 4, 2, 3, 3, 1, 1, 5, 4, 5, 6, 3, 4, 3, 4, 4, 1, 7, 4, 1, 1, 2, 4, 6, 7, 3, 7, 2, 4, 6, 2, 3, 4, 3, 2, 0, 4, 4, 2, 8, 7, 5, 3, 4, 4, 3, 2, 3, 5, 4, 5, 4, 0, 1, 2, 6, 7, 4, 4, 3, 1, 5, 1, 3, 7, 5, 2, 4, 9, 1, 0, 8, 5, 4, 2, 8, 3, 1, 0, 6, 5, 6, 5, 5, 4, 3, 3, 3, 3, 2, 2, 3, 1, 4, 1, 5, 7, 6, 5, 4, 3, 4, 3, 4, 2, 1, 2, 3, 0, 6, 7, 3, 4, 5, 4, 3, 3, 4, 2, 5, 4, 2, 2, 0, 2, 6, 4, 1, 1, 2, 6, 4, 6, 4, 2, 3, 7, 1, 0, 5, 2, 0, 2, 2, 4, 7, 3, 4, 5, 2, 6, 6, 3, 2, 3, 2, 4, 1, 2, 0, 0, 6, 6, 7, 3, 4, 2, 2, 3, 3, 1, 3, 5, 0, 1, 2, 2, 3, 3, 5, 5, 2, 0, 1, 4, 1, 4, 5, 3, 3, 6, 3, 5, 5, 2, 4, 4, 1, 0, 1, 2, 3, 3, 5, 6, 5, 2, 1, 1, 6, 2, 4, 3, 5, 3, 5, 3, 3, 2, 1, 1, 4, 2, 2, 2, 4, 4, 3, 3, 4, 5, 4, 2, 4, 1, 2, 2, 3, 6, 5, 6, 6, 0, 2, 3, 5, 8, 8, 4, 2, 1, 1, 2, 9, 6, 3, 5, 4, 2, 2, 0, 6, 5, 2, 4, 2, 5, 2, 3, 3, 5, 2, 4, 3, 3, 0, 1, 6, 5, 3, 4, 1, 3, 2, 3, 5, 4, 3, 5, 1, 2, 0, 3, 6, 5, 5, 5, 3, 3, 2, 1, 4, 4, 2, 4, 1, 2, 0, 3, 3, 7, 5, 3, 5, 1, 2, 5, 5, 4, 1, 5, 3, 3, 2, 1, 6, 4, 4, 5, 7, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 2, 5, 5, 6, 7, 3, 4, 4, 5, 3, 3, 4, 3, 1, 1, 1, 0, 7, 5, 6, 4, 5, 3, 2, 2, 3, 2, 3, 0, 5, 6, 5, 3, 4, 2, 4, 3, 3, 2, 3, 2, 5, 2, 6, 3, 4, 4, 5, 2, 5, 4, 3, 3, 1, 1, 2, 0, 2, 5, 1, 5, 3, 2, 4, 2, 4, 3, 2, 4, 4, 3, 2, 2, 3, 6, 4, 1, 5, 2, 0, 3, 8, 7, 1, 4, 3, 5, 3, 0, 7, 4, 5, 6, 4, 2, 3, 0, 3, 4, 9, 3, 1, 6, 5, 0, 5, 3, 2, 6, 4, 2, 4, 4, 2, 5, 3, 3, 1, 2, 2, 2, 5, 4, 5, 3, 2, 3, 6, 4, 5, 2, 3, 0, 2, 2, 2, 2, 6, 5, 4, 4, 2, 5, 5, 3, 4, 2, 1, 3, 1, 0, 2, 3, 6, 6, 4, 4, 4, 4, 2, 6, 3, 2, 3, 1, 2, 4, 1, 3, 7, 5, 6, 4, 4, 3, 1, 2, 3, 2, 3, 3, 2, 4, 2, 3, 7, 5, 6, 5, 5, 4, 3, 4, 1, 3, 2, 3, 2, 1, 3, 1, 6, 4, 4, 2, 4, 4, 4, 4, 2, 4, 0, 1, 2, 2, 1, 5, 5, 4, 2, 3, 3, 3, 3, 5, 4, 6, 3, 2, 0, 3, 2, 1, 5, 4, 3, 6, 5, 3, 5, 3, 2, 4, 2, 4, 1, 2, 0, 1, 6, 3, 4, 3, 5, 3, 2, 2, 2, 0, 5, 3, 5, 4, 3, 4, 1, 4, 2, 0, 5, 5, 6, 4, 2, 3, 3, 2, 0, 1, 7, 4, 5, 6, 5, 2, 2, 2, 1, 4, 1, 3, 5, 5, 5, 6, 3, 1, 4, 3, 4, 4, 3, 1, 2, 2, 2, 0, 5, 3, 5, 4, 3, 3, 0, 1, 2, 4, 5, 4, 4, 3, 3, 0, 1, 4, 2, 1, 6, 4, 4, 3, 4, 7, 3, 2, 3, 2, 2, 0, 3, 3, 6, 5, 6, 2, 2, 4, 4, 1, 3, 0, 1, 5, 4, 5, 3, 3, 4, 4, 6, 5, 1, 2, 2, 1, 2, 3, 0, 4, 6, 4, 5, 5, 5, 3, 4, 2, 3, 1, 2, 2, 1, 1, 2, 4, 3, 2, 5, 6, 2, 3, 5, 4, 3, 1, 1, 3, 1, 1, 4, 6, 4, 4, 4, 5, 3, 5, 1, 2, 3, 3, 3, 3, 2, 1, 6, 5, 4, 4, 3, 4, 4, 2, 2, 3, 3, 3, 3, 2, 1, 2, 5, 6, 4, 4, 5, 3, 1, 3, 4, 4, 2, 2, 4, 3, 2, 1, 5, 5, 4, 3, 3, 6, 3, 4, 3, 3, 1, 4, 2, 3, 1, 0, 5, 4, 4, 2, 6, 2, 4, 1, 5, 4, 3, 4, 1, 3, 0, 2, 5, 6, 5, 4, 5, 4, 2, 4, 0, 2, 3, 2, 3, 2, 2, 1, 5, 6, 4, 5, 2, 3, 1, 1, 3, 1, 5, 3, 5, 2, 4, 3, 3, 5, 1, 0, 6, 5, 3, 4, 3, 4, 2, 3, 0, 1, 6, 3, 2, 2, 5, 5, 3, 0, 2, 2, 3, 1, 1, 2, 2, 4, 5, 3, 4, 6, 4, 2, 3, 2, 2, 5, 2, 3, 1, 0, 1, 0, 5, 4, 4, 4, 3, 3, 3, 2, 1, 1, 4, 4, 0, 2, 1, 4, 6, 4, 6, 3, 4, 2, 5, 2, 4, 1, 0, 4, 5, 5, 6, 3, 6, 4, 3, 3, 2, 1, 0, 7, 5, 5, 4, 4, 0, 3, 2, 2, 2, 5, 5, 3, 5, 4, 4, 4, 2, 4, 4, 2, 3, 1, 0, 2, 2, 6, 5, 4, 5, 4, 1, 3, 4, 4, 2, 2, 3, 3, 3, 1, 0, 5, 3, 4, 5, 2, 5, 4, 4, 6, 2, 3, 2, 1, 3, 0, 1, 6, 5, 5, 4, 5, 5, 4, 3, 2, 2, 2, 1, 4, 4, 1, 2, 6, 2, 5, 4, 4, 5, 3, 3, 3, 2, 3, 5, 4, 5, 0, 1, 5, 5, 4, 6, 5, 4, 4, 3, 3, 3, 2, 2, 3, 2, 2, 1, 4, 4, 4, 5, 4, 3, 3, 3, 0, 1, 2, 3, 2, 4, 3, 5, 4, 6, 4, 5, 5, 5, 3, 4, 1, 1, 1, 2, 3, 2, 2, 2, 6, 5, 5, 4, 5, 3, 4, 3, 2, 3, 0, 2, 1, 3, 2, 2, 6, 3, 3, 2, 3, 1, 3, 3, 5, 5, 1, 4, 3, 1, 2, 3, 5, 4, 6, 4, 3, 2, 1, 2, 1, 2, 6, 5, 4, 4, 4, 4, 2, 4, 2, 2, 3, 0, 4, 2, 2, 2, 4, 3, 6, 4, 4, 2, 4, 5, 1, 3, 4, 2, 3, 1, 4, 0, 4, 6, 4, 5, 5, 5, 4, 2, 0, 3, 1, 2, 3, 3, 1, 2, 5, 6, 6, 5, 5, 3, 3, 4, 2, 0, 2, 1, 5, 5, 6, 4, 4, 5, 2, 3, 1, 4, 0, 3, 5, 5, 6, 5, 4, 3, 3, 2, 5, 2, 0, 2, 1, 5, 2, 3, 2, 3, 3, 3, 4, 4, 2, 1, 4, 2, 1, 0, 3, 5, 4, 4, 2, 4, 1, 2, 3, 1, 1, 4, 1, 2, 1, 2, 5, 3, 3, 4, 4, 2, 3, 3, 2, 1, 2, 3, 1, 3, 1, 0, 6, 4, 5, 4, 4, 3, 4, 4, 3, 3, 2, 2, 4, 2, 2, 1, 5, 4, 5, 4, 3, 5, 2, 1, 3, 3, 3, 4, 4, 1, 4, 2, 5, 6, 4, 4, 5, 3, 4, 4, 3, 3, 1, 1, 5, 2, 1, 2, 4, 3, 5, 2, 5, 3, 3, 5, 4, 0, 6, 3, 1, 2, 2, 2, 3, 2, 4, 2, 3, 5, 4, 5, 3, 2, 3, 4, 0, 2, 3, 5, 5, 6, 4, 5, 4, 2, 3, 1, 3, 2, 3, 3, 0, 2, 4, 3, 3, 3, 6, 2, 2, 5, 4, 2, 2, 1, 5, 4, 2, 3, 2, 2, 2, 6, 4, 0, 6, 5, 4, 4, 2, 3, 3, 2, 0, 1, 4, 7, 6, 1, 4, 4, 4, 5, 2, 3, 1, 2, 0, 2, 1, 5, 7, 5, 4, 4, 1, 2, 3, 3, 2, 4, 2, 3, 1, 0, 5, 7, 2, 4, 2, 3, 0, 1, 5, 5, 4, 3, 2, 1, 2, 4, 7, 6, 4, 3, 5, 3, 3, 4, 2, 0, 1, 6, 5, 5, 2, 4, 4, 5, 3, 5, 2, 0, 1, 6, 7, 5, 3, 4, 4, 2, 1, 4, 3, 2, 1, 2, 5, 4, 4, 6, 2, 4, 2, 4, 4, 2, 4, 2, 1, 0, 2, 6, 5, 5, 2, 4, 2, 5, 4, 4, 3, 1, 1, 1, 2, 2, 1, 5, 5, 5, 4, 2, 3, 3, 1, 5, 3, 4, 3, 0, 2, 3, 0, 4, 4, 5, 3, 1, 5, 3, 5, 4, 3, 2, 3, 2, 3, 1, 5, 6, 4, 5, 3, 4, 4, 4, 3, 3, 3, 2, 3, 2, 2, 2, 3, 4, 4, 5, 5, 6, 5, 3, 4, 3, 2, 3, 0, 2, 4, 2, 1, 6, 3, 4, 4, 3, 4, 1, 0, 5, 2, 4, 2, 5, 1, 4, 2, 4, 5, 5, 5, 4, 4, 3, 2, 3, 4, 2, 4, 3, 2, 0, 0, 5, 6, 5, 4, 4, 2, 2, 4, 2, 4, 5, 2, 0, 3, 1, 1, 6, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 4, 6, 3, 1, 2, 1, 4, 4, 3, 2, 6, 3, 5, 3, 1, 1, 2, 6, 5, 4, 4, 3, 4, 4, 4, 3, 2, 1, 4, 0, 1, 2, 3, 6, 5, 5, 0, 4, 3, 2, 4, 5, 2, 4, 2, 1, 2, 4, 1, 6, 5, 5, 5, 1, 3, 4, 3, 3, 3, 3, 1, 3, 1, 3, 1, 5, 4, 2, 4, 5, 2, 3, 4, 2, 1, 0, 2, 6, 5, 3, 4, 3, 1, 3, 3, 3, 1, 0, 3, 5, 4, 4, 6, 3, 3, 4, 2, 1, 2, 1, 1]
        self.full_losses = [4, 3, 3, 2, 3, 5, 1, 2, 5, 4, 6, 6, 3, 4, 5, 4, 1, 0, 2, 4, 4, 3, 2, 5, 4, 5, 4, 6, 6, 4, 5, 6, 1, 0, 2, 2, 4, 3, 5, 4, 4, 5, 4, 4, 6, 5, 6, 6, 3, 2, 3, 3, 3, 3, 2, 2, 3, 4, 6, 5, 6, 5, 6, 5, 0, 1, 3, 3, 2, 3, 5, 4, 5, 6, 4, 4, 5, 5, 6, 5, 1, 1, 1, 4, 4, 4, 5, 4, 5, 3, 3, 5, 4, 5, 6, 6, 3, 3, 2, 1, 5, 4, 4, 3, 3, 6, 1, 4, 6, 6, 5, 5, 1, 1, 4, 1, 6, 4, 3, 5, 5, 3, 4, 5, 7, 4, 3, 5, 0, 1, 2, 5, 3, 5, 6, 6, 4, 3, 4, 2, 3, 7, 6, 5, 3, 2, 3, 4, 4, 6, 3, 6, 4, 2, 3, 5, 4, 0, 6, 7, 1, 3, 4, 5, 1, 4, 6, 7, 1, 2, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 4, 6, 3, 6, 2, 0, 1, 2, 3, 4, 3, 4, 3, 5, 6, 5, 4, 7, 1, 0, 4, 3, 2, 3, 4, 4, 3, 5, 2, 3, 5, 5, 7, 5, 0, 2, 5, 5, 4, 1, 2, 1, 3, 4, 3, 0, 5, 6, 2, 4, 6, 4, 4, 3, 0, 4, 2, 2, 4, 1, 1, 3, 4, 3, 4, 3, 5, 4, 6, 6, 1, 1, 0, 3, 3, 4, 4, 4, 3, 5, 3, 2, 6, 5, 4, 4, 3, 3, 1, 1, 4, 6, 5, 2, 5, 2, 1, 3, 3, 0, 3, 1, 1, 4, 2, 2, 5, 6, 5, 4, 4, 4, 2, 1, 2, 5, 6, 6, 1, 5, 3, 4, 1, 3, 1, 3, 3, 4, 5, 5, 2, 4, 4, 4, 2, 2, 3, 3, 2, 1, 2, 4, 2, 5, 4, 4, 4, 2, 3, 3, 3, 7, 5, 4, 3, 1, 1, 4, 5, 6, 6, 5, 0, 2, 4, 4, 4, 5, 5, 7, 0, 2, 4, 3, 4, 1, 5, 3, 3, 1, 4, 2, 4, 3, 6, 5, 1, 1, 3, 3, 5, 3, 5, 3, 1, 3, 3, 1, 5, 4, 6, 3, 0, 2, 1, 1, 3, 3, 5, 5, 3, 2, 4, 3, 5, 4, 6, 3, 4, 0, 1, 4, 2, 6, 5, 2, 1, 3, 6, 2, 4, 4, 5, 6, 1, 3, 3, 2, 0, 3, 5, 4, 4, 3, 5, 4, 5, 4, 4, 5, 1, 1, 1, 0, 4, 3, 3, 2, 4, 4, 3, 4, 6, 6, 6, 7, 0, 2, 1, 3, 2, 4, 5, 5, 4, 5, 4, 7, 2, 1, 2, 4, 3, 5, 3, 4, 4, 5, 4, 5, 1, 4, 0, 3, 2, 3, 1, 5, 2, 3, 3, 3, 5, 5, 4, 6, 4, 1, 5, 1, 3, 4, 2, 4, 2, 3, 4, 2, 2, 3, 4, 4, 3, 0, 2, 5, 1, 4, 6, 3, 1, 2, 6, 4, 4, 3, 4, 7, 2, 3, 3, 3, 4, 5, 4, 7, 4, 4, 0, 4, 6, 3, 3, 7, 1, 3, 4, 0, 3, 4, 3, 3, 4, 1, 4, 3, 5, 4, 4, 4, 2, 2, 1, 4, 4, 3, 1, 2, 1, 4, 4, 6, 4, 4, 4, 4, 0, 1, 3, 3, 4, 1, 2, 3, 2, 4, 5, 4, 5, 6, 4, 3, 1, 1, 3, 2, 3, 2, 5, 1, 4, 5, 4, 6, 5, 3, 6, 4, 0, 2, 1, 3, 3, 4, 6, 4, 3, 5, 4, 4, 5, 3, 5, 4, 0, 1, 1, 1, 2, 3, 4, 3, 6, 4, 5, 4, 5, 6, 4, 6, 1, 2, 3, 3, 2, 2, 2, 2, 4, 3, 6, 5, 4, 4, 4, 2, 1, 2, 4, 3, 4, 3, 4, 2, 2, 0, 4, 4, 6, 3, 4, 5, 1, 2, 4, 0, 2, 3, 2, 3, 4, 2, 4, 3, 5, 4, 6, 5, 0, 4, 3, 3, 1, 3, 4, 4, 4, 6, 1, 3, 1, 2, 4, 2, 5, 3, 4, 6, 1, 2, 0, 3, 4, 3, 3, 4, 6, 5, 0, 3, 2, 1, 2, 5, 5, 5, 6, 3, 6, 4, 1, 2, 1, 1, 3, 5, 2, 3, 2, 3, 3, 5, 5, 4, 4, 6, 0, 3, 1, 2, 2, 3, 6, 5, 4, 2, 2, 2, 2, 3, 3, 6, 5, 2, 4, 5, 1, 2, 2, 3, 3, 0, 3, 4, 3, 4, 4, 6, 3, 3, 1, 1, 1, 4, 4, 2, 2, 5, 3, 6, 5, 2, 2, 1, 3, 3, 3, 3, 0, 2, 5, 4, 4, 5, 4, 3, 6, 2, 0, 3, 1, 2, 1, 4, 2, 4, 3, 5, 4, 5, 5, 5, 4, 2, 3, 4, 2, 0, 3, 4, 2, 1, 3, 5, 4, 3, 4, 4, 3, 0, 1, 3, 1, 2, 4, 1, 6, 5, 4, 4, 4, 4, 5, 6, 0, 1, 2, 1, 4, 3, 3, 5, 5, 4, 4, 4, 3, 5, 6, 5, 1, 0, 1, 1, 2, 4, 6, 4, 3, 3, 5, 5, 3, 4, 5, 6, 1, 1, 3, 3, 4, 0, 3, 2, 3, 4, 5, 3, 4, 3, 5, 6, 1, 2, 2, 4, 1, 4, 3, 5, 1, 2, 4, 3, 5, 3, 6, 4, 1, 0, 1, 2, 2, 3, 4, 3, 6, 5, 3, 4, 3, 4, 4, 5, 1, 0, 2, 2, 4, 4, 5, 5, 3, 5, 1, 3, 1, 4, 3, 3, 3, 2, 5, 6, 0, 1, 4, 3, 3, 2, 4, 3, 6, 5, 0, 2, 3, 3, 1, 1, 3, 5, 3, 3, 3, 4, 4, 3, 3, 2, 1, 3, 2, 0, 2, 3, 2, 3, 3, 1, 3, 2, 4, 5, 4, 5, 0, 1, 0, 1, 3, 3, 3, 3, 4, 5, 2, 2, 6, 4, 4, 2, 1, 3, 1, 4, 2, 5, 2, 5, 3, 6, 7, 2, 2, 1, 1, 4, 2, 3, 4, 5, 5, 6, 7, 0, 2, 2, 2, 2, 7, 4, 5, 5, 5, 1, 2, 3, 2, 2, 2, 2, 4, 3, 2, 5, 3, 5, 6, 4, 4, 0, 1, 2, 1, 3, 5, 4, 3, 3, 4, 5, 3, 4, 3, 5, 6, 2, 3, 2, 2, 4, 2, 2, 2, 0, 5, 3, 4, 5, 3, 6, 5, 0, 1, 3, 2, 2, 2, 3, 4, 5, 4, 5, 6, 3, 4, 6, 5, 0, 5, 2, 3, 3, 1, 4, 4, 3, 5, 3, 2, 4, 3, 7, 6, 1, 1, 2, 0, 3, 3, 3, 4, 5, 4, 5, 5, 4, 5, 5, 6, 2, 2, 3, 2, 2, 3, 3, 3, 6, 5, 4, 3, 4, 3, 3, 2, 2, 0, 2, 1, 2, 2, 3, 3, 5, 5, 5, 4, 3, 4, 5, 4, 0, 1, 1, 2, 2, 3, 3, 4, 4, 3, 6, 4, 5, 4, 4, 4, 0, 3, 3, 4, 3, 5, 3, 3, 1, 1, 5, 2, 3, 5, 4, 3, 1, 3, 1, 2, 3, 4, 5, 4, 5, 4, 0, 1, 3, 2, 2, 2, 4, 3, 4, 4, 3, 6, 3, 4, 5, 4, 2, 4, 0, 3, 2, 4, 2, 2, 5, 3, 3, 4, 3, 5, 2, 6, 2, 0, 2, 2, 1, 2, 3, 4, 6, 3, 5, 4, 4, 3, 5, 4, 2, 1, 1, 2, 2, 4, 4, 3, 5, 7, 5, 6, 2, 2, 1, 3, 3, 2, 5, 4, 6, 3, 7, 4, 2, 2, 1, 2, 3, 4, 4, 5, 2, 5, 7, 5, 4, 0, 3, 2, 3, 2, 2, 2, 1, 1, 3, 4, 1, 3, 4, 5, 2, 0, 1, 1, 3, 1, 4, 3, 2, 4, 4, 1, 4, 3, 4, 3, 0, 2, 2, 1, 1, 3, 2, 2, 3, 4, 3, 2, 4, 2, 4, 5, 1, 2, 2, 3, 1, 2, 3, 2, 4, 4, 5, 5, 3, 5, 5, 6, 1, 1, 1, 1, 4, 2, 5, 6, 4, 4, 4, 3, 3, 6, 3, 5, 1, 0, 1, 1, 2, 4, 3, 3, 4, 4, 6, 6, 2, 5, 6, 5, 2, 3, 1, 4, 1, 3, 4, 2, 2, 6, 0, 4, 5, 5, 4, 4, 4, 4, 3, 4, 3, 1, 2, 1, 4, 4, 4, 2, 6, 4, 3, 1, 1, 0, 3, 1, 3, 4, 4, 5, 4, 4, 3, 3, 6, 4, 2, 3, 2, 3, 0, 4, 4, 2, 2, 4, 4, 5, 1, 2, 4, 3, 4, 4, 4, 0, 2, 6, 0, 1, 2, 2, 4, 3, 3, 4, 6, 5, 2, 0, 1, 5, 3, 3, 3, 2, 4, 3, 4, 4, 5, 3, 4, 2, 0, 1, 3, 3, 4, 5, 4, 3, 4, 2, 4, 2, 4, 5, 2, 0, 4, 3, 3, 3, 5, 4, 1, 2, 2, 3, 4, 5, 5, 3, 0, 1, 3, 4, 2, 4, 4, 3, 5, 7, 6, 1, 2, 2, 5, 3, 3, 2, 4, 2, 5, 7, 6, 1, 0, 2, 4, 3, 3, 5, 6, 3, 4, 5, 6, 4, 1, 3, 3, 0, 5, 2, 3, 3, 2, 4, 2, 4, 4, 5, 3, 0, 2, 1, 4, 2, 4, 1, 3, 3, 3, 4, 5, 4, 5, 3, 4, 1, 2, 1, 3, 5, 3, 4, 5, 1, 2, 2, 3, 5, 3, 3, 5, 2, 2, 2, 4, 6, 1, 4, 1, 1, 4, 5, 4, 5, 4, 6, 2, 0, 1, 2, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 5, 5, 4, 1, 2, 1, 2, 0, 2, 4, 3, 3, 5, 4, 7, 5, 3, 5, 6, 0, 3, 2, 2, 3, 3, 5, 6, 2, 4, 3, 4, 2, 5, 2, 4, 2, 1, 1, 1, 3, 2, 4, 4, 4, 3, 4, 2, 3, 4, 6, 6, 1, 0, 1, 2, 2, 4, 4, 3, 4, 3, 2, 5, 6, 3, 5, 5, 0, 2, 2, 3, 4, 3, 3, 4, 5, 4, 4, 2, 0, 3, 5, 4, 5, 2, 2, 3, 4, 0, 3, 1, 3, 5, 5, 4, 1, 1, 2, 3, 3, 3, 3, 2, 3, 4, 5, 2, 6, 5, 4, 3, 0, 1, 1, 6, 3, 3, 4, 3, 1, 5, 2, 4, 5, 4, 3, 5, 0, 1, 1, 1, 5, 3, 3, 4, 3, 3, 4, 5, 4, 5, 3, 5, 1, 2, 4, 2, 1, 4, 3, 2, 3, 5, 6, 4, 0, 1, 3, 2, 3, 5, 3, 3, 3, 5, 6, 3, 1, 2, 2, 0, 3, 3, 2, 4, 5, 4, 5, 5]

    def full_teams(self):
        full_teams = list(itertools.chain.from_iterable(self.teams))
        return full_teams

    def event_lengths(self):
        event_lengths = [len(event) for event in self.teams]
        return event_lengths

    def full_seeds(self):
        full_seeds = list(itertools.chain.from_iterable(self.seeds))
        return full_seeds

    def combine_wins(self):
        #Evaluates normally but evaluates twice in the dataframe for some reason
        pool_wins = self.pool_wins
        for wins, winners in zip(pool_wins, self.bracket_winners):
            for key, value in wins.items():
                if key in wins and key in winners:
                    wins[key] += winners[key]
        full_wins = list(itertools.chain.from_iterable([event.values() for event in pool_wins]))
        return full_wins

    def combine_losses(self):
        #Evaluates normally but evaluates twice in the dataframe for some reason
        pool_losses = self.pool_losses
        for losses, losers in zip(pool_losses, self.bracket_losers):
            for key, value in losses.items():
                if key in losses and key in losers:
                    losses[key] += losers[key]
        full_losses = list(itertools.chain.from_iterable([event.values() for event in pool_losses]))
        return full_losses

    def results(self):
        results = [dict([(key, standing[key]) for key in teams_list if key in standing]) for teams_list, standing in zip(self.teams, self.standings)]
        full_results = list(itertools.chain.from_iterable([result.values() for result in results]))
        return full_results

    def seed_diff(self):
        seed_diff = [x - y for x, y in zip(self.full_seeds(), self.results())]
        return seed_diff

    def games_played(self):
        games_played = [x + y for x, y in zip(self.combine_wins(), self.combine_losses())]
        return games_played

    def spirit_scores(self):
        spirit_teams = pd.DataFrame(self.spirit, columns=['Teams', 'Spirit'])
        return spirit_teams

    def nulls(self):
        nulls = [0] * len(self.full_seeds())
        return nulls

    def team_events_df(self):
        columns = {'seed': self.full_seeds(), 
                   'result': self.results(), 
                   'seed_diff': self.seed_diff(),
                   'spirit_score': self.nulls(),
                   'games_played': self.games_played(),
                   'wins': self.full_wins,
                   'losses': self.full_losses}
        team_events = pd.DataFrame(data=columns)
        team_events.index += 1
        return team_events

    def team_events_index_by_event(self):
        indexes_by_event = self.team_events_df().index.tolist()
        team_events_index_by_event = [indexes_by_event[x - y: x] for x, y in zip(accumulate(self.event_lengths()), self.event_lengths())]
        return team_events_index_by_event
    
    def team_event_ids_by_event(self):
        team_event_id_dicts = [dict(zip(teams, ids)) for teams, ids in zip(self.teams, self.team_events_index_by_event())]
        return team_event_id_dicts

print(Team_Events().spirit_scores())

#spirit scores:
#https://www.usaultimate.org/archives/2010_club.aspx
#https://www.usaultimate.org/archives/2011_club.aspx
#https://www.usaultimate.org/archives/2012_club.aspx
#https://www.usaultimate.org/archives/2013_club.aspx
#https://www.usaultimate.org/archives/2014_club.aspx
#https://play.usaultimate.org/events/Emerald-City-Classic-TCT-Pro-Finale/
#https://www.usaultimate.org/archives/2015_club.aspx
#https://www.usaultimate.org/archives/2016_club.aspx
#https://play.usaultimate.org/events/TCT-Elite-Select-Challenge-2016-Oshadega-Invite/
#https://play.usaultimate.org/events/TCT-Pro-Flight-Finale-2016/
#https://www.usaultimate.org/archives/2017_club.aspx
#https://docs.google.com/spreadsheets/d/1pBFslUEgHGzlty15FLcQ84A7v_ogqExJU-IWhx7Adfo/edit
#https://docs.google.com/spreadsheets/d/18TdiALb-TaUP0BmfKUBNwt7gui32nQ9fyTQ2KtVouTA/edit#gid=0
#https://play.usaultimate.org/events/TCT-Pro-Championships-2017/
#https://www.usaultimate.org/archives/2018_club.aspx
#https://play.usaultimate.org/events/TCT-Pro-Elite-Challenge-2018/
#https://tct.usaultimate.org/2018/09/05/2018-pro-championships-spirit-scores/
#https://www.usaultimate.org/archives/2019_club.aspx
#https://drive.google.com/file/d/1FYLAaEPXiYCJ4TW2iYlks_MNQaZvtr06/view
'''
Missing spirit:
2013 Elite Select CO Challenge
2013 Elite Select WA Challenge
2013 Pro Elite Challenge
2013 Pro Flight Finale
2014 Elite Select Challenge
2014 Pro Elite NY Challenge
2014 Pro Elite VA Challenge
2015 Elite Select Challenge
2015 Pro Elite Challenge
2015 Pro Flight Finale
2015 Select Flight Invite
2016 Pro Elite Challenge
2016 Select Flight Invite
2017 Elite Select Challenge
2018 Elite Select Challenge
2018 Select Flight Invite
2019 Elite Select Challenge
2019 Pro Elite Challenge
2019 Select Flight Invite
'''