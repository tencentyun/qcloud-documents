## Deleting Cluster Node

## 1. API Description
 
This API (DeleteClusterInstances) is used to delete cluster nodes.

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>

* <font style="color:red">This API can be called only when "status" of cluster is "Running", "Isolated" or "Abnormal".</font>
* If the capacity of remaining nodes is sufficient for the CUP and memory required for the container configuration, the deleted cluster node will automatically dispatch the container on the current node to another node that meets the condition.
* When the cluster is deleted, CVMs with Prepaid mode can only be removed, not returned.


## 2. Input Parameters


The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://www.qcloud.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the clusterId in the returned fields of the API "Query Clusters".  |
| instanceIds.n | Yes |String | ID of CVM to be deleted |
| nodeDeleteMode | No | String| The method to delete cluster nodes, which is mainly used for CVMs with Postpaid mode. CVMs with Prepaid mode can only be removed. <br>RemoveOnly (Only remove)<br>Return (return). <br>By default, CVMs with Postpaid mode are terminated, and those with Prepaid mode are removed |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed |
| message | String | Module error message description depending on API|
| requestId | Int | Task ID |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=DeleteClusterInstances
  &clusterId=clus-xxxxx
  &instanceIds.0=ins-xxxx
  &instanceIds.1=ins-xxxx
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
      "data"{
       "requestId":11333
      }
  }

```
