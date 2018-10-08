## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (DescribeContainerInstanceEvents) is used to query the event list for a container instance.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeContainerInstanceEvents |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceName | Yes | String | Container instance name |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| EventList | Array of [Event](/document/api/858/17776#Event) | Event list of a container instance |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting. |

## 4. Error Codes

The following only lists the error codes related to this API. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Query the event list for the container instance "sshdlog"

#### Input example

```
https://cis.tencentcloudapi.com/?Action=DescribeContainerInstanceEvent
&InstanceName=sshdlog
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "EventList": [
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:34:03.000+08:00",
        "LastSeen": "2018-05-18T14:34:03.000+08:00",
        "Level": "Normal",
        "Message": "Created container",
        "Reason": "Created"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:34:03.000+08:00",
        "LastSeen": "2018-05-18T14:34:03.000+08:00",
        "Level": "Normal",
        "Message": "Successfully pulled image \"jdeathe/centos-ssh:centos-7\"",
        "Reason": "Pulled"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:34:03.000+08:00",
        "LastSeen": "2018-05-18T14:34:03.000+08:00",
        "Level": "Normal",
        "Message": "Started container",
        "Reason": "Started"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:33:51.000+08:00",
        "LastSeen": "2018-05-18T14:33:51.000+08:00",
        "Level": "Normal",
        "Message": "pulling image \"jdeathe/centos-ssh:centos-7\"",
        "Reason": "Pulling"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:33:40.000+08:00",
        "LastSeen": "2018-05-18T14:33:40.000+08:00",
        "Level": "Normal",
        "Message": "MountVolume.SetUp succeeded for volume \"default-token-mqfh6\" ",
        "Reason": "SuccessfulMountVolume"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:33:40.000+08:00",
        "LastSeen": "2018-05-18T14:33:40.000+08:00",
        "Level": "Warning",
        "Message": "No nodes are available that match all of the predicates: Insufficient memory (12), MatchInterPodAffinity (27).",
        "Reason": "FailedScheduling"
      },
      {
        "Count": "1",
        "FirstSeen": "2018-05-18T14:33:40.000+08:00",
        "LastSeen": "2018-05-18T14:33:40.000+08:00",
        "Level": "Normal",
        "Message": "Successfully assigned sshdlog-1a082ocw-cisapp to 10.0.20.45",
        "Reason": "Scheduled"
      }
    ],
    "RequestId": "d9b28ae4-5343-43c2-a6c1-48b716abde67"
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

