from bs4 import BeautifulSoup
import urllib2 as u
import MySQLdb

import config

# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
db = MySQLdb.connect(host, user, passwd, db)
con = db.cursor()

PRINTERS = {
    '10.233.32.8': 'HP8100-328',
	'10.233.32.5': 'BR8085-325',
    '10.233.32.3': 'HP8500-323',
}


for ip, model in PRINTERS.items():
    print "-------------------------------------------------"
    if model == 'HP8100-328':
        url = "http://%s/DevMgmt/ProductUsageDyn.xml" % ip
        doc = u.urlopen(url).read()
        bs = BeautifulSoup(doc)
        page = bs.findAll('dd:totalimpressions')[0].getText()
        print ip, model, " - [ONLINE] Numero de paginas: ", page
        #todo: split in two tables (models and page counters)
        query = "INSERT INTO printers (hostname, macaddr,serial, numpat, numpag) VALUES ('%s', '%s', '%s', '%s' ,'%s')" % ( model,"2c-76-8a-cd-95-f5","serial","018.xxxxxx",page)
        con.execute( query )

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
        print "MAC: ", ip
        print "Numero de paginas: ", page

