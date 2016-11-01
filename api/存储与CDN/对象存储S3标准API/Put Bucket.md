## 功能描述

Put Bucket请求可以在指定账号下创建一个Bucket。

## 请求

### 请求语法

```Http
PUT / HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: *date*
Authorization: authorization string
```

### 请求参数

无特殊请求参数

#### 推荐使用头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private \| public-read \| public-read-write，默认值：private | String | 否    |
| X-cos-grant-read         | 赋予被授权者读的权限<br />格式X-cos-grant-read: uin=" ",uin=" " | String | 否    |
| X-cos-grant-write        | 赋予被授权者写的权限<br />格式X-cos-grant-write: uin=" ",uin=" " | String | 否    |
| X-cos-grant-full-control | 赋予被授权者读写权限<br />格式X-cos-grant-full-control: uin=" ",uin=" " | String | 否    |

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容