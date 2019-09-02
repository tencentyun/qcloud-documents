# Request Domain Name

Domain name for public network API request: <font style="color:red">kms-region.api.qcloud.com</font>

Domain name for private network API request: <font style="color:red">kms-region.api.tencentyun.com</font>

> Whenever (including during internal trial) any public network downstream traffic is generated from the use of a public network domain name, a fee is charged. It is strongly recommended that users whose services are on the Tencent Cloud use **private network** domain names, because no fee is charged for the traffic consumed in the private network.

> Only HTTP protocol is supported.

# Region

The "region" in the API request domain name needs to be replaced with a specific region. The region is subject to the "region" of the domain name, and the region value in common parameters is ignored here. Currently, the regions launched in KMS are shown in the following table:

| Region | Replacement Value | Domain Name for Public Network Request | Domain Name for Private Network Request |
|---------|---------|---------|---------|
| Beijing | bj | kms-bj.api.qcloud.com|kms-bj.api.tencentyun.com |
| Shanghai | sh | kms-sh.api.qcloud.com|kms-sh.api.tencentyun.com |
| Guangzhou | gz | kms-gz.api.qcloud.com|kms-gz.api.tencentyun.com |






