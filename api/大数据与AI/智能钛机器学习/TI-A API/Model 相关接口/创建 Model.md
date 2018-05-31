## 接口描述
本接口（CreateModel）用于在指定的集群上部署一个模型，以此来提供服务。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---
| Name | 是 | String | 模型名称。 |
| Description | 否 | String | 关于模型的描述。 |
| Cluster | 是 | String | 指定集群的名称。|
| Model | 是 | String | 要部署模型的路径名。|
| RuntimeVersion | 否 | String | 运行环境镜像的标签。|
| Replicas | 否 | Integer | 要部署的模型副本数目。|
| Expose | 否 | String | 暴露外网或内网，默认暴露外网。|
| ServType | 否 | String | 要部署模型的机器配置。|

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Model | Model | 模型的详细信息。|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| FailedOperation.AlreadyExists | 资源已存在。|
| FailedOperation.TimeOut | 操作超时。|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| UnauthorizedOperation | 未授权操作。|
| UnsupportedOperation.UnsupportedVersion |集群版本过低。|

## 示例
#### 场景描述
在名为 ap-beijing 的集群上运行一个名为 test-model 的模型，对外提供服务。使用预提供的标签为 tiaserv-1.6.0-cpu 的运行环境，指定机器配置为：4 核 CPU，8G 内存，不使用 GPU。

#### 输入：
```
 https://tia.tencentcloudapi.com/?Action=CreateModel
&Name=test-model
&Description=test-model
&Cluster=ap-beijing
&Model=/* nfs or cos address */
&RuntimeVersion=tiaserv-1.6.0-cpu
&Replicas=1
&Expose=external
&ServType=4U8G0P
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "Model": {
      "AppId": "xxxxxxxxxx",
      "Cluster": "ap-beijing",
      "CreateTime": "2018-05-23 10:00:00 +0800 CST",
      "Description": "test-model",
      "Expose": "external",
      "Message": "creating",
      "Model": "/* nfs or cos address */",
      "Name": "test-model",
      "Replicas": 1,
      "RuntimeVersion": "tiaserv-1.6.0-cpu"
    },
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```