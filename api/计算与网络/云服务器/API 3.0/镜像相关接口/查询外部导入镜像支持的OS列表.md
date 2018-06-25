
## 1. 接口描述

查看可以导入的镜像操作系统信息。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：DescribeImportImageOs |
| Version | 是 | String | 公共参数，本接口取值：2017-03-12 |

## 3. 输出参数



| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ImportImageOsListSupported | Array of String | 支持的导入镜像的操作系统类型 |
| ImportImageOsVersionSupported | Array of String | 支持的导入镜像的操作系统版本 |
| RequestId | String | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码



## 5. 示例

## 示例1 查询导入镜像支持的操作系统配置信息

### 请求参数

```
https://cvm.tencentcloudapi.com/?Action=DescribeImportImageOs
&<公共请求参数>
```
### 返回参数

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


        