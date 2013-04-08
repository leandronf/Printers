from bs4 import BeautifulSoup
import urllib2 as u

class Device:
    serial = None
    contador = None
    macaddr = None
    numpat= None
    hostname = None

devices[0] = Device()
devices[0].hostname = "HP8100-328"
devices[1].hostname = "BR8085-325"
devices[2].hostname = "HP8500-323"


#PRINTERS = {
    #'10.233.32.8': 'HP8100-328',
#	'10.233.32.5': 'BR8085-325',
 #   '10.233.32.3': 'HP8500-323',
#
#}


for device in devices

    print device.



    print "-------------------------------------------------"
    if model == 'HP8100-328':
        url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
        doc = u.urlopen(url).read()
        bs = BeautifulSoup(doc)
        page = bs.findAll('dd:totalimpressions')[0].getText()
        print ip, model, " - [ONLINE] Numero de paginas: ", page

    if model == 'HP8500-323':
        url = "http://%s/index.htm?cat=info&page=printerInfo" % ip
        doc = u.urlopen(url).read()
        bs = BeautifulSoup(doc)
        tabela = bs.find("table", id="tableDeviceDetails")
        linhas = tabela.findAll("tr")[8]
        colunas = linhas.findAll("td")[1]
        print ip, model, " - [ONLINE] Numero de paginas: ", colunas.text.strip()

    if(model == 'BR8085-325'):
        url = "http://%s/main/main.html" % ip
        doc = u.urlopen(url).read()
        bs = BeautifulSoup(doc)
        page = bs.findAll("td")[51].getText()[16:].strip()
        serial = bs.findAll("td")[47].getText()[13:].strip()
        print "Hostname : ", model
        print "Serial : ", serial
        print "IP: ",ip
        print "Numero de paginas: ",page



