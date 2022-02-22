import MySQLdb
import json

db = MySQLdb.connect(...)
cursor = db.cursor()

dic = {'office': {'component_office': ['Word2010SP0', 'PowerPoint2010SP0']}}
sql = "INSERT INTO ep_soft(ip_address, soft_data) VALUES (%s, %s)"

cursor.execute(sql, ("192.xxx.xx.xx", json.dumps(dic)))
cursor.commit()