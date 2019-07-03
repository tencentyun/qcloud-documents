## 功能简介
CC 防护对网站特定的 URL 进行访问保护，CC 防护2.0全新改版，支持根据用户访问源 IP 或者 SESSION 频率制定防护规则对访问进行处置，处置措施包括告警、人机识别和阻断。

>!使用基于 SESSION 的 CC 防护策略，需要先进行 SESSION 设置，才能设置基于 SESSION 的 CC 防护策略置。

## 配置步骤
**示例一： 基于访问源 IP 的 CC 防护设置**
基于 IP 的 CC 防护策略不需要对 SESSION 维度进行设置，直接配置即可。
1. 进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【防护设置】> 【域名列表】 ，单击对应域名【防护配置】进入配置页面，单击【CC 防护设置】进行 CC 规则配置。
![](https://main.qcloudimg.com/raw/2fc445cb9cffdae68389bdedb1b50cf9.png)
2. 选择【CC 规则设置】 ，单击【添加规则】填写相应信息，识别模式为 IP。
![](https://main.qcloudimg.com/raw/558d87d9861b38cdbcdaa8130ac48bd6.png)
 - **配置项说明：**
**识别模式：** IP、SESSION。
**匹配条件：** 包括相等、前缀匹配和包含。
 - **高级匹配：**
**访问频次：**根据业务情况设置，访问频次。建议输入，正常人访问速度的3 - 10倍，例如网站人平均访问20次/分钟，可配置为60 - 200/分钟；可依据被攻击严重程度调整。
**执行动作：**观察、人机识别和阻断。
**惩罚时长：**最短为1分钟，最长为一周。
**优先级：**请输入1 - 100的整数，数字越小，代表这条规则的执行优先级越高；相同优先级下，创建时间越晚，优先级越高。

3. 规则操作，选择已经创建的规则，可以对规则进行关闭、修改和删除。
![](https://main.qcloudimg.com/raw/5e6f39af9efcce9fd09c670c34db78ea.png)

4. 根据规则设置，触发 CC 攻击行为。
![](https://main.qcloudimg.com/raw/d5fa43ac17ab42057198cba8abed4463.png)
5. 查看 IP 实时阻断信息。单击【IP 管理】>【IP 封堵状态】 ，可以查看到 实时阻断的 IP 信息 ,可以对 IP 进行加白或者加黑处理。
![](https://main.qcloudimg.com/raw/fa3f56e2511f96dff04c4dc374588a5f.png)

**示例二： 基于 SESSION 的 CC 防护设置**
基于 SESSION 访问速率 CC 防护，能够有效地解决在办公网、商超和公共 WIFI 场合，用户因使用相同 IP 出口而导致的误拦截问题。
1. 设置 SESSION 维度信息。单击【防护设置】>【域名列表】，选择对应域名单击【防护配置】>【CC 防护设置】进入配置页面。
![](https://main.qcloudimg.com/raw/5c49844f0029ef5156ff74adafbc5087.png)
2. 单击【设置】进行 SESSION 设置，此示例中，选择 COOKIE 作为测试内容,标识为：security，开始位置为0，结束位置为9。
![](https://main.qcloudimg.com/raw/eb778e9f0416b1864763ff4471713725.png)
	- **配置项说明：**
**SESSION 位置 ：**可选择 COOKIE、GET 或 POST，SESSION 维度取值选项，其中 GET 或 POST 是指 HTTP 请求内容参数，非 HTTP 头部信息。
**匹配说明 ：**位置匹配或者字符串匹配。
**SESSION标识 ：**取值标识。
**开始位置：**字符串或者位置匹配的开始位置。
**结束位置：**字符串或者位置匹配的开始位置。
	- **GET/POST 示例 ：**
如果一条请求的完整参数内容为：key_a = 124&key_b = 456&key_c = 789。
字符串匹配模式下，SESSION 标识为 key_b = ，结束字符为&；则匹配内容为456。
位置匹配模式下，SESSION 标识为 key_b，开始位置为0，结束位置2；则匹配内容为456。
	- **COOKIE 示例 ：**
如果一条请求的完整 COOKIE 内容为：cookie_1 = 123;cookie_2 = 456;cookie_3 = 789。
字符串匹配模式下，SESSION 标识为 cookie_2 =，结束字符为;；则匹配内容为456。
位置匹配模式下，SESSION 标识为 cookie_2，开始位置为0，结束位置2；则匹配内容为456。<br> SESSION 维度信息测试。添加完成后，单击【测试】填写将内容进行测试。
![](https://main.qcloudimg.com/raw/609ec01219b193df419be772490b7145.png)
根据步骤1中添加的信息，设置内容为 security = 0123456789……。
![](https://main.qcloudimg.com/raw/4cf3e563d464dfe01e9ed535162f8ffb.png)
后继腾讯云 WAF 将把 security 后面10位字符串作为 SESSION 标识。SESSION 信息也可以删除重新配置。

3. 设置基于 SESSION 的 CC 防护策略，配置过程和示例一保持一致，识别模式选择 SESSION 即可。
![](https://main.qcloudimg.com/raw/682b86ed46276e6cf32e5c76734e7363.png)
配置完成，基于 SESSION 的防护 CC 防护策略生效。
>!使用 SESSION CC 防护机制，无法在 IP 封堵状态中查看封堵信息。

[上一步：DNS 劫持检测](/document/product/627/11708)
[下一步：网页防篡改](/document/product/627/11710)
