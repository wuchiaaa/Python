import pandas as pd
import numpy as np
import os

dir1 = 'C:\workspace\pro0704\Week1'
os.chdir(dir1)  # 設置默認操作路徑
folder = os.listdir(dir1)  # os包 讀取路徑下所有文件名
print(folder)

# 測試讀取
# check = pd.read_csv(folder[0], engine='python', skiprows=3, nrows=3, encoding='gb18030')   # 打開文件會發現內容是從第4行開始的，不給任何指示的話，python會困擾
# print(check)

# 循環導入所有文件，並合併
new_data = pd.DataFrame(
    columns=['指标', '2019年', '2018年', '2017年', '2016年', '2015年', '2014年', '2013年', '2012年', '2011年', '2010年'])
for i in range(len(folder)):
    temp = pd.read_csv(folder[i], skiprows=3, nrows=3, encoding='gb18030')
    temp['Province'] = folder[i][:-4]
    # print(temp)
    new_data = new_data.append(temp)
    # print(new_data)
print(new_data.shape)
print(new_data.head())

# 測試導出
# print(new_data['Province'].unique().tolist())            # ['北京市', '安徽省', '广东省', '甘肃省', '福建省']
# print(new_data.loc[new_data['Province'] == '北京市'])

# 循環導出
writer = pd.ExcelWriter('Summary.xlsx')
new_data.to_excel(writer, sheet_name='Total', index=False, encoding='gb18030')
for i in new_data['Province'].unique().tolist():
    new_data.loc[new_data['Province'] == i, ].to_excel(writer, i, index=False)
writer.save()

