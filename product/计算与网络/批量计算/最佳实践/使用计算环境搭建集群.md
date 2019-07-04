## 如何快速创建集群？

使用批量计算的计算环境能力，可以轻松高效的维护云服务器集群，Batch 的计算环境可以简单的对应常规的集群概念，下面的例子介绍如何使用计算环境能力来快速创建/销毁一个超性价比资源集群，目前计算环境仅支持命令行调用，请先参照开始准备安装命令行工具。

## 开始前的准备

开始前请根据文档 [开始前的准备](/doc/product/599/10807) 里的检查清单做好准备，同时本例将使用到命令行工具（CLI），用户需要先安装和配置命令行工具。

### 安装和配置命令行工具

配置命令行工具请查看 [配置命令行工具](/doc/product/440/6184)，安装完后检查下安装成功。
```
qcloudcli batch help

CreateComputeEnv                        	|DescribeJobSubmitInfo
CreateTaskTemplate                      	|DescribeJobs
DeleteComputeEnv                        	|DescribeTask
DeleteJob                               	|DescribeTaskTemplates
DeleteTaskTemplates                     	|ModifyTaskTemplate
DescribeAvailableCvmInstanceTypes       	|SubmitJob
DescribeComputeEnv                      	|TerminateJob
DescribeComputeEnvs                     	|TerminateTaskInstance
DescribeJob
```

## 创建计算环境

您可以将官方提供的例子修改为在您的账号下可执行的 Batch 计算环境。在此之前，请先查看计算环境配置的各项含义。
您也可以参考 [创建计算环境](/document/api/599/12691) 等计算环境相关接口。

下面的例子在广州二区快速创建包含10台 BS1.LARGE8（批量计算通用型 CPU 4核 内存 8GB）类型集群。

```
qcloudcli batch CreateComputeEnv --Version 2017-03-12 --ComputeEnv '{
    "EnvName": "batch-env",          // 计算环境名称
    "EnvDescription": "batch env demo",   // 计算环境描述
    "EnvType": "MANAGED",                   // 计算环境类型，托管型
    "EnvData": {                            // 具体配置（可参照 CVM 创建实例说明）
        "InstanceType": "BS1.LARGE8",       // 计算环境内CVM 实例类型
        "ImageId": "img-m4q71qnf",          // 计算环境内CVM 镜像 ID（可替换成自定义镜像）
        "LoginSettings": {
            "Password": "B1[habcd"          // 计算环境内CVM 登录密码
        },
        "InternetAccessible": {
            "PublicIpAssigned": "TRUE",     // 计算环境内CVM 是否需要公网IP
            "InternetMaxBandwidthOut": 10   // 计算环境内CVM 带宽上限
        },
        "SystemDisk": {
            "DiskType": "CLOUD_BASIC",      // 计算环境内CVM 磁盘类型（目前是普通云硬盘）
            "DiskSize": 50                  // 计算环境内CVM 磁盘大小
        }
    },
    "DesiredComputeNodeCount": 10           // 计算节点期望个数
}'
--Placement'{
    "Zone": "ap-guangzhou-2"                // 可用区（当前广州二区可能需替换）
}'
```

#### 请求示例

```
qcloudcli batch CreateComputeEnv --Version 2017-03-12 --ComputeEnv '{"EnvName":"batch-env","EnvDescription":"batch env demo","EnvType":"MANAGED","EnvData":{"InstanceType":"BS1.LARGE8","ImageId":"img-m4q71qnf","LoginSettings":{"Password":"B1[habcd"},"InternetAccessible":{"PublicIpAssigned":"TRUE","InternetMaxBandwidthOut":50},"SystemDisk":{"DiskType":"CLOUD_BASIC","DiskSize":50}},"DesiredComputeNodeCount":1}' --Placement '{"Zone": "ap-guangzhou-2"}'
```

#### 返回示例

返回值，其中 EnvId 为 Batch 计算环境的唯一标识。
```
{
    "Response": {
        "EnvId": "env-c96rwhnf",
        "RequestId": "bead16d4-b33b-47b5-9b86-6a02b4bed1b2"
    }
}
```
创建的主机可以通过云服务器控制台来查看，也可以通过 Batch 的计算环境接口来查看和管理，后面将介绍如何通过 Batch 的命令行接口来查看计算环境以及计算环境内的实例信息，会使用到 EnvId，可以记录返回的 EnvId。

## 查看计算环境列表

您可以通过 Batch 的命令行接口来查看创建的所有计算环境列表。

#### 请求示例

```
qcloudcli batch DescribeComputeEnvs --Version 2017-03-12
```

#### 返回示例

```
{
    "Response": {
        "TotalCount": 1,
        "ComputeEnvSet": [
            {
                "EnvId": "env-c96rwhnf",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "EnvType": "MANAGED",
                "EnvName": "test compute env",
                "ComputeNodeMetrics": {
                    "CreatedCount": 0,
                    "DeletingCount": 0,
                    "CreationFailedCount": 0,
                    "SubmittedCount": 0,
                    "CreatingCount": 0,
                    "AbnormalCount": 0,
                    "RunningCount": 2
                },
                "CreateTime": "2017-11-27T07:10:02Z"
            }
        ],
        "RequestId": "bac76f1c-06cd-4ef4-82a9-f230fa5a1992"
    }
}
```
返回结果中包含了所要查询的计算环境信息。

## 查看指定计算环境以及包含的节点列表

#### 请求示例

```
qcloudcli batch DescribeComputeEnv --Version 2017-03-12 --EnvId env-c96rwhnf
```

#### 返回示例

```
{
    "Response": {
        "EnvId": "env-c96rwhnf",
        "Placement": {
            "Zone": "ap-guangzhou-2"
        },
        "EnvType": "MANAGED",
        "EnvName": "test compute env",
        "RequestId": "12dc7dba-f33b-4d5a-8cd6-ebd1df17ebf7",
        "ComputeNodeMetrics": {
            "CreatedCount": 0,
            "DeletingCount": 0,
            "CreationFailedCount": 0,
            "SubmittedCount": 0,
            "CreatingCount": 0,
            "AbnormalCount": 0,
            "RunningCount": 2
        },
        "ComputeNodeSet": [
            {
                "ComputeNodeId": "node-838udz1w",
                "ComputeNodeState": "RUNNING",
                "Mem": 2,
                "ResourceCreatedTime": "2017-11-27T07:10:46Z",
                "ComputeNodeInstanceId": "ins-q09nyg5g",
                "AgentVersion": "1.0.7",
                "TaskInstanceNumAvailable": 1,
                "Cpu": 1
            },
            {
                "ComputeNodeId": "node-c4z8f8xc",
                "ComputeNodeState": "RUNNING",
                "Mem": 2,
                "ResourceCreatedTime": "2017-11-27T07:10:41Z",
                "ComputeNodeInstanceId": "ins-fgqcau4q",
                "AgentVersion": "1.0.7",
                "TaskInstanceNumAvailable": 1,
                "Cpu": 1
            }
        ],
        "CreateTime": "2017-11-27T07:10:02Z"
    }
}
```

包含了计算环境整体，以及每个节点的详细信息。

## 销毁计算环境

#### 请求示例

```
qcloudcli batch DeleteComputeEnv --Version 2017-03-12 --EnvId env-c96rwhnf
```

#### 返回示例
```
{
    "Response": {
        "RequestId": "389f011a-7dbd-4993-82fe-334ac923ff88"
    }
}
```

调用后计算环境会自动销毁集群内所有的云服务器。
