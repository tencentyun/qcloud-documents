
本文档将为您介绍 Web 应用防火墙（WAF）攻击 IP 惩罚功能，可以快速拦截恶意 Web 攻击 IP ，快速反应应对恶意扫描及代理，Web 攻击威胁等行为，可提升攻防对抗效率。
## 背景信息
攻击 IP 惩罚：自动阻断在短时间内发起多次 Web 攻击（规则引擎触发）的客户端 IP，一段时间内阻止所有请求，阻断日志可以在 [攻击日志](https://cloud.tencent.com/document/product/627/50995) 中查看。

## 前提条件
- 您已经 [购买 Web 应用防火墙套餐](https://buy.cloud.tencent.com/buy/waf)，完成防护域名添加，域名处于正常防护状态。
- 情报 IP 封禁当前处于灰度阶段，如需试用请 [联系我们](https://cloud.tencent.com/act/event/connect-service) 进行开通。在灰度期间您可以免费使用，正式发布后，将按官网公布刊例价正常收取费用。

## 操作步骤
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia)，在左侧导航栏中，选择【IP 管理】>【IP 封禁管理】，进入封禁管理页面。
2. 在封禁管理页面上方，对攻击 IP 惩罚进行设置。
![](https://main.qcloudimg.com/raw/4c81cf6cd4bca6f6d63e49967b981002.png)
字段和操作说明：
 - **封禁开关**：开启关闭攻击 IP 惩罚模块，默认关闭。
 - **Web 攻击次数**：统计攻击源 IP 在指定时间内触发 Web 攻击（规则引擎触发，不包括 AI 引擎、自定义策略、CC 攻击等模块）的次数，默认为：20次。
 - **检测时长**：指定统计攻击源 IP 检测时长，默认检测时长为：20分钟。
 - **封禁时间**：封禁该IP的请求时长，默认封禁时间为：20分钟。
 - **操作**：在攻击 IP 惩罚模块右上角，单击【设置】，可对默认参数进行修改。
![](https://main.qcloudimg.com/raw/b58180ac2bbaac049bc4c23cbd15b9d7.png)
