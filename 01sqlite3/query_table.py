import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('sz_lianjia.db')
    c = conn.cursor()
    tables = c.execute('SELECT * FROM SQLITE_MASTER')
    for table in tables:
        print(table)
    c.close()
    conn.close()
