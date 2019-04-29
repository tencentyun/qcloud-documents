## API Description

This API (ModifyClusterAsgLabel) is used to modify the label of a cluster scaling group. Only the key in the label passed is modified, and the original key in the label remains unchanged.

Domain name for API request:
```
ccs.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Description | Required | Type |
|---------|---------|---------|---------|
| clusterId | Cluster ID. Enter the clusterId field returned by the API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448) | Yes | String |  
| autoScalingGroupId | Scaling group ID | Yes | String |
| label | label | No | Array |



## Output Parameters
 
| Parameter Name | Description | Type |
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |



## Example

### Input

```
  https://domain/v2/index.php?Action=ModifyClusterAsgLabel
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupId=asg-xxxxxxxx
  &label.key=val
  &other common parameters
```
### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}

```

