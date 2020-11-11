from event_info import Brackets, Full_Bracket_Info, Counter, accumulate
from team_events import Team_Events
from event_day_connector import Event_Day_Converter
import pandas as pd
import numpy as np
import itertools
import time

class Bracket_Games:
    def __init__(self):
        self.bracket_teams = Full_Bracket_Info().full_bracket_teams()
        self.team_event_ids = Team_Events().team_event_ids_by_event()
        self.bracket_scores = Full_Bracket_Info().full_bracket_scores()
        self.bracket_types = Full_Bracket_Info().full_bracket_types()
        self.bracket_round_lengths = Full_Bracket_Info().full_bracket_round_lengths()
        self.bracket_datetimes = Full_Bracket_Info().full_bracket_datetimes()
        self.event_day_ids = Event_Day_Converter().event_day_ids()

    def final_bracket_lengths(self):
        bracket_round_lengths = list(itertools.chain.from_iterable(self.bracket_round_lengths))
        for x in bracket_round_lengths:
            if x == 1 or x == 5:
                x -= 1
        final_br_lengths = [int(x/2) for x in bracket_round_lengths]
        return final_br_lengths

    def event_bracket_lengths(self):
        event_brackets = [len(bracket) for bracket in self.bracket_round_lengths]
        bracket_lengths = [self.final_bracket_lengths()[x - y: x] for x, y in zip(accumulate(event_brackets), event_brackets)]
        event_bracket_lengths = [sum(event) for event in bracket_lengths]
        return event_bracket_lengths

    def bracket_game_days(self):
        full_bracket_gametimes = list(itertools.chain.from_iterable(self.bracket_datetimes))
        bracket_game_days = []
        bracket_game_times = []
        for x, day in enumerate(full_bracket_gametimes):
            for y, length in enumerate(self.final_bracket_lengths()):
                if x == y:
                    if length == 1:
                        bracket_game_days.extend([day.split(' ')[0]])
                        bracket_game_times.extend([' '.join(day.split(' ')[1:])])
                    elif length == 3:
                        bracket_game_days.extend([day.split(' ')[0]] * 2)
                        bracket_game_days.extend([day.split(' ')[3]] * 1)
                        bracket_game_times.extend([' '.join(day.split(' ')[1:3])] * 2)
                        bracket_game_times.extend([' '.join(day.split(' ')[4:])])
                    else:
                        bracket_game_days.extend(['null'] * length)
                        bracket_game_times.extend(['null'] * length)
        return bracket_game_days, bracket_game_times

    def bracket_days_by_event(self):
        bracket_days_by_event = [self.bracket_game_days()[0][x - y: x] for x, y in zip(accumulate(self.event_bracket_lengths()), self.event_bracket_lengths())]
        return bracket_days_by_event

    def add_nulls_event_day_ids(self):
        event_day_ids = self.event_day_ids
        for ids in event_day_ids:
            ids.update({'null': 'null'})
        return event_day_ids

    def full_event_day_ids(self):
        event_day_ids = [[k for day in days for k, v in ids.items() if day == v] for days, ids in zip(self.bracket_days_by_event(), self.add_nulls_event_day_ids())]
        event_day_ids[50].insert(11, 'null')
        full_event_day_ids_raw = list(itertools.chain.from_iterable(event_day_ids))
        full_event_day_ids = [0 if x == 'null' else x for x in full_event_day_ids_raw]
        return full_event_day_ids

    def clean_bracket_teams(self):
        bracket_teams_raw = self.bracket_teams
        del bracket_teams_raw[6][22]
        del bracket_teams_raw[-3][-1]
        return bracket_teams_raw

    def bracket_team_event_ids(self):
        bracket_team_event_ids = []
        for x, event in enumerate(self.clean_bracket_teams()):
            for y, ids in enumerate(self.team_event_ids):
                if x == y:
                    for team in event:
                        for k, v in ids.items():
                            if team == k:
                                bracket_team_event_ids.append(v)
        return bracket_team_event_ids

    def clean_bracket_scores(self):
        bracket_scores_raw = self.bracket_scores
        bracket_scores_raw[0] = bracket_scores_raw[0][:-2]
        del bracket_scores_raw[1][22:24]
        del bracket_scores_raw[6][22:26]
        del bracket_scores_raw[7][24:26]
        bracket_scores_raw[-3] = bracket_scores_raw[-3][:-2]
        bracket_scores = list(itertools.chain.from_iterable(bracket_scores_raw))
        clean_bracket_scores = [0 if x == '' else x for x in bracket_scores]
        full_bracket_scores = list(map(int, clean_bracket_scores))
        return full_bracket_scores

    def bracket_types_raw(self):
        full_bracket_types = list(itertools.chain.from_iterable(self.bracket_types))
        return full_bracket_types

    def bracket_types_clean(self):
        '''
        bracket_type_codes = {1: ['Championship Bracket', '1st Place Bracket', '1st Place', 'Semifinals', 'Championship', 'Bracket', '1v1', "Men's Champion", "Women's Champion"], 
                              2: ['3rd Place', '3rd Place Bracket', '2v2', '3rd Place (both teams qualify for 2018 WUCC)', '3rd Place (2018 WUCC Qualifier)', '3rd Place Game'],
                              3: ['5th Place Bracket', '5th Place', 'Pro Flight / 5th Place Bracket', '5th Place Bracket (Pro Flight)', '3v3', 'Pro Flight 5th Place', '5th Place Game', '5th Place Bracket - 1', '5th Place Bracket - 2'],
                              4: ['7th Place', '7th Place Bracket', 'Pro Flight Play-In / 7th Place Bracket (A)', 'Pro Flight Play-In / 7th Place Bracket (B)', 'Pro Flight Play-In / 7th Place Bracket (1)', 'Pro Flight Play-In / 7th Place Bracket (2)', '4v4', '7th Place Game', 'Pro Flight Play-In Bracket', '7th Place Bracket -- Pro Flight Play-In (A)', '7th Place Bracket -- Pro Flight Play-In (B)', 'Pro Flight Qualification Bracket', 'Pro Flight Qualification'],
                              5: ['9th Place Bracket', '9th Place', '9th Place (tie)', '5v5', '9th Place Finals'],
                              6: ['11th Place', '11th Place Bracket', '11th Place Game', '6v6'],
                              7: ['13th Place', '13th Place Bracket', '13th Place (tie)', '7v7'],
                              8: ['15th Place', '15th place', '15th Place Game'],
                              9: ['Crossover', 'Crossover Showcase', '5 vs 7 friendly', 'Saturday Friendly - 2pm', 'Sunday Friendly - 9:30am']}
        bracket_types_clean = [btype_code if btype in btypes else 0 for btype in self.bracket_types_raw() for btype_code, btypes in bracket_type_codes.items()]
        '''
        bracket_types_clean = []
        for btype in self.bracket_types_raw():
            if btype in ['Championship Bracket', '1st Place Bracket', '1st Place', 'Semifinals', 'Championship', 'Bracket', '1v1', "Men's Champion", "Women's Champion"]:
                bracket_types_clean.extend([1])
            elif btype in ['3rd Place', '3rd Place Bracket', '2v2', '3rd Place (both teams qualify for 2018 WUCC)', '3rd Place (2018 WUCC Qualifier)', '3rd Place Game']:
                bracket_types_clean.extend([2])
            elif btype in ['5th Place Bracket', '5th Place', 'Pro Flight / 5th Place Bracket', '5th Place Bracket (Pro Flight)', '3v3', 'Pro Flight 5th Place', '5th Place Game', '5th Place Bracket - 1', '5th Place Bracket - 2']:
                bracket_types_clean.extend([3])
            elif btype in ['7th Place', '7th Place Bracket', 'Pro Flight Play-In / 7th Place Bracket (A)', 'Pro Flight Play-In / 7th Place Bracket (B)', 'Pro Flight Play-In / 7th Place Bracket (1)', 'Pro Flight Play-In / 7th Place Bracket (2)', '4v4', '7th Place Game', 'Pro Flight Play-In Bracket', '7th Place Bracket -- Pro Flight Play-In (A)', '7th Place Bracket -- Pro Flight Play-In (B)', 'Pro Flight Qualification Bracket', 'Pro Flight Qualification']:
                bracket_types_clean.extend([4])
            elif btype in ['9th Place Bracket', '9th Place', '9th Place (tie)', '5v5', '9th Place Finals']:
                bracket_types_clean.extend([5])
            elif btype in ['11th Place', '11th Place Bracket', '11th Place Game', '6v6']:
                bracket_types_clean.extend([6])
            elif btype in ['13th Place', '13th Place Bracket', '13th Place (tie)', '7v7']:
                bracket_types_clean.extend([7])
            elif btype in ['15th Place', '15th place', '15th Place Game']:
                bracket_types_clean.extend([8])
            elif btype in ['Crossover', 'Crossover Showcase', '5 vs 7 friendly', 'Saturday Friendly - 2pm', 'Sunday Friendly - 9:30am']:
                bracket_types_clean.extend([9])
            else:
                bracket_types_clean.extend([0])
        return bracket_types_clean

    def bracket_game_types(self):
        game_type_codes_by_length = {1: [1], 2: [2, 1], 3: [2, 2, 1], 4: [3, 3, 2, 1], 5: [3, 2, 3, 2, 1], 6: [3, 3, 2, 3, 2, 1], 7: [3, 3, 2, 3, 3, 2, 1], 9: [4, 3, 3, 2, 4, 3, 3, 2, 1], 11: [4, 3, 4, 3, 2, 4, 3, 4, 3, 2, 1], 15: [4, 4, 3, 4, 4, 3, 2, 4, 4, 3, 4, 4, 3, 2, 1]}
        bracket_game_types = [v for x in self.final_bracket_lengths() for k, v in game_type_codes_by_length.items() if x == k]
        full_bracket_game_types = list(itertools.chain.from_iterable(bracket_game_types))
        return full_bracket_game_types

    def bracket_games_df_main(self):
        columns = {'bracket_type_id': self.bracket_types_clean(),
                   'bracket_game_type_id': self.bracket_game_types(),
                   'event_day_id': self.full_event_day_ids(),
                   'game_time': self.bracket_game_days()[1],
                   'first_team_event_id': self.bracket_team_event_ids()[::2],
                   'first_team_score': self.clean_bracket_scores()[::2]
                   }
        bracket_games_df = pd.DataFrame(data=columns)
        bracket_games_df.index += 1
        return bracket_games_df
    
    def bracket_games_df_second(self):
        columns = {'second_team_event_id': self.bracket_team_event_ids()[1::2],
                   'second_team_score': self.clean_bracket_scores()[1::2]}
        bracket_games_df = pd.DataFrame(data=columns)
        bracket_games_df.index += 1
        return bracket_games_df