## SDK 下载

腾讯云消息队列目前支持 java、python、php 及 C++ SDK，后续会支持更多语言。也欢迎广大开发者根据 API 说明开发更多语言的 SDK 版本。

#### GitHub 地址如下：

- [Java SDK](https://github.com/tencentyun/cmq-java-sdk)


- [Python SDK](https://github.com/tencentyun/cmq-python-sdk)


- [PHP SDK](https://github.com/tencentyun/cmq-php-sdk)


- [C++ SDK](https://github.com/tencentyun/cmq-cpp-sdk)

#### 下载地址如下：

- [Java SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_java_sdk_V1.0.4.zip)


- [Python SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_python_sdk_V1.0.4.zip)


- [HP SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_php_sdk_V1.0.4.zip)


- [C++ SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_cpp_sdk_V1.0.4.zip)


## SDK 使用注意事项

使用 SDK 前至少要获取 [secret id](https://console.cloud.tencent.com/capi)、 [secret key](https://console.cloud.tencent.com/capi) 和 endpoint（即请求发到哪个地域，走内网还是外网）。

### endpoint 说明：

#### 队列模式：

**请参照下面说明将域名中的 region 替换成相应地域：**

内网 endpoint：`http ://cmq-queue-region.api.tencentyun.com`

公网 endpoint：`http(s)://cmq-queue-region.api.qcloud.com`

#### 主题模式 ：

**请参照下面说明将域名中的 region 替换成相应地域：**

内网 endpoint：`http ://cmq-topic-region.api.tencentyun.com`

公网 endpoint：`http(s)://cmq-topic-region.api.qcloud.com`
 
如果业务进程也部署在腾讯云的 CVM 子机上，强烈建议使用同地域的内网 endpoint。例如在腾讯云北京地域的 CVM 子机则建议您使用 `http://cmq-queue-bj.api.tencentyun.com`。原因是：
- 同地域内网时延更低；
- 目前消息队列对于公网下行流量是要收取流量费用的，用内网可以节省这部分的费用。

region 需用具体地域替换：gz（广州），sh（上海），bj（北京），shjr（上海金融），szjr（深圳金融），hk（香港）,ca(北美)，cd（成都），usw（美西），sg（新加坡）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。

外网域名请求既支持 http，也支持 https。内网请求仅支持 http。
