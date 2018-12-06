## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (DescribeContainerLog) is used to get log information about a container instance.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeContainerLog |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceName | Yes | String | Container instance name |
| ContainerName | No | String | Container name |
| Tail | No | Integer | Number of lines from the bottom of the log to be displayed |
| SinceTime | No | String | Start time of logging |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| ContainerLogList | Array of [ContainerLog](/document/api/858/17776#ContainerLog) | Array of container logs |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting. |

## 4. Error Codes

The following only lists the error codes related to the API logic. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Get log information of the container instance "sshdlog"

#### Input example

```
https://cis.tencentcloudapi.com/?Action=DescribeContainerLog
&InstanceName=sshdlog
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "ContainerLogList": [
      {
        "Log": "2018-05-18 06:34:04,123 CRIT Supervisor is running as root.  Privileges were not dropped because no user is specified in the config file.  If you intend to run as root, you can set user=root in the config file to avoid this message.",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:04"
      },
      {
        "Log": "2018-05-18 06:34:04,123 WARN No file matches via include \"/etc/supervisord.d/*.ini\"",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:04"
      },
      {
        "Log": "2018-05-18 06:34:04,123 INFO Included extra file \"/etc/supervisord.d/sshd-bootstrap.conf\" during parsing",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:04"
      },
      {
        "Log": "2018-05-18 06:34:04,123 INFO Included extra file \"/etc/supervisord.d/sshd-wrapper.conf\" during parsing",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:04"
      },
      {
        "Log": "2018-05-18 06:34:04,126 INFO supervisord started with pid 1",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:04"
      },
      {
        "Log": "2018-05-18 06:34:05,129 INFO spawned: 'supervisor_stdout' with pid 7",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "2018-05-18 06:34:05,131 INFO spawned: 'sshd-bootstrap' with pid 8",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "2018-05-18 06:34:05,205 INFO spawned: 'sshd-wrapper' with pid 9",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "2018-05-18 06:34:05,605 INFO success: supervisor_stdout entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "2018-05-18 06:34:05,605 INFO success: sshd-bootstrap entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "2018-05-18 06:34:05,605 INFO success: sshd-wrapper entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:05"
      },
      {
        "Log": "sshd-bootstrap stdout | Initialising SSH.",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "sshd-bootstrap stdout | ",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "================================================================================",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "SSH Details",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "--------------------------------------------------------------------------------",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "user : app-admin",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "password : n1KI5zLucvzr8hqY",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "id : 500:500",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "home : /home/app-admin",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "chroot path : N/A",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "shell : /bin/bash",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "sudo : ALL=(ALL) ALL",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "key fingerprints :",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "dd:3b:b8:2e:85:04:06:e9:ab:ff:a8:0a:c0:04:6e:d6 (insecure key)",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "rsa host key fingerprint :",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "37:aa:b8:20:2f:b1:05:59:5d:af:aa:1b:28:d6:fc:ad",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "--------------------------------------------------------------------------------",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "3.21979",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      },
      {
        "Log": "2018-05-18 06:34:08,617 INFO exited: sshd-bootstrap (exit status 0; expected)",
        "Name": "sshd",
        "Time": "2018-05-18 14:34:08"
      }
    ],
    "RequestId": "44156dc9-c6b5-4f58-b11f-7aeec0beac76"
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

