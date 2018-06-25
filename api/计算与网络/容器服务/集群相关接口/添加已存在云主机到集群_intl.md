## 1. API Description
 
This API (AddClusterInstancesFromExistedCvm) is used to add existing CVMs to a cluster.

Domain for API request: ccs.api.qcloud.com

* This API can be called only when "status" of cluster is "Running".
* This API can be called only when the status of current CVM is "Normal" or "Shut down". For more information, please see the list of instance statuses in [DescribeInstances](https://cloud.tencent.com/document/api/213/831) API.
* The current CVM will be reinstalled, and the system is the same as the one specified when the cluster is created. Please ensure that there is no important file in the system disk.
* The added CVMs and the current cluster must locate in the same VPC.
* The added CVMs must belong to the default project.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterId   | Yes    | String | Cluster ID. You can obtain this ID from the *clusterId* returned by the [*DescribeCluster*](https://cloud.tencent.com/document/api/457/9448) API.  |
| instanceIds | Yes | String | Enter the unInstanceId (instance ID) field returned via [DescribeInstances](https://cloud.tencent.com/document/api/213/831) API . |
| password | No | String | Instance password. It will be generated randomly if not set, and be sent via internal message. Linux instance's password should be a combination of 8-16 characters comprised of at least two of the following types: letters [a-z, A-Z], numbers [0-9], and special characters [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' < > , . ? / ]. Windows instance's password should be a combination of 12-16 characters comprised of at least three of the following types: lowercase letters [a-z], uppercase letters [A-Z], numbers [0-9] and special characters [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. |
| keyId | No | String | [Key](https://intl.cloud.tencent.com/document/product/213/6092) ID. You can use the key to log in to the instance after the key is associated. "keyId" can be obtained through [DescribeKeyPairs](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AF%86%E9%92%A5) API. Key and password cannot both be specified, and specifying key is not supported by Windows operating systems. |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| succInstanceIds | Obj Array | List of CVMs added to the cluster successfully |
| faliInstanceIds | Obj Array | List of CVMs failed to be added to the cluster |

Details of "faliInstanceIds" field

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | Instance ID |
| message | String | Reason for failure |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=AddClusterInstancesFromExistedCvm&clusterId=clus-xxxxx&instanceIds.0=ins-xxxxxx&instanceIds.1=ins-xxxxxx
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
      "data"{
       "succInstanceIds":["ins-xxxxxx","ins-xxxxxx"],
      }
  }

```
