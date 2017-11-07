# 拉取 CloudAudit 列表
## 接口描述
  ListAudits 用于拉取 CloudAudit 列表。
## 请求参数
详见 [公共请求参数](https://cloud.tencent.com/document/api/214/4183)  页面。

## 响应参数
以下是 auditLists 列表的数据。

|参数名称|类型|描述|
|---------|---------|---------|
|Name|string|CloudAudit 名字|
|bucketName|string|COS 存储桶名称|
|prefix|string|日志前缀|
|status|number|状态（0：关闭，1：开启）|
|isMultiRegionTrail|number|是否开启多地域采集（0：否，1：是）|

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
            "isMultiRegionTrail":0
        },
        {
            "name": "xxx-1",
            "bucketName":"xxx",
            "prefix":"xxx",
            "status":1
            "isMultiRegionTrail":0
        }
    ]
}
```


