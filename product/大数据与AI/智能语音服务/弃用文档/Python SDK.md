## 开发准备
### 相关环境
实时语音识别 [Python SDK 下载地址>>](https://main.qcloudimg.com/raw/f66a99a01f0e657a014e7db9971acd0a/RASRsdk.py)

### 环境依赖
此版本 SDK 适用于 Python 2.7，暂不适用于 Python3。

### 安装SDK
**源码安装**
根据下载地址下载源码，将源码中的 RASRsdk.py 复制到项目中即可使用。

### 卸载 SDK
卸载方式即删除 RASRsdk.py 即可。

## 快速入门
```
# -*- coding:utf-8 -*-
# 引用 SDK
import RASRsdk

# 用户需修改为自己官网的appid，secretid与sectretkey
secret_key = 'kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP'
secretid = 'AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8'
appid = '1255628450'

# 识别引擎 8k_0 or 16k_0
engine_model_type = '16k_0'
# 结果返回方式 0：同步返回 or 1：尾包返回
res_type = 0
# 识别结果文本编码方式 0:UTF-8,1:GB2312,2:GBK,3:BIG5
result_text_format = 0
#  语音编码方式 1:wav 4:sp 6:skill
voice_format = 1
# 音频文件路径
filepath = "./test.wav"
# 语音切片长度 cutlength<200000
cutlength = 64000
# 调用语音识别函数获得识别结果
RASRsdk.sendVoice(secret_key, secretid, appid, engine_model_type,
res_type, result_text_format, voice_format, filepath,cutlength)
	```
