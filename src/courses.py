import requests
from bs4 import BeautifulSoup

class Course:
    def __init__(self, crn: str):
        self.crn = crn
    
    def __get_registration_info(self, term: str):
        url = 'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in='
        url += term + '&crn_in=' + self.crn

        with requests.Session() as s:
            with s.get(url) as page:
                soup = BeautifulSoup(page.content, 'html.parser')
                table = soup.find('caption', string='Registration Availability').find_parent('table')

                if len(table) == 0: raise ValueError()

                data = [int(info.getText()) for info in table.findAll('td', class_='dddefault')]
                return data

    def get_registration_info(self, term: str):
        data = self.__get_registration_info(term)

        if len(data) < 6: raise ValueError()

        waitlist_data = {
            'seats': data[3],
            'taken': data[4],
            'vacant': data[5]
        }
        load = {
            'seats': data[0],
            'taken': data[1],
            'vacant': data[2],
            'waitlist': waitlist_data
        }
        return load
