# cardigann

import logging
import urllib

import requests


import htpc
from htpc.helpers import fix_basepath, striphttp


logger = logging.getLogger('modules.torrentsearch.cardigann')


def search(query, cat):

    # http://localhost:5060/torznab/aggregate/api?apikey=76d1fd301dae19a578d3f134554a4306&format=json&q=solsidan&t=search
    host = htpc.settings.get('torrents_cardigann_host').rstrip('/')
    url = '%s/torznab/aggregate/api?apikey=%s&format=json&q=%s&t=search' % (host,
                                                                            htpc.settings.get('torrents_cardigann_apikey'),
                                                                            urllib.quote_plus(query))
    print url

    r = requests.get(url)
    results = []

    try:
        json = r.json()
        if json:

            for torrent in json.get('Items'):
                dd = {'Provider': 'cardigann',
                      'BrowseURL': torrent['GUID'],
                      'DownloadURL': torrent['Link'],
                      'ReleaseName': torrent['Title'],
                      'Seeders': torrent['Seeders'],
                      'Leechers': torrent['Peers'],
                      'Size': int(torrent['Size']),
                      'Container': 'N/A',
                      'Snatched': torrent.get('Grabs')}

                results.append(dd)

    except Exception as e:
        logger.exception('Some weird shit happend with cardigann %s' % e)


    return results

"""
                    {
      "Site": "eztv",
      "Title": "James Corden 2017 01 05 Jamie Foxx HDTV x264-SORNY [eztv]",
      "Description": "",
      "GUID": "https://eztv.ag/ep/177498/james-corden-2017-01-05-jamie-foxx-hdtv-x264-sorny/",
      "Comments": "https://eztv.ag/ep/177498/james-corden-2017-01-05-jamie-foxx-hdtv-x264-sorny/",
      "Link": "http://localhost:5060/download/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsIjoiaHR0cHM6Ly9lenR2LmFnL2VwLzE3NzQ5OC9qYW1lcy1jb3JkZW4tMjAxNy0wMS0wNS1qYW1pZS1mb3h4LWhkdHYteDI2NC1zb3JueS8iLCJuYmYiOjE0ODM3NDIyNDksInMiOiJlenR2In0.bkXi1Z3BHLkyAYgd3k-q93yt1HVYJ7EVnR6lWQmnm9g/James+Corden+2017+01+05+Jamie+Foxx+HDTV+x264-SORNY+%5Beztv%5D.torrent",
      "Category": 5000,
      "Size": 447120000,
      "Files": 0,
      "Grabs": 0,
      "PublishDate": "2017-01-06T23:30:05.3428512+01:00",
      "Seeders": 0,
      "Peers": 0,
      "MinimumRatio": 1,
      "MinimumSeedTime": 172800000000000,
      "DownloadVolumeFactor": 0,
      "UploadVolumeFactor": 0
    },
"""