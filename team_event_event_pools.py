from collections import defaultdict
import pandas as pd
from event_pools import Event_Pools
from team_events import Team_Events

class Team_Event_Event_Pools:
    def __init__(self):
        self.event_pool_ids = Event_Pools().event_pools_index_by_event()
        self.pool_teams = Event_Pools().pool_teams
        self.team_event_ids = Team_Events().team_events_index_by_event()
        self.event_teams = Team_Events().teams
    
    def event_pool_id_teams_dicts(self):
        event_pools_id_teams_dicts = []
        for x, i in enumerate(self.event_pool_ids):
            for y, event in enumerate(self.pool_teams):
                if x == y:
                    event_pools_id_teams_dicts.append(dict(zip(i, event)))
        return event_pools_id_teams_dicts
    
    def team_event_id_teams_dicts(self):
        team_event_id_teams_dicts = []
        for x, i in enumerate(self.team_event_ids):
            for y, event in enumerate(self.event_teams):
                if x == y:
                    team_event_id_teams_dicts.append(dict(zip(event, i)))
        return team_event_id_teams_dicts
    
    def team_event_event_pools_dict(self):
        event_pool_ids = []
        team_event_ids = []
        for x, event in enumerate(self.team_event_id_teams_dicts()):
            for y, pool in enumerate(self.event_pool_id_teams_dicts()):
                if x == y:
                    for team, team_event_id in event.items():
                        for pool_id, pool_team in pool.items():
                            if team == pool_team:
                                event_pool_ids.append(pool_id)
                                team_event_ids.append(team_event_id)
        team_event_event_pools_dict_unordered = dict(zip(event_pool_ids, team_event_ids))
        team_event_event_pools_tuple = sorted(team_event_event_pools_dict_unordered.items(), key=lambda x: x[0])
        team_event_event_pools_dict = dict(team_event_event_pools_tuple)
        return team_event_event_pools_dict
    
    def team_event_event_pools_df(self):
        columns = {'event_pool_id': list(self.team_event_event_pools_dict().keys()), 'team_event_id': list(self.team_event_event_pools_dict().values())}
        team_event_event_pools_df = pd.DataFrame(data=columns)
        team_event_event_pools_df = team_event_event_pools_df.set_index('event_pool_id')
        return team_event_event_pools_df