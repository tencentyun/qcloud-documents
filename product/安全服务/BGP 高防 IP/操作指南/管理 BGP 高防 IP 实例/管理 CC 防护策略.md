DDoS 高防 IP 支持 HTTP/HTTPS CC 防护功能。当高防 IP 统计的 HTTP/HTTPS 请求量超过设定的【http/https 请求数阈值】时，将自动触发 HTTP/HTTPS CC 防护。

DDoS 高防 IP 提供设置访问控制策略功能。开启 HTTP/HTTPS CC 防护功能，用户可以使用常见 HTTP/HTTPS 报文的字段（如 host 参数、CGI 参数、Referer 和 User-Agent 等）设置匹配条件，对公网用户的访问请求进行管控，对命中条件的请求执行阻断、人机识别动作。用户也可以设置限速规则，对访问 IP 执行限速处理。
DDoS 高防 IP 还支持 URL 白名单、IP 白名单、IP 黑名单策略配置：
-  白名单中的 URL，其访问请求将无需执行 CC 攻击检测，直接被放行。
-  白名单中 IP，其 HTTP/HTTPS 访问请求将无需执行 CC 攻击检测，直接被放行。
-  黑名单中 IP，其 HTTP/HTTPS 访问请求将直接被拒绝。


## 开启CC防护
**HTTP CC 防护**
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中选择【DDoS 高防 IP】>【防护配置】，在防护配置页面下，单击【CC 防护】，选择目标实例。
1. 在【HTTP CC 防护】区域，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/9d7bb2c60a2b375acb45614f39e4986f.png"  style="margin:0;"> 开启 HTTP CC 防护，单击【http 请求数阈值】右侧的下拉框选择合适的阈值即可。
![](https://main.qcloudimg.com/raw/ca2bd6306d3a29cf32a834dccc8816bb.png)
>?CC 防护状态默认关闭。防护状态开启后，才可设置 HTTP 请求数阈值。

**HTTPS CC 防护**
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中选择【DDoS 高防 IP】>【防护配置】，在防护配置页面下，单击【CC 防护】，选择目标实例。
2. 在【HTTPS CC】区域，选择防护域名，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/9d7bb2c60a2b375acb45614f39e4986f.png"  style="margin:0;"> 开启 HTTPS CC 防护，单击【https 请求数阈值】右侧的下拉框选择合适的阈值。
![](https://main.qcloudimg.com/raw/452ead2f4b71df2dc06f3a978ffeb5b6.png)
>?CC 防护状态默认关闭。防护状态开启后，才可设置 HTTPS 请求数阈值。


## 自定义 CC 防护策略
>? 
- **需要开启 HTTP/HTTPS CC 防护，才可设置自定义 CC 防护策略，最多可添加5条。**
- **仅在该高防 IP 正在遭受CC攻击时，自定义策略才会生效。**
-  **匹配模式下**，每个自定义策略最多可以设置**4**个策略条件进行特征控制，且多个条件之间是“与”的关系，需要所有条件全部匹配策略才生效。
-  **限速模式下**，每个自定义策略只允许设置**1**条策略条件。
>
1. 登录  [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中，选择【DDoS 高防 IP】>【防护配置】，进入防护配置页面，单击【CC 防护】，选择地域和线路，选择目的实例，单击【添加访问控制策略】。
2. 在【添加访问控制策略】弹出框，根据实际业务需求设置以下参数，单击【确定】即可。
![](https://main.qcloudimg.com/raw/83d50ac7be9edfaa1ff7dd62b58463a2.png)
	- 策略名称
输入策略名称，长度为1 - 20字符，不限制字符类型。
	- 协议
目前支持 HTTP、HTTPS 两种协议。
	- 防护域名
只有勾选 HTTPS 协议，才需要选择对应的防护域名。可选择的防护域名范围，等于已完成配置的转发规则中，属于 HTTPS 协议的网站域名。
	- 模式
		- 匹配模式：匹配到 HTTP / HTTPS 对应字段头的请求，执行拦截或人机识别操作。
		- 限速模式：对源 IP 访问进行限速处理，**HTTPS 协议不支持选择限速模式**。
	- 策略
		- **当选择【匹配模式】时，协议是 HTTP**，支持从 HTTP 报文的 host 参数、CGI 参数、Referer 和 User-Agent 多个特征进行组合，组合逻辑包括包含、不包含和等于。最多可以设置4个策略条件进行特征控制。若**协议是 HTTPS 时**，支持从 HTTPS 报文的 CGI 参数、Referer 和 User-Agent 多个特征进行组合，组合逻辑包括包含、不包含和等于。最多可以设置3个策略条件进行特征控制，字段描述如下：
		<table>
		<tr><th>匹配字段</th><th>字段描述</th><th>适用的逻辑符</th></tr>
		<tr><td>host</td><td>访问请求的域名。</td><td>包含、不包含、等于</td></tr>
		<tr><td>CGI</td><td>访问请求的 URI 地址。</td><td>包含、不包含、等于</td></tr>
		<tr><td>Referer</td><td>访问请求的来源网址，表示该访问请求是从哪个页面跳转产生的。</td><td>包含、不包含、等于</td></tr>
		<tr><td>User-Agent</td><td>发起访问请求的客户端浏览器标识等相关信息。</td><td>包含、不包含、等于</td></tr>
		</table>
		- 当选择【限速模式】时，对每个源 IP 访问进行限速处理。只允许设置1个策略条件。
![](https://main.qcloudimg.com/raw/55907e363ea9230f4258bd499f43f7a1.png)
	- 执行
仅当选择【匹配模式】时，需要设置该参数。表示策略匹配后，需执行的处理动作，包括拦截和验证码。

## 设置黑白名单
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中，选择【DDoS 高防 IP】>【防护配置】，进入防护配置也页面，单击【CC 防护】，选择地域和线路，选择目的实例。
2. 勾选页面右侧【HTTP】或【HTTPS】，选择【URL 白名单】、【IP 白名单】或【IP 黑名单】，进行黑白名单设置，支持添加、修改，也支持批量导入导出。
![](https://main.qcloudimg.com/raw/aa6affedb8ef027a9b5d316c04a892f2.png)
