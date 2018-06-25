## 1. API Description
 
This API (DescribeCluster) is used to query the list of clusters.

Domain for API request: ccs.api.qcloud.com



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| clusterName | No | String| Filter criteria: cluster name |
| status| No | String| Cluster status |
| orderField | No | String| Sorting field. Supported values: clusterId, clusterName, createdAt, updatedAt. Default is createdAt |
| orderType | No | String| Ascending (asc) or descending (desc). Default is desc |
| offset | No | Int | Offset. Default is 0 |
| limit | No | Int| Maximum displayed entries. Default is 20 |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| message | String | Module error message description depending on API|
| totalCount | Int | Number of clusters |
| clusterSet | Array | Cluster information array |

``clusterSet`` contains a lot of instance information, and the data structure for each instance information is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| clusterId |String | Cluster ID |
| clusterName |String | Cluster name |
| description | String | Cluster description |
| clusterCIDR | String | CIDR of cluster container and service IP |
| unVpcId | String | Cluster VPC ID (string) |
| vpcId | Int | Cluster VPC ID (Int) |
| status | string | Cluster status. Details can be found below the parameter list |
| nodeNum | Int | Number of nodes in the cluster |
| nodeStatus | String |Cluster node status. Details can be found below the parameter list |
| totalCpu | Int | Total number of CPU millicores in the cluster |
| totalMem | Int | Total amount of memory in the cluster (in Mi) |
| os | String | Operating system used by the nodes in the cluster |
| createdAt | String | Creation time of cluster |
| updatedAt | Int | Update time of cluster |
| regionId | Int | Region |
| k8sVersion | String | The kubernetes version used in the cluster |
| clusterExternalEndpoint |String | URL for accessing kubernetesAPI, which is used to work with cluster by using kubernetesAPI directly |


Details of ``status``

| Type | Description |
|---------|---------|
| Creating | Creating cluster |
| Running | Running cluster |
| Deleting | Deleting cluster |
| Scaling | Scaling cluster |
| Upgrading | Upgrading cluster |
| Isolated | Isolating cluster due to arrears |
| Abnormal | Cluster exception |

Details of ``nodeStatus``

| Type | Description |
|---------|---------|
| AllNormal | All the cluster nodes are normal |
| AllAbnormal | All the cluster nodes are exceptional |
| PartialAbnormal | Part of the cluster nodes are exceptional |

## 4. Example

Input

```
  https://domain/v2/index.php?Action=DescribeCluster&offset=0&limit=20
```
Output

```
  {
    "code": 0,
    "message": "", 
	"data"{
	    "totalCount": 1,
	    "clusters": [
	        {   
	            "clusterId": "cls-xxxxx",
                "clusterName": "test",
                "description": "",
                "status": "Running",
                "unVpcId": "vpc-xxxx",
                "vpcId": 895,
                "clusterCIDR": "172.21.0.0/16",
                "createdAt": "2017-03-17 15:03:24",
                "updatedAt": "2017-03-24 11:13:01",
                "nodeStatus": "AllNormal",
                "nodeNum": 1,
                "os": "ubuntu16.04.1 LTSx86_64",
                "totalCpu": 1000,
                "totalMem": 1024,
                "regionId": 1,
                "k8sVersion": "",
                "clusterExternalEndpoint": null,
	        }   
	    ]
	}
}

```
