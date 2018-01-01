## 1. API Description

This API (GetInstanceAttributes) is used to obtain the attributes of a CKafka instance under the user account.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | Instance ID |

## 3. Output Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| instanceId | String | Instance ID |
| instanceName | String | Instance name |
| vip | String | vip accessing the instance |
| vport | Int | vport accessing the instance |
| status | Int | Status of instance. 0: Creating; 1: Running; 2: Deleting. |
| bandwith | Int | Instance bandwidth (in Mbps) |
| diskSize | Int | Storage size of instance (in GB) |
| vpcId | String | Being left empty means it is a basic network |
| subnetId | String |   |
| zoneId | Int | Availability zone |
| maxRetentionTime | Int | The maximum retention time of instance log (in minute) |
| createTime | Int | Creation time, expressed as timestamp (in second) |

## 4. Example

Input:

```
 https://domain/v2/index.php?Action=GetInstanceAttributes&instanceId=ckafka-xxxxxx&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
      "message" : "ok",
		"codeDesc":"Success",
        "instanceId":"ckafka-xxooa0",
		"instanceName":"test",
		"vip":"10.2.3.2",
		"vport":9020,
		"zoneId":9020,
		"vpcId":"",
		"subnetId":"",
		"status":0,
		"bandwith":100,
		"diskSize":100,
		"maxRetentionTime":1000
  }
```







