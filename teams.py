import pandas as pd
from make_soup import Soup_Objects
from event_info import Full_Seeds_Pools_Info, Counter

class Teams:
    def __init__(self):
        self.teams = Full_Seeds_Pools_Info().event_teams()
        self.divisions = Soup_Objects().event_divisions()

    def event_divisions(self):
        event_divisions = []
        for division_index, division in enumerate(self.divisions):
            for team_list_index, team_list in enumerate(self.teams):
                if division_index == team_list_index:
                    event_divisions.append([division] * len(team_list))
        return event_divisions
    
    def division_ids(self):
        full_divisions = []
        division_ids = []
        for event_division in self.event_divisions():
            full_divisions.extend(event_division)
        for division in full_divisions:
            if division == 'Mixed':
                division_ids.append(1)
            elif division == 'Open':
                division_ids.append(2)
            else:
                division_ids.append(3)
        return division_ids
    
    def full_teams(self):
        full_teams = []
        for event_team in self.teams:
            full_teams.extend(event_team)
        return full_teams
    
    def teams_divisions_dict(self):
        teams_dict = dict(zip(self.full_teams(), self.division_ids()))
        teams_dict['Storm'] = 3
        return teams_dict
    
    def teams_divisions_dict_cleanup(self):
        teams = list(self.teams_divisions_dict().keys())
        teams[4] = 'The Chad Larson Experience'
        teams[43] = 'BENT'
        teams[54] = 'Mesteño'
        teams[62] = 'Odyssée'
        teams[63] = 'American Barbecue'
        teams[68] = 'Boost FC'
        teams[76] = 'Ki.e'
        teams[86] = 'Jackwagon'
        teams[92] = "D'oh! Abides"
        teams[99] = '7 Express'
        teams[105] = 'Revolution'
        teams[113] = 'PleasureTown'
        teams[127] = 'Seattle Mixtape'
        teams[129] = 'Machine'
        teams[144] = teams[144][:-1]
        teams[158] = 'Birdfruit'
        teams[160] = 'Riot'
        teams[168] = 'Freaks'
        teams[203] = 'DiG'
        teams[205] = 'Mesteño'
        teams[213] = 'Condors'
        teams[223] = teams[223][:-3] + teams[223][-1]
        teams[238] = 'Temper'
        teams[239] = 'Floodwall'
        teams[252] = 'Revolution'
        teams[257] = 'Ivy'
        teams[262] = 'Rhino Slam!'
        teams[299] = 'Smokestack'
        return teams
    
    def clean_teams_divisions_dict(self):
        clean_teams_divisions_dict = dict(zip(self.teams_divisions_dict_cleanup(), self.teams_divisions_dict().values()))
        return clean_teams_divisions_dict
    
    def team_location(self):
        team_location = ['Boston', 'New Haven', 'Atlanta', 'Minneapolis', 'Ames', 'San Francisco', 'San Francisco', 'Ann Arbor', 'Philadelphia', 'Los Angeles', 'Tucson', 'Dallas', 'Montréal', 'Triangle Area', 'Houston', 'Iowa City', 
        'Boston', 'San Francisco', 'Austin', 'Atlanta', 'Washington DC', 'Seattle', 'Denver', 'New York', 'Chicago', 'Philadelphia', 'Raleigh', 'San Diego', 'Vancouver', 'Madison', 'Columbus', 'Nashville', 
        'Seattle', 'San Francisco', 'Boston', 'Toronto', 'Washington DC', 'Vancouver', 'Raleigh', 'Denver', 'Austin', 'Chicago', 'Minneapolis', 'New York', 'San Diego', 'Atlanta', 'Montréal', 'St Louis', 'Boston',
        'Portland', 'San Francisco', 'Los Angeles', 'Morristown', 'Jacksonville', 'Denver', 'Tallahassee', 'Toronto', 'Minneapolis', 'Pittsburgh', 'SoCal', 'Eugene', 'Nashville', 'Montréal', 'Oakland', 'Missoula', 
        'Boston', 'Austin', 'Portland', 'Bay Area', 'Madison', 'San Francisco', 'Portland', 'Seattle', 'Pittsburgh', 'Bogotá', 'Salt Lake City', 'Medellín', 'Denver', 'Bogotá', 'Triangle Area', 'Seattle',
        'Dallas', 'Kansas City', 'Chicago', 'Florida', 'Poolesville', 'Boulder', 'Philadelphia', 'Washington DC', 'San Francisco', 'Asheville', 'Denver', 'Seattle', 'Portland', 'Cincinnati', 'Minneapolis', 
        'Washington DC', 'Sunnyvale', 'Tokyo', 'New York', 'Montréal', 'Bogotá', 'Copenhagen', 'Montréal', 'Edogawa-ku', 'Medellín', 'Columbus', 'Boston', 'Madison', 'Minneapolis', 'Somerville', 'Fayetteville', 
        'Ann Arbor', 'Cambridge', 'Orlando', 'Pittsburgh', 'San Diego', 'Boston', 'Vancouver', 'Nashville', 'Seattle', 'Willamette Valley', 'Pittsburgh', 'Gainesville', 'New York', 'Pittsburgh', 'Chicago',
        'Baltimore', 'Toronto', 'Bucaramanga', 'London', 'Medellín', 'London', 'Bogotá', 'St Louis', 'Des Moines', 'Chicago', 'Champaign-Urbana', 'Charlottesville', 'Portland', 'Philadelphia', 'Phoenix',
        'Princeton', 'Salt Lake City', 'Québec', 'Los Angeles', 'Dallas', 'Columbus', 'Mianus', 'Seattle', 'Chicago', 'Charleston', 'San Diego', 'Charlotte', 'Chattanooga', 'Orlando', 'Denver', 'San Luis Obispo',
        'Huntsville', 'Houston', 'Pine Apple', 'Birmingham', 'Houston', 'Baltimore', 'Austin', 'Baton Rouge', 'Saint Paul', 'Memphis', 'Fayetteville', 'Tulsa', 'Kansas City', 'Houston', 'Chicago', 'New Orleans',
        'Melbourne', 'London', 'Berlin', 'Winnipeg', 'Pittsburgh', 'Princeton', 'Seattle', 'Indianapolis', 'Cleveland', 'Lombard', 'Milwaukee', 'Toronto', 'Denver', 'Fort Collins', 'Dallas', 'Minneapolis',
        'Gainesville', 'Boston', 'Chico', 'Oakland', 'Iowa City', 'Mansfield', 'Ben Avon', 'San Francisco', 'Indianapolis', 'New York', 'Chicago', 'Somerville', 'Kansas City', 'Atlanta', 'Washington DC',
        'Salt Lake City', 'New York', 'Minneapolis', 'Bucaramanga', 'Panamá', 'Durham', 'Winnipeg', 'Cajicá', 'Boston', 'Seattle', 'West Chester', 'Phoenix', 'Durham', 'St Louis', 'Columbus', 'Baltimore',
        'Kitchener', 'Richmond', 'Madison', 'Dayton', 'Ottawa', 'Birmingham', 'Cleveland', 'Tucson', 'Indianapolis', 'Matsumoto', 'Bogotá', 'Tokyo', 'Ciudad de Mexico', 'Bologna', 'Toyota', 'Boston',
        'Boise', 'Montréal', 'Portland', 'Boston', 'Washington DC', 'New York', 'Portland', 'Oakland', 'Washington DC', 'San Francisco', 'Bozeman', 'Seattle', 'Iowa City', 'Eugene', 'Dallas',
        'St Louis', 'Boise', 'San Marcos', 'Orem', 'Vancouver', 'Seattle', 'Chicago', 'Minneapolis', 'Darmstadt', 'Tokyo', 'Tokyo', 'London', 'Osaka', 'Southeast Asia', 'West Chester', 'Florida',
        'Chicago', 'Madison', 'Halifax', 'Lombard', 'Montana', 'Asheville', 'Omaha', 'Milwaukee', 'Atlanta', 'Frederick', 'Ann Arbor', 'Durham', 'Philadelphia', 'Ferndale', 'Tampa Bay', 'Halifax', 
        'Richmond', 'Tokyo', 'Tokyo', 'Edogawa', 'Bogotá', 'Bogotá', 'Darmstadt']
        return team_location

    def team_state(self):
        team_state = ['Massachusetts', 'Connecticut', 'Georgia', 'Minnesota', 'Iowa', 'California', 'California', 'Michigan', 'Pennsylvania', 'California', 'Arizona', 'Texas', 'Quebec', 'North Carolina', 'Texas', 'Iowa', 
        'Massachusetts', 'California', 'Texas', 'Georgia', 'Washington DC', 'Washington', 'Colorado', 'New York', 'Illinois', 'Pennsylvania', 'North Carolina', 'Streetgang', 'British Columbia', 'Wisconsin', 'Ohio', 'Tennessee', 
        'Washington', 'California', 'Massachusetts', 'Ontario', 'Washington DC', 'British Columbia', 'North Carolina', 'Colorado', 'Texas', 'Illinois', 'Minnesota', 'New York', 'California', 'Georgia', 'Quebec', 'Missouri', 'Massachusetts',
        'Oregon', 'California', 'California', 'New Jersey', 'Florida', 'Colorado', 'Florida', 'Ontario', 'Minnesota', 'Philadelphia', 'California', 'Oregon', 'Tennessee', 'Quebec', 'California', 'Montana', 
        'Massachusetts', 'Texas', 'Oregon', 'California', 'Wisconsin', 'Nightlock', 'Oregon', 'Washington', 'Philadelphia', 'Colombia', 'Utah', 'Colombia', 'Colorado', 'Colombia', 'North Carolina', 'Washington',
        'Texas', 'Missouri', 'Illinois', 'Florida', 'Maryland', 'Colorado', 'Pennsylvania', 'Washington DC', 'California', 'North Carolina', 'Colorado', 'Washington', 'Oregon', 'Ohio', 'Minnesota', 
        'Washington DC', 'California', 'Japan', 'New York', 'Quebec', 'Colombia', 'Denmark', 'Quebec', 'Japan', 'Colombia', 'Ohio', 'Massachusetts', 'Wisconsin', 'Minnesota', 'Massachusetts', 'Arkansas', 
        'Michigan', 'Massachusetts', 'Florida', 'Pennsylvania', 'California', 'Massachusetts', 'British Columbia', 'Tennessee', 'Washington', 'Oregon', 'Pennsylvania', 'Florida', 'New York', 'Pennsylvania', 'Illinois',
        'Maryland', 'Ontario', 'Colombia', 'Great Britain', 'Colombia', 'Great Britain', 'Colombia', 'Missouri', 'Iowa', 'Illinois', 'Illinois', 'Virginia', 'Maine', 'Pennsylvania', 'Arizona',
        'New Jersey', 'Utah', 'Quebec', 'California', 'Texas', 'Ohio', 'Connecticut', 'Washington', 'Illinois', 'South Carolina', 'California', 'North Carolina', 'Tennessee', 'Florida', 'Colorado', 'California',
        'Alabama', 'Texas', 'Alabama', 'Alabama', 'Texas', 'Maryland', 'Texas', 'Louisiana', 'Minnesota', 'Tennessee', 'Arkansas', 'Oklahoma', 'Kansas', 'Texas', 'Illinois', 'Louisiana',
        'Australia', 'Great Britain', 'Germany', 'Manitoba', 'Pennsylvania', 'New Jersey', 'Washington', 'Indiana', 'Ohio', 'Illinois', 'Wisconsin', 'Ontario', 'Colorado', 'Colorado', 'Texas', 'Minnesota',
        'Florida', 'Massachusetts', 'California', 'California', 'Iowa', 'Massachusetts', 'Pennsylvania', 'California', 'Indiana', 'New York', 'Illinois', 'Massachusetts', 'Kansas', 'Georgia', 'Washington DC',
        'Utah', 'New York', 'Minnesota', 'Colombia', 'Panamá', 'North Carolina', 'Manitoba', 'Colombia', 'Massachusetts', 'Washington', 'Pennsylvania', 'Arizona', 'North Carolina', 'Missouri', 'Ohio', 'Maryland',
        'Ontario', 'Virginia', 'Wisconsin', 'Ohio', 'Ontario', 'Alabama', 'Ohio', 'Arizona', 'Indiana', 'Japan', 'Colombia', 'Japan', 'Mexico', 'Italy', 'Japan', 'Massachusetts',
        'Idaho', 'Quebec', 'Oregon', 'Massachusetts', 'Washington DC', 'New York', 'Oregon', 'California', 'Washington DC', 'California', 'Montana', 'Washington', 'Iowa', 'Oregon', 'Texas',
        'Missouri', 'Idaho', 'Texas', 'Utah', 'British Columbia', 'Washington', 'Illinois', 'Minnesota', 'Germany', 'Japan', 'Japan', 'Great Britain', 'Japan', 'Southeast Asia', 'Pennsylvania', 'Florida',
        'Illinois', 'Wisconsin', 'Nova Scotia', 'Illinois', 'Montana', 'North Carolina', 'Nebraska', 'Wisconsin', 'Georgia', 'Maryland', 'Michigan', 'North Carolina', 'Pennsylvania', 'Michigan', 'Florida', 'Nova Scotia', 
        'Virginia', 'Japan', 'Japan', 'Japan', 'Colombia', 'Colombia', 'Germany']
        return team_state

    def team_region(self):
        team_region = ['Northeast', 'Northeast', 'Southeast', 'North Central', 'North Central', 'Southwest', 'Southwest', 'Great Lakes', 'Mid-Atlantic', 'Southwest', 'Southwest', 'South Central', 'Northeast', 'Southeast', 'South Central', 'North Central', 
        'Northeast', 'Southwest', 'South Central', 'Southeast', 'Mid-Atlantic', 'Northwest', 'South Central', 'Northeast', 'Great Lakes', 'Mid-Atlantic', 'Southeast', 'Southwest', 'Northwest', 'North Central', 'Great Lakes', 'Southeast',
        'Northwest', 'Southwest', 'Northeast', 'Northeast', 'Mid-Atlantic', 'Northeast', 'Southeast', 'South Central', 'South Central', 'Great Lakes', 'North Central', 'Northeast', 'Southwest', 'Southeast', 'Northeast', 'North Central', 'Northeast',
        'Northwest', 'Southwest', 'Southwest', 'Mid-Atlantic', 'Southeast', 'South Central', 'Southeast', 'Northeast', 'North Central', 'Mid-Atlantic', 'Southwest', 'Northwest', 'Southeast', 'Northeast', 'Southwest', 'Northwest', 
        'Northeast', 'South Central', 'Northwest', 'Southwest', 'North Central', 'Southwest', 'Northwest', 'Northwest', 'Mid-Atlantic', 'International', 'Northwest', 'International', 'South Central', 'International', 'Southeast', 'Northwest',
        'South Central', 'North Central', 'Great Lakes', 'Southeast', 'Mid-Atlantic', 'South Central', 'Mid-Atlantic', 'Mid-Atlantic', 'Southwest', 'Southeast', 'South Central', 'Northwest', 'Northwest', 'Great Lakes', 'North Central', 
        'Mid-Atlantic', 'Southwest', 'International', 'Northeast', 'Northeast', 'International', 'International', 'Northeast', 'International', 'International', 'Great Lakes', 'Northeast', 'North Central', 'North Central', 'Northeast', 'South Central', 
        'Great Lakes', 'Northeast', 'Southeast', 'Mid-Atlantic', 'Southwest', 'Northeast', 'Northwest', 'Southeast', 'Northwest', 'Northwest', 'Mid-Atlantic', 'Southeast', 'Northeast', 'Mid-Atlantic', 'Great Lakes',
        'Mid-Atlantic', 'Northeast', 'International', 'International', 'International', 'International', 'International', 'North Central', 'North Central', 'Great Lakes', 'Great Lakes', 'Mid-Atlantic', 'Northeast', 'Mid-Atlantic', 'Southwest',
        'Mid-Atlantic', 'Northwest', 'Northeast', 'Southwest', 'South Central', 'Great Lakes', 'Northeast', 'Northwest', 'Great Lakes', 'Southeast', 'Southwest', 'Southeast', 'Southeast', 'Southeast', 'South Central', 'Southwest',
        'Southeast', 'South Central', 'Southeast', 'Southeast', 'South Central', 'Mid-Atlantic', 'South Central', 'Southeast', 'North Central', 'Southeast', 'South Central', 'South Central', 'North Central', 'South Central', 'Great Lakes', 'Southeast',
        'International', 'International', 'International', 'North Central', 'Mid-Atlantic', 'Mid-Atlantic', 'Northwest', 'Great Lakes', 'Great Lakes', 'Great Lakes', 'North Central', 'Northeast', 'South Central', 'South Central', 'South Central', 'North Central',
        'Southeast', 'Northeast', 'Southwest', 'Southwest', 'North Central', 'Northeast', 'Mid-Atlantic', 'Southwest', 'Great Lakes', 'Northeast', 'Great Lakes', 'Northeast', 'North Central', 'Southeast', 'Mid-Atlantic',
        'Northwest', 'Northeast', 'North Central', 'International', 'International', 'Southeast', 'North Central', 'International', 'Northeast', 'Northwest', 'Mid-Atlantic', 'Southwest', 'Southeast', 'North Central', 'Great Lakes', 'Mid-Atlantic',
        'Northeast', 'Mid-Atlantic', 'North Central', 'Great Lakes', 'Northeast', 'Southeast', 'Great Lakes', 'Southwest', 'Great Lakes', 'International', 'International', 'International', 'International', 'International', 'International', 'Northeast',
        'Northwest', 'Northeast', 'Northwest', 'Northeast', 'Mid-Atlantic', 'Northeast', 'Northwest', 'Southwest', 'Mid-Atlantic', 'Southwest', 'Northwest', 'Northwest', 'North Central', 'Northwest', 'South Central',
        'North Central', 'Northwest', 'South Central', 'Northwest', 'Northwest', 'Northwest', 'Great Lakes', 'North Central', 'International', 'International', 'International', 'International', 'International', 'International', 'Mid-Atlantic', 'Southeast',
        'Great Lakes', 'North Central', 'Northeast', 'Great Lakes', 'Northwest', 'Southeast', 'North Central', 'North Central', 'Southeast', 'Mid-Atlantic', 'Great Lakes', 'Southeast', 'Mid-Atlantic', 'Great Lakes', 'Southeast', 'Northeast', 
        'Mid-Atlantic', 'International', 'International', 'International', 'International', 'International', 'International']
        region_ids = []
        for region in team_region:
            if region == 'Great Lakes':
                region_ids.extend([1])
            elif region == 'Mid-Atlantic':
                region_ids.extend([2])
            elif region == 'North Central':
                region_ids.extend([3])
            elif region == 'Northeast':
                region_ids.extend([4])
            elif region == 'Northwest':
                region_ids.extend([5])
            elif region == 'South Central':
                region_ids.extend([6])
            elif region == 'Southeast':
                region_ids.extend([7])
            elif region == 'Southwest':
                region_ids.extend([8])
            elif region == 'International':
                region_ids.extend([9])
        return region_ids
    
    def region_df(self):
        unique_regions = ['Great Lakes', 'Mid-Atlantic', 'North Central', 'Northeast', 'Northwest', 'South Central', 'Southeast', 'Southwest', 'International']
        region_columns = {'region': unique_regions}
        region_df = pd.DataFrame(data=region_columns)
        region_df.index += 1
        return region_df

    def teams_dataframe(self):
        team_names = [*self.clean_teams_divisions_dict()]
        team_divisions = list(self.clean_teams_divisions_dict().values())
        teams_columns = {'team_name': team_names, 'team_location': self.team_location(), 'team_state': self.team_state(), 'division_id': team_divisions, 'region_id': self.team_region()}
        df = pd.DataFrame(data=teams_columns)
        df.index += 1
        return df