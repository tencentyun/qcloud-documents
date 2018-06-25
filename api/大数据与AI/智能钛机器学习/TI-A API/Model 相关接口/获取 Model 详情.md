## 接口描述
本接口（DescribeModel）用于获取 Model 详情。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Name | 是 | String | 模型名称。|
| Cluster | 是 | String | 模型所在集群名称。|

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Model | Model | 模型信息。|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| ResourceNotFound | 资源不存在。|

## 示例
#### 输入：
```
 https://tia.tencentcloudapi.com/?Action=DescribeModel
&Name=test-model
&Cluster=ap-beijing
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "Model": {
      "AppId": 1000000000,
      "Cluster": "ap-beijing",
      "CreateTime": "2018-04-26 16:00:00 +0800 CST",
      "Description": "test-model",
      "Message": "xxxxxxxxxx",
      "Model": "/* cos or nfs address */",
      "Name": "test-model",
      "RuntimeVersion": "tiaserv-1.6.0-cpu",
      "ServType": "1U2G0P",
      "ServingUrl": "192.0.0.168",
      "State": "Running"
    },
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```