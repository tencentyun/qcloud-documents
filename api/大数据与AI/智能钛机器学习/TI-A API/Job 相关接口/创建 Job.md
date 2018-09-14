## 接口描述
本接口（CreateJob）用于创建训练任务。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Name | 是 | String | 任务名称 |
| Cluster | 是 | String | 运行任务的集群 |
| RuntimeVersion | 是 | String | 运行任务的环境 | 
| PackageDir | 否 | Array of String | 挂载的路径，支持 NFS、COS(COS 只在 TI-A 运行环境中支持) |
| Command | 否 | Array of String | 任务启动命令 |
| Args | 否 | Array of String | 任务启动参数  |
| ScaleTier | 否 | String |  运行任务的配置信息 |
| MasterType | 否 | String |（ScaleTier 为 Custom 时）Master 机器类型 |
| WorkerType | 否 | String |（ScaleTier为Custom时）Worker 机器类型 |
| ParameterServerType | 否 | String |（ScaleTier为Custom时）Parameter server 机器类型 |
| WorkerCount | 否 | Integer |（ScaleTier为Custom时）Worker 机器数量|
| ParameterServerCount | 否 | Integer |（ScaleTier 为 Custom 时）parameter server 机器数量| 

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Job | Job | 训练任务信息。|
| RequestId | String| 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|
## 错误码
|错误码|描述|
|---|---|
| FailedOperation.AlreadyExists | 资源已存在。|
| FailedOperation.TimeOut | 操作超时。|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| ResourceUnavailable | 资源不可用。|
| UnauthorizedOperation | 未授权操作。|
| UnsupportedOperation.UnsupportedVersion| 集群版本过低。|
## 示例
在名为 ap-beijing 的集群上创建一个名为 test-job 的分布式任务，采用 1 个 Master、1 个 ps 和 2 个 Worker 的结构，使用预提供的标签为 tia-1.7.0 的运行环境。

#### 输入：
```
https://tia.tencentcloudapi.com/?Action=CreateJob\
&Name=test-job
&Cluster=ap-beijing
&RuntimeVersion=tia-1.7.0
&ScaleTier=Custom
&MasterType=1U1G0P
&WorkerType=1U1G0P
&ParameterServerType=1U1G0P
&WorkerCount=2
&ParameterServerCount=1
&PackageDir.0=/* nfs or cos address */
&Command.0=python
&Args.0=mnist_saved_model.py
&<公共请求参数>
```
#### 输出：
```
 {
  "Response": {
    "Job": {
      "Args": [
        "mnist_saved_model.py"
      ],
      "Cluster": "ap-beijing",
      "Command": [
        "python"
      ],
      "CreateTime": "2018-05-23 10:00:00.000000000 +0800 CST m=+66666.666666666",
      "MasterType": "1U1G0P",
      "Message": "creating",
      "Name": "test-job",
      "PackageDir": [
        "/* nfs or cos address */"
      ],
      "ParameterServerCount": 1,
      "ParameterServerType": "1U1G0P",
      "RuntimeVersion": "tia-1.7.0",
      "ScaleTier": "Custom",
      "WorkerCount": 2,
      "WorkerType": "1U1G0P"
    },
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```
