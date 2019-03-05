## 1. API Description
 
This API (UpdateInstanceBandwidthHour) is used to adjust the public network bandwidth of postpaid instances.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* The adjustment takes effect immediately. Both upgrade and downgrade are supported.
* This API only applies to postpaid instances. For prepaid instances, please use [UpdateInstanceBandwidth](https://cloud.tencent.com/doc/api/229/1251) API.
* The minimum bandwidth can be 0Mpbs. The maximum bandwidth is 100Mbps for postpaid instances, 200Mbps for charge-by-fixed-bandwidth instances, and 1000Mbps for the instances on dedicated hosts.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| bandwidth | Yes | Int | Bandwidth value (Mpbs); It is peak bandwidth for postpaid instances.

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81). |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81). |
 

## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=UpdateInstanceBandwidthHour
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &bandwidth=8
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```

{
    "code": 0,
    "message": "ok"
}
```





