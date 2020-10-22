from sqlalchemy import create_engine
import pymysql
import pandas as pd
from itertools import accumulate
from collections import Counter
import calendar
from make_soup import Soup_Objects

class Event_Day_Converter:
    def __init__(self):
        self.db_connection_str = 'mysql+pymysql://root:underground@localhost/club'
        self.db_connection = create_engine(self.db_connection_str)
        self.dates = Soup_Objects().event_dates()
        self.event_ids = [1,1,1,2,2,2,4,4,4,3,3,3,8,8,9,9,11,11,11,6,6,7,10,10,10,5,5,5,15,15,15,17,17,17,14,13,13,16,16,16,12,12,12,19,19,19,23,23,23,20,20,20,22,22,22,21,21,21,18,18,18,25,25,25,29,29,29,26,26,26,28,28,28,27,27,27,24,24,24,33,33,33,35,35,35,30,30,30,34,34,34,31,31,31,32,32,32,39,39,39,41,41,41,36,36,36,40,40,40,37,37,37,38,38,38,46,46,46,48,48,48,42,42,42,47,47,47,43,43,43,45,45,45]

    def event_day_ids_df(self):
        df = pd.read_sql('SELECT ed.event_day_date, edd.event_day_id, e.event_id, LEFT(DAYNAME(ed.event_day_date), 3) as day_of_week FROM club.event_days ed INNER JOIN club.event_day_days edd ON ed.event_day_id = edd.event_day_id INNER JOIN club.events e ON edd.event_id = e.event_id ORDER BY 2, 1', con=self.db_connection)
        df.index += 1
        return df
    
    def event_day_id_dicts(self):
        event_counter = list(Counter(self.event_day_ids_df().event_id).values())
        event_day_ids = [self.event_day_ids_df().event_day_id[x - y: x] for x, y in zip(accumulate(event_counter), event_counter)]
        days_of_week = [self.event_day_ids_df().day_of_week[x - y: x] for x, y in zip(accumulate(event_counter), event_counter)]
        event_day_id_dicts = []
        for x, event in enumerate(event_day_ids):
            for y, days in enumerate(days_of_week):
                if x == y:
                    event_day_id_dicts.append(dict(zip(event, days)))
        return event_day_id_dicts
    
    def event_day_ids(self):
        event_day_ids = []
        for event_id in self.event_ids:
            for x, event_days in enumerate(self.event_day_id_dicts()):
                if x == event_id-1:
                    event_day_ids.append(event_days)
        return event_day_ids