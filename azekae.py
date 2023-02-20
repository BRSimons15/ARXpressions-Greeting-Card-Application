import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect('database.db')
# conn.row_factory = dict_factory
conn.row_factory = dict_factory

cur = conn.cursor()
abc_id=1

wish = cur.execute('SELECT * FROM wish').fetchall()
conn.close()
print(wish)
# print(cur.execute('SELECT * FROM wish'))
