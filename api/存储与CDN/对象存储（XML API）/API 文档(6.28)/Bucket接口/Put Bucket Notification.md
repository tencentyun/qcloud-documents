## 功能描述

Put Bucket Notification 接口实现配置用户回调通知。目前支持用户主动触发的 Object 创建与删除的回调通知，不支持自动策略，例如生命周期管理和跨区域复制的回调通知，只支持回调自己的业务资源。

**回调支持事件**

| 回调关联事件 | 描述 |
| ---------------------------------------- | ---------------------------------------- |
| cos:ObjectCreated:Put | 使用 Put Object 接口创建文件 |
| cos:ObjectCreated:Post | 使用 Post Object 接口创建文件 |
| cos:ObjectCreated:Copy | 使用 Put Object - Copy 接口创建文件 |
| cos:ObjectCreated:Append | 使用 Append Object 接口创建文件 |
| cos:ObjectCreated:CompleteMultipartUpload | 使用 CompleteMultipartUploadt 接口创建文件 |
| cos:ObjectCreated:* | 使用以上提到的"ObjectCreated"类型接口创建文件 |
| cos:ObjectRemove:Delete | 在未开启版本管理的 Bucket下 使用 Delete Object 接口删除的 Object，或者使用 versionid 删除指定版本的 Object |
| cos:ObjectRemove:DeleteMarkerCreated | 在开启或者暂停版本管理的 Bucket 下使用 Delete Object 接口删除的 Object |
| cos:ObjectRemove:* | 使用以上提到的"ObjectRemove"类型接口删除文件 |

## 请求

### 请求语法

```HTTP
PUT /?notification HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth

<XML File>
```

### 请求参数

无特殊请求参数。

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

### 请求内容

| 名称                       | 描述                                                         | 类型      | 是否必选 |
| -------------------------- | ------------------------------------------------------------ | --------- | ---- |
| NotificationConfiguration  | 说明本Bucket回调请求的所有内容，支持覆盖，当内容为空时，意为删除原有配置 | Container | 是   |
| CloudFunctionConfiguration | 配置的回调请求，支持配置一条或多条 Configuration，不可以使用重叠前缀，不可以使用重叠后缀<br> 父节点：NotificationConfiguration | Container | 是   |
| Id                         | 用来标示回调规则的 ID<br>父节点：CloudFunctionConfiguration      | String    | 否   |
| Filter                     | 应用回调规则的目录范围，不指定则为根目录 父节点：CloudFunctionConfiguration | Container | 否   |
| S3Key                      | 包含多条 FilterRule<br> 父节点：Filter                            | Container | 否   |
| FilterRule                 | 包含具体的前缀或者后缀策略，支持配置一个或两个 FilterRule<br> 父节点：S3Key | Container | 否   |
| Name                       | FilterRule 的类型，枚举值：Prefix，Suffix<br> 父节点：FilterRule  | String    | 否   |
| Value                      | 前缀或者后缀的值<br> 父节点：FilterRule                          | String    | 否   |
| CloudFunction              | Lambda 回调地址，格式：qcs:0:lambda:地区(sh):用户表示(appid/10000):业务标识(ID) <br>父节点：CloudFunctionConfiguration | String    | 是   |
| Event                      | 回调关联事件，支持配置一个或多个回调关联事件<br> 父节点：CloudFunctionConfiguration | String    | 是   |

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

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

### 返回内容

无返回内容。
