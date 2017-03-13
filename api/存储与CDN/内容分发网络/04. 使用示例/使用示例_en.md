To help you quickly use the Content Delivery Network (CDN) API, we will give you an example.
To use the Content Delivery Network, you need to add an accelerated domain to the CDN first. The domain must meet the following conditions:

+ It has not been added to Tencent Cloud CDN;
+ It has been filed with MIIT for the record.



## Add Accelerated Domain
Here we add a domain www.test.com to Tencent Cloud CDN. We specify the project as default project (project ID is 0), self-owned origin as the connection method, and 8.8.8.8 as the origin server IP address. The API request parameters are as follows:

| Parameter Name      | Description   | Value     |
| --------------- | ---------------------------- | ------------------ |
| host      | The domain host to be added    | www.test.com |
| projectId | The project to which the specified domain is added | 0 |
| hostType  | The connection type. Only two values are available: "cname" means that the user is using a self-owned origin server, and "ftp" means that the user is using FTP hosted origin provided by CDN.** Note: If you select FTP origin, you do not need to enter origin server configurations.**      | cname |
| origin    | Origin server configuration. This can be set to an origin server domain, or set to multiple origin server IPs (the "ip: port" type is supported, such as 8.8.8.8:8080). The port number should be between 0 and 65535 (exclusive of 0)    | 8.8.8.8 |

By combining common request parameters and API request parameters, you can get the final form of request as follows:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=AddCdnHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462440051
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&projectId=0
&hostType=cname
&origin=8.8.8.8
```

The returned result of the above request is as follows, which indicates that the domain has been successfully added:

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}

```










