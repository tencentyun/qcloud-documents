## 接入准备
### SDK 获取
录音文件识别 Python SDK 以及 Demo 的下载地址：[Python SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/python_record_asr_sdk.tar.gz)。
### 接入须知
开发者在调用前请先查看录音文件识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/37139) ，了解接口的**使用要求**和**使用步骤**。
### 开发环境
**环境依赖**
该接口目前仅支持 Python2.7 版本，后续会支持Python3。
**安装 requests**
+ 方法1：pip install requests 。
+ 方法2：先下载[ requests](https://2.python-requests.org//zh_CN/latest/user/install.html#install)，然后进入下载目录执行：python setup.py install 。

## 快速接入
1. 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey，并将```Python_record_asr_sdk/src/Config.py```中的配置项按需改成自己的值。
+ 参考 ```python_record_asr_sdk/src/OfflineClient.py``` 接入：

```
# 说明：请先将 Config.py 中的配置项按需改成自己的值，然后再开始使用。

# 音频文件路径。每调用一次task_process方法，可发出一份请求。
# 语音 URL，公网可下载。当 source_type值为 0时须填写该字段，为 1时不填；长度大于 0，小于 2048
audio_url = "https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav"
# 调用语音识别函数获得识别结果
result = offlineSdk.task_process(audio_url)
print (result)

# ------------------------------------------------------------------------------------
# 若需中途调整参数值，可直接修改，然后继续发请求即可。例如：
Config.config.CALLBACK_URL = ""
Config.config.ENGINE_MODEL_TYPE = "16k_0"
# ......
audio_url = "https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav"
result = offlineSdk.task_process(audio_url)
print (result)
```

