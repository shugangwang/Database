import sqlite3
from pandas import read_csv

if __name__ == '__main__':
    with sqlite3.connect('sz_lianjia2.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS t_sz_lianjia(
            id                integer PRIMARY KEY AUTOINCREMENT,
            estate_name       text,
            property_type     text,
            selling_condition text,
            location          text,
            rooms             text,
            area              text,
            tag               text,
            unit_price        text,
            total_price       text);
        ''')

        df = read_csv('深圳_链家.csv')
        for i in range(len(df)):
            c.execute('INSERT INTO t_sz_lianjia VALUES(?,?,?,?,?,?,?,?,?,?)',
                      (None,
                       df.loc[i][1],
                       df.loc[i][2],
                       df.loc[i][3],
                       df.loc[i][4],
                       df.loc[i][5],
                       df.loc[i][6],
                       df.loc[i][7],
                       df.loc[i][8],
                       df.loc[i][9]
                       ))
        conn.commit()
        c.close()
        conn.commit()
