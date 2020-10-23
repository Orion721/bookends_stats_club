import sqlalchemy
from sqlalchemy import create_engine
import pymysql
from file_connector import Teams, Team_Team_Events, Team_Events

class Export_Table:
    def __init__(self):
        self.db_connection_str = 'mysql+pymysql://root:underground@localhost/club'
        self.db_connection = create_engine(self.db_connection_str)
        self.teams_df = Teams().teams_dataframe()
        #self.team_team_events_df = Team_Team_Events().team_team_events_df()
        #self.team_events_df = Team_Events().team_events_df()

    def export_teams(self):
        self.teams_df.to_sql(name='teams', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='team_id',
                            dtype={'team_name': sqlalchemy.types.CHAR(length=100), 
                                   'team_city': sqlalchemy.types.CHAR(length=100), 
                                   'team_state': sqlalchemy.types.CHAR(length=100), 
                                   'division_id': sqlalchemy.types.INTEGER(), 
                                   'region_id': sqlalchemy.types.INTEGER()})
'''
    def export_team_team_events(self):
        self.teams_df.to_sql(name='team_team_events', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='team_team_event_id',
                            dtype={'team_id': sqlalchemy.types.INTEGER()})

    def export_team_events(self):
        self.teams_df.to_sql(name='team_events', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='team_event_id',
                            dtype={'seed': sqlalchemy.types.INTEGER(), 
                                   'result': sqlalchemy.types.INTEGER(), 
                                   'seed_diff': sqlalchemy.types.INTEGER(), 
                                   'spirit_score': sqlalchemy.types.DECIMAL(), 
                                   'games_played': sqlalchemy.types.INTEGER(),
                                   'wins': sqlalchemy.types.INTEGER(),
                                   'losses': sqlalchemy.types.INTEGER()})
                                   
    def export_team_event_events(self):
        self.team_event_events_df.to_sql(name='team_event_events',
                                        con=self.db_connection,
                                        if_exists='replace',
                                        index=True,
                                        index_label='team_event_id',
                                        dtype={'event_id': sqlalchemy.types.INTEGER()})
    
    def export_team_event_event_pools(self):
        self.team_event_event_pools_df.to_sql(name='team_event_event_pools',
                                        con=self.db_connection,
                                        if_exists='replace',
                                        index=True,
                                        index_label='event_pool_id',
                                        dtype={'team_event_id': sqlalchemy.types.INTEGER()})

    def export_event_pools(self):
        self.event_pools_df.to_sql(name='event_pools', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='event_pool_id',
                            dtype={'pool': sqlalchemy.types.CHAR(length=100), 
                                   'pool_start': sqlalchemy.types.INTEGER(), 
                                   'pool_finish': sqlalchemy.types.INTEGER(), 
                                   'pool_wins': sqlalchemy.types.INTEGER(), 
                                   'pool_losses': sqlalchemy.types.INTEGER()})

    def export_pool_games(self):
        self.pool_games_df.to_sql(name='pool_games', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='pool_games_id',
                            dtype={'event_day_id': sqlalchemy.types.INTEGER(), 
                                   'game_time': sqlalchemy.types.time(), 
                                   'first_team_event_id': sqlalchemy.types.INTEGER(), 
                                   'first_team_score': sqlalchemy.types.DECIMAL(), 
                                   'second_team_event_id': sqlalchemy.types.INTEGER(),
                                   'second_team_score': sqlalchemy.types.INTEGER()})
    
    def export_bracket_games(self):
        self.pool_games_df.to_sql(name='bracket_games', 
                            con=self.db_connection, 
                            if_exists='replace', 
                            index=True, 
                            index_label='bracket_games_id',
                            dtype={'bracket_type_id': sqlalchemy.types.INTEGER(), 
                                   'bracket_game_type_id': sqlalchemy.types.INTEGER(), 
                                   'event_day_id': sqlalchemy.types.INTEGER(), 
                                   'game_time': sqlalchemy.types.time(), 
                                   'first_team_event_id': sqlalchemy.types.INTEGER(),
                                   'first_team_score': sqlalchemy.types.INTEGER()})
'''
Export_Table().export_teams()

#Teams
#Team_Team_Events
#Team_Events

#Team_Event_Events
#Team_Event_Event_Pools
#Event_Pools
#Pool_Games
#Bracket_Games

#Populate spirit
#bracket game days, times