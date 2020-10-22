from make_soup import Make_Soup, Soup_Objects, BeautifulSoup
from itertools import accumulate, groupby
from operator import itemgetter
from collections import Counter, defaultdict

class Teams_Seeds:
    def __init__(self, pools):
        self.pools = pools
    
    def teams_raw(self):
        teams = []
        raw_pools = [pool.findAll('a') for pool in self.pools]
        for raw_pool in raw_pools:
            for team in raw_pool:
                teams += team
        return teams

    def overall_seeds_raw(self):
        overall_seeds_raw = []
        overall_seeds = []
        spans = [pool.findAll("span", "ng-star-inserted") for pool in self.pools]
        for span in spans:
            for overall_seed_span in span:
                overall_seeds_raw += overall_seed_span.text.split()
        for seed in overall_seeds_raw:
            if len(seed) == 4 or len(seed) == 3:
                overall_seeds.append(seed[1:-1])
        return overall_seeds

    def teams_seeds_dict(self):
        teams_seeds_raw = dict(zip(self.teams_raw(), self.overall_seeds_raw()))
        teams_seeds_sorted = sorted(teams_seeds_raw.items(), key=lambda x: int(x[1]))
        return teams_seeds_sorted

    def teams_unique_ordered(self):
        sorted_teams = []
        for i in self.teams_seeds_dict():
            sorted_teams.append(i[0])
        return sorted_teams
    
    def seeds_ordered(self):
        sorted_seeds = []
        for i in self.teams_seeds_dict():
            sorted_seeds.append(i[1])
        sorted_seeds_ints = list(map(int, sorted_seeds))
        return sorted_seeds_ints
    
class Team_Pools:
    def __init__(self, pools):
        self.pools = pools

    def pool_seeds(self):
        pool_seeds = []
        pool_seeds_spaces = []
        raw_seeds = [pool.findAll('span', 'seed') for pool in self.pools]
        for raw_seed in raw_seeds:
            for seed in raw_seed:
                pool_seeds_spaces += seed
        for seed in pool_seeds_spaces:
            pool_seeds += seed.split()
        return pool_seeds

    def pool_records(self):
        records_spaces = []
        clean_records = []
        raw_records = [pool.find_all('span', 'record') for pool in self.pools]
        for raw_record in raw_records:
            for record in raw_record:
                records_spaces += record
        for record in records_spaces:
            clean_records.append(record[2:-2])
        return clean_records
    
    def pool_wins(self):
        records = self.pool_records()
        pool_wins = []
        for record in records:
            pool_wins += record[0]
        pool_wins = list(map(int, pool_wins))
        return pool_wins

    def pool_losses(self):
        records = self.pool_records()
        pool_losses = []
        for record in records:
            pool_losses += record[-1]
        pool_losses = list(map(int, pool_losses))
        return pool_losses
    
    def pool_matchups(self):
        raw_matchups = []
        matchups = []
        clean_matchups = []
        pool_games_matchups = [pool.select('td:not(.score)') for pool in self.pools]
        for matchup in pool_games_matchups:
            raw_matchups += matchup
        for matchup in raw_matchups:
            if matchup.text.strip() not in [' ', r'\n', '-','Score','Field','Game']:
                matchups += matchup
        for matchup in matchups:
            clean_matchups.append(matchup.strip())
        return clean_matchups
    
    def pool_scores(self):
        raw_scores = []
        scores = []
        clean_scores = []
        pool_games_scores = [pool.find_all('td', 'score') for pool in self.pools]
        for score in pool_games_scores:
            raw_scores += score
        for score in raw_scores:
            scores += score
        for score in scores:
            clean_scores.append(score.strip())
        return clean_scores

class Brackets:
    def __init__(self, event_brackets):
        self.event_brackets = event_brackets
    
    def bracket_types_unique(self):
        bracket_types = []
        bracket_types_raw = [bracket.find("div", "title").text for bracket in self.event_brackets]
        for bracket_type in bracket_types_raw:
            bracket_type = " ".join(bracket_type.split())
            bracket_types.append(bracket_type)
        return bracket_types

    def bracket_datetimes(self):
        bracket_times_raw = [bracket.find("div", "time").text for bracket in self.event_brackets]
        bracket_times = []
        clean_bracket_times = []
        for bracket_time in bracket_times_raw:
            bracket_time = " ".join(bracket_time.split())
            bracket_times.append(bracket_time)
        bracket_times = [bracket_time for bracket_time in bracket_times]
        return bracket_times

    def bracket_teams_raw(self):
        bracket_teams = [bracket.findAll('a') for bracket in self.event_brackets]
        return bracket_teams
    
    def bracket_teams(self):
        teams_raw = []
        clean_teams = []
        for bracket in self.bracket_teams_raw():
            for team in bracket:
                teams_raw += team
        for team in teams_raw:
            team = " ".join(team.split())
            clean_teams.append(team)
        return clean_teams

    def bracket_scores_raw(self):
        bracket_scores_raw = [bracket.findAll("td", "score") for bracket in self.event_brackets]
        bracket_scores = []
        bracket_scores_clean = []
        for raw_score in bracket_scores_raw:
            for score in raw_score:
                bracket_scores += score
        for bracket_score in bracket_scores:
            bracket_score = " ".join(bracket_score.split())
            bracket_scores_clean.append(bracket_score)
        return bracket_scores_clean
    
    def bracket_scores_clean(self):
        bracket_teams = self.bracket_teams()
        bracket_scores = self.bracket_scores_raw()
        diff = len(bracket_scores) - len(bracket_teams)
        while diff != 0:
            bracket_scores.remove('')
            diff -= 1
        else:
            return bracket_scores

    def bracket_round_lengths(self):
        bracket_round_lengths = []
        for bracket in self.bracket_teams_raw():
            bracket_round_lengths.append(len(bracket))
        return bracket_round_lengths

    def bracket_types(self):
        bracket_types_clean = []
        for x in range(len(self.bracket_types_unique())):
            for y in range(len(self.bracket_round_lengths())):
                if x == y:
                    bracket_types_clean.extend([self.bracket_types_unique()[x]] * int(self.bracket_round_lengths()[y]/2))
        return bracket_types_clean
    
    def bracket_winners(self):
        bracket_winners_raw = [bracket.findAll("tr", "won") for bracket in self.event_brackets]
        bracket_winners_teams = []
        bracket_winners_teams_clean = []
        for bracket in bracket_winners_raw:
            for team in bracket:
                bracket_winners_teams += team.find('a')
        for bracket_winner in bracket_winners_teams:
            bracket_winner = " ".join(bracket_winner.split())
            bracket_winners_teams_clean.append(bracket_winner)
        return bracket_winners_teams_clean
    
    def bracket_losers(self):          
        teams = self.bracket_teams()
        for winner in self.bracket_winners():
            teams.remove(winner)
        return teams

class Full_Seeds_Pools_Info:
    def __init__(self):
        self.pools = Soup_Objects().pools()

    #Creates list of team lists by event, in order of seeding
    def event_teams(self):
        event_teams_unique = []
        for event in self.pools:
            event_teams_unique.append(Teams_Seeds(event).teams_unique_ordered())
        event_teams_unique[110] = ['Guerrilla', 'Rhino Slam', 'Furious George', 'Prairie Fire', 'Voodoo', 'Illusion', 'Mad Men', 'Dark Star', 'Nitro', 'Black Market', 'CaSTLe', 'Sawtooth', 'Gamble', 'PowderHogs', 'The Killjoys']
        return event_teams_unique
    
    #Creates list of team lists by event, in order of pools, pool result
    def event_teams_raw(self):
        event_teams_raw = []
        for event in self.pools:
            event_teams_raw.append(Teams_Seeds(event).teams_raw())
        return event_teams_raw
    
    def event_teams_full(self):
        event_teams_full = []
        for event in self.event_teams_raw():
            event_teams_full.extend(event)
        return event_teams_full
    
    #Creates list of seed lists by event, in order of seeding
    def full_seeds(self):
        full_seeds = []
        for event in self.pools:
            full_seeds.append(Teams_Seeds(event).seeds_ordered())
        full_seeds[110] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        return full_seeds
    
    #Creates list of pool seed lists by event, in order of pool result
    def full_pool_seeds(self):
        full_pool_seeds = []
        for event in self.pools:
            full_pool_seeds.append(Team_Pools(event).pool_seeds())
        return full_pool_seeds
    
    def team_pool_wins(self):
        team_pool_wins = []
        for event in self.pools:
            team_pool_wins.append(Team_Pools(event).pool_wins())
        return team_pool_wins
    
    def team_pool_losses(self):
        team_pool_losses = []
        for event in self.pools:
            team_pool_losses.append(Team_Pools(event).pool_losses())
        return team_pool_losses
    
    #Creates list of {teams, wins} dictionaries by event in order of pool finish
    def team_pool_wins_raw(self):
        pool_wins = []
        for event in self.pools:
            pool_wins.append(list(tuple(zip(Teams_Seeds(event).teams_raw(), Team_Pools(event).pool_wins()))))
        pool_wins_unique_unordered = []
        for event in pool_wins:
            pool_wins_unique_unordered.append(dict([(key, sum(map(itemgetter(1), ele))) for key, ele in groupby(sorted(event, key = itemgetter(0)), key = itemgetter(0))]))
        return pool_wins_unique_unordered
    
    #https://www.geeksforgeeks.org/python-aggregate-values-by-tuple-keys/
    #ans = dict(list(Counter.update((key for key, num in test for idx in range(num)).items()))) #Removes tuples with value 0
    #Orders pool wins dictionaries by event in order of seeding
    def team_pool_wins_ordered(self):
        wins_dict_ordered = []
        for x, teams_list in enumerate(self.event_teams()):
            for y, wins_dict in enumerate(self.team_pool_wins_raw()):
                if x == y:
                    wins_dict_ordered.append(dict([(key, wins_dict[key]) for key in teams_list if key in wins_dict]))
        return wins_dict_ordered
    
    #Creates list of {teams, losses} dictionaries by event in order of pool finish
    def team_pool_losses_raw(self):
        pool_losses = []
        for event in self.pools:
            pool_losses.append(list(tuple(zip(Teams_Seeds(event).teams_raw(), Team_Pools(event).pool_losses()))))
        pool_losses_unique_unordered = []
        for event in pool_losses:
            pool_losses_unique_unordered.append(dict([(key, sum(map(itemgetter(1), ele))) for key, ele in groupby(sorted(event, key = itemgetter(0)), key = itemgetter(0))]))
        return pool_losses_unique_unordered
    
    #Orders pool wins dictionaries by event in order of seeding
    def team_pool_losses_ordered(self):
        losses_dict_ordered = []
        for x, teams_list in enumerate(self.event_teams()):
            for y, losses_dict in enumerate(self.team_pool_losses_raw()):
                if x == y:
                    losses_dict_ordered.append(dict([(key, losses_dict[key]) for key in teams_list if key in losses_dict]))
        return losses_dict_ordered
    
    def full_pool_matchups(self):
        full_pool_matchups = [Team_Pools(event).pool_matchups() for event in self.pools]
        return full_pool_matchups
    
    def full_pool_scores(self):
        full_pool_scores = [Team_Pools(event).pool_scores() for event in self.pools]
        return full_pool_scores

class Full_Bracket_Info:
    def __init__(self):
        self.brackets = Soup_Objects().brackets()
    
    def full_bracket_types_unique(self):
        full_bracket_types_unique = [Brackets(event).bracket_types_unique() for event in self.brackets]
        return full_bracket_types_unique

    def full_bracket_types(self):
        full_bracket_types = [Brackets(event).bracket_types() for event in self.brackets]
        return full_bracket_types
    
    def full_bracket_datetimes(self):
        full_bracket_datetimes = [Brackets(event).bracket_datetimes() for event in self.brackets]
        return full_bracket_datetimes

    def full_bracket_round_lengths(self):
        full_bracket_round_lengths = [Brackets(event).bracket_round_lengths() for event in self.brackets]
        return full_bracket_round_lengths

    def full_bracket_teams(self):
        full_bracket_teams = [Brackets(event).bracket_teams() for event in self.brackets]
        return full_bracket_teams
    
    def full_bracket_scores(self):
        full_bracket_scores = [Brackets(event).bracket_scores_raw() for event in self.brackets]
        return full_bracket_scores

    def full_bracket_winners(self):
        full_bracket_winners = [Counter(Brackets(bracket).bracket_winners()) for bracket in self.brackets]
        return full_bracket_winners
    
    def full_bracket_losers(self):
        full_bracket_losers = [Counter(Brackets(bracket).bracket_losers()) for bracket in self.brackets]
        return full_bracket_losers