"""
<練習題>
民政局人口資料，找出指定數據(0-4歲加總)
"""
import numpy as np

# 方法一
data = np.genfromtxt('population.csv', skip_header=1, delimiter=',', encoding='utf8', dtype=int, unpack=True)
#print(data.shape)
print(sum(data[1, 1:]))
print('-' * 30)

# 方法二
data1 = np.delete(data, 0, axis=0)
data2 = np.delete(data1, 0, axis=1)
print(sum(data2[0]))
print('-' * 30)

# 方法三
data = np.genfromtxt('population.csv', skip_header=1 and 2, delimiter=',', encoding='utf8', unpack=True, dtype='int')
print(sum(data[1]))


