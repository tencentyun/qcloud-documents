
## 接口描述
ListAudits 用于拉取跟踪集列表。
接口访问域名：`cloudaudit.api.qcloud.com`

## 请求参数
详见 [公共请求参数](https://cloud.tencent.com/document/product/599/12707)  页面。

## 响应参数

|参数名称|类型|描述|
|---------|---------|---------|
|auditLists|Array|跟踪集列表|

以下是 auditLists 列表的数据。

|参数名称|类型|描述|
|---------|---------|---------|
|Name|String|跟踪集名称|
|bucketName|String|COS Bucket 名称|
|prefix|String|日志前缀|
|status|Number|Audit 状态，0代表关闭，1代表开启|
|IsMultiRegionAudit|Number|是否开启多地域采集，0：否，1：是|

## 实际案例
### 请求

```
{
}
```
### 响应

```
{
    "auditLists": [
        {
            "name": "xxx-1",
            "bucketName":"xxx",
            "prefix":"xxx",
            "status":1,
            "IsMultiRegionAudit":0
        },
        {
            "name": "xxx-1",
            "bucketName":"xxx",
            "prefix":"xxx",
            "status":1,
            "IsMultiRegionAudit":0
        }
    ]
}
```
