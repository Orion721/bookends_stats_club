from event_info import Team_Pools, Soup_Objects, Full_Seeds_Pools_Info, accumulate, groupby
from event_pools import Event_Pools
from event_day_connector import Event_Day_Converter
import more_itertools as mit
import pandas as pd
from more_itertools import split_before

class Pool_Games:
    def __init__(self):
        self.pool_matchups = Full_Seeds_Pools_Info().full_pool_matchups()
        self.pool_scores = Full_Seeds_Pools_Info().full_pool_scores()
        self.event_pool_ids = Event_Pools().event_pool_id_pool_seeds_dicts()
        self.days = ['Thu', 'Fri', 'Sat', 'Sun', 'Mon']
        self.event_day_ids = Event_Day_Converter().event_day_ids()

    def pool_seeds_to_pool_ids(self):
        pool_id_matchups = self.pool_matchups
        for x, event in enumerate(pool_id_matchups):
            for y, pool_id_dict in enumerate(self.event_pool_ids):
                if x == y:
                    for i, item in enumerate(event):
                        for pool_seed, pool_id in pool_id_dict.items():
                            if item == pool_seed:
                                event[i] = pool_id
                            else:
                                continue
        return pool_id_matchups
    
    def full_matchups(self):
        full_matchups = []
        for event in self.pool_seeds_to_pool_ids():
            for x in event:
                if isinstance(x, int):
                    full_matchups.append(x)
        return full_matchups
    
    def full_scores(self):
        full_scores = []
        for event in self.pool_scores:
            full_scores.extend(event)
        return full_scores
    
    def games_times_by_day(self):
        games_times_by_day = [list(g) for event in self.pool_matchups for k,g in groupby(event,lambda x:x in self.days) if not k]
        return games_times_by_day
    
    def pool_days(self):
        pool_days = [x for event in self.pool_matchups for x in event if x in self.days]
        return pool_days
    
    def pool_times(self):
        pool_times = [x for event in self.pool_matchups for x in event if ':' in x]
        return pool_times
    
    def matchups_by_day_time(self):
        matchups_day_time = []
        for day in self.games_times_by_day():
            matchups_day_time.append(list(split_before(day, lambda x:':' in x)))
        return matchups_day_time
    
    def round_matchups_counts(self):
        round_matchups_counts = []
        for event in self.matchups_by_day_time():
            for pool_round in event:
                round_matchups_counts.append(sum(1 for x in pool_round if len(x) == 2))
        return round_matchups_counts
    
    def full_pool_times(self):
        full_pool_times = [] 
        for x, time in enumerate(self.pool_times()):
            for y, time_count in enumerate(self.round_matchups_counts()):
                if x == y:
                    full_pool_times.extend([time] * int(time_count/2))
        return full_pool_times
    
    def day_counts(self):
        day_time_counts = [len(day) for day in self.matchups_by_day_time()]
        matchup_by_day_counts = [self.round_matchups_counts()[x - y: x] for x, y in zip(accumulate(day_time_counts), day_time_counts)]
        day_counts = [int(sum(day)/2) for day in matchup_by_day_counts]
        return day_counts
    
    def full_pool_days(self):
        full_pool_days = []
        for x, day in enumerate(self.pool_days()):
            for y, day_count in enumerate(self.day_counts()):
                if x == y:
                    full_pool_days.extend([day] * day_count)
        return full_pool_days

    def pool_days_by_event(self):
        pool_games_by_event = []
        for event in Pool_Games().pool_matchups:
            pool_games_by_event.append(int(sum(1 for x in event if ':' not in x and x not in self.days)/2))
        pool_days_by_event = [self.full_pool_days()[x - y: x] for x, y in zip(accumulate(pool_games_by_event), pool_games_by_event)]
        return pool_days_by_event

    def full_event_day_ids(self):
        full_event_day_ids = []
        for x, days in enumerate(self.pool_days_by_event()):
            for y, ids in enumerate(self.full_event_day_ids):
                if x == y:
                    full_event_day_ids.extend([k for day in days for k, v in ids.items() if day == v])
        return full_event_day_ids

    def pool_games_df(self):
        columns = {'event_day_id': self.full_event_day_ids(),
                   'game_time': self.full_pool_times(),
                   'first_team_event_id': self.full_matchups()[::2],
                   'first_team_score': self.full_scores()[::2],
                   'second_team_event_id': self.full_matchups()[1::2],
                   'second_team_score': self.full_scores()[1::2]}
        pool_games_df = pd.DataFrame(data=columns)
        pool_games_df.index += 1
        return pool_games_df