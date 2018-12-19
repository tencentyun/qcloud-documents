## 接口描述
本接口（ListModel）用于列举某个指定集群上运行的模型。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Cluster | 是 | String | 需要获得模型列表的目标集群名称。|

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Models | Array of Model | Model 数组，用以显示所有模型的信息。|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| FailedOperation.TimeOut | 操作超时。|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| ResourceNotFound | 资源不存在。|
| ResourceUnavailable | 资源不可用。|
| UnauthorizedOperation | 未授权操作。|
| UnsupportedOperation.UnsupportedVersion | 集群版本过低。|

## 示例
#### 输入：
```
 https://tia.tencentcloudapi.com/?Action=ListModel
&Cluster=ap-beijing
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "Models": [
      {
        "AppId": 1000000000,
        "Cluster": "ap-beijing",
        "CreateTime": "2018-04-26 14:30:00 +0800 CST",
        "Description": "test-model",
        "Message": "ReplicaSet \"test-model-685b46f8b\" has successfully progressed.",
        "Model": "/* cos of nfs address */",
        "Name": "test-model",
        "RuntimeVersion": "tiaserv-1.6.0-cpu",
        "ServType": "4U8G0P",
        "ServingUrl": "192.0.0.168",
        "State": "Creating"
      }
    ],
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```
