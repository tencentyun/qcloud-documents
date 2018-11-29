
## SDK下载

目前支持 java, python, php, c++ sdk, 后续会支持更多语言。也欢迎广大开发者根据api说明开发更多语言的sdk版本。


[java sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_java_sdk_V1.0.2.zip)


[python sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_python_sdk_V1.0.2.zip)


[php sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_php_sdk_V1.0.2.zip)


[c++ sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_cpp_sdk_V1.0.2.zip)


## SDK使用注意事项

使用sdk，至少要获取[secret id](https://console.cloud.tencent.com/capi)， [secret key](https://console.cloud.tencent.com/capi)，endpoint（即请求发到哪个地域，走内网还是外网）。

endpoint 说明：
	
内网endpoint：http(s)://cmq-queue-region.api.tencentyun.com

内网endpoint：http(s)://cmq-queue-region.api.qcloud.com

- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持http，也支持https。内网请求仅支持http。
