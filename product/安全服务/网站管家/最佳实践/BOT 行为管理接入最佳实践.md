本文将为您如何接入 BOT 行为管理，以及日常运营对抗恶意流量的最佳实践。方便您快速进行相关业务接入 BOT 行为管理，快速识别并对抗恶意流量。

## 前提条件
BOT 行为管理需要购买 WAF [对应实例的扩展包](https://cloud.tencent.com/document/product/627/11730#.E6.89.A9.E5.B1.95.E5.8C.85.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E)。
>?WAF 企业版、旗舰版用户当前可免费试用新版本的 BOT 行为管理功能，以观察网站受 BOT 影响的情况。

## 解析验证码
当客户端类型为 App、小程序、客户端以及跨域调用时，由于无法解析识别来自 WAF 下发的验证码，导致 BOT 行为管理在下发人机识别动作时，无法正常解析及弹出人机识别验证码，用户便无法正常进行人机识别交互，在触发多次验证码后，造成正常用户的访问请求被拦截，导致业务受损。

因此，在配置处置动作为人机识别时，需要对前端/客户端业务进行针对性改造，使其可以适配相关验证码，相关改造文档可参见 [前后端分离站点接入 WAF 验证码](https://cloud.tencent.com/document/product/627/68386)。

## 通用业务接入业务
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**配置中心** > **BOT 与业务安全**，进入 BOT 与业务安全页面。
2. 在 BOT 与业务安全页面，左上角选择需要防护的域名，单击 **BOT 管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/a902a359eab9987bf9d232ea59e5e239.png)

### 开启 BOT流量分析开关
在 BOT 管理页面，单击规则概览的![](https://qcloudimg.tencent-cloud.cn/raw/180f2bd28c577185924e76f8a19396fe.png)，即可开启 BOT 流量分析。
![](https://qcloudimg.tencent-cloud.cn/raw/33811d103768d7a431f35b5761623aba.png)

### 设置前端对抗
1. 在 BOT 管理页面的前端对抗模块，单击![](https://qcloudimg.tencent-cloud.cn/raw/180f2bd28c577185924e76f8a19396fe.png)开启前端对抗分析开关。
>!
>- 确认当前访问客户端类型：公众号/H5、APP、小程序、客户端。
>- 当客户端类型有且仅有浏览器/公众号/H5 并且跨域调度时，开启前端对抗，以达到最佳的防护效果。
>- 开启前端对抗后，访问前端对抗保护路径将会校验客户端是否有 JavaScripts 解析能力，会下发一段 JavaScripts 代码作为验证当前客户端是否为真实浏览器。小程序、APP、以及 API 调用由于不会主动解析 WAF上下发的质询功能，会导致客户端无法正常解析。
>
 ![](https://qcloudimg.tencent-cloud.cn/raw/703aa95d487aa7127aa61f5ad914fa5d.png)
2. 在前端对抗模块，单击**前往设置**，对重点页面进行防护配置。
>?更多操作详情请参见 [BOT 管理 ](https://cloud.tencent.com/document/product/627/65688)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/34e0950fcf435f869db31a96c25721e4.png)
### 设置威胁情报
1. 在 BOT 管理页面的威胁情报模块，单击![](https://qcloudimg.tencent-cloud.cn/raw/f3f8be1cf90fd16cb762064d1bc2bf57.png)，即可开启威胁情报模块。初次开启威胁情报开关将会开启所有识别项，开启对应识别项后可识别来自威胁情报、IDC 的访问源。并提供不同的恶意程度。
![](https://qcloudimg.tencent-cloud.cn/raw/82874ee48b9ddf18339694a99d39ca4c.png)
2. 在威胁情报模块，单击**前往配置**，设置 IDC 网络和威胁情报库开关。
>?当前业务存在业务回调接口在 IDC 域内：
 - 如果不清楚来源 IP，请 [联系我们](https://cloud.tencent.com/online-service) 对 IDC 进行加白处理，即关闭对应威胁情报中对应业务 IDC 的选项。
 - 如果清楚当前回调业务的 IP，请在 BOT-自定义规则处加白对应来源 IP，详情请参见 [精准白名单管理](https://cloud.tencent.com/document/product/627/64382)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/595fec5e97baf92bf1f787028e70bf0e.png)
### 开启 AI 评估开关
 在 BOT 管理页面的 AI 评估模块，单击![](https://qcloudimg.tencent-cloud.cn/raw/25ee88daf408bcac2a80287e314e669c.png)，即可开启 AI 评估模块。
![](https://qcloudimg.tencent-cloud.cn/raw/0218d3e6eb5c3f457e4def9bc3c029b4.png)

### 开启智能统计开关
在 BOT 管理页面的智能统计模块，单击智能统计模块的![](https://qcloudimg.tencent-cloud.cn/raw/f05a86c4176526c2846a61f2a2207a37.png)，即可开启智能统计模块。
![](https://qcloudimg.tencent-cloud.cn/raw/c371efa02e59ba380c1e715b60d592b0.png)

### 设置动作得分
1. 在 BOT 管理页面的动作设置模块，单击**配置动作得分**。
![](https://qcloudimg.tencent-cloud.cn/raw/d21ab846e4cb7836510bf2d650f98439.png)
2. 在动作设置页面，用户可根据配置不同分数段的动作实现风险访问的精准拦截。
![](https://qcloudimg.tencent-cloud.cn/raw/7d40fd4b7f95182a78368bc95b35edd1.png)
**使用说明**
 - **模式设置：** 提供宽松模式、中等模式、严格模式、自定义模式这四种默认处置模式，宽松、中等、严格这三种模式为预设模式，分别代表 BOT行为管理针对不同危害程度的 BOT 的推荐分类及处置策略。这三种预设模式可进行修改，修改后为自定义模式。
 - **分数段设置：**分数段区间总分数为 0-100 分，每个分数段总共可以添加10条，配置的分数区间范围左闭右开，分数段不可重合，分数区间可设置为空，设置为空时，空的分数段不处置动作。
 - **动作设置：**可设置为信任、监控、重定向（重定向至特定网站 URL）、人机识别（验证码）或拦截。
 - **标签设置：**可设置为友好 BOT、恶意 BOT、正常流量或疑似 BOT。
    - **友好 BOT：**为默认对网站友好/合法的 BOT。
    - **疑似 BOT：** 为识别出该访问源流量疑似为 BOT，但无法判断其对网站的是否为有害。
    - **正常流量：**为认为访问的流量为正常人类。
    - **恶意 BOT：**为对网站产生恶意流量/访问请求不友好的 BOT。
4. 设置完成后，单击界面左下方的**立即发布**，即可生效。
