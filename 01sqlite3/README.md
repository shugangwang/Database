# sqlite3

## 1 创建数据库

``` python

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

```

## 2 查询表信息
``` python
import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('sz_lianjia.db')
    c = conn.cursor()
    tables = c.execute('SELECT * FROM SQLITE_MASTER')
    for table in tables:
        print(table)
    c.close()
    conn.close()
```

## 3 查询数据

``` python
import sqlite3
import csv

if __name__ == '__main__':
    conn = sqlite3.connect('sz_lianjia.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM t_sz_lianjia')

    with open('深圳_链家.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        title = ['序号', '楼盘名称', '物业类型', '销售状态', '位置', '房型', '面积', '标签', '单价', '总价']
        writer.writerow(title)
        for items in data:
            writer.writerow(items)
    c.close()
    conn.close()
```

## 4 数据去重

``` python
from pandas import read_csv

if __name__ == '__main__':
    df = read_csv('深圳_链家.csv')
    new_df = df.drop_duplicates(
        ['楼盘名称', '物业类型', '销售状态', '位置', '房型', '面积', '标签', '单价', '总价'])
    new_df.to_csv('tmp.csv', index=False)

```

## 5 插入数据

``` python
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

```