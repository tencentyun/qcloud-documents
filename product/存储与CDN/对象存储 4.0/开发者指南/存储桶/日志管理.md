## 简介
日志管理是存储桶的功能之一，该功能通过将指定源存储桶的日志记录保存到目标存储桶来实现日志管理，记录源存储桶的详细访问日志。

在目标存储桶中，日志记录路径为：
```
目标存储桶/{对象键前缀}/cos_logset_guangzhou/cos_topic_guangzhou/{y}/{m}/{d}/{time}_{random}_{index}.gz
```
日志每 5 分钟生成一次，一条记录为一行，每条记录包含多个字段，字段之间以`\t`分割，目前日志字段为：

| 序号   | 字段名称            | 说明        | 序号   | 字段名称            | 说明        |
| ---- | --------------- | --------- | ---- | --------------- | --------- |
| 01   | eventVersion    | 记录版本      | 11   | reqPath         | 请求路径      |
| 02   | bucketName      | 存储桶名称     | 12   | reqMethod       | 请求方法      |
| 03   | qcsRegion       | 请求地域      | 13   | userAgent       | 用户 UA      |
| 04   | eventTime       | 事件时间      | 14   | resHttpCode     | HTTP 返回码|
| 05   | eventSource     | 事件来源      | 15   | resErrorCode    | 错误码       |
| 06   | eventName       | 事件名称      | 16   | resErrorMsg     | 错误信息      |
| 07   | remoteIp        | 来源 IP      | 17   | resBytesSent    | 返回字节数     |
| 08   | userAccessKeyId | 用户访问 KeyId | 18   | resTotalTime    | 请求总耗时     |
| 09   | reqQcsSource    | 请求 qcs 源信息  | 19   | resTrueTime     | 内部处理耗时    |
| 10   | reqBytesSent    | 请求字节数     |   |

> **注意：**
> - 目前日志管理功能仅支持北京、上海、广州和成都这四个园区。
> - 日志管理功能要求源存储桶与目标存储桶必须在同一园区。
> - 存放日志的目标存储桶可以是源存储桶本身，但不推荐。
> - 目前只有 XML API 以及基于 XML API 实现的 SDK、工具等进行的请求访问存储桶时，才会记录日志；JSON API 以及基于 JSON API 实现的 SDK、工具等进行的访问，不会记录日志。

## 启用日志管理
### 使用控制台
用户可以通过控制台快速开启日志管理功能。操作指引参见 [日志管理控制台指南](https://cloud.tencent.com/document/product/436/17040)。

### 使用 API 
使用 API 为指定存储桶开启日志管理功能时，请参考以下步骤：
1. 创建日志角色
2. 日志角色绑定权限
3. 开启日志管理

#### 1. 创建日志角色
创建日志角色，具体接口信息参见 [CreateRole](https://cloud.tencent.com/document/product/598/13886)。
其中，roleName 必须为： CLS_QcsRole；
policyDocument 为：
```
{
    "version":"2.0",
    "statement":[{
        "action":"name/sts:AssumeRole",
        "effect":"allow",
        "principal":{
            "service":"cls.cloud.tencent.com",
        }
    }]
}
```
#### 2. 日志角色绑定权限
角色权限绑定权限，具体接口信息参见 [AttachRolePolicy](https://cloud.tencent.com/document/product/598/13889)。
其中，policyName 为：QcloudCOSAccessForCLSRole；roleName 为第 1 步中的 CLS_QcsRole，也可以使用创建 roleName 时返回的 roleID。

#### 3. 创建日志角色
调用接口，开启日志管理功能，具体接口信息参见 [PUT Bucket logging](https://cloud.tencent.com/document/product/436/17054)，其中，要求存放日志的目标存储桶和源存储桶在同一园区。
