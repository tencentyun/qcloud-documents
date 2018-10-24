## 1. Service Address

Tencent Cloud APIs are divided into different function modules, with each module accessed using a different domain name. You can access these APIs from a closest region or a specified region. For example, the access domain name of a nearest CVM is cvm.tencentcloudapi.com, and that of the Guangzhou region is cvm.ap-guangzhou.tencentcloudapi.com.

The list of supported domain names:

| Region | Domain Name |
|----------|------|
| The nearest region (recommended) | \*.tencentcloudapi.com|
| South China (Guangzhou) |\*.ap-guangzhou.tencentcloudapi.com|
| East China (Shanghai) |\*.ap-shanghai.tencentcloudapi.com|
| North China (Beijing) |\*.ap-beijing.tencentcloudapi.com|
| Southwest China (Chengdu) |\*.ap-chengdu.tencentcloudapi.com|
| Southwest China (Chongqing) |\*.ap-chongqing.tencentcloudapi.com|
| Southeast Asia (Seoul) |\*.ap-seoul.tencentcloudapi.com|
| East China (Shanghai Finance) |\*.ap-shanghai-fsi.tencentcloudapi.com|
| South China (Shenzhen Finance) |\*.ap-shenzhen-fsi.tencentcloudapi.com|
| Southeast Asia (Singapore) |\*.ap-singapore.tencentcloudapi.com|
| Asia Pacific (Mumbai) |\*.ap-mumbai.tencentcloudapi.com|
| Western U.S. (Silicon Valley) |\*.na-siliconvalley.tencentcloudapi.com|
| Eastern U.S. (Virginia) |\*.na-ashburn.tencentcloudapi.com|

**Note: Since Finance regions and non-Finance regions are isolated and not interconnected, when accessing a service in a Finance region (the common parameter Region is a Finance region), you need to specify a domain name containing the Finance region that should be identical to the value of Region field.**

## 2. Communication Protocol

All Tencent Cloud APIs communicate over HTTPS to provide high-security channels.

## 3. Request Methods

Both POST and GET requests are supported. Content-Type can only be application/x-www-form-urlencoded in POST request.

## 4 Character Encoding

UTF-8 encoding is always used.

