import pymysql


def conn_mysql():
    conn = pymysql.connect(host='115.28.56.***', port=3306, user='root', password='12345678', db='student',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute('select id from t1 order by id asc')
    result = cur.fetchall()
    cur.close()
    conn.close()
    print(result)


if __name__ == '__main__':
    conn_mysql()
