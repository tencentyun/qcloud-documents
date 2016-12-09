## 功能描述

Head Object请求可以取回对应Object的元数据，Head的权限与Get的权限一致

## 请求

### 请求语法

```Http
HEAD /ObjectName HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 推荐使用头部

| 名称                | 描述                                      | 类型     | 必选   |
| ----------------- | --------------------------------------- | ------ | ---- |
| If-Modified-Since | 当Object在指定时间后被修改，则返回对应Object元信息，否则返回304 | String | 否    |

### 请求内容

无请求内容

## 返回值

### 返回头部

| 名称                | 描述                                       | 类型     |
| ----------------- | ---------------------------------------- | ------ |
| x-cos-meta-*      | 用户自定义的元数据                                | String |
| x-cos-object-type | 用来表示object是否可以被追加上传，枚举值：normal或者appendable | string |


### 返回内容

无返回内容