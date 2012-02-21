metadata = {
    'name': 'Montana',
    'abbreviation': 'mt',
    'legislature_name': 'Montana Legislature',
    'upper_chamber_name': 'Senate',
    'lower_chamber_name': 'House of Representatives',
    'upper_chamber_title': 'Senator',
    'lower_chamber_title': 'Representative',
    'upper_chamber_term': 4,
    'lower_chamber_term': 2,
    'terms': [
        {'name': '2011-2012',
         'sessions': ['2011'],
         'session_number': '62nd',
         'start_year': 2011, 'end_year': 2012},
    ],
    'session_details': {
        '2011': {'display_name': '2011 Regular Session',
                 'years': [2011, 2012],
                 '_scraped_name': '2011 Regular Session',
                },
    },
    'feature_flags': [],
    '_ignored_scraped_sessions': ['2009 Regular Session',
                                  '2007 Special     Session',
                                  '2007 Regular Session',
                                  '2005 Special     Session',
                                  '2005 Regular Session',
                                  '2003 Regular Session',
                                  '2002 Special     Session',
                                  '2001 Regular Session',
                                  '2000 Special     Session',
                                  '1999 Regular Session',
                                  '1999 Special     Session']
}

def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://leg.mt.gov/css/bills/Default.asp',
        "//td[@id='cont']/ul/li/a/text()")

