## 注意事项
- 小程序仅支持 NPM 方式安装 SDK 。
- 本 SDK 支持微信小程序和 QQ 小程序。

> ?aegis-sdk 默认使用 `aegis.qq.com` 作为上报域名，您也可以选择使用 `tamaegis.com` 作为上报域名。

>! 正式环境接入小程序需要将上报域名添加到安全域名中。

## 安装 SDK

执行下列命令，在 npm 仓库安装 aegis-mp-sdk。
<dx-codeblock>
::: Linux
$ npm install --save aegis-mp-sdk
:::
</dx-codeblock>

## 初始化

参考下列步骤新建一个 Aegis 实例，传入相应的配置，初始化 SDK

<dx-codeblock>
::: Linux
import Aegis from 'aegis-mp-sdk';

const aegis = new Aegis({
  id: "pGUVFTCZyewxxxxx", // 项目key
  uin: 'xxx', // 用户唯一 ID（可选）
  reportApiSpeed: true, // 接口测速
  spa: true, // 页面切换的时候上报 pv
});
:::
</dx-codeblock>

> ?为了不遗漏数据，须尽早进行初始化。如果您的小程序项目中使用了 `miniprogram-api-promise` 来封装 `wx.request` 请求，需要注意：由于我们是通过重写 `wx.request` 来进行接口监控的，所以需要您将初始化 Aegis 放在引入这个包之前执行，否则可能会导致接口信息无法完整收集。
> 当您完成安装并初始化 SDK 之后，可以开始使用前端性能监控提供的以下功能：
>
> 1. 错误监控：JS执行错误。  
> 2. 测速功能：接口测速。
> 3. 数据统计和分析：可在前端性能监控控制台 [**数据总览**](https://console.cloud.tencent.com/rum/web) 页面上进行各个维度的数据分析。


