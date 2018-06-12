
## API Description

This API (CreateClusterAsg) is used to create a cluster scaling group.

Domain name for API request:
```
ccs.api.qcloud.com
```

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/product/457/9463).

| Parameter Name | Description | Required | Type |
| ----------------------- | ------------------------------------------------------------ | ---- | ------ |
| clusterId | Cluster ID. Enter the clusterId field returned by the API [Query Cluster List](https://cloud.tencent.com/document/product/457/9448) | Yes | String |
| instanceId | Reference CVM, which must be a node in the cluster. Enter the instanceId field returned by the API [Query Cluster Node List](https://cloud.tencent.com/document/product/457/9449). The launch configuration for scale-up is generated based on this node's configuration (including vCPU, memory, model, VPC, subnet, system disk, type and size of data disk, bandwidth, billing method of bandwidth, whether to assign public IP, etc.). | Yes | String |
| minSize | The minimum size of a scaling group | Yes | Int |
| maxSize | The maximum size of a scaling group, which itself is limited for auto scaling. For more information, please see AS documentation. | Yes | Int |
| password | Node password. It is generated randomly if not set, and sent via internal message. It must be a combination of 8-16 characters comprised of at least two of the following types: uppercase/lowercase letters (a-z, A-Z), numbers (0-9), and special characters (**( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' < > , . ? /**). | No | String |
| keyId | Key ID. You can use the key to log in to the node after it is associated. The keyId can be obtained through the API [Query key](https://cloud.tencent.com/document/api/213/1946). Key and password cannot both be specified. | No | String |
| label | label | No | Array |
| autoScalingGroupName | Scaling group name, which must be unique and is automatically generated if not specified. | No | String |
| launchConfigurationName | Launch configuration name, which must be unique and is automatically generated if not specified. | No | String |

## Output Parameters
| Parameter Name | Description | Type |
| -------- | ------------------------------------------------------------ | ------ |
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## Example
### Input
```
  https://domain/v2/index.php?Action=CreateClusterAsg
  &clusterId=cls-xxxxxxxx
  &instanceId=ins-xxxxxxxx
  &password=yourpass
  &minSize=0
  &maxSize=10
  &label.yourkey=yourval
  &autoScalingGroupName=yourasgname
  &launchConfigurationName=yourlcname
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

