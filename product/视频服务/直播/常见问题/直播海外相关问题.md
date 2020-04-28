### 海外直播推流如何加速？
在直播控制台 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 部分，默认的推流域名是配置海外推流加速的。如果需要使用自己的推流域名，那么可以添加推流域名，按要求完成 CNAME 操作后，即可完成推流域名海外加速的配置。
		
### 海外播放域如何加速？
在直播控制台 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 部分，添加播放域名，可选择两种类型：**全球加速**，该加速类型需要域名在中国大陆完成域名备案，否则会配置失败；**中国港澳台地区及海外地区加速**，只需要按引导完成配置即可，但该种加速类型中国大陆无法播放。
	 
### 如何确认自己的域名有没有配置完海外加速？
使用海外的机器 ping 下推流、播放域名，服务端 IP 为就近的节点的即完成了海外加速配置；或者使用 [https://tools.ipip.net/dns.php工具](https://tools.ipip.net/dns.php)，拨测下自己的域名，看下解析出来的 IP 是不是对应加速区域的 IP。
	 
### 海外直播播放失败如何排查？
目前海外播放支持 HTTP-FLV、HLS、RTMP 播放。对于播放异常的问题，可以通过以下方式逐步排查：
1. **ping 域名是否能通？**
如果不通，检查当前的网络环境。
2. **获取到的 HTTP 的状态码是否为200？**
	如果非200，区分不同的失败情况，403通常是播放鉴权失败，检查防盗链计算格式是否符合要求，404通常是播放的流不在平台上，检查推流是否正常。其他错误码可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 协助排查。
	 
### 海外直播推流支持何种协议？
目前海外直播推流只支持 RTMP 协议。
	 
### 海外直播播放是否支持 HTTPS？
支持，在域名管理部分，对需要配置 HTTPS 拉流的域名添加 HTTPS 证书即可，具体操作：[域名管理](https://console.cloud.tencent.com/live/domainmanage) > 对应播放域名 > 管理 > 高级配置 > HTTPS 配置。
	 
### 直播海外播放加速区域是否可以修改？
可以，在控制台的域名管理部分进行修改即可，一般生效时间为15分钟。
	 
### 海外推流加速是否支持 HTTPDNS 调度？
支持，暂时需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 后台配置。
