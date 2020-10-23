import pandas as pd
from teams import Teams, Full_Seeds_Pools_Info

class Team_Team_Events:
    def __init__(self):
        self.teams = Full_Seeds_Pools_Info().event_teams()
        self.teams_df = Teams.teams_dataframe

    def team_ids_dict(self):
        team_ids_dict = dict(zip(list(Teams().teams_dataframe()['team_name']), list(Teams().teams_dataframe().index)))
        return team_ids_dict
    
    def clean_teams(self):
        teams_raw = []
        for event in self.teams:
            teams_raw.extend(event)
        team_cleaner = {'OdyssÃ©e': 'Odyssée', 'OmertÃƒ': 'OmertÃ', 'PanamÃƒÂ¡': 'PanamÃ¡', 
                        'Chad Larson Experience': 'The Chad Larson Experience', 'Chicago Machine': 'Machine', 
                        'Seattle Riot': 'Riot', 'Revolution (Columbia)': 'Revolution', 'Jack Wagon': 'Jackwagon',
                        'Club Deportivo Revolution': 'Revolution', 'MesteÃ±o': 'Mesteño', 'SoCal Condors': 
                        'Condors', 'American BBQ': 'American Barbecue', 'Boost Mobile': 'Boost FC', 'Kie': 'K.ie', 
                        'The DOH Abides': "D'oh! Abides", '7Express': '7 Express', 'Seattle Mixed': 'Seattle Mixtape', 
                        'Pittsburgh Temper': 'Temper', 'BirdFruit': 'Birdfruit', 'Richmond Floodwall': 'Floodwall',
                        'Bent': 'BENT', 'Rhino Slam': 'Rhino Slam!', 'Portland Ivy': 'Ivy', 'Freaks Uv Nature': 'Freaks', 'CLE Smokestack': 'Smokestack'}
        clean_teams = [team_cleaner.get(x,x) for x in teams_raw]
        return clean_teams

    def get_team_ids(self):
        team_ids = [self.team_ids_dict()[x] for x in self.clean_teams() if x in self.team_ids_dict()]
        return team_ids
    
    def team_team_events_df(self):
        cols = {'team_id': self.get_team_ids()}
        df = pd.DataFrame(data=cols)
        df.index += 1
        return df