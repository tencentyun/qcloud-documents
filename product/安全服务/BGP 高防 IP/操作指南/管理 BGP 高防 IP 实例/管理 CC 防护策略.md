BGP 高防 IP 支持 HTTP/HTTPS CC 防护功能。当高防 IP 统计的 HTTP/HTTPS 请求量超过设定的【http/https 请求数阈值】时，将自动触发 HTTP/HTTPS CC 防护。
BGP 高防 IP 提供自定义 CC 防护策略，用户可根据业务特点和防护需求，通过自定义防护策略实现更精准的 CC 攻击拦截。同时，还支持 URL 白名单、IP 白名单和 IP 黑名单策略配置：
-  白名单中的 URL，其访问请求将无需执行 CC 攻击检测，直接被放行。
-  白名单中 IP，其 HTTP/HTTPS 访问请求将无需执行 CC 攻击检测，直接被放行。
-  黑名单中 IP，其 HTTP/HTTPS 访问请求将直接被拒绝。


## 开启CC防护
**HTTP CC 防护**
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中选择【BGP 高防 IP】>【防护配置】，在【防护策略】页面下，选择目标实例。
1. 在【HTTP CC 防护】区域，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/9d7bb2c60a2b375acb45614f39e4986f.png"  style="margin:0;"> 开启 HTTP CC 防护，单击【http 请求数阈值】右侧的下拉框选择合适的阈值即可。
![](https://main.qcloudimg.com/raw/ca2bd6306d3a29cf32a834dccc8816bb.png)
>?CC 防护状态默认关闭。防护状态开启后，才可设置 HTTP 请求数阈值。

**HTTPS CC 防护**
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中选择【BGP 高防 IP】>【防护配置】，在【防护策略】页面下，选择目标实例。
2. 在【HTTPS CC】区域，选择防护域名，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/9d7bb2c60a2b375acb45614f39e4986f.png"  style="margin:0;"> 开启 HTTPS CC 防护，单击【https 请求数阈值】右侧的下拉框选择合适的阈值。
![](https://main.qcloudimg.com/raw/452ead2f4b71df2dc06f3a978ffeb5b6.png)
>?CC 防护状态默认关闭。防护状态开启后，才可设置 HTTPS 请求数阈值。


## 自定义 CC 防护策略
>? 
- **需要开启 HTTP/HTTPS CC 防护，才可设置自定义 CC 防护策略，最多可添加5条。**
- **仅在该高防 IP 正在被攻击状态时，自定义策略才会生效。**
-  **匹配模式下**，每个自定义策略最多可以设置**4**个策略条件进行特征控制，且多个条件之间是“与”的关系，需要所有条件全部匹配策略才生效。
-  **限速模式下**，每个自定义策略只允许设置**1**条策略条件。

1. 登录  [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中选择【BGP 高防 IP】>【防护配置】，单击【CC 攻击防护】页签，选择地域和线路，选择目的实例，单击【添加策略】。
2. 在【添加自定义策略】弹出框，根据实际业务需求设置以下参数，单击【确定】即可。
![](https://main.qcloudimg.com/raw/e625c87b845bc66f169004e01f3a538c.png)
	- 策略名称
输入策略名称，长度为1 - 20字符，不限制字符类型。
	- 协议
目前支持 HTTP、HTTPS 两种协议。
	- 防护域名
只有勾选 HTTPS 协议，才需要选择对应的防护域名。可选择的防护域名范围，等于已完成配置的转发规则中，属于 HTTPS 协议的网站域名。
	- 模式
		- 匹配模式：匹配到 HTTP / HTTPS 对应字段头的请求，执行拦截或验证码操作。
		- 限速模式：对源 IP 访问进行限速处理，**HTTPS 协议不支持选择限速模式**。
	- 策略
		- **当选择【匹配模式】时，协议是 HTTP**，支持从 HTTP 报文的 host 参数、CGI 参数、Referer 和 User-Agent 多个特征进行组合，组合逻辑包括包含、不包含和等于。最多可以设置4个策略条件进行特征控制。若**协议是 HTTPS 时**，支持从 HTTPS 报文的 CGI 参数、Referer 和 User-Agent 多个特征进行组合，组合逻辑包括包含、不包含和等于。最多可以设置3个策略条件进行特征控制。
		- 当选择【限速模式】时，对每个源 IP 访问进行限速处理。只允许设置1个策略条件。
![](https://main.qcloudimg.com/raw/55907e363ea9230f4258bd499f43f7a1.png)

 - 执行
仅当选择【匹配模式】时，需要设置该参数。表示策略匹配后，需执行的处理动作，包括拦截和验证码。

## 设置黑白名单
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，前往【BGP 高防 IP】>【防护配置】，单击【CC 攻击防护】页签，选择地域和线路，选择目的实例。
1. 勾选页面右侧【HTTP】或【HTTPS】，选择【URL 白名单】、【IP 白名单】或【IP 黑名单】，进行黑白名单设置，支持添加、修改。
![](https://main.qcloudimg.com/raw/c2a740f586066edaed33a9e09c1ff930.png)
