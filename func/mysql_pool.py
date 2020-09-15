import queue

import pymysql

mysqlInfo = {
    "host": '115.28.56.168',
    "user": 'root',
    "passwd": '12345678',
    "db": 'student',
    "port": 3306,
    "charset": 'utf8'
}


class MMysql(object):
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', 10)
        self.kwargs = kwargs
        self.conn_queue = queue.Queue(maxsize=self.size)
        for i in range(self.size):
            self.conn_queue.put(self.get_sql_conn())

    def get_sql_conn(self):
        conn = pymysql.connect(host='115.28.56.168', port=3306, user='root', password='12345678', db='student',
                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        return conn

    def _put_conn(self, conn):
        self.conn_queue.put(conn)

    def _get_conn(self):
        conn = self.conn_queue.get()
        if conn is None:
            conn = self.get_sql_conn()
        return conn

    def exec_sql(self, sql):
        conn = self._get_conn()
        # start transaction
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        except Exception as e:
            # end transaction
            print(e)
        finally:
            self._put_conn(conn)

    def __del__(self):
        try:
            while True:
                conn = self.conn_queue.get_nowait()
                if conn:
                    conn.close()
        except queue.Empty:
            pass


if __name__ == '__main__':
    opm = MMysql()

    sql = "select * from t1 order by id asc"

    res = opm.exec_sql(sql)
    print(res)
