## 1. Cluster Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Cluster List | [DescribeCluster](https://www.qcloud.com/document/api/457/9448) | Query cluster list
| Create Cluster | [CreateCluster](https://www.qcloud.com/document/api/457/9444) | Create cluster
| Delete Cluster | [DeleteCluster](https://www.qcloud.com/document/api/457/9445) | Delete cluster
| Query Cluster Node List | [DescribeClusterInstances](https://www.qcloud.com/document/api/457/9449) |  Query cluster nodes and return information of the nodes in the cluster
| Add Cluster Node | [AddClusterInstances](https://www.qcloud.com/document/api/457/9447) |  Add nodes for cluster
| Delete Cluster Node | [DeleteClusterInstances](https://www.qcloud.com/document/api/457/9446) |  Delete nodes in the cluster
| Add Existing CVM to Cluster | [AddClusterInstancesFromExistedCvm](https://www.qcloud.com/document/api/457/9450) | Add existing CVMs to cluster


## 2. Service Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Service List | [DescribeClusterService](https://www.qcloud.com/document/api/457/9440) | Query service list. Lists returned from this API only include general information of the services
| Query Service Details | [DescribeClusterServiceInfo](https://www.qcloud.com/document/api/457/9441) | Query detailed information of a single service
| Create Service | [CreateClusterService](https://www.qcloud.com/document/api/457/9436) |  Create service
| Modify Service | [ModifyClusterService](https://www.qcloud.com/document/api/457/9434) |  Update service
| Delete Service | [DeleteClusterService](https://www.qcloud.com/document/api/457/9437) | Delete service
| Modify Service Description | [ModifyServiceDescription](https://www.qcloud.com/document/api/457/9435) |  Modify service description
| Acquire Service Event List | [DescribeServiceEvent](https://www.qcloud.com/document/api/457/9443) | Query list of events occurred for the service within the last hour
| Resume Service Update | [ResumeClusterService](https://www.qcloud.com/document/api/457/9442) | Resume paused service update operation
| Pause Service Update | [PauseClusterService](https://www.qcloud.com/document/api/457/9439) | Pause service update operation
| Rollback Service | [RollBackClusterService](https://www.qcloud.com/document/api/457/9438) | Restore the service back to the configuration prior to update (to the previous configuration only)



## 3. Service Pod Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Service Pod List | [DescribeServiceInstance](https://www.qcloud.com/document/api/457/9433)|  Query the list of service pods
| Modify Service Pod Replica Number | [ModifyServiceReplicas](https://www.qcloud.com/document/api/457/9431) | Modify the number of containers for the service
| Delete Service Pod | [DeleteInstances](https://www.qcloud.com/document/api/457/9432) | Delete pods

## 4. Namespace Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query Cluster Namespace | [DescribeClusterNameSpaces](https://www.qcloud.com/document/api/457/9430) | Query cluster namespaces
| Create Cluster Namespace | [CreateClusterNamespace](https://www.qcloud.com/document/api/457/9428) |  Create namespaces
| Delete Cluster Namespace | [DeleteClusterNamespace](https://www.qcloud.com/document/api/457/9429) | Delete namespaces


