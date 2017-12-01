
## 接口描述
 ListCosBuckets 用于拉取 COS 的 Bucket 列表。
## 请求参数
详见 [公共请求参数](https://cloud.tencent.com/document/product/599/12707)  页面。

## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| cosBucketsList | Array | COS Bucket 列表 |

其中 cosBucketsList 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| name | String | COS Bucket 名称 |
| region | String | Bucket 所在的地域 |
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


