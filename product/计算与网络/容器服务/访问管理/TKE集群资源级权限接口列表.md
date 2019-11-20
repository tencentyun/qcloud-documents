资源级权限指的是能够指定允许用户对哪些资源具有执行操作的能力。TKE（原 CCS）支持部分资源级权限，这意味着对于某些 TKE 操作，您可以控制何时允许用户执行操作 (基于必须满足的条件)或是允许用户使用的特定资源。
TKE 中可授权的资源类型：

|资源类型|授权策略中的资源描述方法|
|----|-----|
|集群相关|`qcs::ccs:$region::cluster/*`|

下表将介绍当前支持资源级权限的 TKE（TKE，Tencnet Kubernetes Engines，容器服务） API 操作。指定资源路径的时候，您可以在路径中使用 * 通配符。
>**注意：**
>如果某一个 TKE API 操作在下表中没有列出，则它不支持资源级权限。如果TKE API 操作不支持资源级权限，那么您还是可以向用户授予使用该操作的权限，但是必须为策略语句的资源元素指定 * 。

|API 操作|资源路径|
|-----|-----|
|DescribeClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeClusterServiceInfo|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|CreateClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>负载均衡资源<br>`qcs::clb:$region:$account:clb/*`<br>云硬盘资源<br>`qcs::cvm:$region:$account:volume/*`<br>`qcs::cvm:$region:$account:volume/$diskId`|
|ModifyClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>负载均衡资源<br>`qcs::clb:$region:$account:clb/*`<br>云硬盘资源<br>`qcs::cvm:$region:$account:volume/*`<br>`qcs::cvm:$region:$account:volume/$diskId`|
|DeleteClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|ModifyServiceDescription|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeServiceEvent|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|ResumeClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|PauseClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|RollBackClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|ModifyClusterServiceImage|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|RedeployClusterService|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeServiceInstance|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|ModifyServiceReplicas|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DeleteInstances|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeClusterNameSpaces|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|CreateClusterNamespace|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DeleteClusterNamespace|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeCluster|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|CreateCluster|云服务器资源<br>`qcs::cvm:$region:$account:instance/*`|
|DeleteCluster|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|DescribeClusterInstances|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
|AddClusterInstances|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>云服务器资源<br>`qcs::cvm:$region:$account:instance/*`|
|DeleteClusterInstances|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>云服务器资源<br>`qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`|
|AddClusterInstancesFromExistedCvm|集群资源<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>云服务器资源<br>`qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId`|


