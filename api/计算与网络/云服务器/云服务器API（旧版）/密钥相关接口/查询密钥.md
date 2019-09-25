>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (DescribeKeyPairs) 用于查询密钥。

接口请求域名：cvm.api.qcloud.com

* [密钥对](/document/product/213/6092) 是通过一种算法生成的一对密钥，在生成的密钥对中，一个向外界公开，称为公钥；另一个用户自己保留，称为私钥。密钥的公钥内容可以通过这个接口查询，但私钥内容系统不保留。
* 可通过`keyIds.n`或`keyName`输入参数作为过滤条件查询。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/document/api/213/6976) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| keyIds.n  | 否 | String | 密钥ID（此接口支持同时传入多个ID进行过滤。此参数的具体格式可参考 API [简介](https://cloud.tencent.com/doc/api/229/568) 的`id.n`一节）。
| keyName  | 否 | String | 密钥名称。
| projectId|否|String | 项目 ID，使用项目 ID 过滤结果。
| offset| 否| Int| 偏移量，默认为0。关于`offset`的更进一步介绍参考 API [简介](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89) 中的相关小节。
| limit| 否| Int| 返回数量，默认 20，最大值 100。关于`limit`的更进一步介绍参考 API [简介](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89) 中的相关小节。

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| totalCount |   int | 符合过滤条件的密钥个数。 |
| keyId |  String | 密钥ID。 |
| keyName |   String | 密钥名称。 |
| pubkey  |  String | 密钥的公钥内容。  |
| status | int |  密钥状态。0为正常，1为非正常。|
| bindUnInstanceIds | int | 绑定的实例ID列表。|
| bindIps | String List |  绑定的实例IP列表。|
| createTime | String | 密钥的创建时间。|

## 4. 示例

输入
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeKeyPairs
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "totalCount": 2,
        "sshSet": [
            {
                "keyId": "skey-xxxx",
                "keyName": "test1",
                "pubkey": "ssh-rsa xxxxxx skey_32228",
                "status": 0,
                "bindIps": [
                    
                ],
                "createTime": "2015-11-05 17:26:21",
                "bindUnInstanceIds": [
                    
                ]
            },
            {
                "keyId": "skey-xxxxx",
                "keyName": "test2",
                "pubkey": "ssh-rsa xxxxxx skey_32228",
                "status": 0,
                "bindIps": [
                    "xx.xx.xx.xx"
                ],
                "createTime": "2015-11-06 20:52:21",
                "bindUnInstanceIds": [
                    "ins-xxxxxx"
                ]
            }
            
        ]
    }
    
}

```





