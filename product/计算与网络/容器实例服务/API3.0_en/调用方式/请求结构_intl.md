## 1. Service Address

This API supports access from the nearest region via a domain name, such as cvm.tencentcloudapi.com for this service, or access via the domain name for a designated region, for example, the domain name for Guangzhou region is "cvm.ap-guangzhou.tencentcloudapi.com".

It is recommended to use the domain name for access from the nearest region. Depending on the location where the client makes an API call, the domain name is automatically resolved to a server in the specific **nearest** region. For example, when a request is made in Guangzhou, the domain name is automatically resolved to a Guangzhou server, just like the way you specify "cvm.ap-guangzhou.tencentcloudapi.com".

The list of supported domain names:

| Region | Domain Name |
|----------|------|
| Access from the nearest region (recommended, and only for non-Finance regions) | cvm.tencentcloudapi.com |
| South China (Guangzhou) | cvm.ap-guangzhou.tencentcloudapi.com |
| East China (Shanghai) | cvm.ap-shanghai.tencentcloudapi.com |
| North China (Beijing) | cvm.ap-beijing.tencentcloudapi.com |
| Southwest China (Chengdu) | cvm.ap-chengdu.tencentcloudapi.com |
| Southwest (Chongqing) | cvm.ap-chongqing.tencentcloudapi.com |
| Southeast Asia (Seoul) | cvm.ap-seoul.tencentcloudapi.com |
| Southeast Asia (Singapore) | cvm.ap-singapore.tencentcloudapi.com |
| Asia Pacific (Mumbai) | cvm.ap-mumbai.tencentcloudapi.com |
| Western U.S. (Silicon Valley) | cvm.na-siliconvalley.tencentcloudapi.com |
| Eastern U.S. (Virginia) | cvm.na-ashburn.tencentcloudapi.com |

**Note: Since [Finance regions](https://cloud.tencent.com/document/product/304/2766) and non-Finance regions are isolated and not interconnected, when accessing a service in a Finance region (the common parameter Region is a Finance region), you need to specify a domain name containing the Finance region that should be identical to the value of Region field.**

| Region for Accessing Finance Region | Finance Region Domain Name |
|----------|------|
| East China (Shanghai Finance Region) | cvm.ap-shanghai-fsi.tencentcloudapi.com |
| South China (Shenzhen Finance Region) | cvm.ap-shenzhen-fsi.tencentcloudapi.com |

## 2. Communication Protocol

All Tencent Cloud APIs communicate over HTTPS to provide high-security connections.

## 3. Request Methods

Both POST and GET requests are supported. Content-Type can only be application/x-www-form-urlencoded in POST requests.

## 4. Character Encoding

UTF-8 encoding is always used.

