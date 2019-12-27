import sqlite3

if __name__ == '__main__':
    with sqlite3.connect('sz_lianjia.db') as conn:
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
        c.close()
        conn.commit()
