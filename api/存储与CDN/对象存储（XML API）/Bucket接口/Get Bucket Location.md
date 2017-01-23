## 功能描述
Get Bucket Location接口获取Bucket所在地域信息，只有Bucket所有者有权限读取信息。

## 请求

### 请求语法

```HTTP
GET /?location HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                 | 描述                                       | 类型     |
| ------------------ | ---------------------------------------- | ------ |
| LocationConstraint | Bucket所在区域，枚举值：china-east，china-south，china-north，china-west，singapore | String |

