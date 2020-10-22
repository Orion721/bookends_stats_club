from bs4 import BeautifulSoup
import os
from os import listdir
from pathlib import Path

class Make_Soup:
    def __init__(self, file):
        self.file = file
        self.soup = BeautifulSoup(self.read_file(), 'html.parser')

    def read_file(self):
        file = open(self.file)
        data = file.read()
        file.close()
        return data

    def open_file(self):
        #with open(self.file) as f:
        #    file_contents = f.read()
        #return file_contents
        pass

    def event_name(self):
        tournament = self.soup.find('h1').text.split()
        tournament = tournament[:tournament.index('-')]
        tournament = ' '.join(tournament)
        return tournament

    def event_date(self):
        raw_date = self.soup.find('h2').text.split()
        return raw_date

    def event_year(self):
        event_year = self.event_date()[-1]
        return event_year

    def event_division(self):
        division_raw = self.soup.findAll("span", "mat-button-wrapper")[-1].text.split()[1]
        return division_raw

    def pools(self):
        pools = self.soup.find_all('app-schedule-pool')
        return pools

    def brackets(self):
        brackets = self.soup.find_all('app-schedule-bracket')
        return brackets
    
    def standings_tables(self):
        tables = self.soup.find_all('table')
        return tables

class Soup_Objects:
    def __init__(self):
        self.source_path = Path(__file__).parent
        self.file_path = os.path.join(self.source_path, 'ultiarchive_html\\')
        self.file_names = listdir(self.file_path)
        self.club_2010_open_brackets = Make_Soup(r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\ultiarchive_html\club_2010_nationals_open.html').brackets()

    def file_paths(self):
        file_paths = []
        for file_name in self.file_names:
            file_paths.append(self.file_path + file_name)
        return file_paths
    
    def event_names(self):
        event_names = []
        for file_path in self.file_paths():
            event_names.append(Make_Soup(file_path).event_name())
        return event_names
    
    def event_dates(self):
        event_dates = []
        for file_path in self.file_paths():
            event_dates.append(Make_Soup(file_path).event_date())
        return event_dates
    
    def event_years(self):
        event_years = []
        for file_path in self.file_paths():
            event_years.append(Make_Soup(file_path).event_year())
        return event_years
    
    def event_divisions(self):
        event_divisions = []
        for file_path in self.file_paths():
            event_divisions.append(Make_Soup(file_path).event_division())
        return event_divisions
    
    def pools(self):
        pools = []
        for file_path in self.file_paths():
            pools.append(Make_Soup(file_path).pools())
        return pools

    def brackets(self):
        brackets = []
        for file_path in self.file_paths():
            brackets.append(Make_Soup(file_path).brackets())
        return brackets