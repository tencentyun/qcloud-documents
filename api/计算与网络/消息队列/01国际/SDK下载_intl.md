## Downloading SDK

Tencent Cloud's message queue supports java, python, php, and C++ SDKs currently, and will support more languages later. You are also welcome to develop more SDK versions of other languages based on API descriptions.

Here are the download links:

- [java sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_java_sdk_V1.0.3.zip)


- [python sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_python_sdk_V1.0.3.zip)


- [php sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_php_sdk_V1.0.3.zip)


- [c++ sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_cpp_sdk_V1.0.3.zip)


## Notes about SDK

Before using a SDK, you need to at least get the [secret id](https://console.cloud.tencent.com/capi), [secret key](https://console.cloud.tencent.com/capi), and endpoint (it indicates the region to which the request is to be sent, and whether the request is sent through a private network or a public network).

Instructions for endpoint:
	
Private network endpoint: `http://cmq-queue-region.api.tencentyun.com`

Public network endpoint: `https://cmq-queue-region.api.qcloud.com`

- If the business process is also deployed on a Tencent Cloud CVM, we strongly recommend that you use a private network endpoint in the same region. For example, if your business process is deployed on a CVM of Tencent Cloud in Beijing, we recommend that you use `http://cmq-queue-bj.api.tencentyun.com`.
Reasons: 1) The latency is lower for a private network in the same region; 2) Currently, message queue charges a fee for the downstream traffic of public networks, so using a private network can save the cost.
- region should be replaced with a specific region: gz (Guangzhou), sh (Shanghai), or bj (Beijing). The region value in the common parameters should be consistent with the region value of the domain. If there is an inconsistency, the request will be sent to the region specified by the domain.
- Public network domain requests support both HTTP and HTTPS. Private network requests only support HTTP.

