## Request Domain Name

Queue Model

- Domain for public network API request: `cmq-queue-region.api.qcloud.com`
- Domain for private network API request: `cmq-queue-region.api.tencentyun.com`


Topic Model

- Domain for public network API request: cmq-topic-region.api.qcloud.com
- Domain for private network API request: cmq-topic-region.api.tencentyun.com

Description:

1. "region" needs to be replaced with a specific region, such as gz (Guangzhou), sh (Shanghai), bj (Beijing), shjr (Shanghai Finance), szjr (Shenzhen Finance) and hk (Hong Kong). The value of "region" in the common parameters should be consistent with that of its domain name. For any inconsistency, the request will be sent to the region specified by its domain name.
1. Public network domain requests support both http and https, while private network domain requests only support http.
1. Some of the input parameters are optional. If not specified, the default value will be taken.
1. All the output parameters will be returned to the user if the request is successful; otherwise, at least code, message, and requestId will be returned to the user.


> **Note:**
>  
> Whenever (including during internal trial) any public network downstream traffic is generated from the use of a public network domain name, a fee is charged. It is strongly recommended that users whose services are on the Tencent Cloud use private network domain names, because no fee is charged for the traffic consumed in the private network.

## Region

The "region" in the API request domain name needs to be replaced with a specific region. The region depends on the "region" of the domain name, and the region value in common parameters is ignored here. Currently, the regions launched in CMQ are shown in the following table:

### Queue Model

| Region | Replacement Value | Domain Name for Public Network Request | Domain Name for Private Network Request |
|---------|---------|---------|---------|
| Beijing | bj | `cmq-queue-bj.api.qcloud.com` | `cmq-queue-bj.api.tencentyun.com` |
| Shanghai | sh | `cmq-queue-sh.api.qcloud.com` | `cmq-queue-sh.api.tencentyun.com` |
| Guangzhou | gz | `cmq-queue-gz.api.qcloud.com` | `cmq-queue-gz.api.tencentyun.com` |
| Shanghai Finance | shjr | `cmq-queue-shjr.api.qcloud.com` | `cmq-queue-shjr.api.tencentyun.com` |
| Shenzhen Finance | szjr | `cmq-queue-szjr.api.qcloud.com` | `cmq-queue-szjr.api.tencentyun.com` |
| Hong Kong | hk | `cmq-queue-hk.api.qcloud.com` | `cmq-queue-hk.api.tencentyun.com` |
| North America | ca | `cmq-queue-ca.api.qcloud.com` | `cmq-queue-ca.api.tencentyun.com` |
| Chengdu | cd | `cmq-queue-cd.api.qcloud.com` | `cmq-queue-cd.api.tencentyun.com` |

### Topic Model 

| Region | Replacement Value | Domain Name for Public Network Request | Domain Name for Private Network Request |
|---------|---------|---------|---------|
| Beijing | bj | `cmq-topic-bj.api.qcloud.com` | `cmq-topic-bj.api.tencentyun.com` |
| Shanghai | sh | `cmq-topic-sh.api.qcloud.com` | `cmq-topic-sh.api.tencentyun.com` |
| Guangzhou | gz | `cmq-topic-gz.api.qcloud.com` | `cmq-topic-gz.api.tencentyun.com` |
| Shanghai Finance | shjr | `cmq-topic-shjr.api.qcloud.com` | `cmq-topic-shjr.api.tencentyun.com` |
| Shenzhen Finance | szjr | `cmq-topic-szjr.api.qcloud.com` | `cmq-topic-szjr.api.tencentyun.com` |
| Hong Kong | hk | `cmq-topic-hk.api.qcloud.com` | `cmq-topic-hk.api.tencentyun.com` |
| North America | ca | `cmq-topic-ca.api.qcloud.com` | `cmq-topic-ca.api.tencentyun.com` |
| Chengdu | cd | `cmq-topic-cd.api.qcloud.com` | `cmq-topic-cd.api.tencentyun.com` |

