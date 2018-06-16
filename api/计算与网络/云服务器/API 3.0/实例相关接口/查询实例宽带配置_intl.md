### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceInternetBandwidthConfigs
&InstanceId=ins-6lafsaz0
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InternetBandwidthConfigSet": [
      {
        "EndTime": "2017-04-12T16:00:00Z",
        "InternetAccessible": {
          "InternetChargeType": "BANDWIDTH_PREPAID",
          "InternetMaxBandwidthOut": 50
        },
        "StartTime": "2017-03-12T16:00:00Z"
      }
    ],
    "RequestId": "314161cd-ee40-4c37-921e-b10c4ed5607c"
  }
}
```


