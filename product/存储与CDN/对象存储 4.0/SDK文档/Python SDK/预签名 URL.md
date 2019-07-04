## 简介
Python SDK 提供获取签名，获取请求预签名 URL 接口以及获取对象下载预签名 URL 接口。使用永久密钥或临时密钥获取预签名 URL 的调用方法相同，使用临时密钥时需要在 header 或 query_string 中加上 x-cos-security-token。


## 获取签名

#### 功能说明
获取指定操作的签名，常用于移动端的签名分发。

#### 方法原型

```
get_auth(Method, Bucket, Key, Expired=300, Headers={}, Params={})
```

#### 上传请求示例

```python
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```

#### 下载请求示例

```python
response = client.get_auth(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```

#### 全部参数请求示例

```python
response = client.get_auth(
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=300,
    Headers={
        'Content-Length': 'string',
        'Content-MD5': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Method  |对应操作的 Method, 可选值为 'PUT'，'POST'，'GET'，'DELETE'，'HEAD'|  String |  是 | 
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | Bucket 操作填入根路径`/`，object 操作填入文件的路径| String | 是| 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Headers| 需要签入签名的请求头部| Dict| 否|
 |Params | 需要签入签名的请求参数| Dict| 否|

#### 返回结果说明
该方法返回值为对应操作的签名值。

## 获取预签名 URL

#### 功能说明
获取预签名链接用于分发。

#### 上传请求示例

```python
response = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```

#### 下载请求示例

```python
response = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```


#### 方法原型

```
get_presigned_url(Bucket, Key, Method, Expired=300, Params={}, Headers={})
```
#### 请求示例

```python
response = client.get_presigned_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
    Expired=300,
    Headers={
        'Content-Length': 'string',
        'Content-MD5': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 | 
 | Method  |对应操作的 Method, 可选值为 'PUT'，'POST'，'GET'，'DELETE'，'HEAD'|  String |  是 | 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Params| 签名中要签入的请求参数| Dict| 否|
 |Headers| 签名中要签入的请求头部| Dict| 否|
 
 
#### 返回结果说明
该方法返回值为预签名的 URL。

## 获取预签名下载 URL

#### 功能说明
获取预签名下载链接用于直接下载。

#### 方法原型

```
get_presigned_download_url(Bucket, Key, Expired=300, Params={}, Headers={})
```
#### 请求示例

```python
response = client.get_presigned_download_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 | 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Params| 签名中要签入的请求参数| Dict| 否|
 |Headers| 签名中要签入的请求头部| Dict| 否|

#### 返回结果说明
该方法返回值为预签名的下载 URL。
