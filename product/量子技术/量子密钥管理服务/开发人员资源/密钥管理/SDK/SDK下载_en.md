## Downloading SDK

Currently, Tencent Cloud KMS supports SDKs in java, python, php, C++. More languages will be available soon. We would also like to see more SDK language versions developed by programmers according to the API description.

Github addresses:

- [java sdk](https://github.com/tencentyun/kms-java-sdk)


- [python sdk](https://github.com/tencentyun/kms-python-sdk)


- [php sdk](https://github.com/tencentyun/kms-php-sdk)


- [c++ sdk](https://github.com/tencentyun/kms-cpp-sdk)

Download links (to be expected):

- [java sdk]()


- [python sdk]()


- [php sdk]()


- [c++ sdk]()


## Notes about SDK

Before using a SDK, you need to at least get the [secret id](https://console.cloud.tencent.com/capi), [secret key](https://console.cloud.tencent.com/capi), and endpoint (it indicates the region to which the request is sent, and whether the request is sent through a private network or a public network).

Instructions for endpoint:
	
Private network endpoint: `https://kms-region.api.tencentyun.com`

Public network endpoint: `https://kms-region.api.qcloud.com`

- If the business process is also deployed on a Tencent Cloud CVM submachine, we strongly recommend that you use a private network endpoint in the same region. For example, if your business process is deployed on a CVM submachine of Tencent Cloud in Beijing, we recommend that you use `https://kms-bj.api.tencentyun.com`.
Reasons: 1) The latency is lower for a private network in the same region; 2) Currently, KMS charges a fee for the downstream traffic of public networks, so using a private network can save the cost.
- "region" needs to be replaced with a specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). "region" value in the common parameters should be consistent with that of domain name. For any inconsistency, the request is sent to the region specified by the domain name.

