from . import base_requester
from config import app_properties
from model.model import Location, Truck


class KakaoApiRequester:

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    def __init__(self):
        headers = self.headers.copy()
        headers['X-Auth-Token'] = app_properties.X_AUTH_TOKEN
        data = {'problem': app_properties.PROBLEM}
        res = base_requester.post('/start', headers=headers, data=data)
        print('====== start ======')
        print('problem: {}'.format(res['problem']))
        print('===================')
        self.headers['Authorization'] = res['auth_key']

    def locations(self):
        locations = base_requester.get('/locations', headers=self.headers)['locations']
        return [Location(location) for location in locations]

    def trucks(self):
        trucks = base_requester.get('/trucks', headers=self.headers)['trucks']
        return [Truck(truck) for truck in trucks]

    def simulate(self, data):
        data = {'commands': data}
        return base_requester.put('/simulate', headers=self.headers, data=data)

    def score(self):
        return base_requester.get('/score', headers=self.headers)
