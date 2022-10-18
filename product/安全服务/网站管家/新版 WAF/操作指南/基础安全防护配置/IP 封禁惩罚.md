Web 应用防火墙（WAF）提供 IP 封禁功能，可以快速拦截恶意攻击 Web 的 IP，快速应对恶意扫描及代理、Web 攻击威胁等行为，可提升攻防对抗效率。
>!当前 IP 封禁支持域名级区分封禁，不同域名检测时长不同，封禁时间也单独计算。

## 背景信息
IP 封禁指自动阻断在短时间内发起多次 Web 攻击（规则引擎触发）的客户端 IP，一段时间内阻止所有请求，阻断日志可以在 [攻击日志](https://cloud.tencent.com/document/product/627/50995) 中查看。

## 前提条件
- 已 [购买 Web 应用防火墙套餐](https://buy.cloud.tencent.com/buy/waf)。
- 完成防护域名添加，域名处于正常防护状态。操作详情请参见 [快速入门](https://cloud.tencent.com/document/product/627/18635)。

## 操作步骤
1.	登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-baseconfig)，在左侧导航栏中，选择**配置中心** > **基础安全** > **WEB 安全**，进入 WEB 安全页面。
2.	在 WEB 安全页面，左上角选择需要防护的域名，单击 IP 封禁处的![](https://qcloudimg.tencent-cloud.cn/raw/a8ff3435ae9b513144b2b56eb4bd04cc.png)，开启 IP 封禁。
![](https://qcloudimg.tencent-cloud.cn/raw/dbd53691fa00628b0ca82594243f2a31.png)
3. 在 WEB 安全页面，单击 IP 封禁处的![](https://qcloudimg.tencent-cloud.cn/raw/36d7cbd5a4d608136e4c77dff95f54dc.png)，对 IP 封禁的默认参数进行修改，单击**确定**即可根据业务情况设置阈值。
![](https://qcloudimg.tencent-cloud.cn/raw/a0577e9781e972ccedf69b338ee0cc78.png)
**字段说明：**
 - **Web 攻击次数：**统计攻击源 IP 在指定时间内触发 Web 攻击（规则引擎触发，不包括 AI 引擎、自定义策略、CC 攻击等模块）的次数。
 - **检测时长：**指定统计攻击源 IP 检测时长。
 - **封禁时间：**封禁该 IP 的请求时长。

