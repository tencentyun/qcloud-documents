## 接口描述
本接口（ListJob）用于列举训练任务。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Cluster | 是 | String | 运行任务的集群。 |

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| Jobs | Array | |
| of | Job |训练任务列表。|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
|错误码|描述|
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
 https://tia.tencentcloudapi.com/?Action=ListJob
&Cluster=ap-beijing
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "Jobs": [
      {
        "AppId": 10000000000,
        "Cluster": "ap-beijing",
        "Command": [
          "python",
          "/tf_cnn_benchmarks.py",
          "--num_batches=100",
          "--num_warmup_batches=5",
          "--summary_verbosity=1",
          "--local_parameter_device=gpu",
          "--cross_replica_sync=True",
          "--batch_size=64",
          "--device=gpu",
          "--variable_update=distributed_all_reduce",
          "--all_reduce_spec=xring",
          "--model=resnet101"
        ],
        "CreateTime": "2018-05-23 14:00:00 +0800 CST",
        "EndTime": "2018-04-26 15:00:00 +0800 CST",
        "MasterType": "16U48G1P",
        "Message": "[MASTER/Failed : Failed/1] ;[WORKER/Running : Running/1]",
        "Name": "testtfgpu0105",
        "PackageDir": [
          ""
        ],
        "RuntimeVersion": "tia_gpu_1.6.0",
        "State": "Failed",
        "WorkerCount": 1,
        "WorkerType": "16U48G1P"
      },
      {
        "AppId": 1000000000,
        "Cluster": "ap-beijing",
        "Command": [
          "python",
          "/tf_cnn_benchmarks.py",
          "--num_batches=100",
          "--num_warmup_batches=5",
          "--summary_verbosity=1",
          "--local_parameter_device=gpu",
          "--cross_replica_sync=True",
          "--batch_size=64",
          "--device=gpu",
          "--variable_update=distributed_all_reduce",
          "--all_reduce_spec=xring",
          "--model=resnet101"
        ],
        "CreateTime": "2018-04-26 14:00:00 +0800 CST",
        "EndTime": "2018-04-26 15:00:00 +0800 CST",
        "MasterType": "16U48G1P",
        "Message": "[MASTER/Succeed : Succeed/1]",
        "Name": "testtfgpu0106",
        "PackageDir": [
          ""
        ],
        "RuntimeVersion": "tia_gpu_1.6.0",
        "State": "Succeed",
        "WorkerType": "16U48G1P"
      },
      {
        "AppId": 100000000,
        "Cluster": "ap-beijing",
        "Command": [
          "python",
          "/tf_cnn_benchmarks.py",
          "--num_batches=100",
          "--num_warmup_batches=5",
          "--summary_verbosity=1",
          "--local_parameter_device=gpu",
          "--cross_replica_sync=True",
          "--batch_size=64",
          "--device=gpu",
          "--variable_update=distributed_all_reduce",
          "--all_reduce_spec=xring",
          "--model=resnet101"
        ],
        "CreateTime": "2018-04-26 14:00:00 +0800 CST",
        "EndTime": "2018-04-26 15:00:00 +0800 CST",
        "MasterType": "16U48G1P",
        "Message": "[MASTER/Failed : Failed/1]",
        "Name": "testtfgpu0107",
        "PackageDir": [
          ""
        ],
        "RuntimeVersion": "tia_gpu_1.6.0",
        "State": "Failed"
      }
    ],
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```