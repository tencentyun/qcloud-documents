
## 1. API Description

This API (DescribeImportImageOs) is used to view the operating system information of an imported image.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeImportImageOs |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| ImportImageOsListSupported | Array of String | Supported operating system types of imported images |
| ImportImageOsVersionSupported | Array of String | Supported operating system versions of imported images |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



## 5. Example

## Example 1: Query the configuration information of the operating system supported by an imported image

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeImportImageOs
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "ImportImageOsListSupported": {
      "linux": [
        "CentOS",
        "Redhat",
        "Ubuntu",
        "Debian",
        "OpenSUSE",
        "SUSE",
        "CoreOS",
        "FreeBSD"
      ],
      "windows": [
        "Windows Server 2008",
        "Windows Server 2012"
      ]
    },
    "ImportImageOsVersionSupported": {
      "CentOS": "centos",
      "CoreOS": "coreos",
      "Debian": "debian",
      "FreeBSD": "freebsd",
      "OpenSUSE": "sles",
      "SUSE": "suse",
      "Ubuntu": "ubuntu",
      "Windows Server 2008": "windows2008",
      "Windows Server 2012": "windows2012",
      "Windows Server 2016": "windows2016"
    },
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
  }
}
```


        
