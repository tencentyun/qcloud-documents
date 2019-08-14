## 1. 接入准备

### 1.1 SDK 获取
实时语音识别 Python SDK 以及 Demo 的下载地址：[Python SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/python_realtime_asr_sdk.tar.gz)。

### 1.2 接入须知
开发者在调用前请先查看实时语音识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/37138) ，了解接口的**使用要求**和**使用步骤**。

### 1.3 开发环境
**环境依赖**
该接口目前仅支持 Python 2.7 版本，后续会支持 Python 3。

**安装 requests**
+ 方法1：pip install requests 。
+ 方法2：先下载[ requests](https://2.python-requests.org//zh_CN/latest/user/install.html#install)，然后进入下载目录执行：python setup.py install 。

## 2. 快速接入
1. 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey 并将```Python_realtime_asr_sdk/src/Config.py```中的配置项按需改成自己的值。
2. 参考 ```Python_realtime_asr_sdk/src/RasrClient.py``` 接入： 

```
# 说明：请先将 Config.py 中的配置项按需改成自己的值，然后再开始使用。
import RASRsdk
import os
import Config
# ----------------------------- 调用方法1 -----------------------------
# 音频文件路径
filepath = "../../test_wavs/8k.wav"
# 调用语音识别函数获得识别结果, 参数2标识是否打印中间结果到控制台
result = RASRsdk.sendVoice(filepath, True)
print("Final result: " + result)

# ---------------------------------------------------------------------
# 若需中途调整参数值，可直接修改，然后继续发请求即可。例如：
Config.config.ENGINE_MODEL_TYPE = '8k_0'

# ----------------------------- 调用方法2 -----------------------------
def requestExample():
    # 将音频文件分解成小的切片数据（即：切分成长度较小的多个字符串）发出。模拟不断发送数据接收回复，最终收完整句话的识别结果。
    filepath = "../../test_wavs/8k.wav"
    file_object = open(filepath, 'rb')
    file_object.seek(0, os.SEEK_END)
    datalen = file_object.tell()
    file_object.seek(0, os.SEEK_SET)
    
    # 发送请求时需要用户自行维护3个变量：voiceId：创建后保持不变； seq：递增； endFlag：前面为0，发送尾部分片的请求时设置为1
    voiceId = RASRsdk.randstr(16)
    seq = 0
    endFlag = 0
    while (datalen > 0):
        if (datalen < Config.config.CUT_LENGTH):
            endFlag = 1
            content = file_object.read(datalen)
        else:
            content = file_object.read(Config.config.CUT_LENGTH)
        res = RASRsdk.sendRequest(content, voiceId, seq, endFlag)
        print(res)  # 打印收到的结果到控制台。示例用途。
        seq = seq + 1
        datalen = datalen - Config.config.CUT_LENGTH
    file_object.close()

# 使用方法2
requestExample()
```
