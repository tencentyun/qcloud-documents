
## 操作背景
TiKit 是腾讯云 TI 平台 TI-ONE 提供的开源 Python sdk软件包。用户可以使用 TiKit 提交训练任务到 TI-ONE。

## 操作步骤
### 环境依赖
目前可以支持 Python 3.4 及以上的版本。

### 安装TiKit
在腾讯云 TI 平台中，notebook和训练任务的容器里面已经内置了TiKit，不用再安装。

非公有云 TI 平台的环境，安装方法如下：

- 安装依赖：
```
#centos:

sudo yum -y install cyrus-sasl cyrus-sasl-devel cyrus-sasl-lib gcc-c++ python3-devel

#ubuntu:

sudo apt-get update
sudo apt-get install -y libsasl2-dev
```
- 方式一：使用pip安装（推荐）
```
pip3 install -U tikit
```
- 方式二：离线安装。在 https://pypi.org/project/tikit/ 上下载安装包，使用whl文件安装，或者使用源码安装：
```
pip3 install tikit-1.0.0-py3-none-any.whl

# 或者，解压源码后
python3 setup.py install
```

### 开始使用

1. 准备好secret_id，secret_key 信息
  登录腾讯云，在页面上获取，如下：
![](https://qcloudimg.tencent-cloud.cn/raw/bc5f93b3272c44b18361ead95afc9cbc.png)
![](https://qcloudimg.tencent-cloud.cn/raw/c20c9a7f320252989e270e9fbc9ef22b.png)
2. 初始化，调用函数
```
from tikit.client import Client

# 初始化 client。在腾讯云 TI 平台公有云环境（包括notebook和训练任务）中可以不填地区，环境变量中已经有地区信息。
client = Client("your_secret_id", "your_secret_key", "<region>")

# 查看算法框架列表。
client.describe_training_frameworks()
```
在 notebook 环境中，会直接显示 html 的内容，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/9106f645dc71fe987ac1cd17183fa995.png)
在非 notebook 环境中，可以把结果 print 出来，如下：
![](https://qcloudimg.tencent-cloud.cn/raw/ad25d8403bfa7e36ad4016f990f19407.png)
3. 查看函数用法
```
help(client.create_image_dataset)
```
![](https://qcloudimg.tencent-cloud.cn/raw/85e458c288d595c6cd086ef817f3ccff.png)
