## 功能描述

使用API读取Object的ACL表

| -          | Bucket维度                | Object维度                |
| ---------- | ----------------------- | ----------------------- |
| Read（读权限）  | GetBucket,HeadBucket    | GetObject, HeadObject   |
| Write（写权限） | PutBucket, DeleteBucket | PutObject, DeleteObject |

## 请求

### 请求语法

```http
GET /ObjectName?acl Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: Auth String
```

### 请求参数

无特殊请求参数

### 必选头部

| 参数名称          | 是否必选 | 类型     | 描述   |
| ------------- | ---- | ------ | ---- |
| Authorization | 是    | String | 签名串  |


### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 参数名称                | 描述                                       |
| ------------------- | ---------------------------------------- |
| AccessControlPolicy | 一条独立的ACL记录                               |
| Owner               | 标识资源的所有者                                 |
| uin                 | 用户QQ号                                    |
| Subacount           | 子账户QQ账号                                  |
| AccessControlList   | 被授权者信息与权限信息                              |
| Grant               | 单条授权信息，一个AccessControlList钟可以拥有100条Grant |
| Grantee             | 被授权者资源信息，type类型可以为RootAcount， SubAccount；当type类型为RootAcount时，可以在UIN中填写QQ，也可以填写anonymous（指代所有类型用户）。当type类型为RootAcount时，UIN代表根账户账号，SubAccount代表子账户账号 |
| Permission          | 权限信息，枚举值：READ，WRITE，FULL_CONTROL         |
