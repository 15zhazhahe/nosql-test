from pandas import DataFrame
from pymongo import MongoClient
import pandas as pd
import numpy as np


"""
将./docs/export_low_small.txt存入至mongodb中
并将常用的字段(画图)使用的字段拆分出来存入clean_data中
"""

# 读取文件
data = pd.read_table('./docs/export_low_small.txt')

# 连接 mongodb 
conn = MongoClient('localhost', 27017)
db = conn.mydb
my_set = db.test_set

tobeInser = data.values[1:, :]  # 取出带插入的有效字段
totalNum = tobeInser.shape[0]   # 获取取出数据的规模
# 循环插入数据，并对数据进行处理
for i in range(totalNum):
    my_set.insert({"freq": int(tobeInser[i, 0]),
                   "phi": float(tobeInser[i, 1]),
                   "vals": tobeInser[i, 2:].astype(np.float64).round(5).tolist() })

# 取出画图常用参数
# 将 theta 转换为度数
theta = data.values[0][2:].astype(np.float64) * 180 / np.pi
# 频率的所有取值
freq = list(set(data.values[1:, 0].astype(np.int64))) # 取出freq所有取值可能
# 将 phi 转换为度数
phi = list(set(data.values[1:, 1].astype(np.float64) * 180 / np.pi)) # 取出phi所有取值可能

np.savetxt('./clean_data/theta.txt', theta)
np.savetxt('./clean_data/freq.txt', freq)
np.savetxt('./clean_data/phi.txt', phi)