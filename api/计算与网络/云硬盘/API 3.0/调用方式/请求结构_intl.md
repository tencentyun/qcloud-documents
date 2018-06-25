## 1. Service Address

Tencent Cloud APIs are divided into different feature modules, with each module accessed using a different domain name. You can access these APIs from a closest region or a specified region. For example, the domain name of a nearest CVM is cvm.tencentcloudapi.com, and that of the Guangzhou region is cvm.ap-guangzhou.tencentcloudapi.com.

The list of supported domain names:

| Region | Domain Name |
|----------|------|
| The nearest region (recommended) | \*.tencentcloudapi.com |
| South China (Guangzhou) | \*.ap-guangzhou.tencentcloudapi.com |
| East China (Shanghai) | \*.ap-shanghai.tencentcloudapi.com |
| North China (Beijing) | \*.ap-beijing.tencentcloudapi.com |
| Southwest China (Chengdu) | \*.ap-chengdu.tencentcloudapi.com |
| Southwest (Chongqing) | \*.ap-chongqing.tencentcloudapi.com |
| Southeast Asia (Seoul) | \*.ap-seoul.tencentcloudapi.com |
| East China (Shanghai Finance Zone) | \*.ap-shanghai-fsi.tencentcloudapi.com |
| South China (Shenzhen Finance Zone) | \*.ap-shenzhen-fsi.tencentcloudapi.com |
| Southeast Asia (Singapore) | \*.ap-singapore.tencentcloudapi.com |
| Southeast Asia (India) | \*.ap-mumbai.tencentcloudapi.com |
| Western U.S. (Silicon Valley) | \*.na-siliconvalley.tencentcloudapi.com |
| Eastern U.S. (Ashburn) | \*.na-ashburn.tencentcloudapi.com |

## 2. Communication Protocol

All the Tencent Cloud APIs achieve communication over HTTPS to provide high-security channels.

## 3. Request Methods

Both POST and GET methods are supported, but they cannot be used together. If the GET method is used, the parameters are obtained from Querystring. If the POST method is used, the parameters are obtained from Request Body, and the parameters in the Querystring are ignored. The rules for parameter formats are the same for both methods. Generally, GET method is used. If parameter strings are too long, POST method is used. For more information, please see the relevant API description.

## 4. Character Encoding

UTF-8 encoding is always used.
