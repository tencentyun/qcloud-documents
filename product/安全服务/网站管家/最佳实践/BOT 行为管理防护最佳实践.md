## 功能介绍
通过 BOT 与业务安全，用户可以根据 BOT 管理中开启并配置对应模块内容 ，并结合 BOT 流量分析与访问日志结合进行观察和分析，根据流量分析提供的会话状态信息进行精细化策略设置，保护网站核心接口和业务的免受 BOT 侵害。BOT 管理设置支持配置客户端风险识别（前端对抗）、威胁情报、AI 评估、智能统计、动作分数、自定义规则、Token 配置、合法爬虫模块，通过配置这些模块，实现对 BOT 的精细化管理。
![](https://qcloudimg.tencent-cloud.cn/raw/ac5f30f9f132a410f60de85502fc3e34.png)

## 开启 BOT流量开关
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**，进入 BOT 与业务安全页面。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击 BOT 管理规则的![](https://qcloudimg.tencent-cloud.cn/raw/6e747bb146cfb582a01183e250330c90.png)，开启 BOT流量开关。
![](https://qcloudimg.tencent-cloud.cn/raw/ebf95eb82bfb4b6f66682fc20faae5ee.png)

## 客户端风险识别（前端对抗）
该功能通过客户端动态安全验证技术，对业务请求的每个客户端生成唯一 ID，检测客户端对 Web 或 H5 页面访问中可能存在机器人和恶意爬虫行为，保护网站业务安全。

本功能**不支持 CLB-WAF，泛域名，以及 App/小程序**，只适用与 Web或 H5 页面，如果有非动态认证，自动化接口脚本需要优先加入白名单。

### 白名单
白名单主要用于对不需要进行设置的接口放行处理。

1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击 **BOT 管理** 。
![](https://qcloudimg.tencent-cloud.cn/raw/6ebbdba50530929ed734fc9743584008.png)
2. 在 BOT 管理页面，单击前端对抗模块的**前往配置**。
3. 在前端对抗页面，单击**添加规则**，弹出添加白名单规则窗口。
![](https://qcloudimg.tencent-cloud.cn/raw/d2627419e930838cfe569b20a7d2bb05.png)
4. 在添加白名单规则窗口中，配置相关参数，单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/ffee9c1a69fe9e400dbd5de8684f85a6.png)

#### 案例一：大量机器自动化脚本请求服务
有大量机器自动化脚本请求服务，禁止类似 CURL，SOAPUI、JMETER、POSTMAN 访问请求。

1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击 **BOT 管理** 。
![](https://qcloudimg.tencent-cloud.cn/raw/6ebbdba50530929ed734fc9743584008.png)
2. 在 BOT 管理页面，单击前端对抗模块的**前往配置**。
3. 在前端对抗页面，单击**编辑**添加防护路径，单击**确定**。
>?指定需要进行防护的路径，匹配方式为前缀匹配，如果配置为：/bot/ ，表示对bot目录防护。支持配置多条路径，最多支持5条。
>
![](https://qcloudimg.tencent-cloud.cn/raw/0766092eb730017620ff7ea9f40dccc9.png)
4. 单击自动化工具识别的![](https://qcloudimg.tencent-cloud.cn/raw/5be282efe2247c29686330d3810c4acc.png)，防护模式选择**拦截**，确认白名单后，单击开关处的![](https://qcloudimg.tencent-cloud.cn/raw/99326315cbc21ef07cd7ff7fdb054284.png)，开启前端对抗功能。
![](https://qcloudimg.tencent-cloud.cn/raw/3adfe2d772ecb2a5a4b959e2688eb0a2.png)

#### 案例二：禁止网页调试
不允许用户打开网页调试，避免针对性爬虫编写。
