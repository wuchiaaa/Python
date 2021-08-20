"""
練習題
"""
import pandas as pd

# 讀取資料
df = pd.read_csv('customer.csv')
print(df)
print('-' * 30)

# 資料基本清理
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(df_sample['age'].mean())
df_sample['gender'] = df_sample['gender'].fillna(method='ffill')
df_sample['area'] = df_sample['area'].fillna(method='bfill')
df_sample.drop_duplicates(subset='id', keep='first', inplace=True)  # 去除重覆記錄
df_sample['job'] = df_sample['job'].str.strip()
df_sample['job'] = df_sample['job'].str.replace(' ', '')  # 去除欄位中的空白
df_sample['age'] = df_sample['age'].astype('int32')     # 轉換值的格式
print(df_sample)
print('=' * 30)

# 篩選Female
print(df_sample[df_sample['gender'] == 'Female'])
# 篩選Male，且age>50
print(df_sample[(df_sample['gender'] == 'Male') & (df_sample['age'] > 50)])
# 篩選'新北市三重區'或'基隆市中正區'
print(df_sample[(df_sample['area'] == '新北市三重區') | (df_sample['area'] == '基隆市中正區')])
# 統計資料：area個數
print(df_sample.groupby('area')['id'].count())
# 統計資料：age平均數
print(df_sample.groupby('gender')['age'].mean())
