[负载均衡型 Web 应用防火墙（WAF）](https://cloud.tencent.com/document/product/627/17470) 通过域名和负载均衡监听器进行绑定，实现对经过负载均衡监听器的 HTTP 或 HTTPS 流量进行检测和拦截。本文档将介绍如何通过负载均衡型 WAF 为已经添加到负载均衡的域名进行 Web 安全防护。

## 前提条件
- 您已成功创建 HTTP 监听器或 HTTPS 监听器，并且域名可以正常访问。操作详情请参考 [负载均衡快速入门](https://cloud.tencent.com/document/product/214/8975)。
- 您已成功购买负载均衡型 WAF。购买方式请参考 [购买方式](https://cloud.tencent.com/document/product/627/47429)。若未购买，可选择 [7天免费试用](https://cloud.tencent.com/act/pro/clbwafenterprise) 负载均衡型 WAF。



## 操作步骤
<span id ="step1"></span>
### 步骤一：确认负载均衡域名配置
本文以防护`www.example.com`域名为例。
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏中，单击**实例管理**。
2. 在“实例管理”页面，选择所在地域，在实例列表中单击目标实例右侧“操作”列的**配置监听器**。
3. 在“监听器管理”页签的“HTTP/HTTPS 监听器”区域，单击目标监听器左侧的**+**查看域名详情。
![](https://main.qcloudimg.com/raw/7de3dbb7dd72f7034af8df684bab203a.png)
4. 确认负载均衡域名配置信息为：负载均衡实例的 ID 为“lb-f8lm****”，监听器的名称为“http-test”，监听器转发规则所监听的域名为`www.example.com`，域名防护状态为“未启用”（所有 ID、名称和域名以实际为准）。

### 步骤二：在 WAF 中添加域名绑定负载均衡
为了使负载均衡型 WAF 能够识别出需要防护的域名，需要在 WAF 中添加负载均衡监听的域名并绑定负载均衡监听器。
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/config)，在左侧导航栏选择**Web 应用防火墙** > **防护设置**。
2. 在“防护设置”页面，单击**负载均衡型**页签。
3. 在“负载均衡”页签，单击**添加域名**。
![](https://main.qcloudimg.com/raw/ccf617497520dbe27ca3f16116bb47b6.png)
4. 在“输入域名”页签，填写需要防护的域名，然后单击**下一步**。
![](https://main.qcloudimg.com/raw/78939fa33234907b355058eb3b45b8a3.png)
5. 在“选择监听器”页签，选择负载均衡对应地域，选择 <a href="#step1">步骤一：确认负载均衡域名配置</a> 中确认的负载均衡实例，单击**选择监听器**。
![](https://main.qcloudimg.com/raw/adb350dbc8bb95fec721c103a530c1b6.png)
6. 在弹出的“选择监听器”对话框，选择 <a href="#step1">步骤一：确认负载均衡域名配置</a> 中确认的负载均衡监听器，单击**确定**。
![](https://main.qcloudimg.com/raw/55378a1cba30abfbb405a43996345233.png)
7. 返回“选择监听器”页签，单击**完成**，完成 WAF 域名和负载均衡监听器的绑定。
8. 返回“域名列表”页面，确认域名、区域、所绑定的负载均衡实例 ID 和监听器等信息正确无误。

### 步骤三：结果验证
1. 参考 <a href="#step1">步骤一：确认负载均衡域名配置</a> 的操作步骤，在“监听器管理”页签，查看域名防护状态为“开启”，流量模式为“镜像模式”，表示域名防护已开启。
 -  若您的域名未配置 DNS 解析，则可参考 WAF 快速入门的 [步骤2：本地测试](https://cloud.tencent.com/document/product/627/18632) 验证 WAF 防护是否生效。
 -  若您的域名已配置 DNS 解析，则可按照以下步骤验证 WAF 防护是否生效。
2. 在浏览器中输入并访问`http://www.example.com/?test=alert(123)`地址。
3. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/config)，在左侧导航栏选择**日志服务** > **攻击日志**。
4. 在“日志查询”页签，选择添加防护的域名`www.example.com`，单击**查询**。若日志列表中出现攻击类型为“XSS攻击”的日志，则表示 WAF 对负载均衡中配置的域名防护已生效。
![](https://main.qcloudimg.com/raw/a83c70cd6fee8acbe4a1889334ef22ac.png)

