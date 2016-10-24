## 功能描述

Put Bucket请求可以在指定账号下创建一个Bucket。

## 请求

### 请求语法

```Http
PUT / HTTP/1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: authorization string
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他内容请参见公共请求头部

### 必选头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private, public-read, public-read-write，默认值：private | String | 否    |
| X-cos-grant-read         | 赋予被授权者读的权限<br />格式X-cos-grant-read: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| X-cos-grant-write        | 赋予被授权者写的权限<br />格式X-cos-grant-write: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| X-cos-grant-full-control | 赋予被授权者读写权限<br />格式X-cos-grant-full-control: uin=" ",uin=" "，当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |

### 推荐使用头部

| 名称   | 描述   | 类型   | 必选   |
| ---- | ---- | ---- | ---- |
|      |      |      |      |

#### 权限相关头部

| 名称   | 描述   | 类型   | 必选   |
| ---- | ---- | ---- | ---- |
|      |      |      |      |

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊请求头部，其他内容请参见公共返回头部

### 返回内容

无

## 示例