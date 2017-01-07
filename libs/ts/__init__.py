#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

class Base(object):
    def __init__(self, q, ):
        if session is None:
            session = requests.Session()

        self._base_url = None


    def _fetch(self, part):
        r = self.session.get(self._base_url + part, **kwargs)
        if r and r.status_code in (200):  # check for more status.
            return r.json()
        return {}


    def clean_url(self):
        pass

    def search(q, cat=None, **kwargs):
        if kwargs:
            pass
        else:
            return urllib.quote_plus(q)

    def supported_cats(self):
        pass

    def parse_json():
        """
        dd = {'Provider': 'cardigann',
                      'BrowseURL': torrent['GUID'],
                      'DownloadURL': torrent['Link'],
                      'ReleaseName': torrent['Title'],
                      'Seeders': torrent['Seeders'],
                      'Leechers': torrent['Peers'],
                      'Size': int(torrent['Size']),
                      'Container': 'N/A',
                      'Snatched': torrent.get('Grabs')}
        """




