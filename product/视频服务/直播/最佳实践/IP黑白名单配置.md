通过 IP 黑白名单配置自定义 IP 黑/白名单及规则和内容，通过请求 IP 对请求进行过滤，实现访问限制，保护直播内容。

## 配置原理
- 配置 IP **白名单**：只有配置的 IP 地址能够访问当前直播内容。
- 配置 IP **黑名单**：只有配置的 IP 地址无法访问当前直播内容。

## 前提条件
- 已开通云直播服务，并登录 [云直播控制台](https://console.cloud.tencent.com/live/livestat)。
- 已添加 [播放域名](https://cloud.tencent.com/document/product/267/20381)。

[](id:set)
## 配置 IP 黑白名单
1. 选择 [域名管理](https://console.cloud.tencent.com/live/domainmanage)，单击需要配置 IP 黑名单的**播放域名**或右侧的**管理**，进入域名管理页。
2. 在**访问控制** > **IP 黑名单配置**中，可选择开启或关闭 IP 黑白名单配置。
![](https://qcloudimg.tencent-cloud.cn/raw/ecac632e3c11e9ad97413d91e63eccc2.png)
3. 单击![](https://qcloudimg.tencent-cloud.cn/raw/b64d8a4343b3a1e340db3adb9002db60.png)按钮，选择开启 IP 黑白名单，并进行如下配置：
![](https://qcloudimg.tencent-cloud.cn/raw/f3e2c63fa37fad855d1c6d1962f87114.png)
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>鉴权类型</td>
<td>单击选择配置 IP 白名单或黑名单：<ul style="margin:0">
<li>白名单和黑名单互斥，同一时间仅可生效一种。</li>
<li>若配置了 IP 白名单，则允许白名单内的 IP 地址访问，可请求到直播内容；拒绝白名单外的 IP 地址访问，无法请求直播内容。</li>
<li>若配置了 IP 黑名单，则拒绝黑名单内的 IP 地址访问，无法请求直播内容；允许黑名单外的 IP 地址访问，可请求到直播内容。</li></ul></td>
</tr><tr>
<td>IP 名单</td>
<td>最多支持配置200条规则，请使用换行符分隔。<ul style="margin:0">
<li>支持 IP 及网段格式（/8/16/24），不支持 IP ：端口格式。</li>
<li>暂不支持 IP v6</li>
<li>若规则内容为空时，则表示 IP 黑白名单均未配置</li></ul></td>
</tr>
</tbody></table>
4.单击**保存**即可保存配置，配置需要一定时间才可生效。
![](https://qcloudimg.tencent-cloud.cn/raw/aa7e017cfb6f01e9c7596c4d404e636a.png)

[](id:change)
## 修改 IP 黑白名单
1. 选择 [域名管理](https://console.cloud.tencent.com/live/domainmanage)，单击需修改 IP 黑白名单配置的 **播放域名** 或右侧的 **管理** ，进入域名管理页。
2. 在**访问控制** > **IP 黑白名单配置**中，单击**编辑**进入 IP 黑白名单配置页。
3. 根据您的实际需求修改配置项信息，单击**保存**即可完成修改。
![](https://qcloudimg.tencent-cloud.cn/raw/baa5efd5c827a8d5273711d99b354675.png)

[](id:close)
## 关闭 IP 黑白名单
开启 IP 黑白名单后，若您需关闭此功能，具体操作如下：
1.选择 [域名管理](https://console.cloud.tencent.com/live/domainmanage)，单击需关闭 IP 黑白名单配置的**播放域名**或右侧的**管理**，进入域名管理页。
2.在**访问控制> IP 黑白名单配置**中，单击**编辑**进入 IP 黑白名单配置页。
3.单击![img](https://main.qcloudimg.com/raw/e72f89a0deb6858428dc3e93ce7e7088.png)按钮，选择关闭 IP 黑白名单。
![](https://qcloudimg.tencent-cloud.cn/raw/c47a203613d62dc339431e50d22438ad.png)
