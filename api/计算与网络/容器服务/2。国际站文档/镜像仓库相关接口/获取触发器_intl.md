## 1. API Description
This API (ListTrigger) is used to obtain a trigger.
Domain name for API request: `ccr.api.qcloud.com`.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/doc/api/457/9463).

| Parameter Name | Description | Type | Required | 
|---------|---------|---------|---------
| triggerName | Specify this parameter to obtain details of a trigger. You can perform an exact match search. | String | No |
| offset | Data offset. Default is 0 | Int | No |
| limit | Number of returned data entries. Default is 20 | Int | No |
| reponame | This parameter is used to query a trigger that is bound to a specified repository | String | No |

## 3. Output Parameters
 
| Parameter Name | Description | Type | 
|---------|---------|---------|
| code | Common error code. 0: Successful; other values: Failed. | Int | 
| codeDesc | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. | String |
| message | Module error message description depending on API | String |
| totalCount | Number of query results | Int |
| triggerInfo | Trigger information | Object Array |

"triggerInfo" is composed as follows:

| Parameter Name | Description | Type |  
|---------|---------|---------
| triggerName | Name of the trigger to be updated | String | 
| repoName | Name of the repository bound with the trigger | String | 
| invokeSource | Cause of trigger. The value is always set to "IMAGE_PUSH", which means the trigger is initiated by image push | String | 
| invokeAction | Trigger action. The value is always set to "SERVICE_UPDATE", which means to update the service | String |
| createTime | Time when the trigger is created | String |
| updateTime | Time when the trigger is updated | String |
| invokeCondition | Triggering condition | Object |
| invokePara | Trigger parameter | Object |

"invokeCondition" is composed as follows:

| Parameter Name | Description | Type |  
|---------|---------|---------
| invokeMethod | Trigger method.<br>all: All<br>taglist: Specified tag<br>regex: Regular expression | String | No |
| invokeExpr | The expression of the trigger method<br>If invokeMethod is "all", this parameter is empty<br>If invodeMethod is "taglist", this parameter is tag list. Multiple values are separated with ";", e.g.: v1;v2;v3<br>If invokeMethod is "regex", this parameter is regular expression, such as ^test* | String | No |

"invokePara" is composed as follows:

| Parameter Name | Description | Type |  
|---------|---------|---------
| serviceName | The service name of updated service parameter | String | No |
| clusterId | The cluster ID of updated service parameter | String | No |
| namespace | The namespace of updated service parameter | String | No |
| containerName | The container name of updated service parameter | String | No |
| clusterRegion | The cluster region of updated service parameter<br>Regions are numbered as follows:<br>1: Guangzhou<br>4: Shanghai<br>5: Hang Kong<br>7: Shanghai Finance<br>8: Beijing<br>9: Singapore<br>16: Chengdu | Int | No |

## 4. Example
Input

```
  https://domain/v2/index.php?Action=ListTrigger
  &triggerName=trigger_test
  &offset=0
  &limit=20
  &reponame=test/kube_test
  &other common parameters
```
Output

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "triggerInfo": [
            {
                "triggerName": "trigger_test",
                "invokeSource": "IMAGE_PUSH",
                "invokeAction": "SERVICE_UPDATE",
                "repoName": "test/kube_test",
                "createTime": "2018-03-07 14:30:43",
                "updateTime": "2018-03-08 15:30:43",
                "invokeCondition": {
                    "invokeMethod": "all",
                    "invokeExpr": ""
                },
                "invokePara": {
                    "appId": "1254666666",
                    "clusterId": "cls-xxxxxxxx",
                    "namespace": "default",
                    "serviceName": "nginx-test",
                    "containerName": "nginx-test",
                    "clusterRegion": 1
                }
            }
        ]
    }
}

```

