#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2 as u


PRINTERS = {
    '10.233.32.8': 'HP8100-328',
	'10.233.32.5': 'BR8085-325',
    '10.233.32.3': 'HP8500-323',
}

def VerificaConexao(ip,model):
    if model =='HP8100-328':
        url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
    if model =='BR8085-325':
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
        if model == 'HP8100-328':
            url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
            doc = u.urlopen(url).read()
            bs = BeautifulSoup(doc)
            page = bs.findAll('dd:totalimpressions')[0].getText()
            #page = bs.findAll("td")[51].getText()[16:].strip()
            print "Hostname : ", model
            #print "Serial : ", serial
            print "MAC: ", ip
            print "Numero de paginas: ", page
    else:
        print ip, model, " - [OFFLINE]"





