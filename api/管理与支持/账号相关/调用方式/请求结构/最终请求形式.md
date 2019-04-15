最终的请求 URL 由以下几部分组成：
- 请求域名:[查询实例列表](https://cloud.tencent.com/document/api/213/831)（DescribeInstances）的请求域名为：cvm.api.qcloud.com。实际的请求域名根据接口所属模块的不同而不同，详见各接口说明。
- 请求路径: 云 API 的请求路径固定为/v2/index.php。
- 最终请求参数串: 包括公共请求参数和接口请求参数。

最终的请求 URL 的拼接规则为:
`https:// + 请求域名 + 请求路径 + ? + 最终请求参数串`

因此，我们得到最终的请求 URL 如下，其中前6个参数为公共请求参数，后6个参数为接口请求参数。

```
https://cvm.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003
```
