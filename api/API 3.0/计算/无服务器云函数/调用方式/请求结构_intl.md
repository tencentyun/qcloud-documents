## **1. Service Address**

The Tencent Cloud API is divided into different functional modules by function and each module is accessed via a unique domain name. The API supports access from either a nearby region or a specified region. For example, Cloud Virtual Machine's domain name for the nearby region is cvm.tencentcloudapi.com, and its domain name for the Guangzhou region is cvm.ap-guangzhou.tencentcloudapi.com.

Below lists the currently supported regions:

| Access region | Domain name |
|----------|------|
|Nearby region (recommended)|\*.tencentcloudapi.com|
|South China (Guangzhou)|\*.ap-guangzhou.tencentcloudapi.com|
|East China (Shanghai)|\*.ap-shanghai.tencentcloudapi.com|
|North China (Beijing)|\*.ap-beijing.tencentcloudapi.com|
|Southwest China (Chengdu)|\*.ap-chengdu.tencentcloudapi.com|
|Southwest China (Chongqing)|\*.ap-chongqing.tencentcloudapi.com|
|Southeast Asia (Seoul)|\*.ap-seoul.tencentcloudapi.com|
|East China (Shanghai Financial)|\*.ap-shanghai-fsi.tencentcloudapi.com|
|South China (Shenzhen Financial)|\*.ap-shenzhen-fsi.tencentcloudapi.com|
|Southeast Asia (Singapore)|\*.ap-singapore.tencentcloudapi.com|
|Asia Pacific (Mumbai)|\*.ap-mumbai.tencentcloudapi.com|
|Western America (Silicon Valley)|\*.na-siliconvalley.tencentcloudapi.com|
|Eastern America (Virginia)|\*.na-ashburn.tencentcloudapi.com|

**Note: As financial and non-financial availability zones are isolated, when accessing the services in a financial availability zone (with the common parameter Region specifying a financial availability zone), it is necessary to specify a domain name with the financial availability zone, preferably in the same region as specified in Region.**

## **2. Communications Protocol**

All the interfaces of the Tencent Cloud API communicate via HTTPS, providing highly secure communications tunnels.

## **3. Request Method**

POST and GET requests are supported. Currently, POST requests only support Content-Type application/x-www-form-urlencoded.

## **4. Character Encoding**

Only UTF-8 encoding is used.
