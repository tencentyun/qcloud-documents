本文为您介绍 BOT 行为管理的 AI 评估中 AI 评估模块的功能设置。该功能依托腾讯近二十年的网络安全经验和 BOT 对抗经验，基于人工智能技术和腾讯风控实战沉淀，将风控特征和黑灰产对抗经验转化为 AI 评估模型，快速识别恶意访问者。快速识别并处置来自 BOT 对抗经验积累的 BOT、高级持续威胁 BOT、分布式 BOT。

## 前提条件
购买  Web 应用防火墙及[ BOT 行为管理拓展包](https://cloud.tencent.com/document/product/627/11730#bot-.E8.A1.8C.E4.B8.BA.E7.AE.A1.E7.90.86.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E)，并且打开已接入 WAF 域名 BOT 分析开关。

## 防护配置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击 **BOT 管理** 。
![](https://qcloudimg.tencent-cloud.cn/raw/6ebbdba50530929ed734fc9743584008.png)
3. 在 BOT 管理页面，单击 AI 评估模块的![](https://qcloudimg.tencent-cloud.cn/raw/25ee88daf408bcac2a80287e314e669c.png)，即可开启 AI 评估模块。
![](https://qcloudimg.tencent-cloud.cn/raw/0218d3e6eb5c3f457e4def9bc3c029b4.png)
4. 在发现 AI 检出误报时，可以单击**添加白名单**定向加白特定的 URL 检出，减少误报。
![](https://qcloudimg.tencent-cloud.cn/raw/2bd80682ad084198ff765c18e78de0bb.png)
5. 在 AI 评估页面中，可加白相关 URL 白名单，避免核心业务/回调业务的访问频次过多造成核心业务异常拦截，可增加对应 URL 的 AI 评估白名单，避免误拦截。
>?此处 AI 评估白名单仅影响 AI 评估模块，不影响其他模块的正常检出。
>
![](https://qcloudimg.tencent-cloud.cn/raw/b5704d015b77ef8e59971fbeab8e943f.png)
   **参数说明：**
   - 策略名称： 该策略的名称，不影响 AI评 估结果。
   - 规则描述：该策略的描述，不影响 AI 评估结果。
   - 加白 URL：AI 评估的加白路径，影响 AI 评估的得分结果。
   - 规则开关： 可以控制当条 AI 评估白名单的开关，开启状态时，当前 AI 评估白名单生效，在 URL 命中 AI 评估白名单时，AI 评估将不增加其分数，其 BOT 评估分值由威胁情报、智能统计进行提供。


## AI评估最佳实践
由于 AI 评估通过 BOT 对抗历史经验积累以及 BOT 攻防实验室相互积累运营，可快速发现通用 BOT 以及 高级持续威胁 BOT， 因此建议在任何情况下开启 AI 评估，并且 AI 评估白名单中加白来自业务回调接口。

