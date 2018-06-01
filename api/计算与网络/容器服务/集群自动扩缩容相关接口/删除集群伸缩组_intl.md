## API Description
 
This API (DeleteClusterAsg) is used to delete a cluster scaling group. Deleting a scaling group will terminate the CVMs in the scaling group. Please proceed with caution.

Domain name for API request:
```
ccs.api.qcloud.com
```
## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Description | Required | Type |
|---------|---------|---------|---------|
| clusterId | Cluster ID. Enter the clusterId field returned by the API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448) | Yes | String |
| autoScalingGroupIds | Scaling group ID list | Yes | Array |



## Output Parameters
 
| Parameter Name | Description | Type |
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |



## Example

### Input

```
  https://domain/v2/index.php?Action=DeleteClusterAsg
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupIds.0=asg-xxxxxxxx
  &other common parameters
```
### Output

```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
    }
}

```

