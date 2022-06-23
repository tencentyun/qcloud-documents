## 概述
本文将指导您介绍如何使用腾讯云 API 批量申请证书并下载证书。

## 前提条件
- 子用户创建并授权云 API 与 SSL 证书全部权限。
- 已安装 Python 版本最新版本，如需安装，请前往 [Python 官网](https://www.python.org/downloads/) 进行下载。
- 已安装 PyCharm 版本最新版本，如需安装，请前往 [PyCharm 官网](http://www.jetbrains.com/pycharm/download/#section=windows) 进行下载。
>!
>- 为了保障您的账户以及云上资产的安全，请谨慎保管 SecretId 与 SecretKey 并定期更新。
>- 创建子账号请参考 [创建子账号并授权](https://cloud.tencent.com/document/product/598/54458)。

## 操作步骤
1. 打开命令提示符，查看 Python 版本。命令行如下：
```
python -V
```
2. 查看 Python 目前已经安装的第三方模块，命令行如下：
```
pip list
```
![](https://qcloudimg.tencent-cloud.cn/raw/a9e6874edf016baa7f88f52352222dcb.png)
>!例如缺少 requests，可通过 `pip install requests` 安装该模块。
>
3. 通过 pip 安装腾讯云 Python SDK。命令行如下：
```
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
```
3. 前往 [Github 仓库](https://github.com/tencentcloud/tencentcloud-sdk-python) 或者 [Gitee 仓库](https://gitee.com/tencentcloud/tencentcloud-sdk-python) 下载最新代码至本地，并进行解压。
4. 打开 PyCharm，导入最新的代码文件，进入 `tencentcloud-sdk-python/tencentcloud/ssl` 目录下并创建新的 Python 文件，例如 `apply.py`。添加以下代码并执行。
```
import json,base64
from time import time,sleep
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ssl.v20191205 import ssl_client, models

start = time()
#SecretId 请填写您的 API 密钥ID，SecretKey 请填写您的 API 密钥KEY
cred = credential.Credential("SecretId", "SecretKey")
httpProfile = HttpProfile()
httpProfile.endpoint = "ssl.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
domain_name = []
while True:
    domain = input('要申请证书的域名：')#输入您需要申请的证书绑定的域名，如不需要继续申请，请直接按回车键
    if domain == '':
        break
    else:
        domain_name.append(domain)

for i in range(len(domain_name)):
    client = ssl_client.SslClient(cred, "", clientProfile)
    try:

        req = models.ApplyCertificateRequest()
        params = {
            "DvAuthMethod": "DNS_AUTO",
            "DomainName": domain_name[i]
        }
        req.from_json_string(json.dumps(params))

        resp = client.ApplyCertificate(req)
        response = json.loads(resp.to_json_string())
        print('域名：{0}资料已提交，五秒钟后自动验证'.format(domain_name[i]))
        certid = response['CertificateId']
        sleep(5)
        try:
            req1 = models.CompleteCertificateRequest()
            params1 = {
                "CertificateId": certid
            }
            req1.from_json_string(json.dumps(params1))

            resp1 = client.CompleteCertificate(req1)
            response1 = json.loads(resp1.to_json_string())
            print('域名：{0}验证成功！准备下载证书'.format(domain_name[i]))
            try:
                req2 = models.DownloadCertificateRequest()
                params2 = {
                    "CertificateId": certid
                }
                req2.from_json_string(json.dumps(params2))

                resp2 = client.DownloadCertificate(req2)
                response2 = json.loads(resp2.to_json_string())
                # print(response2['Content'])
                content = response2['Content']
                with open("{0}.zip".format(domain_name[i]), "wb") as f:

                    f.write(base64.b64decode(content))
                    f.close()
            except TencentCloudSDKException as err:
                print(err)
        except TencentCloudSDKException as err:
            print(err)
    except TencentCloudSDKException as err:
        print(err)
end = time()
print('本次代码执行共耗时：', round(end - start, 2), 's')
```

## 结果展示
1. 申请批量证书。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2f22c8fa894171964bbcf0ea1310c716.png)
2. 下载证书内容。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6d9750da93dea520efef6d4eec90b51e.png)
