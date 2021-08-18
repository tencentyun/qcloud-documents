## 简介
本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明
获取对象访问 URL用于匿名下载或分发。

#### 方法原型

```
get_object_url(Bucket, Key)
```

#### 请求示例


[//]: # (.cssg-snippet-get-object-url-alias)
```python
response = client.get_object_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 | 

#### 返回结果说明

该方法返回值为对象访问的 URL。
