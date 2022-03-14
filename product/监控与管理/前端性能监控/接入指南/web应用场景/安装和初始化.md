支持 CDN 和 NPM 两种方式安装 SDK 。


## 以 CDN 方式安装并初始化 SDK
1. 在 HTML 页面的`<head></head>`标签中引入下列代码。
<dx-codeblock>
::: html
<script src="https://cdn-go.cn/aegis/aegis-sdk/latest/aegis.min.js"></script>
:::
</dx-codeblock>
2. 参考下列步骤新建一个 Aegis 实例，传入相应的配置，初始化 SDK 。
<dx-codeblock>
:::  javascript
const aegis = new Aegis({
    id: 'XaKVn5BzYalQMRyjbO', // 应用ID，即上报key
    uin: 'xxx', // 用户唯一 ID（可选）
    reportApiSpeed: true, // 接口测速
    reportAssetSpeed: true, // 静态资源测速
    spa: true // spa 应用页面跳转的时候开启 pv 计算
});
:::
</dx-codeblock>

## 以 NPM 方式安装并初始化 SDK


1. 执行下列命令，在 npm 仓库安装 aegis-web-sdk。
 <dx-codeblock>
::: Linux
$ npm install --save aegis-web-sdk
:::
</dx-codeblock>
2. 参考下列步骤新建一个 Aegis 实例，传入相应的配置，初始化 SDK 。
<dx-codeblock>
:::  javascript
import Aegis from 'aegis-web-sdk';

const aegis = new Aegis({
    id: 'XaKVn5BzYalQMRyjbO', // 应用ID，即上报key
    uin: 'xxx', // 用户唯一 ID（可选）
    reportApiSpeed: true, // 接口测速
    reportAssetSpeed: true, // 静态资源测速
    spa: true // spa 应用页面跳转的时候开启 pv 计算
})
:::
</dx-codeblock>

>?为了不遗漏数据，须尽早进行初始化。当您完成安装并初始化 SDK 之后，可以开始使用前端性能监控提供的以下功能：
>
>- 错误监控：JS 执行错误、Promise 错误、Ajax 请求异常、资源加载失败、返回码异常、PV 上报、白名单检测等。  
>- 测速功能：页面性能测速、接口测速、静态资源测速。
>- 数据统计和分析：可在 [数据总览](https://console.cloud.tencent.com/rum/web) 上进行各个维度的数据分析。
