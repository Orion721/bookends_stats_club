from team_events import Team_Events, Full_Seeds_Pools_Info
import pandas as pd

class Team_Event_Events:
    def __init__(self):
        self.team_event_ids = list(Team_Events().team_events_df().index)
        self.event_ids = [1,1,1,2,2,2,4,4,4,3,3,3,8,8,9,9,11,11,11,6,6,7,10,10,10,5,5,5,15,15,15,17,17,17,14,13,13,16,16,16,12,12,12,19,19,19,23,23,23,20,20,20,22,22,22,21,21,21,18,18,18,25,25,25,29,29,29,26,26,26,28,28,28,27,27,27,24,24,24,33,33,33,35,35,35,30,30,30,34,34,34,31,31,31,32,32,32,39,39,39,41,41,41,36,36,36,40,40,40,37,37,37,38,38,38,46,46,46,48,48,48,42,42,42,47,47,47,43,43,43,45,45,45]
        self.event_teams = Full_Seeds_Pools_Info().event_teams()
    
    def team_counts(self):
        team_counts = [len(event) for event in self.event_teams]
        return team_counts
    
    def full_event_ids(self):
        full_event_ids = []
        for x, count in enumerate(self.team_counts()):
            for y, event_id in enumerate(self.event_ids):
                if x == y:
                    full_event_ids.extend([event_id] * count)
        return full_event_ids
    
    def team_event_events_df(self):
        columns = {'event_id': self.full_event_ids()}
        team_event_events_df = pd.DataFrame(data=columns)
        team_event_events_df.index += 1
        return team_event_events_df