## 1. API Description
This API (AddUpdateServiceTrigger) is used to add a trigger.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| triggerName | Trigger name | String | Yes |
| reponame | Name of the repository bound with the trigger | String | Yes |
| invokeMethod | Trigger method | String | Yes |
| invokeExpr | The expression of the trigger method | String | No |
| serviceName | Service name | String | Yes |
| clusterId | Cluster ID | String | Yes |
| namespace | Namespace | String | Yes |
| containerName | Container name | String | Yes |
| clusterRegion | Region of the cluster | Int | Yes |

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=AddUpdateServiceTrigger
  &triggerName=trigger_test
  &reponame=test/kube_test
  &invokeMethod=taglist
  &invokeExpr=v1;v2
  &serviceName=nginx-test
  &clusterId=cls-xxxxxx
  &namespace=default
  &containerName=nginx-test
  &clusterRegion=1
  &other common parameters
```
Output

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```

