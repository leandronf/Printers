#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2 as u


PRINTERS = {
    '10.233.32.8': '8100',
	'10.233.32.5': 'br8085',
}

def VerificaConexao(ip,model):
    if model =='8100':
        url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
    if model =='br8085':
        url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip

    try:
        doc = u.urlopen(url).read()
        up = True
    except:
        up = False

    if up:
        return True
    else:
        return False



for ip, model in PRINTERS.items():
    if VerificaConexao(ip, model):
        if model == '8100':
            url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
            doc = u.urlopen(url).read()
            bs = BeautifulSoup(doc)
            page = bs.findAll('dd:totalimpressions')[0].getText()
        print ip, model, " - [ONLINE] Numero de paginas: ", page
    else:
        print ip, model, " - [OFFLINE]"





