要使用 MTA 广告效果监测与分析，您需要先在 App中集成 MTA 的 SDK，集成步骤如下：
1. 集成 MTA 的基础 SDK （[Android快速集成入口](/document/product/549/12862) | [iOS快速集成入口](/document/product/549/12857)），如果您已集成过 MTA 的基础 SDK ，可跳过该步骤；
2. 集成广告监测模块（[Android集成代码](/document/product/549/15007) | [iOS集成代码](/document/product/549/15009)），并上报广告监测标准事件；
3. 若您的推广目标是 H5 页面（简称“落地页”），最终通过落地页下载应用统计，您可以在落地页嵌入 MTA 的 JS 代码，可以做到一个落地页多渠道、多平台的统计，适用于微信内、分享、地推、二维码等各场景（[Android集成配置](/document/product/549/15006) | [iOS集成配置](/document/product/549/15008) | [落地页多渠道多平台配置](/document/product/549/15010)）
