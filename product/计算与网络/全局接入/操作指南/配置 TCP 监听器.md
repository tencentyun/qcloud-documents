您可以在全局接入实例上添加一个 TCP 监听器转发来自客户端的 TCP 协议请求。TCP 协议适用于对可靠性和数据准确性要求高、对传输速度要求较低的场景，如文件传输、收发邮件、远程登录等。TCP 协议的监听器，后端服务器可直接获取客户端的真实 IP。

## 前提条件
您需要 [创建全局接入实例](https://cloud.tencent.com/document/product/1510/61383)。



## [步骤一：配置监听器基本信息](id:step1)
1. 登录 [全局接入控制台](https://console.cloud.tencent.com/ga/instance)。
2. 在**实例管理**页面，找到目标实例，单击右侧**操作**列的**配置监听器**。
3. 在 TCP/UDP 监听器页签，单击**新建**。
4. 在弹出的**创建监听器**对话框中，配置 TCP 监听器的基本信息，配置完成后单击**下一步：健康检查**。
![](https://qcloudimg.tencent-cloud.cn/raw/77e75f69a7e3f5e5a9795a171abdcf58.png)
<table>
<thead>
<tr>
<th width="17%">参数</th>
<th width="68%">说明</th>
<th width="15%">示例</th>
</tr>
</thead>
<tbody><tr>
<td><strong>名称</strong></td>
<td>监听器的名称。</td>
<td><span>test-tcp-80&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
</tr>
<tr>
<td><strong>监听协议端口</strong></td>
<td><ul><li>监听协议：选择 TCP。</li><li>监听端口：用来接收请求并向后端服务器转发请求的端口，端口范围为1 - 65535。</li></ul>同一个实例内，监听端口不可重复。</td>
<td>TCP:80</td>
</tr>
<tr>
<td><strong>均衡方式</strong></td>
<td>选择监听器的均衡方式，即调度算法： <br><ul><li><strong>加权轮询</strong>（WRR）：根据后端服务器的权重，按依次将请求分发给不同的服务器。加权轮询算法根据<strong>新建连接数</strong>来调度，权值高的服务器被轮询到的次数（概率）越高，相同权值的服务器处理相同数目的连接数。</li><li><strong>加权最少连接数</strong>（WLC）：根据服务器当前活跃的连接数来估计服务器的负载情况，加权最小连接数根据服务器负载和权重来综合调度，当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。</li></ul>
<dx-alert infotype="explain" title="">
选取加权最小连接数的均衡方式后，监听器不支持开启会话保持功能。
</dx-alert>
</td>
<td>加权轮询</td>
</tr>
</tbody></table>

## [步骤二：配置健康检查](id:step2)
在**健康检查**页签配置监听器的健康检查信息，配置完成后单击**下一步：会话保持**。
<dx-accordion>
::: 配置 TCP 健康检查
![](https://qcloudimg.tencent-cloud.cn/raw/a1931826c183b51adb9c65517521d2e6.png)
<table>
<tr>
<th>参数</th><th>说明</th>
</tr>
<tr>
<td>健康检查</td><td>可开启或关闭健康检查功能。建议您开启健康检查，帮助您自动检查并移除异常的后端 CVM 端口。</td>
</tr>
<tr>
<td>检查协议</td><td>选择<b> TCP </b>表示配置 TCP 健康检查。</td>
</tr>
<tr>
<td>检查端口</td><td>非必填，不填写端口时默认为后端服务器端口。除需要指定特定端口以外，其余情况建议不填写。</td>
</tr>
<tr>
<td>响应超时</td><td><ul><li> 健康检查响应的最大超时时间。</li><li>如果后端云服务器在超时时间内没有正确响应，则判定为健康检查异常。</li><li>可配置范围：2秒 - 60秒。</li></ul></td>
</tr>
<tr>
<td>检测间隔</td><td><ul><li>负载均衡进行健康检查的时间间隔。</li><li>可配置范围：2秒 - 300秒。</li></ul></td>
</tr>
<tr>
<td>不健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果失败，则识别为不健康，控制台显示为<strong>异常</strong>。</li><li>可配置范围：2 - 10次。</li></ul></td>
</tr>
<tr>
<td>健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果为成功，则识别为健康，控制台显示为<strong>健康</strong>。</li><li>可配置范围：2 - 10次。 </li></ul></td>
</tr>
</table>
:::
::: 配置 HTTP 健康检查
![](https://qcloudimg.tencent-cloud.cn/raw/e4d645717b00acce296c9b3a2a8cd197.png)
<table>
<tr>
<th>参数</th><th>说明</th>
</tr>
<tr>
<td>健康检查</td><td>可开启或关闭健康检查功能。建议您开启健康检查，帮助您自动检查并移除异常的后端 CVM 端口。</td>
</tr>
<tr>
<td>检查协议</td><td>选择<b> HTTP </b>表示配置 HTTP 健康检查。</td>
</tr>
<tr>
<td>检查端口</td><td>非必填，不填写端口时默认为后端服务器端口。除需要指定特定端口以外，其余情况建议不填写。</td>
</tr>
<tr>
<td>检查域名</td><td>健康检查域名：
<ul>
<li>长度限制：1 - 80个字符。</li>
<li>默认为转发域名。</li>
<li>不支持正则表达式，当您的转发域名为通配域名时，需要指定某一固定域名（非正则）为健康检查域名。</li>
<li>支持的字符集为：a-z 0-9 . -。</li>
</ul></td>
</tr>
<tr>
<td>检查路径</td><td>健康检查路径 ：
<ul>
<li>长度限制：1 - 200个字符。</li>
<li>默认为 /，且必须以 / 开头。</li>
<li>不支持正则表达，建议指定某个固定 URL 路径（静态页面）进行健康检查。</li>
<li>支持的字符集为：a-z A-Z 0-9 . - _ / = ?。</li>
</ul></td>
</tr>
<tr>
<td>HTTP 请求方式</td><td>健康检查的 HTTP 请求方式，可选：GET 或 HEAD，默认为 GET。
<ul>
<li>若使用 HEAD 方法，服务器仅返回 HTTP 头部信息，可降低后端开销，提升请求效率，对应的后端服务需支持 HEAD。</li>
<li>若使用 GET 方法，则后端服务支持 GET 即可。</li>
</ul></td>
</tr>
<tr>
<td>HTTP 版本</td><td>后端服务的 HTTP 版本。
<ul>
<li>若后端服务器支持的 HTTP 版本为1.0，则无需校验请求的 Host 字段，即无需配置检查域名。</li>
<li>若后端服务器支持的 HTTP 版本为1.1，则需要校验请求的 Host 字段，即需要配置检查域名，否则会返回404错误。</li>
</ul></td>
</tr>
<tr>
<td>正常状态码</td><td>当状态码为所选状态码时，认为后端服务器存活，即健康检查正常。可选：http_1xx、http_2xx、http_3xx、http_4xx 和 http_5xx，支持选择多个状态码。</td>
</tr>
<tr>
<td>响应超时</td><td><ul><li> 健康检查响应的最大超时时间。</li><li>如果后端云服务器在超时时间内没有正确响应，则判定为健康检查异常。</li><li>可配置范围：2秒 - 60秒。</li></ul></td>
</tr>
<tr>
<td>检测间隔</td><td><ul><li>负载均衡进行健康检查的时间间隔。</li><li>可配置范围：2秒 - 300秒。</li></ul></td>
</tr>
<tr>
<td>不健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果失败，则识别为不健康，控制台显示为<strong>异常</strong>。</li><li>可配置范围：2 - 10次。</li></ul></td>
</tr>
<tr>
<td>健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果为成功，则识别为健康，控制台显示为<strong>健康</strong>。</li><li>可配置范围：2 - 10次。 </li></ul></td>
</tr>
</table>
:::
::: 配置自定义协议健康检查
![](https://qcloudimg.tencent-cloud.cn/raw/58fcf2f7ea01f76db1f13882eb98ee25.png)
<table>
<tr>
<th>参数</th><th>说明</th>
</tr>
<tr>
<td>健康检查</td><td>可开启或关闭健康检查功能。建议您开启健康检查，帮助您自动检查并移除异常的后端 CVM 端口。</td>
</tr>
<tr>
<td>检查协议</td><td>选择<b>自定义协议</b>表示配置自定义协议健康检查。</td>
</tr>
<tr>
<td>检查端口</td><td>非必填，不填写端口时默认为后端服务器端口。除需要指定特定端口以外，其余情况建议不填写。</td>
</tr>
<tr>
<td>输入格式</td><td>支持文本和十六进制输入。
<ul>
<li>输入格式为文本是将文本转换成二进制进行请求发送和返回结果对比。</li>
<li>输入格式为十六进制是将十六进制转换成二进制进行请求发送和返回结果对比。</li>
</ul></td>
</tr>
<tr>
<td>检查请求</td><td>自定义健康检查请求内容。例如探测 DNS 服务的检查请求示例为：F13E0100000100000000000003777777047465737403636F6D0774656E63656E7403636F6D0000010001。</td>
</tr>
<tr>
<td>检查返回结果</td><td>自定义健康检查请求时，必须配置健康检查返回结果。例如探测 DNS 服务的检查返回结果示例为：F13E。</td>
</tr>
<tr>
<td>响应超时</td><td><ul><li> 健康检查响应的最大超时时间。</li><li>如果后端云服务器在超时时间内没有正确响应，则判定为健康检查异常。</li><li>可配置范围：2秒 - 60秒。</li></ul></td>
</tr>
<tr>
<td>检测间隔</td><td><ul><li>负载均衡进行健康检查的时间间隔。</li><li>可配置范围：2秒 - 300秒。</li></ul></td>
</tr>
<tr>
<td>不健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果失败，则识别为不健康，控制台显示为<strong>异常</strong>。</li><li>可配置范围：2 - 10次。</li></ul></td>
</tr>
<tr>
<td>健康阈值</td><td><ul><li>如果连续 n 次（n 为填写的数值）收到的健康检查结果为成功，则识别为健康，控制台显示为<strong>健康</strong>。</li><li>可配置范围：2 - 10次。 </li></ul></td>
</tr>
</table>
:::
</dx-accordion>

## 步骤三：配置会话保持
在**会话保持**页签配置监听器的会话保持，配置完成后单击**完成**。
![](https://qcloudimg.tencent-cloud.cn/raw/b03694613966fd2220d28688c300438f.png)
<table>
<thead>
<tr>
<th width="15%">参数</th>
<th width="70%">说明</th>
<th width="15%">示例</th>
</tr>
</thead>
<tbody><tr>
<td><strong>会话保持状态</strong></td>
<td><ul><li>开启或关闭会话保持。开启会话保持后，监听器会将来自同一客户端的访问请求分发到同一台后端服务器上。</li><li>TCP 协议是基于客户端 IP 地址的会话保持，即来自同一 IP 地址的访问请求转发到同一台后端服务器上。</li><li>加权轮询调度支持会话保持，加权最小连接数不支持。</li></ul></td>
<td><span>开启</span></td>
</tr>
<tr>
<td><strong>会话保持时间</strong></td>
<td> <ul><li>当超过保持时间，连接内无新的请求，将会自动断开会话保持，但不会断开与后端服务的连接。</li><li>可配置范围30s - 3600s。</li></ul></td>
<td>30s</td>
</tr>
</tbody></table>


## 后续操作
[绑定目标组](https://cloud.tencent.com/document/product/1510/61384#BindTargetGroup)
