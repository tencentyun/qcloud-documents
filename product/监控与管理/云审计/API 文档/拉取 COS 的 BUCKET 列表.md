# 拉取 COS 的 BUCKET 列表
## 接口描述
 ListCosBuckets 用于拉取 COS 的 BUCKET 列表。
## 请求参数
详见 [公共请求参数](https://cloud.tencent.com/document/api/214/4183)  页面。

## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| cosBucketsList | Array | COS Bucket 数组 |

其中 cosBucketsList 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| name | string | COS Bucket 名称 |
| region | string | Bucket 所在的区域 |
## 实际案例
### 请求

```
{
}
```
### 响应

```
{
    "cosBucketsList": [
        {
            "region": "gz",
            "name": "xxx-1"
        },
        {
            "region": "gz",
            "name": "xxx-2"
        }
    ]
}
```


