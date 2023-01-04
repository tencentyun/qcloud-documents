本文为您介绍 BOT 流量管理的 AI策略模块。该功能依托腾讯近二十年的网络安全经验和 BOT 对抗经验，基于人工智能技术和腾讯风控实战沉淀，将风控特征和黑灰产对抗经验转化为 AI策略模型，快速识别恶意访问者。快速识别并处置来自 BOT 对抗经验积累的 BOT、高级持续威胁 BOT、分布式 BOT。

## 前提条件
购买  Web 应用防火墙及 [BOT 流量管理拓展包](https://cloud.tencent.com/document/product/627/11730#bot-.E8.A1.8C.E4.B8.BA.E7.AE.A1.E7.90.86.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E)，并且打开已接入 WAF 域名 BOT 规则管理开关。

## 防护配置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击**BOT 管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/642d93faac4b01d62cf0b84583318040.png)
3. 在全局设置中，单击AI策略模块的**前往配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/f2ad16fadb337da7c43d3360c20c1dc4.png)
4. 在发现 AI 检出误报时，可以单击**添加白名单**定向加白特定的 URL 检出，减少误报。
![](https://qcloudimg.tencent-cloud.cn/raw/a0882d4f943de70e62e0b4f60f31d933.png)
5. 在AI 策略页面中，可加白相关 URL 白名单，避免核心业务/回调业务的访问频次过多造成核心业务异常拦截，可增加对应 URL 的 AI 策略白名单，避免误拦截。
>?此处 AI 策略白名单仅影响 AI 策略模块，不影响其他模块的正常检出。
>
![](https://qcloudimg.tencent-cloud.cn/raw/b5704d015b77ef8e59971fbeab8e943f.png)
   **参数说明：**
   - **策略名称**： 策略的名称。
   - **规则描述**：策略的描述。
   - **加白 URL**：AI 策略的加白路径，影响 AI策略的得分结果。
   - **规则开关**： AI 策略白名单的开关，开启状态时，当前 AI策略白名单生效，在 URL 命中 AI策略白名单时，AI策略将不增加其分数，其 BOT 评估分值由威胁情报、智能统计进行提供。
6. 配置完成 AI 策略相关配置之后，在场景化管理中，选择目标场景，单击右侧的**查看配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/b82861df9363c2a0f46a3a1f7b645079.png)
7. 在场景详情页面，单击 AI 策略模块的![](https://qcloudimg.tencent-cloud.cn/raw/c9174793080a26017ba65359b80ddde0.png)，即可针对该场景开启 AI 策略模块。
![](https://qcloudimg.tencent-cloud.cn/raw/f8ace57ad5d5a8d5b7d1641e6dbc3739.png)

## AI 策略最佳实践
AI 策略基于 BOT 对抗历史经验以及 BOT 攻防实验室运营经验，可快速发现通用 BOT 以及高级持续威胁 BOT， 因此建议在任何情况下开启 AI 策略，并且AI 策略白名单中加白来自业务回调接口。
