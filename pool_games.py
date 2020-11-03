from event_info import Team_Pools, Soup_Objects, Full_Seeds_Pools_Info, accumulate, groupby
from event_pools import Event_Pools, Counter
from event_day_connector import Event_Day_Converter
import itertools
import more_itertools as mit
import pandas as pd
from more_itertools import split_before

class Pool_Games:
    def __init__(self):
        self.pool_matchups = Full_Seeds_Pools_Info().full_pool_matchups()
        self.pool_scores = Full_Seeds_Pools_Info().full_pool_scores()
        self.event_pool_ids = Event_Pools().event_pool_id_pool_seeds_dicts()
        self.days = ['Thu', 'Fri', 'Sat', 'Sun', 'Mon']
        self.pool_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        self.event_day_ids = Event_Day_Converter().event_day_ids()

    def pool_seeds_to_pool_ids(self):
        pool_id_matchups = zip(self.pool_matchups, self.event_pool_ids)
        full_pool_ids = [v for event, ids in pool_id_matchups for seed in event for k, v in ids.items() if seed == k]
        return full_pool_ids
    
    def full_scores(self):
        full_score_strings = list(itertools.chain.from_iterable(self.pool_scores))
        full_scores = list(map(int, full_score_strings))
        return full_scores
    
    def pool_days(self):
        pool_days = [x for event in self.pool_matchups for x in event if x in self.days]
        return pool_days
    
    def full_pool_days(self):
        pool_matchup_counts = [sum(1 for x in pool_day if len(x) == 2 and x[0] in self.pool_names) for pool_day in self.games_times_by_day()]
        full_pool_days_by_day = [[day] * int(count/2) for count, day in zip(pool_matchup_counts, self.pool_days())]
        full_pool_days = list(itertools.chain.from_iterable(full_pool_days_by_day))
        return full_pool_days
    
    def pool_days_by_event(self):
        counts_by_event = [int(len(x)/2) for x in Pool_Games().pool_scores]
        pool_days_by_event = [self.full_pool_days()[x - y: x] for x, y in zip(accumulate(counts_by_event), counts_by_event)]
        return pool_days_by_event

    def full_event_day_ids(self):
        event_day_ids = [k for days, ids in zip(self.pool_days_by_event(), self.event_day_ids) for day in days for k, v in ids.items() if day == v]
        return event_day_ids
    
    def pool_times(self):
        pool_times = [x for event in self.pool_matchups for x in event if ':' in x]
        return pool_times
    
    def games_times_by_day(self):
        games_times_by_day = [list(g) for event in self.pool_matchups for k,g in groupby(event,lambda x:x in self.days) if not k]
        return games_times_by_day
    
    def matchups_by_day_time(self):
        matchups_day_time = [list(split_before(day, lambda x:':' in x)) for day in self.games_times_by_day()]
        return matchups_day_time
    
    def round_matchups_counts(self):
        round_matchups_counts = [sum(1 for x in pool_round if len(x) == 2 and x[0] in self.pool_names) for event in self.matchups_by_day_time() for pool_round in event]
        return round_matchups_counts
    
    def full_pool_times(self):
        pool_times = [[time] * int(time_count/2) for time, time_count in zip(self.pool_times(), self.round_matchups_counts())]
        full_pool_times = list(itertools.chain.from_iterable(pool_times))
        return full_pool_times

    def pool_games_df(self):
        columns = {'event_day_id': self.full_event_day_ids(),
                   'game_time': self.full_pool_times(),
                   'first_team_event_id': self.pool_seeds_to_pool_ids()[::2],
                   'first_team_score': self.full_scores()[::2],
                   'second_team_event_id': self.pool_seeds_to_pool_ids()[1::2],
                   'second_team_score': self.full_scores()[1::2]}
        pool_games_df = pd.DataFrame(data=columns)
        pool_games_df.index += 1
        return pool_games_df