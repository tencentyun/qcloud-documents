## 获取 SDK

[Python SDK 下载>>](https://github.com/tencentyun/qcloud-cos-sts-sdk)

## 查看示例

请查看 `sts_demo.py` 文件，里面描述了如何调用 SDK。

## 使用方法

拷贝 `sts.py` 文件到您的 Python 工程中，调用代码如下：

```
from sts import Sts

config = {
	# 临时密钥有效时长，单位是秒，如果没有设置，默认是30分钟
	'duration_in_seconds': 1800,
	# 您的secret id
	'secret_id': 'xxx',
	# 您的secret key
	'secret_key': 'xxx',
}

sts = Sts(config)
response = sts.get_credential()
json_content = response.content
```

## 返回结果

成功的话，可以拿到包含密钥的 JSON 文本：

```
{"code":0,"message":"","codeDesc":"Success","data":{"credentials":{"sessionToken":"2a0c0ead3e6b8eed9608899eb74f2458812208ab30001","tmpSecretId":"AKIDBSrMaeFD0ZAECKuBzohnjAhJ53XNCE2F","tmpSecretKey":"UC7YjMrIlcuFgoWGwnrHwsMBrQrpUwYI"},"expiredTime":1526288317}}
```


## 自定义策略

默认情况下返回的密钥可以访问所有 cos 下的资源，如果你希望精确控制密钥的访问级别，例如访问某个路径下的资源，您可以通过以下方式设置 policy：

```
config = {
	...,
	policy: 'your-policy'
};
```

关于策略描述和数据安全的最佳实践，请参见 [数据安全性最佳实践](https://cloud.tencent.com/document/product/666/17921)。