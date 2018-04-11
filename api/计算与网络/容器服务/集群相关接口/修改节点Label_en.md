## 1. API Description
This API (ModifyClusterNodeLabel) is used to modify node Label. Set the node affinity scheduling by creating/updating the parameter `nodeAffinity` of the service.
Domain name for API request: `ccs.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. For additional parameters, please see [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| clusterId | Cluster ID, which needs to be entered the field `clusterId` returned via the API [Query Cluster List](/doc/api/457/9448) | String | Yes |
| instanceId | Node ID | String | Yes |
| labels | The Label needs to be placed on the node | Object Array | Yes |

`labels` is described as follows:

| Field | Description | Type | Required |  
|---------|---------|---------|---------|
| key | The key of the Label | String | Yes | 
| value | The value of the Label | String | No |

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input
```
  https://domain/v2/index.php?Action=ModifyClusterNodeLabel
  ------------Basic Parameters----------
  &clusterId=cls-xxxxx
  &instanceId=ins-xxx
  ------------Labels------------
  &labels.0.key=foo
  &labels.0.value=bar
  &labels.1.key=foo2
  &labels.1.value=bar2
 
  &Other Common Parameters
```
Output
```
  {
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```

