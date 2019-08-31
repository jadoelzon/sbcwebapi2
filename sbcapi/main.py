# from flask import Flask, jsonify, Blueprint, request
# from flask_cors import CORS
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
from flask import Flask

# import sys, os
# sys.path.insert(0, os.getcwd()+"/PO")
# import pofunc

# from config import app #database config (config.py)

# CORS(app)

# mysql = MySQL(app)

@app.route('/')
def index():
	return "Hello Jad!"

# @app.route('/po/<trno>', methods=['GET'])
# def get_po(trno):
# 	return pofunc.get_po(trno)


# @app.route('/po/', methods=['GET'])
# def get_all_po():
# 	return pofunc.get_all_po()

# @app.route('/po/stock/<trno>', methods=['GET'])
# def get_po_stock(trno):
# 	return pofunc.get_po_stock(trno)


# @app.route('/login', methods=['POST'])
# def user_login():
# 	if request.method == 'POST' and 'username' in request.json and 'password' in request.json:
# 		username = request.json['username']
# 		password = request.json['password']
# 		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# 		cur.execute("select userid, accessid, username from useraccess where username = %s and password = %s", (username, password))
# 		account = cur.fetchone()
# 		cur.close()

# 		if account:
# 			with mysql.connection.cursor() as cur:
# 				cur.execute("select id, name, seq, class, doc from left_parent order by seq")
# 				result = cur.fetchall()
# 				cur.close()
# 			# return str(result)
# 			parentmenu = []
# 			for row in result:
# 				p = {
# 					'id': row[0],
# 					'name': row[1],
# 					'seq': row[2],
# 					'class': row[3],
# 					'doc': row[4]
# 				}
# 				parentmenu.append(p)

# 			with mysql.connection.cursor() as cur:
# 				cur.execute("select parent.id, parent.name, parent.class as pclass, parent.doc as pdoc, menu.doc, menu.url, menu.module, menu.class as mclass, menu.access from left_parent as parent left join left_menu as menu on menu.parent_id = parent.id order by parent.seq, menu.id")
# 				menu = cur.fetchall()
# 				cur.close()
# 			childmenu = []
# 			for row in menu:
# 				m = {
# 					'id': row[0],
# 					'name': row[1],
# 					'pclass': row[2],
# 					'pdoc': row[3],
# 					'doc': row[4],
# 					'url': row[5],
# 					'module': row[6],
# 					'mclass': row[7],
# 					'access': row[8]
# 				}
# 				childmenu.append(m)
# 			return jsonify({'user':account, 'msg':'login success', 'status':'true', 'parentmenu':parentmenu, 'childmenu':childmenu})
# 		else:
# 			return jsonify({'msg':'invalid username or password', 'status':'false'})
# 	else:
# 		return jsonify({'msg':'error', 'status':'false'})



# def pojson(result):
# 	po = []
# 	for row in result:
# 		waw = {
# 			'center': row[0],
# 			'trno': row[1],
# 			'docno': row[2],
# 			'client': row[3],
# 			'terms': row[4],
# 			'cur': row[5],
# 			'forex': row[6],
# 			'yourref': row[7],
# 			'ourref': row[8],
# 			'dateid': row[9],
# 			'clientname': row[10],
# 			'address': row[11],
# 			'shipto': row[12],
# 			'rem': row[13],
# 			'agent': row[14],
# 			'whid': row[15],
# 			'wh': row[16],
# 			'due': row[17],
# 			'groupid': row[18],
# 			'shipto': row[19],
# 			'controlno': row[20],
# 			'isimport': row[21]
# 		}
# 		po.append(waw)
# 	return po


if __name__ == '__main__':
	app.run()
