import pymysql


# 这里只能用 utf8，不能用 utf-8
connect = pymysql.connect(host='',
                          port=3306,
                          user='',
                          password='',
                          charset='utf8')
cur = connect.cursor()

cur.excute('sql')