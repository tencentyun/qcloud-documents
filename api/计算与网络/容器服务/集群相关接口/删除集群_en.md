## 1. API Description
 
This API (DeleteCluster) is used to delete cluster.

Domain for API request: ccs.api.qcloud.com

* This API can be called only when *status* of cluster is "Running", "Isolated" or "Abnormal".
* All the services in the cluster will be deleted if the cluster is deleted.
* When the cluster is deleted, CVMs with Prepaid mode can ONLY be removed, not returned.


## 2. Input Parameters
The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| nodeDeleteMode | No | String| The method to delete cluster nodes, which is mainly used for CVMs with Postpaid mode. CVMs with Prepaid mode can only be removed. <br>RemoveOnly (Only remove)<br>Return (return). <br>By default, CVMs with Postpaid mode are terminated, and those with Prepaid mode are removed |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| requestId | Int | Task ID |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=DeleteCluster&clusterId=clus-xxxxx
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
