# python3操作mysql数据库：pymysql、mysql-client
import pymysql

from handle_conf import conf


# # 这里只能用 utf8，不能用 utf-8
# # 1.连接数据库
# con = pymysql.connect(host='',
#                           port=3306,
#                           user='',
#                           password='',
#                           charset='utf8')
# # 2.创建一个游标对象
# cur = con.cursor()
# # 3.执行sql
# res = cur.excute('sql')
# # 4.提交事务
# con.commit()
# # 上面两个步骤可以使用with简化
# # with con as cur:
# #     sql = ""
# #     cur.excute(sql)
# # 5.关闭
# cur.close()
# con.close()


class HandleDB:
    def __init__(self):
        # self.con = pymysql.connect(host='',
        #                           port=3306,
        #                           user='',
        #                           password='',
        #                           charset='utf8')
        self.con = pymysql.connect(host=conf.get('mysql', 'host'),
                                   port=conf.get('mysql', 'port'),
                                   user=conf.get('mysql', 'user'),
                                   password=conf.get('mysql', 'passqord'),
                                   charset='utf8',
                                   # cursorclass=pymql.cursors.DictCursor  # 加了这个返回的是字典
                                   )

    def find_one(self, sql):
        """查询一条数据"""
        with self.con as cur:
            cur.excute(sql)
        cur.close()
        return cur.fetchone()

    def find_count(self, sql):
        """sql执行完成之后，返回的数据条数"""
        with self.con as cur:
            res = cur.excute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()
