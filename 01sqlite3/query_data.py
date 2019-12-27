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
