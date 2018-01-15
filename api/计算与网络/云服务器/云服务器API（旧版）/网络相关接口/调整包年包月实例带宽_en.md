## 1. API Description

This API (UpdateInstanceBandwidth) is used to adjust the public network bandwidth of instances with an annual or monthly plan.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* This API only applies to [prepaid instances](https://cloud.tencent.com/doc/product/213/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AE%A1%E7%90%86%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98#1.-.E4.BB.80.E4.B9.88.E6.98.AF.E5.B8.A6.E5.AE.BD.E5.8C.85.E6.A8.A1.E5.BC.8F.EF.BC.9F).  * For postpaid instances, please use [UpdateInstanceBandwidthHour](https://cloud.tencent.com/doc/api/229/1345) API.
* Bandwidth can only be upgraded but not degraded.
* The maximum bandwidth is 100Mbps for pay-per-use instances, 200Mbps for charge-by-fixed-bandwidth instances, and 1000Mbps for the instances on dedicated hosts.
* <font style="color:red">Only charge-by-fixed-bandwidth model is supported.</font>

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| bandwidth | Yes | Int | The upgraded bandwidth (Mbps). The upgraded bandwidth should not be less than the current bandwidth. For users with bandwidth package, it can be adjusted to 65535 and can be increased or decreased within the range of 0-65535.
| startTime | Yes | String | Start date. It should take the format such as 2016-10-30. It should not be earlier than the current time. If it is today, the upgrade takes effect immediately.
| endTime | Yes | String | End date. It should take the format such as 2017-11-30. The validity period of modified bandwidth includes the date, which should not be later than the expiration date of the instance. The expiration date of the instance can be queried using [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81). |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81). |
| dealIds | Array | The generated order number, which is used to query the information on execution.


## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=UpdateInstanceBandwidth
  &instanceId=qcvm12345
  &bandwidth=2
  &startTime=2014-07-20
  &endTime=2014-08-20
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

 * Note: dealIds does not apply to postpaid instances.

```

  {
      "code" : 0,
      "message" : "ok",
      "dealIds":[
          12194872988
      ]
  }

```





