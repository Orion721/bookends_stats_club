import pandas as pd
import time
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
    
    def full_teams(self):
        full_teams = []
        for event in self.teams:
            full_teams.extend(event)
        return full_teams

    def event_lengths(self):
        event_lengths = [len(event) for event in self.teams]
        return event_lengths

    def full_seeds(self):
        full_seeds = []
        for event in self.seeds:
            full_seeds.extend(event)
        return full_seeds

    def combine_wins(self):
        for x, wins in enumerate(self.pool_wins):
            for y, winners in enumerate(self.bracket_winners):
                if x == y:
                    for key, value in wins.items():
                        if key in wins and key in winners:
                            wins[key] = value + winners[key]
        full_wins = []
        for event in self.pool_wins:
            full_wins.extend(event.values())
        return full_wins

    def combine_losses(self):
        for x, losses in enumerate(self.pool_losses):
            for y, losers in enumerate(self.bracket_losers):
                if x == y:
                    for key, value in losses.items():
                        if key in losses and key in losers:
                            losses[key] = value + losers[key]
        full_losses = []
        for event in self.pool_losses:
            full_losses.extend(event.values())
        return full_losses

    def results(self):
        results = []
        for x, teams_list in enumerate(self.teams):
            for y, standing in enumerate(self.standings):
                if x == y:
                    results.append(dict([(key, standing[key]) for key in teams_list if key in standing]))
        full_results = []
        for result in results:
            full_results.extend(result.values())
        return full_results

    def seed_diff(self):
        seed_diff = [x - y for x, y in zip(self.full_seeds(), self.results())]
        return seed_diff

    def games_played(self):
        games_played = [x + y for x, y in zip(self.combine_wins(), self.combine_losses())]
        return games_played

    def nulls(self):
        nulls = [0] * len(self.full_seeds())
        return nulls

    def team_events_df(self):
        columns = {'seed': self.full_seeds(), 
                   'result': self.results(), 
                   'seed_diff': self.seed_diff(),
                   'spirit_score': self.nulls(),
                   'games_played': self.games_played(),
                   'wins': self.combine_wins(),
                   'losses': self.combine_losses()}
        team_events = pd.DataFrame(data=columns)
        team_events.index += 1
        return team_events

    def team_events_index_by_event(self):
        indexes_by_event = self.team_events_df().index.tolist()
        team_events_index_by_event = [indexes_by_event[x - y: x] for x, y in zip(accumulate(self.event_lengths()), self.event_lengths())]
        return team_events_index_by_event
    
    def team_event_ids_by_event(self):
        team_event_id_dicts = []
        for x, teams in enumerate(self.teams):
            for y, ids in enumerate(self.team_events_index_by_event()):
                if x == y:
                    team_event_id_dicts.append(dict(zip(teams, ids)))
        return team_event_id_dicts