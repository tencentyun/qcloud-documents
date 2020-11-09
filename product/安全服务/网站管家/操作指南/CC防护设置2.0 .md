## 功能简介
CC 防护对网站特定的 URL 进行访问保护，CC 防护2.0全新改版，支持紧急模式 CC 防护和自定义 CC 防护策略。紧急模式 CC 防护，综合源站异常响应情况（超时、响应延迟）和网站历史访问大数据分析，紧急模式决策生成防御策略，实时拦截高频访问请求。自定义 CC 防护可以根据用户访问源 IP 或者 SESSION 频率制定防护规则，对访问进行处置，处置措施包括告警、人机识别和阻断。
>!
- 紧急模式 CC 防护策略和自定义 CC 规则防护策略，不能同时开启。
- 使用基于 SESSION 的 CC 防护策略，需要先进行 SESSION 设置，才能设置基于 SESSION 的 CC 防护策略。
- 如果您使用的 Web 应用防火墙版本不支持 CC 防护设置2.0，请您参考 [旧版 CC 防护设置](https://cloud.tencent.com/document/product/627/35525) 进行配置。

## 配置步骤
#### **示例一：紧急模式 CC 防护配置**
紧急模式 CC 防护默认关闭，开启前请确认自定义 CC 防护规则处于未启用状态。

1. 进入 [ Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 应用防火墙】>【防护设置】，进入防护设置页面，在域名列表中，找到需要防护的域名，单击【防护配置】进入配置页面。
![](https://main.qcloudimg.com/raw/9be71efc16d6a472dfd7590b6ae11763.png)
2. 单击【CC 防护设置2.0】，进行紧急模式 CC 防护配置。
![](https://main.qcloudimg.com/raw/f0da1e170b1376e6213d10d988a49a2b.png)
**配置项说明：**
**状态开关：** 当开启紧急模式 CC 防护时，若网站遭大流量 CC 攻击会自动触发防护（网站 QPS 不低于1000QPS），无需人工参与。若无明确的防护路径，建议启用紧急模式 CC 防护，可能会存在一定误报。可以在控制台进入 [IP管理-IP封堵状态](https://console.cloud.tencent.com/guanjia/ip/record)，查看拦截 IP 信息，并及时处理。
>? 如果知晓明确的防护路径，建议使用自定义 CC 规则进行防护。

#### **示例二： 基于访问源 IP 的 CC 防护设置**
基于 IP 的 CC 防护策略，不需要对 SESSION 维度进行设置，直接配置即可。
1. 进入 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 应用防火墙】>【防护设置】，进入防护设置页面，在域名列表中，找到需要防护的域名，单击【防护配置】进入配置页面。
![](https://main.qcloudimg.com/raw/9be71efc16d6a472dfd7590b6ae11763.png)
2. 单击【CC 防护设置2.0】进行 CC 规则配置，单击【添加规则】填写相应信息。
![](https://main.qcloudimg.com/raw/587d2e546abf2809d12023fe54639495.png)
3. 进入添加 CC 防护规则页面，填写相应信息。
<img src="https://main.qcloudimg.com/raw/2488202ce1c74df0c7fd9728ffb3627f.png" style="zoom:80%;" /><br>
**配置项说明：**
 - **识别模式：** IP、SESSION。
 - **匹配条件：** 包括相等、前缀匹配和包含。
 - **高级匹配：**通过进行 GET 表单和 POST 表单参数过滤，支持更加精细化频率控制，提高命中率。
	 - **匹配字段**：指定请求方法，支持 GET 或 POST。
	 - **参数名**：请求字段中的参数名，最多512字符。
	 - **参数值**：请求字段中的参数值，最多512字符。
	 **示例说明**：如下三条 GET 请求测试数据：a=1&b=11、a=2&b=12、 a=&b=13。
		- 如果 GET 配置参数名为 a，参数值为1，则1命中。
		- 如果 GET 配置参数名为 a，参数值为\*，则1、2、3均命中。
 - **访问频次：**根据业务情况设置访问频次。建议输入正常访问次数的3倍 - 10倍，例如，网站人平均访问20次/分钟，可配置为60次/分钟 - 200次/分钟，可依据被攻击严重程度调整。
 - **执行动作：**观察、人机识别和阻断。
 - **惩罚时长：**最短为1分钟，最长为一周。
 - **优先级：**请输入1 - 100的整数，数字越小，代表这条规则的执行优先级越高，相同优先级下，创建时间越晚，优先级越高。
4. 规则操作，选择已经创建的规则，可以对规则进行关闭、修改和删除。
![](https://main.qcloudimg.com/raw/5e6f39af9efcce9fd09c670c34db78ea.png)
5. 根据规则设置，触发 CC 攻击行为。
![](https://main.qcloudimg.com/raw/46867af97968b3ddd28b96645d9e91ae.png)
6. 查看 IP 实时阻断信息。在左侧导航栏，选择【IP 管理】>【IP 封堵状态】 ，可以查看实时阻断的 IP 信息 ,并对 IP 进行加白或者加黑处理。

#### **示例三： 基于 SESSION 的 CC 防护设置**
基于 SESSION 访问速率的 CC 防护，能够有效解决在办公网、商超和公共 WIFI 场合，用户因使用相同 IP 出口而导致的误拦截问题。
1. 进入 [ Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 应用防火墙】>【防护设置】，进入防护设置页面，在域名列表中，找到需要防护的域名，单击【防护配置】进入配置页面。
![](https://main.qcloudimg.com/raw/9f30721ac5c501c07935833eeb364417.png)
2. 选择【CC 防护设置2.0】>【设置】，设置 SESSION 维度信息。
![](https://main.qcloudimg.com/raw/a9bbf8a68bdd04f6bb66b97081ffb86e.png)
3. 进入 SESSION 设置页面，此示例选择 COOKIE 作为测试内容，标识为 security，开始位置为0，结束位置为9，配置完成后单击【设置】。
![](https://main.qcloudimg.com/raw/eb778e9f0416b1864763ff4471713725.png)
 - **配置项说明：**
 - **SESSION 位置 ：**可选择 COOKIE、GET 或 POST，其中 GET 或 POST 是指 HTTP 请求内容参数，非 HTTP 头部信息。
 - **匹配说明 ：**位置匹配或者字符串匹配。
 - **SESSION 标识 ：**取值标识。
 - **开始位置：**字符串或者位置匹配的开始位置。
 - **结束位置：**字符串或位置匹配的结束位置。
 - **GET/POST 示例 ：**
如果一条请求的完整参数内容为：key_a = 124&key_b = 456&key_c = 789。
 - 字符串匹配模式下，SESSION 标识为 key_b = ，结束字符为&，则匹配内容为456。
 - 位置匹配模式下，SESSION 标识为 key_b，开始位置为0，结束位置2，则匹配内容为456。
 - **COOKIE 示例 ：**
如果一条请求的完整 COOKIE 内容为：cookie_1 = 123;cookie_2 = 456;cookie_3 = 789。
 - 字符串匹配模式下，SESSION 标识为 cookie_2 =，结束字符为“;”，则匹配内容为456。
 - 位置匹配模式下，SESSION 标识为 cookie_2，开始位置为0，结束位置2，则匹配内容为456。

4. SESSION 维度信息测试。添加完成后，单击【测试】将填写内容进行测试。。
![](https://main.qcloudimg.com/raw/1eddcdb937b9e529167d24c98ca904d4.png)
5. 进入 SESSION 设置页面，设置内容为 security = 0123456789……，后继 Web 应用防火墙将把 security 后面10位字符串作为 SESSION 标识，SESSION 信息也可以删除重新配置。
![](https://main.qcloudimg.com/raw/bf87f5f7037e7758d8c281151852ad70.png)
6. 设置基于 SESSION 的 CC 防护策略，配置过程和示例一保持一致，识别模式选择 SESSION 即可。
![](https://main.qcloudimg.com/raw/9e8ec2f34900d53081cf881f8a902327.png)
7. 配置完成，基于 SESSION 的 CC 防护策略生效。
>!使用基于 SESSION 的 CC 防护机制，无法在 IP 封堵状态中查看封堵信息。

[上一步：DNS 劫持检测](/document/product/627/11708)
[下一步：网页防篡改](/document/product/627/11710)
