通过 Referer 防盗链配置自定义 Referer 黑/白名单及规则内容，允许或拒绝播放请求，保护直播内容；同时云直播支持用户选择是否允许空 Referer 访问。

## 配置原理

基于 HTTP 协议支持的 Referer 机制，Referer 防盗链通过 HTTP request 中携带的 Referer 字段识别请求的来源，验证访问的合法性，进而允许或拒绝对直播内容的请求。

## 注意事项
- Referer 信息包含在 HTTP 中，RTMP、WebRTC 和 QUIC 等非 HTTP 协议不受 Referer 配置限制。若需限制 RTMP 拉流，防止客户通过 RTMP 拉流绕过 Referer 防盗链，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系线下修改。
- 开启、关闭或修改 Referer 防盗链配置后，约15分钟-20分钟即可生效，无需重新推流。
- Referer 防盗链是通过 HTTP 请求 header 中的 Referer 信息进行验证，确认请求合法来控制是否允许直播，但可能存在伪造 Referer 绕过校验盗用服务的情况，故不建议业务强依赖 于Referer 进行内容保护。

## 前提条件

- 已开通云直播服务，并登录 [云直播控制台](https://console.cloud.tencent.com/live/livestat)。
- 已 [添加播放域名](https://cloud.tencent.com/document/product/267/20381)。


[](id:open)
## 开启 Referer 防盗链

1.  选择 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)**，单击需配置 Referer 防盗链的 **播放域名** 或右侧的 **管理**，进入域名管理页。
2.  在 **访问控制**>**Referer防盗链配置** 中，单击**编辑**进入 Referer 防盗链配置页。
 ![](https://main.qcloudimg.com/raw/d6949ba7921409a09968d33811856146.png)
3.  单击![](https://main.qcloudimg.com/raw/c032c517e25867ff592f128424154688.png)按钮，选择开启 Referer 防盗链，并进行如下配置：
 ![](https://main.qcloudimg.com/raw/dfaee7724fcc8a31fa9beb7603e96e89.png)
<table id="setmess">
<tr><th width="14%">配置项</th><th>说明</th>
</tr><tr>
<td>防盗链类型</td>
<td>单击选择配置 Referer <b>黑名单</b>或<b>白名单</b>：
<ul style="margin:0">
<li>黑名单和白名单互斥，同一时间仅可生效一种。</li>
<li>若配置了 Referer 白名单，则允许白名单内用户的访问，可请求到直播内容；拒绝白名单外用户的访问，无法请求直播内容。</li>
<li>若配置了 Referer 黑名单，则拒绝黑名单内用户的访问，无法请求直播内容；允许黑名单外用户的访问，可请求到直播内容。</li>
</ul></td>
</tr><tr>
<td>允许空 Referer</td>
<td><ul style="margin:0">
<li>若选择允许，则 HTTP 请求中 Referer 字段为空或无字段的访问将被允许，允许直接通过浏览器访问直播 URL。</li>
<li>若选择不允许，则空 Referer 访问将被拒绝。</li>
</ul></td>
</tr><tr>
<td>防盗链规则</td>
<td><ul style="margin:0">
<li>最多支持配置<b>100</b>条规则，请使用换行符分隔。 </li>
<li>支持输入 <b>IP</b> 和<b>域名</b>两种格式，实际匹配时支持路径前缀匹配（域名和 IP）、支持通配符匹配（泛域名）。如：<ul>
<li/>配置 <code>101.1.0.1</code> 和 <code>www.test.com</code> 后，<code>101.1.0.1/157</code> 和 <code>www.test.com/tencent</code> 均生效。
<li/>配置 <code>*.test.com</code> 后，<code>www.test.com</code> 及 <code>a.test.com</code> 均生效。</ul></li>
<li>若规则内容为空则表示黑白名单均未配置。</li>
</ul></td>
</tr></table>
4. 单击**保存**，即可保存配置。


[](id:change)
## 修改 Referer 防盗链
1.   选择 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)**，单击需修改 Referer 防盗链配置的 **播放域名** 或右侧的 **管理**，进入域名管理页。
2.   在 **访问控制**>**Referer防盗链配置** 中，单击 **编辑** 进入 Referer 防盗链配置页。
3.   根据您的实际需求修改 [配置项](#setmess) 信息，单击 **保存** 即可完成修改。

![](https://main.qcloudimg.com/raw/696fe5a20ee56b969a4383c8aa477a4c.png)

[](id:close)
## 关闭 Referer 防盗链
[开启 Referer 防盗链](#open) 后，若您需关闭此功能，具体操作如下：

1.   选择 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)**，单击需关闭 Referer 防盗链配置的 **播放域名** 或右侧的 **管理**，进入域名管理页。
2.   在 **访问控制**>**Referer防盗链配置** 中，单击 **编辑** 进入 Referer 防盗链配置页。
3.   单击![](https://main.qcloudimg.com/raw/e72f89a0deb6858428dc3e93ce7e7088.png)按钮，选择关闭 Referer 防盗链。
4.   单击**保存**即可。

![](https://main.qcloudimg.com/raw/e8795543f82c78ac2b3728bd0403f47e.png)






