#! /usr/bin/env python3

import urllib2
from xml.dom import minidom


def main():

    county = 'FLC086'  # County code
    url = 'http://alerts.weather.gov/cap/wwaatmget.php?x={COUNTY_CODE}&y=1'.format(COUNTY_CODE=county)
    
    site = urllib2.urlopen(url)
    data = site.read()

    xml = minidom.parseString(data)
    feed = xml.getElementsByTagName('feed')[0]
    entry = feed.getElementsByTagName('entry')[0]
    title = entry.getElementsByTagName('title')
    update = entry.getElementsByTagName('updated')
    

    print("Updated on: {}".format(update[0].firstChild.data))
    print(title[0].firstChild.data)

if __name__ == '__main__':
    main()
