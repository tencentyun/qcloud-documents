## 概述
腾讯云消息队列 CMQ 目前支持 Java、Python、PHP 及 C++ 等语言版本的 SDK ，后续会支持更多语言。也欢迎广大开发者根据 API 说明开发更多语言的 SDK 版本。
由于分配资源和释放资源需要1s 左右的时间，当前消息队列 SDK 在创建及删除队列/主题时会有1s 延迟，建议在程序中增加创建和删除的时间间隔保障调用成功。

>!
- 为了保障数据传输的安全，为您提供更加可靠的服务，腾讯云团队将在2019年1月31日23:59:59停止对主题及队列的公网 HTTP 方式的访问，建议您将公网接口请求域名改为 HTTPS。
- 修改公网接口请求域名的方式如下：
判断接入域名中使用的协议是否为 HTTP，如果有，将其替换为 HTTPS 即可。
例如：`endpoint=http://cmq-topic-gz.api.qcloud.com`该接入方式为 HTTP 协议访问广州主题公网域名，修改为：`endpoint=https://cmq-topic-gz.api.qcloud.com`。

## 下载地址
不同语言版本的 SDK 下载地址如下：
- [Java SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_java_sdk_V1.0.4.zip)
- [Python SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_python_sdk_V1.0.4.zip)
- [PHP SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_php_sdk_V1.0.4.zip)
- [C++ SDK](http://cmqsdk-10016717.cossh.myqcloud.com/qc_cmq_cpp_sdk_V1.0.4.zip)
- [C# SDK](https://main.qcloudimg.com/raw/2fe051dcc6ee0b3088f16d5d04182f64.zip)

#### GitHub 地址
- [Java SDK](https://github.com/tencentyun/cmq-java-sdk)
- [Python SDK](https://github.com/tencentyun/cmq-python-sdk)（默认为 Python2 SDK，您可切换至 Python3 分支中查看 Python3 SDK ）
- [PHP SDK](https://github.com/tencentyun/cmq-php-sdk)
- [C++ SDK](https://github.com/tencentyun/cmq-cpp-sdk)

## 注意事项
使用 SDK 前至少要获取 [SecretId](https://console.cloud.tencent.com/capi)、 [SecretKey](https://console.cloud.tencent.com/capi) 和 endpoint（即请求发到哪个地域，走内网还是外网）。endpoint 说明如下。

#### 队列模型
**请参照下面说明将域名中的 {$region} 替换成相应地域：**
- 外网接口请求域名：`https://cmq-queue-{$region}.api.qcloud.com`
- 内网接口请求域名：`http://cmq-queue-{$region}.api.tencentyun.com`


#### 主题模型
**请参照下面说明将域名中的 {$region} 替换成相应地域：**
- 外网接口请求域名：`https://cmq-topic-{$region}.api.qcloud.com`
- 内网接口请求域名：`http://cmq-topic-{$region}.api.tencentyun.com`
 
如果业务进程也部署在腾讯云的 CVM 子机上，强烈建议使用同地域的内网 endpoint。例如：在腾讯云北京地域的 CVM 子机，则建议您使用 `http://cmq-queue-bj.api.tencentyun.com`。原因如下：
- 同地域内网时延更低。
- 目前消息队列对于公网下行流量是要收取流量费用的，用内网可以节省这部分的费用。

#### 说明
{$region}需用具体地域替换：gz（广州），sh（上海），bj（北京），shjr（上海金融），szjr（深圳金融），hk（香港），cd（成都），ca(北美)，usw（美西），sg（新加坡）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。

