
## SDK下载

目前支持 java, python, php, c++ sdk, 后续会支持更多语言。也欢迎广大开发者根据api说明开发更多语言的sdk版本。


[java sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_java_sdk_V1.0.0.zip)


[python sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_python_sdk_V1.0.0.zip)


[php sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_php_sdk_V1.0.0.zip)


[c++ sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_cpp_sdk_V1.0.0.zip)


## SDK使用注意事项

使用sdk，至少要获取[secret id](https://console.qcloud.com/capi)， [secret key](https://console.qcloud.com/capi)，endpoint（即请求发到哪个地域，走内网还是外网）。

endpoint 说明：
	
内网endpoint：http(s)://cmq-queue-region.api.tencentyun.com

公网endpoint：http(s)://cmq-queue-region.api.qcloud.com

- 如果业务进程也部署在腾讯云的CVM子机上，强烈建议使用同地域的内网endpoint。例如在腾讯云北京地域的CVM子机，可以使用http://cmq-queue-bj.api.tencentyun.com。原因：1）同地域内网时延更低；2）目前消息队列对于公网下行流量是要收取流量费用的，用内网可以节省这部分的费用。
- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
- 外网域名请求既支持http，也支持https。内网请求仅支持http。
