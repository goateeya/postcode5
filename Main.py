import sqlite3
from flask import Flask
app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('zip5.db')
    cursor = conn.cursor()
    cursor.execute('drop table zip')
    cursor.execute('create table zip (zip5 int, city varchar(10), area varchar(10), road varchar(100), scope varchar(10)), full varchar(255)')
    cursor.execute('create index zip_zip5_idx on zip (zip5)')
    # cursor.execute('select * from zip where zip5 = 22061')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.commit()
    conn.close()


def get_conn():
    return sqlite3.connect('zip5.db')



def query(search_key):
    result_list = []
    search_keys = search_key.split()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('select * from zip')
    rows = cursor.fetchall()
    for row in rows:
        hit = False
        for key in search_keys:
            hit = True
            if key not in row[5]:
                hit = False
                break
        if hit:
            result_list.append(row)
    cursor.close()
    conn.commit()
    conn.close()
    return result_list


# if __name__ == '__main__':
@app.route('/address/<key>')
def search(key):
    result_list = []
    for row in query(key):
        result_list.append('{} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4]))
    return '<br>'.join(result_list)


if __name__ == "__main__":
    app.run()