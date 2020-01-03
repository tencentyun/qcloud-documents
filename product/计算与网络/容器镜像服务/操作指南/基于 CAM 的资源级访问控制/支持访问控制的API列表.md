
### 实例相关
| API 操作 | 资源路径 |
| :-------- | -------------- |
| CreateInstance | `qcs::tcr:$region:$account:instance/$instanceid`|
| DeleteInstance | `qcs::tcr:$region:$account:instance/$instanceid`|
| ModifyInstance | `qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeInstances | `qcs::tcr:$region:$account:instance/*`<br>`qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeInstanceStatus | `qcs::tcr:$region:$account:instance/$instanceid` |
| CreateInstanceToken | `qcs::tcr:$region:$account:instance/$instanceid` |

### 网络访问控制相关
| API 操作 | 资源路径 |
| :-------- | -------------- |
| ManageExternalEndpoint | `qcs::tcr:$region:$account:instance/$instanceid` |
| CreateSecurityPolicy | `qcs::tcr:$region:$account:instance/$instanceid` |
| ModifySecurityPolicy | `qcs::tcr:$region:$account:instance/$instanceid` |
| DeleteSecurityPolicy | `qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeExternalEndpointStatus | `qcs::tcr:$region:$account:instance/$instanceid` |
| ManageInternalEndpoint | `qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeInternalEndpoints | `qcs::tcr:$region:$account:instance/$instanceid` |

### 实例同步相关
| API 操作 | 资源路径 |
| :-------- | -------------- |
| ManageReplication | `qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeReplication | `qcs::tcr:$region:$account:instance/$instanceid` |

### 命名空间相关
| API 操作 | 资源路径 |
| :-------- | -------------- |
| CreateNamespace | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename`|
| DeleteNamespace | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename`|
| ModifyNamespace | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename` |
| DescribeNamespaces | `qcs::tcr:$region:$account:instance/$instanceid/*`<br>`qcs::tcr:$region:$account:instance/$instanceid/$namespacename` |

### 镜像仓库相关
| API 操作 | 资源路径 |
| :-------- | -------------- |
| CreateRepository | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename/$repositoryname`|
| DeleteRepository | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename/$repositoryname`|
| ModifyRepository | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename/$repositoryname` |
| DescribeRepositories | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename/*`<br>`qcs::tcr:$region:$account:instance/$instanceid/$namespacename/$repositoryname` |
| PullRepository | `qcs::tcr:$region:$account:instance/$instanceid/$namespacename/$repositoryname`|

