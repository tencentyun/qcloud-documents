## 开发准备
### 相关环境
一句话语音识别 [Python SDK 下载地址>>](https://main.qcloudimg.com/raw/f1d52c7dd9c1b9ed3f468020a7607bc0/SASRsdk.py)

### 环境依赖
此版本 SDK 适用于 Python 2.7，暂不适用于 Python3。

### 安装 SDK 
**源码安装**
根据下载地址下载源码。将源码中的 SASRsdk.py 复制到项目中即可使用。

### 卸载 SDK
卸载方式即删除 RASRsdk.py 即可。

##  快速入门
```
# -*- coding:utf-8 -*-
# 引入 SDK
import SASRsdk

# 用户需修改为自己官网的secretid与sectretkey
secretKey = 'kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP'
SecretId = 'AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8'

# 识别引擎 8k or 16k
EngSerViceType = '16k'
# 语音数据来源 0:语音url or 1:语音数据 bodydata
SourceType = 1
# 语音数据地址
URI = '15s.wav'
# URI='http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav'
# 音频格式 mp3 or wav
VoiceFormat = 'wav'
# 调用 sentVoice 函数获得识别结果
SASRsdk.sentVoice(secretKey, SecretId, EngSerViceType, SourceType, URI, VoiceFormat)
```
