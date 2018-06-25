## 1. API Description
This API (ModifyUpdateServiceTrigger) is used to modify service update trigger.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| triggerName | Name of the trigger to be updated | String | Yes |
| reponame | Name of the repository bound with the trigger | String | No |
| newTriggerName | Name of the new trigger | String | No |
| invokeMethod | Trigger method.<br>all: All<br>taglist: Specified tag<br>regex: Regular expression | String | No |
| invokeExpr | The expression of the trigger method<br>If `invokeMethod` is `all`, this parameter is empty<br>If `invodeMethod` is `taglist`, this parameter is tag list. Multiple values are separated with ";", e.g.: v1;v2;v3<br>If `invokeMethod` is `regex`, this parameter is regular expression, such as ^test* | String | No |
| serviceName | The service name of updated service parameter | String | No |
| clusterId | The cluster ID of updated service parameter | String | No |
| namespace | The namespace of updated service parameter | String | No |
| containerName | The container name of updated service parameter | String | No |
| clusterRegion | The cluster region of updated service parameter<br>Regions are numbered as follows:<br>1: Guangzhou<br>4: Shanghai<br>5: Hong Kong<br>7: Shanghai Finance<br>8: Beijing<br>9: Singapore<br>16: Chengdu | Int | No |

## 3. Output Parameters
 
| Parameter Name | Description | Type |
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int |
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=ModifyUpdateServiceTrigger
  &triggerName=trigger_test
  &reponame=test/kube_test
  &newTriggerName=trigger_test_new
  &invokeMethod=taglist
  &invokeExpr=v1;v2
  &serviceName=nginx-test
  &clusterId=cls-xxxxxxxx
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
