>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 接口描述
本接口 ( DescribeClusterRequestLimitInfo ) 用于查询集群 CPU、内存的 Request 和 Limit 信息。

接口请求域名：
```
ccs.api.qcloud.com
```


## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。


| 参数名称   | 描述                               | 类型     | 必选 |
|-----------|-----------------------------------|----------|------|
|clusterId|集群 ID，请填写 [查询集群列表](/doc/api/457/9448) 接口中返回的 clusterId 字段|String|是|

## 输出参数

| 参数名称 | 描述 |类型 |
|---------|---------|---------|
| code |公共错误码。0 表示成功，其他值表示失败| Int |
| codeDesc | 业务错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message | 模块错误信息描述，与接口相关|String |
| data | 返回参数的数据部分，此接口返回为 null |Object |

其中，data 字段的结构如下：

| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
|totalCpuRequest|集群整体 CPU 的 Request|Int|
|totalCpuLimit|集群整体 CPU 的 Limit|Int|
|totalMemRequest|集群整体内存的 Request|Int|
|totalMemLimit|集群整体内存的 Limit|Int|
|totalGpuLimit|集群整体 GPU 的 Limit|Int|
|requestLimitInfo.InstanceIp|集群内节点的 Request 和 Limit 的详细分配详细，结构内为实例内网 IP|Object|
|totalCpu|集群整体 CPU 使用量| Int
totalMem|集群整体内存 的 Limit| Int
totalGpu|集群整体 GPU 使用量| Int

data 字段中的 requestLimitInfo.InstanceIp 字段结构如下：

| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
|cpuRequest|集群内对应 InstanceIp 实例 cpuRequest|Int|
|cpuLimit|集群内对应 InstanceIp 实例 cpuLimit|Int|
|memRequest|集群内对应 InstanceIp 实例 memRequset|Int|
|memLimit|集群内对应 InstanceIp 实例 memLimit|Int|
|gpuLimit|集群内对应 InstanceIp 实例 gpuLimit|Int|

## 示例
### 输入
```
  https://domain/v2/index.php?Action=GetLogDaemonStatus
  &clusterId=cls-xxxxxx
  &其它公共参数
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCpuRequest": 0.26,
        "totalCpuLimit": 0,
        "totalMemRequest": 0.07,
        "totalMemLimit": 0,
        "totalGpuLimit": 0,
        "requestLimitInfo": {
            "172.27.0.7": {
                "cpuRequest": 0.26,
                "cpuLimit": 0,
                "memRequest": 0.07,
                "memLimit": 0,
                "gpuLimit": 0
            }
        },
        "totalCpu": 0.94,
        "totalMem": 0.71,
        "totalGpu": 0
    }
}
```
