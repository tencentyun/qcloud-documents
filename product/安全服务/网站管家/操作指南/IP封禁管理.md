本文档将为您介绍 Web 应用防火墙（WAF）攻击 IP 惩罚功能，可以快速拦截恶意 Web 攻击 IP ，快速反应应对恶意扫描及代理，Web 攻击威胁等行为，可提升攻防对抗效率。
## 背景信息
攻击 IP 惩罚：自动阻断在短时间内发起多次 Web 攻击（规则引擎触发）的客户端 IP，一段时间内阻止所有请求，阻断日志可以在 [攻击日志](https://cloud.tencent.com/document/product/627/50995) 中查看。

## 前提条件
- 您已经 [购买 Web 应用防火墙套餐](https://buy.cloud.tencent.com/buy/waf)，完成防护域名添加，域名处于正常防护状态。
- 情报 IP 封禁当前处于灰度阶段，如需试用请 [联系我们](https://cloud.tencent.com/act/event/connect-service) 进行开通。在灰度期间您可以免费使用，正式发布后，将按官网公布刊例价正常收取费用。

## 操作步骤
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia)，在左侧导航栏中，选择**基础安全** > **WEB 安全**。
2. 在 WEB 安全页面，单击 IP封禁左侧的![](https://qcloudimg.tencent-cloud.cn/raw/08734b1e9842d5856880e145b4e10e61.png)，开启 IP 封禁开关。
>? 封禁开关：开启关闭攻击 IP 惩罚模块，默认关闭。
>
![](https://qcloudimg.tencent-cloud.cn/raw/400b89d5126fde55ecb86a209ee5dd0f.png)
3. 在 WEB 安全页面，单击 IP封禁右侧的![](https://qcloudimg.tencent-cloud.cn/raw/713476d527e22308e1774364cdec868d.png)，对攻击 IP 惩罚进行设置，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/17a0bed9655b59c4eabadd1c02800960.png)
**字段说明：**
 - Web 攻击次数：统计攻击源 IP 在指定时间内触发 Web 攻击（规则引擎触发，不包括 AI 引擎、自定义策略、CC 攻击等模块）的次数，默认为：20次。
 - 检测时长：指定统计攻击源 IP 检测时长，默认检测时长为：20分钟。
 - 封禁时间：封禁该IP的请求时长，默认封禁时间为：20分钟。
 
