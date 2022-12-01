腾讯云提供HTTP响应头配置功能，通过此功能，您可以定义HTTP事务中的具体操作参数。响应头部配置是域名维度的，因此一旦配置生效，会对域名下任意一个资源的响应消息生效。


## 前提条件
- 已登录 [云直播控制台](https://console.cloud.tencent.com/live)。
- 已添加 [播放域名](https://cloud.tencent.com/document/product/267/20381)。

[](id:limit) 
## 使用限制
- 最多可以支持10条配置。
- 禁止重复的消息头，有多个取值的参数，可以通过参数：`值1,值2,值3` 来实现。
- 当您配置的参数名与后台的私有参数名冲突时，系统会进行提示，您需要修改参数名。
- 自定义参数名可由大小写字母、数字及 - 组成，长度支持1个 - 100个字符。
- 参数取值不能为空，不支持中文，长度可支持1个 - 1000个字符。


## 配置 HTTP 响应头
1. 进入 [域名管理](https://console.cloud.tencent.com/live/domainmanage)，单击需配置的 **播放域名** 或右侧的 **管理** 进入域名详情页。
2. 选择 **高级配置** 页签，进入查看 **HTTP响应头配置** 标签。
![](https://qcloudimg.tencent-cloud.cn/raw/236de0982d3e166f7030f26cde4426c4.png)
3. 单击**编辑**按钮，对 HTTP 响应头进行配置，支持编辑已有规则、删除已有规则、新增规则。
![](https://qcloudimg.tencent-cloud.cn/raw/a1b598ad50629cdde2814c4592649d5b.png)
若您需新增规则，可单击 **新增规则**：
	- 单击 **可选参数**，支持选择已有参数：`Access-Control-Allow-Methods`、`Access-Control-Max-Age`、`Access-Control-Expose-Headers` 进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/196aa2031095ab92047667d31625b9a3.png)
<table>
<thead><tr><th style="width:30%">头部参数</th><th>说明</th></tr></thead>
<tbody>
<tr>
<td>Access-Control-Allow-Methods</td>
<td>用于设置跨域允许的 HTTP 请求方法，可同时设置多个方法，如下：<br><code>Access-Control-Allow-Methods: POST, GET, OPTIONS</code>。</td>
</tr>
<tr>
<td>Access-Control-Max-Age</td>
<td>用于指定预请求的有效时间，单位为秒。
</tr>
<tr>
<td>Access-Control-Expose-Headers</td>
<td>用于指定哪些头部可以作为响应的一部分暴露给客户端。
</tr>
</tbody></table>
	- 单击 **自定义参数**，支持进行自定义参数配置。
>! 自定义参数名可由大小写字母、数字及 - 组成，长度支持1个 - 100个字符；参数取值不支持中文，长度支持1个 - 1000个字符。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2becbedf4b932ffdec4aa8448b58b84e.png)
5. 配置完成后，您可以单击**提交**功能，系统会根据后台生效情况展示：`配置中，未生效`、`配置失败：失败原因`、`配置已生效`。
![](https://qcloudimg.tencent-cloud.cn/raw/5208a2f1d536e7570719277e62a29c90.png)
