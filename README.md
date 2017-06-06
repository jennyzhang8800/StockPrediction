# StockPrediction
华量杯-股票预测
大赛链接：http://106.14.126.65/
数据集： http://pan.baidu.com/s/1gf7ScON 密码: j8su

### 一、数据预处理
代码：[clean.py](https://github.com/jennyzhang8800/StockPrediction/blob/master/clean.py)
### 二、利用LSTM模型

#### 1. 安装keras框架

Keras安装之前，需要先安装好numpy,scipy。
下面是在windows下的安装。

**(1)安装pip**
```
https://pypi.python.org/pypi/pip#downloads
```
下载对应版本的pip。如"pip-9.0.1.tar.gz (md5, pgp)"

然后解压，进入到pip-9.0.1这个目录中，运行下面的代码安装

```
python setup.py install
```
重启，使环境变量生效

**（2）安装numpy**

注意，不能用pip install numpy的方式安装，会缺少依赖的库。采用下面的方法：

下载numpy‑1.11.3+mkl‑cp27‑cp27m‑win_amd64.whl，(由于我的python版本是2.7.9,是windows 64位)下载的地址为：
```
http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
```
下载好之后，进入到numpy‑1.11.3+mkl‑cp27‑cp27m‑win_amd64.whl所在目录，运行下面的命令安装：
```
pip install numpy‑1.11.3+mkl‑cp27‑cp27m‑win_amd64.whl
```
**（3）安装scipy**

注意，不能用pip install scipy的方式安装，会报下面的错：
```
File "scipy\linalg\setup.py", line 20, in configuration
        raise NotFoundError('no lapack/blas resources found')
    numpy.distutils.system_info.NotFoundError: no lapack/blas resources found
```

正确的做法是，采用下面的方法进行安装：

首先，下载scipy‑0.19.0‑cp27‑cp27m‑win_amd64.whl，(由于我的python版本是2.7.9,是windows 64位)下载的地址为：
```
http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
```
下载好之后，进入到scipy‑0.19.0‑cp27‑cp27m‑win_amd64.whl所在目录，运行下面的命令安装：
```
pip install scipy‑0.19.0‑cp27‑cp27m‑win_amd64.whl
```

**（4）安装keras**
运行下面的命令：
```
pip install keras
```
现在keras己经安装好了。接下来就可以用Keras提供的LSTM进行训练了！

#### 2. 训练，测试，评估
在运行代码前需要把keras的backend改一下，改成theano，而不用tensorflow。因为theano在keras安装时己经安装好了，而tensorflow还要重新安装。
首先找到keras.json文件，在下面的目录：
```
C:\Users\zhangyanni\.keras\keras.json
```
然后把下面"backend": "tensorflow" 中的tensorflow改成theano
```
{
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "image_data_format": "channels_last", 
    "backend": "tensorflow"
}
```
改成：

```
{
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "image_data_format": "channels_last", 
    "backend": "theano"
}
```
接下来，就可以运行predict.py了

代码:[predict.py](https://github.com/jennyzhang8800/StockPrediction/blob/master/predict.py)
