import urllib2 as u



url = "http://%s/DevMgmt/ProductUsageDyn.xml" % '10.233.32.8'

try:
    doc = u.urlopen(url).read()
    up = True
except:
    up = False

if up:
    print 'online'
else:
    print 'offline'





