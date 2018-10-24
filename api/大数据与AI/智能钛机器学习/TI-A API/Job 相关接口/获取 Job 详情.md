## 接口描述
本接口（DescribeJob）用用于获取训练任务详情。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Name | 是 | String | 任务名称。 |
| Cluster | 是 | String | 运行任务的集群。 |

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Job | Job | 训练任务信息。|
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
 https://tia.tencentcloudapi.com/?Action=DescribeJob
&Name=test-job
&Cluster=ap-beijing
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "Job": {
      "AppId": 10000000000,
      "Cluster": "ap-beijing",
      "Command": [
        "python",
        "/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py",
        "--num_batches=100",
        "--num_warmup_batches=5",
        "--summary_verbosity=1",
        "--local_parameter_device=gpu",
        "--cross_replica_sync=True",
        "--batch_size=128",
        "--device=gpu",
        "--variable_update=tfplus",
        "--model=resnet101"
      ],
      "CreateTime": "2018-04-26 15:00:00 +0800 CST",
      "EndTime": "2018-04-26 16:00:00 +0800 CST",
      "MasterType": "16U48G1P",
      "Name": "test-job",
      "PackageDir": [
        ""
      ],
      "RuntimeVersion": "tfplus-1.6.0-gpu",
      "State": "Succeeded",
      "WorkerCount": 45,
      "WorkerType": "16U48G1P"
    },
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```