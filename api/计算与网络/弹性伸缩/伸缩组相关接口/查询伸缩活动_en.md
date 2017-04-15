## 1. API Description

This API (DescribeScalingActivity) is used to query scaling activities
Domain name: scaling.api.qcloud.com


## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | |
| scalingActivityIds.n (scalingActivityIds is an array, whose elements need to be entered as input parameters) | No | String | |
| offset | No | Int | |
| limit | No | Int | |
| startTime | No | datetime | |
| endTime | No | datetime | |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed |
| message | String | Error message |
| data | Array | Description (to be added) |
| data.scalingActivitySet | Array | Description (to be appended) | 
| data.scalingActivitySet.status | Int | Description (to be appended) | 
| data.scalingActivitySet.code | Int | Description (to be appended) | 
| data.scalingActivitySet.autoScalingGroupId | String | Description (to be appended) | 
| data.scalingActivitySet.cause | String | Description (to be appended) | 
| data.scalingActivitySet.hostIndex | Int | Description (to be appended) | 
| data.scalingActivitySet.desciption | String | Description (to be appended) | 
| data.scalingActivitySet.detail | String | Description (to be appended) | 
| data.scalingActivitySet.startTime | String | Description (to be appended) | 
| data.scalingActivitySet.hostIp | String | Description (to be appended) | 
| data.scalingActivitySet.msg | String | Description (to be appended) | 
| data.scalingActivitySet.scalingPolicyId | String | Description (to be appended) | 
| data.scalingActivitySet.scalingActivityId | String | Description (to be appended) | 
| data.scalingActivitySet.endTime | String | Description (to be appended) | 
| data.scalingActivitySet.createTime | String | Description (to be appended) | 
| data.scalingActivitySet.scalingGroupId | String | Description (to be appended) | 


## 4. Example
Input
```
https://scaling.api.qcloud.com/v2/index.php?Action=DescribeScalingActivity
&scalingGroupId=asg-1urw3bm9
&startTime=2016-04-25 17:36:00
&COMMON_PARAMS
```
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "totalCount":"2",
        "scalingActivitySet":[
            {
                "status":"2",
                "code":"0",
                "autoScalingGroupId":"asg-1urw3bm9",
                "cause":"curr instance less than desired capacity",
                "hostIndex":"0",
                "desciption":"scale out 1 instance",
                "detail":"{"vpcId": "vpc-gb6juqdg", "appName": "1251707795", "intSubnetId": 6608, "hostIndex": 0, "desciption": "scale out 1 instance", "defaultProtectedFromScaleIn": 0, "uin": "3321337994", "owner": "1251707795", "maxSize": 10, "num": 1, "warmup": 600, "defaultLifeCycleHookId": "", "subnetId": "subnet-g6syt4ph", "stepNum": 1, "needSecurityAgent": 0, "id": 5, "bManual": 0, "subnet": [{"subnetId": "subnet-g6syt4ph", "intSubnetId": 6608, "zoneId": 200001}], "password": "", "lb": [], "zone": [], "launchConfigurationId": "asc-0ej76sn7", "projectId": 0, "ownerUin": "3321337994", "imageId": "img-0ayoybdd", "zoneId": 200001, "minSize": 2, "autoScalingGroupId": "asg-1urw3bm9", "keyId": "", "needMonitorAgent": 1, "wanIp": 1, "type": 0, "lifeCycleHookId": "", "imageType": 1, "status": 0, "desiredCapacity": 2, "scalingPolicyId": "", "mem": 2, "terminationPolicy": 1, "replaceUnhealthyInstanceScalingPolicyId": "asp-6z6e1c3t", "defaultCooldown": 300, "appCname": "\u817e\u8baf\u4e91", "intImageId": 14210, "hostIp": "0.0.0.0", "scalingActivityId": "asa-hekmoz15", "storageSize": 50, "notificationConfiguration": [], "createTime": "2016-04-25 16:56:58", "bandwidthType": 1, "bEnabledMetrics": 1, "name": "joezou-AS1", "classicLinkVpcId": "", "cause": "curr instance less than desired capacity", "rootSize": 50, "bandwidth": 1, "alarmPolicyGroupId": "677967", "osName": "centos7.1x86_64", "storageType": 2, "hasNum": 1, "launchConfigurationName": "joezou-as1-\u52ff\u5220", "defaultResult": 0, "intVpcId": 389, "sg": [{"sgId": "sg-rmn4vf1c"}], "cpu": 2, "bInScalingActivity": 1}",
                "startTime":"2016-04-25 17:37:42",
                "hostIp":"10.110.120.100",
                "msg":"success",
                "scalingPolicyId":"",
                "scalingActivityId":"asa-hekmoz15",
                "endTime":"2016-04-25 17:49:33",
                "createTime":"2016-04-25 17:37:39",
                "scalingGroupId":"asg-1urw3bm9"
            },
            {
                "status":"2",
                "code":"0",
                "autoScalingGroupId":"asg-1urw3bm9",
                "cause":"curr instance more than desired capacity",
                "hostIndex":"0",
                "desciption":"scale in 1 instance",
                "detail":"{"vpcId": "vpc-gb6juqdg", "appName": "1251707795", "hostIndex": 0, "desciption": "scale in 1 instance", "defaultProtectedFromScaleIn": 0, "uin": "3321337994", "maxSize": 1, "num": 1, "warmup": 600, "defaultLifeCycleHookId": "", "owner": "1251707795", "stepNum": 1, "needSecurityAgent": 0, "id": 5, "bManual": 0, "subnet": [{"status": 1, "subnetId": "subnet-g6syt4ph", "owner": "1251707795", "zoneId": 200001}], "password": "", "lb": [], "zone": [], "launchConfigurationId": "asc-0ej76sn7", "projectId": 0, "ownerUin": "3321337994", "imageId": "img-0ayoybdd", "minSize": 1, "autoScalingGroupId": "asg-1urw3bm9", "keyId": "", "needMonitorAgent": 1, "wanIp": 1, "type": 1, "lifeCycleHookId": "", "imageType": 1, "status": 0, "desiredCapacity": 1, "scalingPolicyId": "", "mem": 2, "terminationPolicy": 1, "replaceUnhealthyInstanceScalingPolicyId": "asp-6z6e1c3t", "defaultCooldown": 300, "appCname": "\u817e\u8baf\u4e91", "bEnabledMetrics": 1, "hostIp": "0.0.0.0", "scalingActivityId": "asa-170ocmmt", "storageSize": 50, "notificationConfiguration": [], "createTime": "2016-04-25 16:56:58", "bandwidthType": 1, "alarmPolicyGroupId": "677967", "name": "joezou-AS1", "classicLinkVpcId": "", "cause": "curr instance more than desired capacity", "bandwidth": 1, "bInScalingActivity": 1, "storageType": 2, "launchConfigurationName": "joezou-as1-\u52ff\u5220", "defaultResult": 0, "rootSize": 50, "sg": [{"sgId": "sg-rmn4vf1c"}], "cpu": 2, "hasNum": 1}",
                "startTime":"2016-04-25 17:36:00",
                "hostIp":"10.110.120.100",
                "msg":"success",
                "scalingPolicyId":"",
                "scalingActivityId":"asa-170ocmmt",
                "endTime":"2016-04-25 17:36:26",
                "createTime":"2016-04-25 17:35:59",
                "scalingGroupId":"asg-1urw3bm9"
            }
        ]
    }
}
```


