## 1. Cluster Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Cluster List | [DescribeCluster](https://cloud.tencent.com/document/api/457/9448) | Query cluster list
| Create Cluster | [CreateCluster](https://cloud.tencent.com/document/api/457/9444) | Create cluster
| Delete Cluster | [DeleteCluster](https://cloud.tencent.com/document/api/457/9445) | Delete cluster
| Query Cluster Node List | [DescribeClusterInstances](https://cloud.tencent.com/document/api/457/9449) |  Query cluster nodes and return information of the nodes in the cluster
| Add Cluster Node | [AddClusterInstances](https://cloud.tencent.com/document/api/457/9447) |  Add nodes for cluster
| Delete Cluster Node | [DeleteClusterInstances](https://cloud.tencent.com/document/api/457/9446) |  Delete nodes in the cluster
| Add Existing CVM to Cluster | [AddClusterInstancesFromExistedCvm](https://cloud.tencent.com/document/api/457/9450) | Add existing CVMs to cluster


## 2. Service Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Service List | [DescribeClusterService](https://cloud.tencent.com/document/api/457/9440) | Query service list. Lists returned from this API only include general information of the services
| Query Service Details | [DescribeClusterServiceInfo](https://cloud.tencent.com/document/api/457/9441) | Query detailed information of a single service
| Create Service | [CreateClusterService](https://cloud.tencent.com/document/api/457/9436) |  Create service
| Modify Service | [ModifyClusterService](https://cloud.tencent.com/document/api/457/9434) |  Update service
| Delete Service | [DeleteClusterService](https://cloud.tencent.com/document/api/457/9437) | Delete service
| Modify Service Description | [ModifyServiceDescription](https://cloud.tencent.com/document/api/457/9435) |  Modify service description
| Acquire Service Event List | [DescribeServiceEvent](https://cloud.tencent.com/document/api/457/9443) | Query list of events occurred for the service within the last hour
| Resume Service Update | [ResumeClusterService](https://cloud.tencent.com/document/api/457/9442) | Resume paused service update operation
| Pause Service Update | [PauseClusterService](https://cloud.tencent.com/document/api/457/9439) | Pause service update operation
| Rollback Service | [RollBackClusterService](https://cloud.tencent.com/document/api/457/9438) | Restore the service back to the configuration prior to update (to the previous configuration only)



## 3. Pod Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Pod List | [DescribeServiceInstance](https://cloud.tencent.com/document/api/457/9433)|  Query the list of service pods
| Modify Pod Number | [ModifyServiceReplicas](https://cloud.tencent.com/document/api/457/9431) | Modify the number of containers for the service
| Delete Pod | [DeleteInstances](https://cloud.tencent.com/document/api/457/9432) | Delete pods

## 4. Namespace Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Cluster Namespace | [DescribeClusterNameSpaces](https://cloud.tencent.com/document/api/457/9430) | Query cluster namespaces
| Create Cluster Namespace | [CreateClusterNamespace](https://cloud.tencent.com/document/api/457/9428) |  Create namespaces
| Delete Cluster Namespace | [DeleteClusterNamespace](https://cloud.tencent.com/document/api/457/9429) | Delete namespaces


