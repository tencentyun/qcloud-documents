## API Description
 
This API (ModifyClusterAsgRange) is used to modify the maximum size, minimum size and label of a cluster scaling group. The label is modified by resetting it.

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
| minSize | The minimum size of a scaling group | No | Int |
| maxSize | The maximum size of a scaling group, which itself is limited for auto scaling. For more information, please see AS documentation. | No | Int |
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
  https://domain/v2/index.php?Action=ModifyClusterAsgRange
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupId=asg-xxxxxxxx
  &maxSize=10
  &other common parameters
```
### Output

```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 4411
    }
}

```

