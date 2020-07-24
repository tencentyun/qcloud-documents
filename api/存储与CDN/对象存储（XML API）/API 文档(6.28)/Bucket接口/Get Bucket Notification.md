## 功能描述

Get Bucket Notification 接口实现读取用户回调通知配置。

## 请求

### 请求语法

```HTTP
GET /?notification HTTP 1.1
Host:<Bucketname>-<AppID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数。

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

无请求内容。

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

| 名称                       | 描述                                                         | 类型      |
| -------------------------- | ------------------------------------------------------------ | --------- |
| NotificationConfiguration  | 说明本 Bucket 回调请求的所有内容，支持覆盖，当内容为空时，意为删除原有配置 | Container |
| CloudFunctionConfiguration | 配置的回调请求，支持配置一条或多条 Configuration，不可以使用重叠前缀，不可以使用重叠后缀<br> 父节点：NotificationConfiguration | Container |
| Id                         | 用来标示回调规则的 ID<br>父节点：CloudFunctionConfiguration      | String    |
| Filter                     | 应用回调规则的目录范围，不指定则为根目录<br>父节点：CloudFunctionConfiguration | Container |
| S3Key                      | 包含多条 FilterRule <br>父节点：Filter                            | Container |
| FilterRule                 | 包含具体的前缀或者后缀策略，支持配置一个或两个 FilterRule<br> 父节点：S3Key | Container |
| Name                       | FilterRule的类型，枚举值：Prefix，Suffix<br> 父节点：FilterRule  | String    |
| Value                      | 前缀或者后缀的值<br> 父节点：FilterRule                          | String    |
| CloudFunction              | Lambda 回调地址，格式：qcs:0:lambda:地区(sh):用户表示(appid/10000):业务标识(ID)<br> 父节点：CloudFunctionConfiguration | String    |
| Event                      | 回调关联事件，支持配置一个或多个回调关联事件<br>父节点：CloudFunctionConfiguration | String    |




```xml
<NotificationConfiguration>
  <CloudFunctionConfiguration>
    <Id></Id>
    <Filter>
      <S3Key>
        <FilterRule>
          <Name></Name>
          <Value></Value>
        </FilterRule>
        ...
      </S3Key>
    </Filter>
    <CloudFunction></CloudFunction>
    <Event></Event>
    ...
  </CloudFunctionConfiguration>
  ...
</NotificationConfiguration>
```
