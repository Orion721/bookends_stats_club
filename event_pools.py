from itertools import accumulate
from collections import Counter
import pandas as pd
from event_info import Full_Seeds_Pools_Info

class Event_Pools:
    def __init__(self):
        self.pool_seeds = Full_Seeds_Pools_Info().full_pool_seeds()
        self.pool_teams = Full_Seeds_Pools_Info().event_teams_raw()
        self.pool_wins = Full_Seeds_Pools_Info().team_pool_wins()
        self.pool_losses = Full_Seeds_Pools_Info().team_pool_losses()

    def pools(self):
        pools = []
        for event in self.pool_seeds:
            for pool_seed in event:
                pools.append(pool_seed[0])
        return pools
    
    def event_lengths(self):
        event_lengths = [len(event) for event in self.pool_seeds]
        return event_lengths
    
    def pools_by_event(self):
        pools_by_event = [self.pools()[x - y: x] for x, y in zip(accumulate(self.event_lengths()), self.event_lengths())]
        return pools_by_event

    def pool_starts(self):
        pool_starts = []
        for event in self.pool_seeds:
            for pool_seed in event:
                pool_starts.append(pool_seed[-1])
        return pool_starts

    def pool_finish(self):
        pool_team_counts = []
        for event in self.pools_by_event():
            pool_team_counts.append(Counter(event))
        pool_finish = []
        for event in pool_team_counts:
            for pool_count in event.values():
                pool_finish.extend(range(1, pool_count+1))
        return pool_finish

    def full_pool_wins(self):
        pool_wins = []
        for event in self.pool_wins:
            pool_wins.extend(event)
        return pool_wins

    def full_pool_losses(self):
        pool_losses = []
        for event in self.pool_losses:
            pool_losses.extend(event)
        return pool_losses
    
    def event_pools_df(self):
        columns = {'pool': self.pools(), 
                'pool_start': self.pool_starts(), 'pool_finish': self.pool_finish(), 
                'pool_wins': self.full_pool_wins(), 'pool_losses': self.full_pool_losses()}
        event_pools_df = pd.DataFrame(data=columns)
        event_pools_df.index += 1
        return event_pools_df
    
    def event_pools_index_by_event(self):
        indexes_by_event = self.event_pools_df().index.tolist()
        event_pools_index_by_event = [indexes_by_event[x - y: x] for x, y in zip(accumulate(self.event_lengths()), self.event_lengths())]
        return event_pools_index_by_event
    
    def event_pool_id_pool_seeds_dicts(self):
        event_pools_id_pool_seeds_dicts = []
        for x, i in enumerate(self.event_pools_index_by_event()):
            for y, event in enumerate(self.pool_seeds):
                if x == y:
                    event_pools_id_pool_seeds_dicts.append(dict(zip(event, i)))
        return event_pools_id_pool_seeds_dicts