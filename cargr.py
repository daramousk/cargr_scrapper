# -*- coding: utf-8 -*-
import requests
import json
from pymongo import MongoClient

VEHICLE_TYPES = ['bus', 'builder', 'boat', 'bicycle', 'van', 'truck'
                 'semitruck', 'semitrailer', 'tractor', 'forklift',
                 'trailer', 'taxi', 'motorhome', 'caravan', 'airsport',
                 'radiocontrol', 'gokart', 'watersport', 'snowsport',
                 'car', 'bike']


def _import():
    database = MongoClient().cargr
    for vtype in VEHICLE_TYPES:
        _collection = database[vtype]
        page_no = 1
        listings = []
        while True:
            print 'We are searching for ', vtype
            print 'We are on page', page_no
            response = requests.post(url='''
            https://www.car.gr/mobile/search?&hash=db2a3ce6916ad24136314e335cf22e91&uuid=fd2c0ebe-4b5a-4a9a-b3c2-1e3676648664&fs=1
            ''', data='vtype={}&pg={}'.format(vtype, page_no),
            headers={'Authorization': 'Basic dGVzdDp0ZXN0',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-D722 Build/KOT49I.A1415241157)',
                     #'Host': 'ws.car.gr',
                     'Connection': 'Keep-Alive',
                     'Accept-Encoding': 'gzip'})
            print response.content
            content = json.loads(response.content)
            count_page = len(content['response']['rows'])
            rows = content['response']['rows']
            for listing in rows.iterkeys():
                listings.append(rows[listing])
            page_no += 1
            if count_page == 0:
                break
            print len(listings)
        print 'Inserting', vtype, ' into our database'
        _collection.insert_many(listings)


if __name__ == '__main__':
    _import()
