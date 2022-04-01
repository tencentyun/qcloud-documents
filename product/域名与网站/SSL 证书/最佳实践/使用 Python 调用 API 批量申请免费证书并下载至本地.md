## 概述
本文将指导您介绍如何使用腾讯云 API 批量申请证书并下载证书。

## 前提条件
- 子用户创建并授权云 API 与 SSL 证书全部权限。
- 已安装 Python 版本3.6+。

>!
>- 为了保障您的账户以及云上资产的安全，请谨慎保管 SecretId 与 SecretKey 并定期更新。
>- 创建子账号请参考 [创建子账号并授权](https://cloud.tencent.com/document/product/598/54458)。

## 操作步骤
1. 打开命令提示符，查看 Python 版本如下：
```
python3 -V
```
2. 升级 pip，并通过 pip 安装腾讯云 Python SDK。
```
python -m pip install --upgrade pip
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
```
3. 前往 [Github 仓库](https://github.com/tencentcloud/tencentcloud-sdk-python) 或者 [Gitee 仓库](https://gitee.com/tencentcloud/tencentcloud-sdk-python) 下载最新代码，并进行解压。
```
cd tencentcloud-sdk-python
python setup.py install
```
3. 进入 tencentcloud-sdk-python/tencentcloud/ssl/__init__.py 目录下，添加以下代码并执行。
```
import json,base64
from time import time,sleep
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ssl.v20191205 import ssl_client, models

start = time()
cred = credential.Credential("SecretId", "SecretKey")
httpProfile = HttpProfile()
httpProfile.endpoint = "ssl.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
domain_name = []
while True:
    domain = input('要申请证书的域名：')
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
