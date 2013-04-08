#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2 as u


PRINTERS = {
    '10.233.32.8': '8100',
	'10.233.32.5': 'br8085',
    '10.233.32.3': '8500',
}


for ip, model in PRINTERS.items():
    if model == '8100':
        url = "http://%s/index.htm?cat=info&page=printerInfo" % ip
        doc = u.urlopen(url).read()
        bs = BeautifulSoup(doc)
        page = bs.findAll('dd:tableDeviceDetails')[0].getText()
        print ip, model, " - [ONLINE] Numero de paginas: ", page
    else:
        print ip, model, " - [OFFLINE]"





