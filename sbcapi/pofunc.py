from flask import Flask, jsonify, Blueprint
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sbc'
app.config['MYSQL_DB'] = 'aimsdb3'
mysql = MySQL(app)

def get_po(trno):
	if trno == 'last':
		with mysql.connection.cursor() as cur:
			cur.execute('''select
				cntnum.center, head.trno, head.docno, client.client, head.terms, head.cur, head.forex, head.yourref, head.ourref,
				left(head.dateid,10) as dateid, head.clientname, address, shipto,head.rem,head.agent,head.wh as whid,
				warehouse.clientname as wh,left(head.due,10) as due,client.groupid,head.shipto, head.controlno, head.isimport
				FROM pohead as head
				left join cntnum on cntnum.trno=head.trno
				left join client on head.client=client.client
				left join client as agent on head.agent=agent.client
				left join client as warehouse on warehouse.client=head.wh
				order by head.trno desc limit 1''')
			result = cur.fetchall()
			cur.close()
	else:
		with mysql.connection.cursor() as cur:
			cur.execute('''select
				cntnum.center, head.trno, head.docno, client.client, head.terms, head.cur, head.forex, head.yourref, head.ourref,
				left(head.dateid,10) as dateid, head.clientname, address, shipto,head.rem,head.agent,head.wh as whid,
				warehouse.clientname as wh,left(head.due,10) as due,client.groupid,head.shipto, head.controlno, head.isimport
				FROM pohead as head
				left join cntnum on cntnum.trno=head.trno
				left join client on head.client=client.client
				left join client as agent on head.agent=agent.client
				left join client as warehouse on warehouse.client=head.wh
				where head.trno = %s''', [trno])
			result = cur.fetchall()
			cur.close()
	
	return jsonify(pojson(result))


def get_all_po():
	with mysql.connection.cursor() as cur:
		cur.execute('''select
			cntnum.center, head.trno, head.docno, client.client, head.terms, head.cur, head.forex, head.yourref, head.ourref,
			left(head.dateid,10) as dateid, head.clientname, address, shipto,head.rem,head.agent,head.wh as whid,
			warehouse.clientname as wh,left(head.due,10) as due,client.groupid,head.shipto, head.controlno, head.isimport
			FROM pohead as head
			left join cntnum on cntnum.trno=head.trno
			left join client on head.client=client.client
			left join client as agent on head.agent=agent.client
			left join client as warehouse on warehouse.client=head.wh
			order by head.trno''')
		result = cur.fetchall()
		cur.close()
	return jsonify(pojson(result))


def get_po_stock(trno):
	with mysql.connection.cursor() as cur:
		cur.execute('''select postock.trno, postock.line, postock.barcode, postock.itemname, item.itemid,
			round(postock.rrcost,2) as rrcost,
			round(postock.cost,2) as cost, postock.uom, postock.disc,
			round(postock.rrqty,2) as rrqty,
			round(postock.qty,2) as qty,
			round(postock.ext,2) as ext, ifnull(postock.void,0) as void, postock.wh as whcode,
			round(postock.qa / case when ifnull(uom.factor,0) = 0 then 1 else uom.factor end,2) as qa,
			postock.refx, postock.linex, postock.ref, postock.length, postock.width, postock.wh, postock.rem, ifnull(uom.factor,1) as uomfactor
			from (postock left join item on item.barcode = postock.barcode) left join uom on uom.itemid = item.itemid and uom.uom = postock.uom where trno = %s 
			''', [trno])
		result = cur.fetchall()
		cur.close()
	postock = []
	for row in result:
		waw = {
			'trno': 	row[0],
			'line': 	row[1],
			'barcode':	row[2],
			'itemname': row[3],
			'itemid':	row[4],
			'rrcost':	row[5],
			'cost':		row[6],
			'uom':		row[7],
			'disc':		row[8],
			'rrqty':	row[9],
			'qty':		row[10],
			'ext':		row[11],
			'void':		row[12],
			'whcode':	row[13],
			'qa':		row[14],
			'refx':		row[15],
			'linex':	row[16],
			'ref':		row[17],
			'length':	row[18],
			'width':	row[19],
			'wh':		row[20],
			'rem':		row[21],
			'uomfactor':row[22]
		}
		postock.append(waw)
	return jsonify(postock)



def pojson(result):
	po = []
	for row in result:
		waw = {
			'center': row[0],
			'trno': row[1],
			'docno': row[2],
			'client': row[3],
			'terms': row[4],
			'cur': row[5],
			'forex': row[6],
			'yourref': row[7],
			'ourref': row[8],
			'dateid': row[9],
			'clientname': row[10],
			'address': row[11],
			'shipto': row[12],
			'rem': row[13],
			'agent': row[14],
			'whid': row[15],
			'wh': row[16],
			'due': row[17],
			'groupid': row[18],
			'shipto': row[19],
			'controlno': row[20],
			'isimport': row[21]
		}
		po.append(waw)
	return po
