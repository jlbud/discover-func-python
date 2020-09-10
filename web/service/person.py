import pymysql

from web.utils.json import to_json


def get_person():
    # cursorclass 设置字典格式的输出
    conn = pymysql.connect(host='115.28.56.***', port=3306, user='root', password='12345678', db='student',
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cur:
            cur.execute('select * from t1 order by id asc')
            result = cur.fetchall()
            for i in result:
                print(i["id"])
    finally:
        conn.close()
    return to_json(result)
