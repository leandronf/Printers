

class Config:
  def banco():
	host="db1.set.eesc.usp.br" 
	user="printers"
	passwd="KV7MmRxEXDMR5pVE"
	db="printers"

	db = MySQLdb.connect(host, user, passwd, db)
	con = db.cursor()