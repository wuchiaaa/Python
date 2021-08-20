"""
練習題
"""
import matplotlib.pyplot as plt
import numpy as np

# 設定圖書分類及銷售額比例
listx = ['商業理財', '文學小說', '藝術設計', '人文科普', '語言電腦', '心靈養生', '生活風格', '親子共享']
listm = [0.14, 0.16, 0.08, 0.13, 0.16, 0.12, 0.16, 0.05]  # 男性比例
listf = [0.1, 0.19, 0.06, 0.1, 0.13, 0.13, 0.2, 0.09]  # 女性比例

# 設定圖表區尺寸以及使用字型
plt.figure(figsize=(10, 8))
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# -----------start--------------------------------------------------------

listm = [x * 100 for x in listm]
listf = [x * 100 for x in listf]

# -------------------
plt.subplot(221)
plt.pie(listm, labels=listx, autopct="%.1f%%")
plt.title('圖書分類銷售比率-男性', fontsize=16)

# -------------------
plt.subplot(222)
plt.pie(listf, labels=listx, autopct="%.1f%%")
plt.title('圖書分類銷售比率-女性', fontsize=16)

# -------------------
plt.subplot(223)
pos = np.arange(len(listx))
width = 0.4
plt.bar(pos - width / 2, listm, width, label='男')
plt.bar(pos + width / 2, listf, width, label='女')
plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)
plt.xticks(pos, listx, rotation=25)
plt.title('圖書分類銷售長條圖-性別', fontsize=16)
plt.legend(loc=2, prop={'size': 8})

# -------------------
plt.subplot(224)
plt.gca().grid(True)
plt.plot(listx, listm, 's-', label='男')
plt.plot(listx, listf, 's-', label='女')
plt.xticks(rotation=25)
plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)
plt.title('圖書分類銷售折線圖-性別', fontsize=16)
plt.legend(loc=3, prop={'size': 8})

plt.show()
