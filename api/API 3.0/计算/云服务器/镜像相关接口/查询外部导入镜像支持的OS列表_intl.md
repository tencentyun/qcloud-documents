## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeImportImageOs) is used to view the operating system information of an imported image.

A maximum of 288 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeImportImageOs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| ImportImageOsListSupported | [ImageOsList](/document/api/213/##ImageOsList) | Supported operating system types of imported images. |
| ImportImageOsVersionSet | Array of [OsVersion](/document/api/213/##OsVersion) | Supported operating system versions of imported images. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Query the configuration information of the operating system supported by an imported image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeImportImageOs
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "ImportImageOsListSupported": {
      "Linux": [
        "CentOS",
        "Ubuntu",
        "Debian",
        "OpenSUSE",
        "SUSE",
        "CoreOS",
        "FreeBSD",
        "Other Linux"
      ],
      "Windows": [
        "Windows Server 2008",
        "Windows Server 2012",
        "Windows Server 2016"
      ]
    },
    "ImportImageOsVersionSet": [
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Windows Server 2008",
        "OsVersions": [
          "-"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Windows Server 2012",
        "OsVersions": [
          "-"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Windows Server 2016",
        "OsVersions": [
          "-"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "CentOS",
        "OsVersions": [
          "5",
          "6",
          "7"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "CoreOS",
        "OsVersions": [
          "7"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Debian",
        "OsVersions": [
          "6",
          "7",
          "8",
          "9"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "FreeBSD",
        "OsVersions": [
          "10"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Redhat",
        "OsVersions": [
          "5",
          "6",
          "7"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "OpenSUSE",
        "OsVersions": [
          "11",
          "12"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "SUSE",
        "OsVersions": [
          "10",
          "11",
          "12",
          "13"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Ubuntu",
        "OsVersions": [
          "10",
          "12",
          "14",
          "16"
        ]
      },
      {
        "Architecture": [
          "x86_64",
          "i386"
        ],
        "OsName": "Other Linux",
        "OsVersions": [
          "-"
        ]
      }
    ],
    "RequestId": "32064a8f-8d3f-4670-8d4f-60123ca97042"
  }
}
```


