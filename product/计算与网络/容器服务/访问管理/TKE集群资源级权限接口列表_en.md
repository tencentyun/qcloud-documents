Resource-level permissions can be used to specify which resources users can work with. CCS supports setting partial permissions for resources. This means that for some CCS operations, you can control the time when users are allowed to perform operations (condition must be met) or to use specified resources.
The type of resource that can be authorized in CCS:

| Resource Type | Resource description method in authorization policy |
|----|-----|
| Cluster-related | `qcs::ccs:$region::cluster/*` |

The following table describes API operations of Cloud Container Service (CCS) that support resource-level permissions. You can use wildcard "*" in the path when specifying resource path.
>**Note:**
>A certain CCS API operation not listed here does not support resource-level permission. If any CCS API operation does not support resource-level permission, you can still authorize the permission of this operation to users, but you must specify * for the resource element of policy statement.

| API Operation | Resource Path |
|-----|-----|
| DescribeClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DescribeClusterServiceInfo | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| CreateClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>Load balance resource<br>`qcs::clb:$region:$account:clb/*`<br>Cloud disk resource<br>`qcs::cvm:$region:$account:volume/*`<br>`qcs::cvm:$region:$account:volume/$diskId` |
| ModifyClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>Load balance resource<br>`qcs::clb:$region:$account:clb/*`<br>Cloud disk resource<br>`qcs::cvm:$region:$account:volume/*`<br>`qcs::cvm:$region:$account:volume/$diskId` |
| DeleteClusterService |Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| ModifyServiceDescription| Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DescribeServiceEvent| Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| ResumeClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| PauseClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| RollBackClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| ModifyClusterServiceImage | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| RedeployClusterService | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DescribeServiceInstance | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| ModifyServiceReplicas | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DeleteInstances | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DescribeClusterNameSpaces | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| CreateClusterNamespace | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DeleteClusterNamespace | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| DescribeCluster | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| CreateCluster | CVM resource<br>`qcs::cvm:$region:$account:instance/*` |
| DeleteCluster | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`|
| DescribeClusterInstances | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId` |
| AddClusterInstances | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>CVM resource<br>`qcs::cvm:$region:$account:instance/*` |
| DeleteClusterInstances | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>CVM resource<br>`qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` |
| AddClusterInstancesFromExistedCvm | Cluster resource<br>`qcs::ccs:region:account:cluster/*`<br>`qcs::ccs:region:account:cluster/$clusterId`<br>CVM resource<br>`qcs::cvm:$region:$account:instance/*`<br>`qcs::cvm:$region:$account:instance/$instanceId` |



