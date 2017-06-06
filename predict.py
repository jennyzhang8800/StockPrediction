
#encoding:utf-8
'''
Created on 2017年6月6日

@author: Administrator
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import tensorflow as tf
import math,random
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import TimeDistributed
from keras.preprocessing import sequence
np.random.seed(13)


# 加载数据集
# 加载数据集
df = pd.read_csv('part2_data.csv', parse_dates=['DepScheduled'])
print df.head(3)

# 查看航班延误时间随日期的分布
flight_no = df.FlightNO.sample(n=1).values[0]
print  "hangbanhao:",flight_no
df.ix[df.FlightNO==flight_no][['DepScheduled','Depdelay']].\
sort_values('DepScheduled').plot(x='DepScheduled',y='Depdelay',
                                 kind='line', sort_columns=True)
plt.title(flight_no)
plt.show()

train_no = df.FlightNO.drop_duplicates().sample(frac=0.7) 
test_no = df.FlightNO.drop_duplicates().drop(train_no.index)
df_train = df[df.FlightNO.isin(train_no)]
df_test = df[df.FlightNO.isin(test_no)]


train = df_train.groupby('FlightNO').apply(
    lambda x: x.sort_values('DepScheduled').Depdelay.values).values
test = df_test.groupby('FlightNO').apply(
    lambda x: x.sort_values('DepScheduled').Depdelay.values).values
testY = [e[-1] for e in test]


'''
LSTM 对输入 X 的形状要求是：
[samples, time steps, features]
'''
def reshape4lstm(S, D, flag=1):
    m_len = max(map(len,S))
    endIdx = m_len if flag else m_len-1
    if endIdx < D+1:
        raise IndexError
    else:
        X = [[] for _ in range(len(S))]
        Y = [[] for _ in range(len(S))]
        for idx,line in enumerate(sequence.pad_sequences(S)):
            for idx2 in xrange(D, endIdx):
                X[idx].append(line[idx2-D:idx2].tolist())
                Y[idx].append([line[idx2]]) # 注意这里 Y 也是3-D array
    return np.asarray(X,dtype='float'), np.asarray(Y, dtype='float')

D = 10 # 特征只包含过去D个时刻
trainX, trainY = reshape4lstm(train, D, 1)
testX,_ = reshape4lstm(test, D, 0)

# 构建 LSTM 模型
EPOCHES = 40
CELL_SIZE = 32 
OUTPUT_SIZE = 1
BATCH_SIZE = len(trainX)
myLstm = Sequential()
myLstm.add(LSTM(input_dim = D, 
                output_dim=CELL_SIZE, 
                return_sequences=True))
myLstm.add(TimeDistributed(Dense(OUTPUT_SIZE)))
myLstm.compile(loss='mean_squared_error', optimizer='adam')
# 模型学习
# 在相同数据集上重复调用 .fit 可以继续学习
myLstm.fit(trainX, trainY 
           , batch_size=BATCH_SIZE
           , nb_epoch=EPOCHES
           , verbose=True
          )

# 模型评估 
test_P = myLstm.predict(testX)
testY_P = test_P[:,-1,0]
train_P = myLstm.predict(trainX)
trainY_P = train_P[:,-1,0]
trainY_last = trainY[:,-1,0]
trainY_last = trainY[:,-1,0]
# 训练集误差(只关注最后一次的输出)
print np.sqrt(np.sum((trainY_P-trainY_last)**2))
# 测试集误差
print np.sqrt(np.sum((testY_P-testY)**2))
