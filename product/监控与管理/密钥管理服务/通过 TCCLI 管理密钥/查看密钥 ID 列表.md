## 概述
调用 ListKeys 列出账号下的密钥列表（KeyId 信息）。

本文示例使用腾讯云 [命令行工具 TCCLI](https://cloud.tencent.com/product/cli)，后续您可以使用任何搜支持的编程语言调用。

该 API 操作没有必选参数，您可以查看 [ListKeys](https://cloud.tencent.com/document/product/573/34415) 接口文档来设置查看结果。


## 示例
看广东区的前5个 KeyId 信息。

#### 输入
```shell
tccli kms ListKeys --region ap-guangzhou --Limit 5
```



#### 输出
```shell
{
    "Keys": [
        {
            "KeyId": "6xxxxxxx-xxxx-xxxx-xxxx-5xxxxxxxxc09"
        },
        {
            "KeyId": "6xxxxxxx-xxxx-xxxx-xxxx-5xxxxxxxxc09"
        },
        {
            "KeyId": "6xxxxxxx-xxxx-xxxx-xxxx-5xxxxxxxxc09"
        },
        {
            "KeyId":"6xxxxxxx-xxxx-xxxx-xxxx-5xxxxxxxxc09"
        },
        {
            "KeyId": "6xxxxxxx-xxxx-xxxx-xxxx-5xxxxxxxxc09"
        }
    ],
    "TotalCount": 114,
    "RequestId": "afaaeb5e-c97d-4726-8012-6ae337d62928"
}
```
