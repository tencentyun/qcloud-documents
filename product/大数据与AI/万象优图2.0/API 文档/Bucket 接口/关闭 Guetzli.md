## 功能描述
用于关闭 Guetzli 压缩功能。

## 请求
#### 请求语法

```
DELETE /?guetzli HTTP/1.1
Host: <BucketName-APPID>.pic.<Region>.myqcloud.com 
Date: GMT Date
Authorization: Auth String
```
>?Authorization: Auth String（详情参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）

#### 请求行

```
DELETE /?guetzli HTTP/1.1
```
该 API 接口接受 DELETE 请求。

#### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情，请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求体
该请求的请求体为空。

## 响应
#### 响应头
#### 公共响应头
该响应使用公共响应头，了解公共响应头详情，请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。
#### 响应体
该响应体返回为空。

