## 概述
调用 ListKeys 列出账号下的密钥列表（KeyId 信息）。

本文示例使用腾讯云 [命令行工具 TCCLI](https://cloud.tencent.com/product/cli)，后续您可以使用任何搜支持的编程语言调用。该 API 操作没有必选参数，您可以查看 [ListKeys](https://cloud.tencent.com/document/product/573/34415) 接口文档来设置查看结果。


## 示例
看广东区的前5个 KeyId 信息。

#### 输入示例
```shell
tccli kms ListKeys --region ap-guangzhou --Limit 5
```



#### 输出示例
```shell
{
    "Keys": [
        {
            "KeyId": "521xxxx6-xxxx-xxxx-xxxx-52540xxxx9d4"
        },
        {
            "KeyId": "6cxxxx6f-xxxx-xxxx-xxxx-5254xxxxd9d4"
        },
        {
            "KeyId": "5xxxx298-xxxx-xxxx-xxxx-525xxxxda05"
        },
        {
            "KeyId": "xxxxxxxx-xxxx-xxxx-xxxx-52540xxxxxxx"
        },
        {
            "KeyId": "81b5xxxx-xxxx-xxxx-xxxx-525xxxx2515b"
        }
    ],
    "TotalCount": 110,
    "RequestId": "286xxxxaa-xxxx-xxxx-xxxx-xxxxxxxxx"
}
```
