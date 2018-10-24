## 1. API Description

This API (UpdateCdnOverseaConfig) is used to update the CDN service configuration of an overseas domain.

Domain name for API request: cdn.api.qcloud.com

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see the [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is UpdateCdnOverseaConfig.

| Parameter Name | Required | Type | Description |
| ------------ | --- | ------ | -------------------- |
| hostId | Yes | Int | Overseas CDN domain ID |
| projectId | No | Int | ID of the project to which the domain belongs |
| serviceType | No | String|Domain content type. There are three modes: "web" means it is static content; "download" means it is downloading content; "media" means it is media streaming content. |
| origin | No | String | Origin server configuration corresponding to the domain |
| fwdHost | No | String | Address for back-to-origin requests |
| refer | No | String | Hotlink protection configuration. For more information, please see the description below |
| cache | No | String | Configuration of caching rules. For more information, please see the description below |
| furlCache | No | String | Filter parameter: "on" means to disable the filter parameter function and enable the full path caching policy; "off" means to enable the filter parameter function and disable the full path caching policy. |
| rspHeader | No | String | Custom response header |
| middle | No | String | "on" or "off", indicating whether the intermediate server is enabled |
| dedicatedLine | No |String | "on" or "off", indicating whether Direct Connect is used |
| https | No |String | Configuration of Https and Http2.0. For more information, please see the description below |

**The configuration of "refer" is as follows:**

`refer` is used to configure the access blacklist or whitelist. The example is as follows:

```json
{"type":2,"list":["*.qq.com","www.test.com"]}
```

- `type` means the type of the list to refer to: "0" means to disable, "1" means blacklist, and "2" means whitelist.
- `list` means the specific list.

**The configuration of cache is as follows:**

`cache` is used to configure the policy for caching resources. The example is as follows:

```json
[{"type":1, "rule":".jpg;.png", "time" : 1, "unit":"s"}]
```

`type` indicates the type of caching. It includes the following four values:

- 0: Indicates that all files are matched. This is the default cache configuration.
- 1: Indicates to match files based on filename extensions.
- 2: Indicates to match folders based on directories.
- 3: Indicates full-path matching.

`rule` indicates the matching rule. It includes four values that correspond to different caching types:

- 0: "all" is entered in a fixed way. This means the matching rule is applicable to all files;
- 1: Indicates the suffix, such as .jps;.js, which are separated with ";".
- 2: Indicates the directory, for example, /www/anc;/a/b, which are separated with ";".
- 3: Indicates the full path, for example, /a/1.html;/b/2.html, which are separated with ";".

`time` indicates the caching time.

`unit` is the caching time unit, including the following four types:

- `d`: in day
- `h`: in hour
- `m`: in minute
- `s`: in second

**The configuration of https is as follows:**

`https` is used to enable or disable the configuration of overseas https. The example is as follows:

```json
https:{"type":1,"cert_id":"83pwaqvc","http2":-1}
```

- `type` indicates the configuration status of https: "0" means to disable https; "1" means to use https as the access method and http as the back-to-origin method; and "2" means to use https as both the access method and the back-to-origin method.
- `cert_id`: To obtain cert_id, you can call the API CertUpload to upload the certificate to Tencent Cloud SSL for hosting, or call the API GetHostCertList to query the Tencent Cloud SSL-hosted https certificate.
- `http2`: "1" means to enable the http2 function, and "-1" means to disable the http2 function.

## 3. Output Parameters

| Parameter | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error message or error code at business side |
| data | Array | Returned result. For more information, please see the description below |

#### `data` Field Description

| Parameter| Type | Description |
| --------------- | ------ | ------------------- |
| app_id | Int | Tencent Cloud service account, [Click to View](http://console.cloud.tencent.com/cloudAccount), corresponding to the UIN |
| host_id | Int | Overseas domain ID |
| project_id | Int | ID of the project to which the domain belongs |
| host | String | Domain name |
| cname | String | The accelerated domain with ".cdn.dnsv1.com" as suffix assigned by CDN |
| host_type | String | Connection method. There are three modes: "cos" means the hosted origin when connecting the domain is COS origin; `cname` means self-owned origin is used when connecting the domain; `ftp` means FTP hosted origin provided by CDN is used when connecting the domain. |
| serviceType | String | Domain content type. There are three modes: `web` means it is static content; `download` means it is downloading content; `media` means it is media streaming content. |
| status | Int | Domain CDN service status code |
| cdn_status | String | Domain CDN service status |
| origin | String | Origin server configuration corresponding to the domain |
| fwd_host | String | Address for back-to-origin requests |
| refer | String | Hotlink protection configuration. For more information, please see the description below |
| cache | String | Configuration of caching rules. For more information, please see the description below |
| furl_cache | String | Filter parameter: `on` means to enable; `off` means to disable |
| rsp_header | String | Custom response header |
| https | Array | Configuration of Https and Http2.0. For more information, please see the description below |
| readonly | Int | Locking status: "0" means not locked, and "1" means locked. |
| deleted | String | "yes" or "no", indicating whether a domain is marked as deleted |
| message | String | Description of domain status |
| create_time | String | Creation time of CDN services |
| update_time | String | Latest update time of CDN services |
| middle_resource | String | "on" or "off", indicating whether the intermediate server is enabled |
| dedicatedLine |String | "on" or "off", indicating whether Direct Connect is used |

#### `cache` Field Description

| Parameter Name | Type | Description |
| ---- | ------ | ---------------------------------------- |
| type | Int    | Type. There are two types: "0" means all files, and "1" means the file type. |
| rule | String | Matching rule, corresponding to the types above |
| time | Int | Cache expiration time (in seconds) |
| unit | String | The unit used to set cache expiration time. There are four types: "d" refers to day, "h" refers to hour, "m" refers to minute, and "s" refers to second. |

#### `refer` Field Description

| Parameter Name | Type | Description |
| ---- | ----- | ---------------------------------------- |
| type | Int | Hotlink protection type. There are three types: "0" means that hotlink protection is not configured; "1" means that the configured list is a blacklist; and "2" means that the configured list is a whitelist. |
| list | Array | Configured hotlink protection list |

### `https` Field Description

| Parameter| Type | Description |
| ---- | ----- | ---------------------------------------- |
| host_id | Int | Overseas domain ID |
| cert_id | String | Configure the ID of the certificate associated with a domain. |
| common_name | String | Information of the domain associated with the certificate |
| source | Int | There are two status values: "0" indicates that the certificate is kept by the user and "1" indicates that the certificate is hosted in the Tencent Cloud SSL. |
| status | String | There are four status values: "progress" means the configuration is in progress; "success" means the configuration is successful; "fail" means the configuration has failed; and "delete" means configuration has been closed. |
| hy | String | There are two back-to-origin request protocols: "http" indicates that back-to-origin requests use the http protocol, and "https" indicates that back-to-origin requests use the https protocol. |
| http2 | Int | "1" means to enable the http2 function, and "-1" indicates to disable the http2 function. |
| message | String | Remarks |
| expire_time | String | Certificate validity period |
| update_time     | String | https configuration update time |

**Note**:

- In case you see fields that not described in this document, please ignore them.

## 4. Example

### 4.1 Example of Input

> hostId: 11111111
> middle: off
> dedicatedLine: off
> https:{"type":1,"cert_id":"8XXXXXXX","http2":-1}

### 4.2 GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=UpdateCdnOverseaConfig
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462434006
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&hostId=11111111
&middle=off
&dedicatedLine=off
&https={"type":1,"cert_id":"8XXXXXXX","http2":-1}
```

### 4.3 POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'UpdateCdnOverseaConfig',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'hostId' => '11111111',
  'middle' => 'off',
  'dedicatedLine' => 'off',
)
```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "host_id": 11111111,
            "app_id": 12345678,
            "project_id": 0,
            "host": "www.test.com",
            "cname": "www.test.com.cdn.dnsv1.com",
            "host_type": "cname",
            "service_type": "download",
            "status": 4,
            "cdn_status": "offline",
            "origin": "8.8.8.8",
            "fwd_host": "www.test.com",
            "refer": {
                "type": 2,
                "list": [
                    "1.1.1.1"
                ],
            },
            "cache": [
                {
                    "type": 0,
                    "rule": "all",
                    "time": 2592000,
                    "unit": "d"
                },
                {
                    "type": "1",
                    "rule": ".jpg;.png;.css;.js",
                    "time": 86400,
                    "unit": "d"
                }
            ],
            "furl_cache": "off",
            "rsp_header": [],
            "https": {
                "type": 0
            },
            "readonly": 0,
            "deleted": "no",
            "message": "Deploying",
            "create_time": "2017-08-08 11:27:59",
            "update_time": "2017-08-08 12:19:11",
            "middle_resource": "off",
            "dedicated_line": "off"
        },
            "https": {
                "host_id": 11111111,
                "cert_id": "8XXXXXXX",
                "common_name": "www.test.com",
                "source": 0,
                "status": "success",
                "hy": "http",
                "http2": -1,
                "message": "www.test.com",
                "expire_time": "2018-01-18 07:59:59",
                "update_time": "2017-11-15 17:10:43",
                "type": 1
           }
    ]
}
```
