from make_soup import Make_Soup, BeautifulSoup

class Raw_Standings:
    standings = {'club_2010_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2010_nationals_standings.html',
    'club_2011_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2011_nationals_standings.html',
    'club_2012_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2012_nationals_standings.html',
    'club_2012_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2012_us_open_standings.html',
    'club_2013_es_challenge_co_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_es_challenge_co_standings.html',
    'club_2013_es_challenge_wa_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_es_challenge_wa_standings.html',
    'club_2013_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_nationals_standings.html',
    'club_2013_pe_challenge_ga_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_pe_challenge_ga_standings.html',
    'club_2013_pe_challenge_pa_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_pe_challenge_pa_standings.html',
    'club_2013_pf_finale_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_pf_finale_standings.html',
    'club_2013_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2013_us_open_standings.html',
    'club_2014_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_es_challenge_standings.html',
    'club_2014_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_nationals_standings.html',
    'club_2014_pe_challenge_ny_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_pe_challenge_ny_standings.html',
    'club_2014_pe_challenge_va_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_pe_challenge_va_standings.html',
    'club_2014_pf_finale_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_pf_finale_standings.html',
    'club_2014_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2014_us_open_standings.html',
    'club_2015_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_es_challenge_standings.html',
    'club_2015_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_nationals_standings.html',
    'club_2015_pe_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_pe_challenge_standings.html',
    'club_2015_pf_finale_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_pf_finale_standings.html',
    'club_2015_sf_invite_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_sf_invite_standings.html',
    'club_2015_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2015_us_open_standings.html',
    'club_2016_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_es_challenge_standings.html',
    'club_2016_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_nationals_standings.html',
    'club_2016_pe_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_pe_challenge_standings.html',
    'club_2016_pf_finale_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_pf_finale_standings.html',
    'club_2016_sf_invite_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_sf_invite_standings.html',
    'club_2016_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2016_us_open_standings.html',
    'club_2017_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_es_challenge_standings.html',
    'club_2017_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_nationals_standings.html',
    'club_2017_pe_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_pe_challenge_standings.html',
    'club_2017_pro_championships_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_pro_championships_standings.html',
    'club_2017_sf_invite_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_sf_invite_standings.html',
    'club_2017_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2017_us_open_standings.html',
    'club_2018_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_es_challenge_standings.html',
    'club_2018_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_nationals_standings.html',
    'club_2018_pe_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_pe_challenge_standings.html',
    'club_2018_pro_championships_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_pro_championships_standings.html',
    'club_2018_sf_invite_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_sf_invite_standings.html',
    'club_2018_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2018_us_open_standings.html',
    'club_2019_es_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_es_challenge_standings.html',
    'club_2019_nationals_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_nationals_standings.html',
    'club_2019_pe_challenge_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_pe_challenge_standings.html',
    'club_2019_pro_championships_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_pro_championships_standings.html',
    'club_2019_sf_invite_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_sf_invite_standings.html',
    'club_2019_us_open_standings': r'C:\Users\hunte\Desktop\bookends\ultiarchive_webscraper\standings_html\club_2019_us_open_standings.html'}

class Standings:
    event_standings = {'club_2010_nationals_mixed_standings': Make_Soup(Raw_Standings.standings.get('club_2010_nationals_standings')).standings_tables()[0]
    ,'club_2010_nationals_open_standings': Make_Soup(Raw_Standings.standings.get('club_2010_nationals_standings')).standings_tables()[1]
    ,'club_2010_nationals_womxns_standings': Make_Soup(Raw_Standings.standings.get('club_2010_nationals_standings')).standings_tables()[2]
    ,'club_2011_nationals_mixed_standings': Make_Soup(Raw_Standings.standings.get('club_2011_nationals_standings')).standings_tables()[0]
    ,'club_2011_nationals_open_standings': Make_Soup(Raw_Standings.standings.get('club_2011_nationals_standings')).standings_tables()[1]
    ,'club_2011_nationals_womxns_standings': Make_Soup(Raw_Standings.standings.get('club_2011_nationals_standings')).standings_tables()[2]
    ,'club_2012_nationals_mixed_standings': Make_Soup(Raw_Standings.standings.get('club_2012_nationals_standings')).standings_tables()[0]
    ,'club_2012_nationals_open_standings': Make_Soup(Raw_Standings.standings.get('club_2012_nationals_standings')).standings_tables()[1]
    ,'club_2012_nationals_womxns_standings': Make_Soup(Raw_Standings.standings.get('club_2012_nationals_standings')).standings_tables()[2]
    ,'club_2012_us_open_mixed_standings': Make_Soup(Raw_Standings.standings.get('club_2012_us_open_standings')).standings_tables()[0]
    ,'club_2012_us_open_open_standings': Make_Soup(Raw_Standings.standings.get('club_2012_us_open_standings')).standings_tables()[1]
    ,'club_2012_us_open_womxns_standings': Make_Soup(Raw_Standings.standings.get('club_2012_us_open_standings')).standings_tables()[2]
    ,'club_2013_es_challenge_co_open': Make_Soup(Raw_Standings.standings.get('club_2013_es_challenge_co_standings')).standings_tables()[0]
    ,'club_2013_es_challenge_co_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_es_challenge_co_standings')).standings_tables()[1]
    ,'club_2013_es_challenge_wa_mixed': Make_Soup(Raw_Standings.standings.get('club_2013_es_challenge_wa_standings')).standings_tables()[0]
    ,'club_2013_es_challenge_wa_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_es_challenge_wa_standings')).standings_tables()[1]
    ,'club_2013_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2013_nationals_standings')).standings_tables()[0]
    ,'club_2013_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2013_nationals_standings')).standings_tables()[1]
    ,'club_2013_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_nationals_standings')).standings_tables()[2]
    ,'club_2013_pe_challenge_ga_open': Make_Soup(Raw_Standings.standings.get('club_2013_pe_challenge_ga_standings')).standings_tables()[0]
    ,'club_2013_pe_challenge_ga_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_pe_challenge_ga_standings')).standings_tables()[1]
    ,'club_2013_pe_challenge_pa_mixed': Make_Soup(Raw_Standings.standings.get('club_2013_pe_challenge_pa_standings')).standings_tables()[0]
    ,'club_2013_pf_finale_mixed': Make_Soup(Raw_Standings.standings.get('club_2013_pf_finale_standings')).standings_tables()[0]
    ,'club_2013_pf_finale_open': Make_Soup(Raw_Standings.standings.get('club_2013_pf_finale_standings')).standings_tables()[1]
    ,'club_2013_pf_finale_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_pf_finale_standings')).standings_tables()[2]
    ,'club_2013_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2013_us_open_standings')).standings_tables()[0]
    ,'club_2013_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2013_us_open_standings')).standings_tables()[1]
    ,'club_2013_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2013_us_open_standings')).standings_tables()[2]
    ,'club_2014_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2014_es_challenge_standings')).standings_tables()[0]
    ,'club_2014_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2014_es_challenge_standings')).standings_tables()[1]
    ,'club_2014_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2014_es_challenge_standings')).standings_tables()[2]
    ,'club_2014_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2014_nationals_standings')).standings_tables()[0]
    ,'club_2014_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2014_nationals_standings')).standings_tables()[1]
    ,'club_2014_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2014_nationals_standings')).standings_tables()[2]
    ,'club_2014_pe_challenge_ny_mixed': Make_Soup(Raw_Standings.standings.get('club_2014_pe_challenge_ny_standings')).standings_tables()[0]
    ,'club_2014_pe_challenge_va_open': Make_Soup(Raw_Standings.standings.get('club_2014_pe_challenge_va_standings')).standings_tables()[0]
    ,'club_2014_pe_challenge_va_womxns': Make_Soup(Raw_Standings.standings.get('club_2014_pe_challenge_va_standings')).standings_tables()[1]
    ,'club_2014_pf_finale_mixed': Make_Soup(Raw_Standings.standings.get('club_2014_pf_finale_standings')).standings_tables()[0]
    ,'club_2014_pf_finale_open': Make_Soup(Raw_Standings.standings.get('club_2014_pf_finale_standings')).standings_tables()[1]
    ,'club_2014_pf_finale_womxns': Make_Soup(Raw_Standings.standings.get('club_2014_pf_finale_standings')).standings_tables()[2]
    ,'club_2014_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2014_us_open_standings')).standings_tables()[0]
    ,'club_2014_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2014_us_open_standings')).standings_tables()[1]
    ,'club_2014_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2014_us_open_standings')).standings_tables()[2]
    ,'club_2015_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_es_challenge_standings')).standings_tables()[0]
    ,'club_2015_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2015_es_challenge_standings')).standings_tables()[1]
    ,'club_2015_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_es_challenge_standings')).standings_tables()[2]
    ,'club_2015_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_nationals_standings')).standings_tables()[0]
    ,'club_2015_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2015_nationals_standings')).standings_tables()[1]
    ,'club_2015_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_nationals_standings')).standings_tables()[2]
    ,'club_2015_pe_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_pe_challenge_standings')).standings_tables()[0]
    ,'club_2015_pe_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2015_pe_challenge_standings')).standings_tables()[1]
    ,'club_2015_pe_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_pe_challenge_standings')).standings_tables()[2]
    ,'club_2015_pf_finale_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_pf_finale_standings')).standings_tables()[0]
    ,'club_2015_pf_finale_open': Make_Soup(Raw_Standings.standings.get('club_2015_pf_finale_standings')).standings_tables()[1]
    ,'club_2015_pf_finale_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_pf_finale_standings')).standings_tables()[2]
    ,'club_2015_sf_invite_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_sf_invite_standings')).standings_tables()[0]
    ,'club_2015_sf_invite_open': Make_Soup(Raw_Standings.standings.get('club_2015_sf_invite_standings')).standings_tables()[1]
    ,'club_2015_sf_invite_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_sf_invite_standings')).standings_tables()[2]
    ,'club_2015_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2015_us_open_standings')).standings_tables()[0]
    ,'club_2015_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2015_us_open_standings')).standings_tables()[1]
    ,'club_2015_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2015_us_open_standings')).standings_tables()[2]
    ,'club_2016_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_es_challenge_standings')).standings_tables()[0]
    ,'club_2016_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2016_es_challenge_standings')).standings_tables()[1]
    ,'club_2016_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_es_challenge_standings')).standings_tables()[2]
    ,'club_2016_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_nationals_standings')).standings_tables()[0]
    ,'club_2016_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2016_nationals_standings')).standings_tables()[1]
    ,'club_2016_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_nationals_standings')).standings_tables()[2]
    ,'club_2016_pe_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_pe_challenge_standings')).standings_tables()[0]
    ,'club_2016_pe_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2016_pe_challenge_standings')).standings_tables()[1]
    ,'club_2016_pe_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_pe_challenge_standings')).standings_tables()[2]
    ,'club_2016_pf_finale_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_pf_finale_standings')).standings_tables()[0]
    ,'club_2016_pf_finale_open': Make_Soup(Raw_Standings.standings.get('club_2016_pf_finale_standings')).standings_tables()[1]
    ,'club_2016_pf_finale_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_pf_finale_standings')).standings_tables()[2]
    ,'club_2016_sf_invite_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_sf_invite_standings')).standings_tables()[0]
    ,'club_2016_sf_invite_open': Make_Soup(Raw_Standings.standings.get('club_2016_sf_invite_standings')).standings_tables()[1]
    ,'club_2016_sf_invite_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_sf_invite_standings')).standings_tables()[2]
    ,'club_2016_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2016_us_open_standings')).standings_tables()[0]
    ,'club_2016_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2016_us_open_standings')).standings_tables()[1]
    ,'club_2016_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2016_us_open_standings')).standings_tables()[2]
    ,'club_2017_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_es_challenge_standings')).standings_tables()[0]
    ,'club_2017_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2017_es_challenge_standings')).standings_tables()[1]
    ,'club_2017_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_es_challenge_standings')).standings_tables()[2]
    ,'club_2017_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_nationals_standings')).standings_tables()[0]
    ,'club_2017_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2017_nationals_standings')).standings_tables()[1]
    ,'club_2017_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_nationals_standings')).standings_tables()[2]
    ,'club_2017_pe_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_pe_challenge_standings')).standings_tables()[0]
    ,'club_2017_pe_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2017_pe_challenge_standings')).standings_tables()[1]
    ,'club_2017_pe_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_pe_challenge_standings')).standings_tables()[2]
    ,'club_2017_pro_championships_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_pro_championships_standings')).standings_tables()[0]
    ,'club_2017_pro_championships_open': Make_Soup(Raw_Standings.standings.get('club_2017_pro_championships_standings')).standings_tables()[1]
    ,'club_2017_pro_championships_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_pro_championships_standings')).standings_tables()[2]
    ,'club_2017_sf_invite_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_sf_invite_standings')).standings_tables()[0]
    ,'club_2017_sf_invite_open': Make_Soup(Raw_Standings.standings.get('club_2017_sf_invite_standings')).standings_tables()[1]
    ,'club_2017_sf_invite_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_sf_invite_standings')).standings_tables()[2]
    ,'club_2017_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2017_us_open_standings')).standings_tables()[0]
    ,'club_2017_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2017_us_open_standings')).standings_tables()[1]
    ,'club_2017_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2017_us_open_standings')).standings_tables()[2]
    ,'club_2018_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_es_challenge_standings')).standings_tables()[0]
    ,'club_2018_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2018_es_challenge_standings')).standings_tables()[1]
    ,'club_2018_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_es_challenge_standings')).standings_tables()[2]
    ,'club_2018_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_nationals_standings')).standings_tables()[0]
    ,'club_2018_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2018_nationals_standings')).standings_tables()[1]
    ,'club_2018_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_nationals_standings')).standings_tables()[2]
    ,'club_2018_pe_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_pe_challenge_standings')).standings_tables()[0]
    ,'club_2018_pe_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2018_pe_challenge_standings')).standings_tables()[1]
    ,'club_2018_pe_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_pe_challenge_standings')).standings_tables()[2]
    ,'club_2018_pro_championships_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_pro_championships_standings')).standings_tables()[0]
    ,'club_2018_pro_championships_open': Make_Soup(Raw_Standings.standings.get('club_2018_pro_championships_standings')).standings_tables()[1]
    ,'club_2018_pro_championships_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_pro_championships_standings')).standings_tables()[2]
    ,'club_2018_sf_invite_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_sf_invite_standings')).standings_tables()[0]
    ,'club_2018_sf_invite_open': Make_Soup(Raw_Standings.standings.get('club_2018_sf_invite_standings')).standings_tables()[1]
    ,'club_2018_sf_invite_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_sf_invite_standings')).standings_tables()[2]
    ,'club_2018_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2018_us_open_standings')).standings_tables()[0]
    ,'club_2018_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2018_us_open_standings')).standings_tables()[1]
    ,'club_2018_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2018_us_open_standings')).standings_tables()[2]
    ,'club_2019_es_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_es_challenge_standings')).standings_tables()[0]
    ,'club_2019_es_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2019_es_challenge_standings')).standings_tables()[1]
    ,'club_2019_es_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_es_challenge_standings')).standings_tables()[2]
    ,'club_2019_nationals_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_nationals_standings')).standings_tables()[0]
    ,'club_2019_nationals_open': Make_Soup(Raw_Standings.standings.get('club_2019_nationals_standings')).standings_tables()[1]
    ,'club_2019_nationals_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_nationals_standings')).standings_tables()[2]
    ,'club_2019_pe_challenge_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_pe_challenge_standings')).standings_tables()[0]
    ,'club_2019_pe_challenge_open': Make_Soup(Raw_Standings.standings.get('club_2019_pe_challenge_standings')).standings_tables()[1]
    ,'club_2019_pe_challenge_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_pe_challenge_standings')).standings_tables()[2]
    ,'club_2019_pro_championships_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_pro_championships_standings')).standings_tables()[0]
    ,'club_2019_pro_championships_open': Make_Soup(Raw_Standings.standings.get('club_2019_pro_championships_standings')).standings_tables()[1]
    ,'club_2019_pro_championships_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_pro_championships_standings')).standings_tables()[2]
    ,'club_2019_sf_invite_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_sf_invite_standings')).standings_tables()[0]
    ,'club_2019_sf_invite_open': Make_Soup(Raw_Standings.standings.get('club_2019_sf_invite_standings')).standings_tables()[1]
    ,'club_2019_sf_invite_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_sf_invite_standings')).standings_tables()[2]
    ,'club_2019_us_open_mixed': Make_Soup(Raw_Standings.standings.get('club_2019_us_open_standings')).standings_tables()[0]
    ,'club_2019_us_open_open': Make_Soup(Raw_Standings.standings.get('club_2019_us_open_standings')).standings_tables()[1]
    ,'club_2019_us_open_womxns': Make_Soup(Raw_Standings.standings.get('club_2019_us_open_standings')).standings_tables()[2]}

class Full_Standings:
    def __init__(self):
        self.standings = Standings.event_standings.values()
    
    def standings_teams(self):
        teams_raw = []
        for value in self.standings:
            teams_raw.append(value.find_all('a'))
        teams = [[x.text for x in event][1:] for event in teams_raw]
        return teams
    
    def standings_results(self):
        results_raw = []
        for value in self.standings:
            results_raw.append(value.find_all('td'))
        results = [list(map(int, [x.text for x in event if len(x) <= 2])) for event in results_raw]
        return results
    
    def standings_dicts(self):
        standings_dicts = []
        for x, teams in enumerate(self.standings_teams()):
            for y, results in enumerate(self.standings_results()):
                if x == y:
                    standings_dicts.append(dict(zip(teams, results)))
        return standings_dicts