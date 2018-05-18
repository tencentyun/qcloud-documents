## 接口描述
本接口（DeleteModel）用于删除一个指定的 Model。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Name | 是 | String | 要删除的模型名称。|
| Cluster | 是 | String |要删除的模型所在的集群名称。|

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| FailedOperation.TimeOut | 操作超时。|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| ResourceNotFound | 资源不存在。|
| UnauthorizedOperation | 未授权操作。|
| UnsupportedOperation.UnsupportedVersion | 集群版本过低。|

## 示例
#### 输入：
```
 https://tia.tencentcloudapi.com/?Action=DeleteModel
&Name=test-model
&Cluster=ap-beijing
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```