from pandas import read_csv

if __name__ == '__main__':
    df = read_csv('深圳_链家.csv')
    new_df = df.drop_duplicates(
        ['楼盘名称', '物业类型', '销售状态', '位置', '房型', '面积', '标签', '单价', '总价'])
    new_df.to_csv('tmp.csv', index=False)
