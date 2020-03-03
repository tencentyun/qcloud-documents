DDoS 高防 IP 专业版支持 HTTP/HTTPS CC 防护功能。当高防系统统计的 HTTP/HTTPS 请求量超过设定的【http/https 请求数阈值】时，将自动触发 CC 防护。
DDoS 高防 IP 专业版提供自定义 CC 防护策略，用户可根据业务特点和防护需求，通过自定义防护策略实现更精准的 CC 攻击拦截。同时，还支持 URL 白名单、IP 白名单和 IP 黑名单策略：
- 白名单中的 URL，其访问请求将无需执行 CC 攻击检测，直接被放行。
- 白名单中 IP，其 HTTP/HTTPS 访问请求将无需执行 CC 攻击检测，直接被放行。
- 黑名单中 IP，其 HTTP/HTTPS 访问请求将直接被拒绝。

## 开启 CC 防护
**HTTP CC 防护**
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航栏中，选择【DDoS 高防 IP 专业版】>【防护配置】，在【防护策略】页签下，选择目标实例。
2. 在【HTTP CC 防护】区域，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/cecd307c728bd0a11f3f1a217ca9b609.png"  style="margin:0;">开启 HTTP CC 防护，单击【http 请求数阈值】右侧的下拉框选择合适的阈值即可。
![](https://main.qcloudimg.com/raw/2ef9639dc862f3d834f4234e1090e8b3.png)
>?HTTP CC 防护状态默认关闭。防护状态开启后，才可设置 HTTP 请求数阈值。

**HTTPS CC 防护**
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航栏中，选择【DDoS 高防 IP 专业版】>【防护配置】，在【防护策略】页签下，选择目标实例。
2. 在【HTTPS CC 防护】区域，选择防护域名，单击【防护状态】右侧的<img src="https://main.qcloudimg.com/raw/cecd307c728bd0a11f3f1a217ca9b609.png"  style="margin:0;">开启 HTTPS CC 防护，单击【https 请求数阈值】右侧的下拉框选择合适的阈值即可。
![](https://main.qcloudimg.com/raw/498d14694644feab0b31783330ff8158.png)
>?HTTPS CC 防护状态默认关闭。防护状态开启后，才可设置 HTTPS 请求数阈值。

## 自定义 CC 防护策略
>?
- **需要开启 HTTP CC 防护，才可设置自定义 CC 防护策略，最多可添加5条。**
- **仅在该高防 IP 正在被攻击状态时，自定义策略才会生效。**
- **匹配模式下**，每个自定义策略最多可以设置4个策略条件进行特征控制，且多个条件之间是“与”的关系，需要所有条件全部匹配策略才生效。
- **限速模式下**，每个自定义策略只允许设置1条策略条件。

1. 登录[ DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航栏中，选择【DDoS 高防 IP 专业版】>【防护配置】，在【CC 攻击防护】页签，单击【添加策略】。
2. 在【添加自定义策略】弹出框，根据实际业务需求设置以下参数，单击【确定】即可。
![](https://main.qcloudimg.com/raw/e8354a42b59fb8a287b00d1f82de0576.png)
	-  策略名称
输入策略名称，长度为1 - 20字符，不限制字符类型。
	-  协议
支持 HTTP 协议。
	- 模式
  - 匹配模式：匹配到 HTTP 对应字段头的请求，执行拦截或验证码操作。
 	- 限速模式：对源IP访问进行限速处理。
	- 策略
		- **当选择【匹配模式】时，协议是 HTTP**，支持从 HTTP 报文的 host 参数、CGI 参数、Referer 和 User-Agent 多个特征进行组合，组合逻辑包括包含、不包含和等于。最多可以设置4个策略条件进行特征控制。
		- 当选择【限速模式】时，对每个源 IP 访问进行限速处理。只允许设置1个策略条件。
![](https://main.qcloudimg.com/raw/970f48a76331e287b19b69efe3ac6f42.png)
	- 执行
仅当选择【匹配模式】时，需要设置该参数。表示策略匹配后，需执行的处理动作，包括拦截和验证码。

## 设置黑白名单
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航栏中，选择【DDoS 高防 IP 专业版】>【防护配置】，进入防护配置页面，单击【CC 攻击防护】，选择目的实例。
1. 勾选页面右侧【HTTP】或【HTTPS】，单击【URL 白名单】、【IP 白名单】或【IP 黑名单】，进行黑白名单设置，支持添加、修改，也支持批量导入导出。
![](https://main.qcloudimg.com/raw/73ea2db63eb4da24eebc6ad66f04eb86.png)

