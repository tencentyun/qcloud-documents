[gRPC](https://grpc.io/docs/what-is-grpc/introduction/) 是 Google 发布的基于 HTTP 2.0 传输层协议的高性能开源软件框架，提供了支持多种编程语言、对网络设备进行配置和纳管的方法。本文指导您通过配置 HTTPS 监听器的 gRPC 协议的健康检查，将客户端的 gRPC 请求通过 CLB 实例转发到后端协议为 gRPC 的后端服务。


## 使用场景
当客户端通过 HTTPS 请求访问协议类型为 gRPC 的后端服务时，您可以通过 CLB 实例的 HTTPS 监听器支持 gRPC 协议来实现。
![](https://qcloudimg.tencent-cloud.cn/raw/f71367bab84383e0d9d9735306528fc4.svg)

 ## 前提条件
 - 您已创建 VPC，详情请参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。
 - 您已在 VPC 中创建了 CVM 实例，并在实例上部署了 gRPC 服务，详情请参见 [通过镜像创建实例](https://cloud.tencent.com/document/product/213/44265)。
 - 您已购买了 CLB 实例，详情请参见 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。
 

## 使用限制
- 仅负载均衡类型支持，传统型负载均衡不支持。
- IPv6 版本 CLB 与开启了七层混绑的 IPv6 版本 CLB 不支持。
- 仅 VPC 网络支持，基础网络不支持。
- 后端服务不支持 SCF（需要 SCF target 内部支持 gRPC 协议）。

 

## 操作步骤

### 步骤一：配置监听器
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏单击**实例管理**。
2. 在 CLB 实例列表页面左上角选择地域，在实例列表右侧的**操作**列中单击**配置监听器**。
![](https://qcloudimg.tencent-cloud.cn/raw/2c0b7f73cd81582c7ace11dbfe7d6c18.png)
3. 在 HTTP/HTTPS 监听器下，单击**新建**，在弹出的**创建监听器**对话框中配置 HTTPS 监听器。
**1. 创建监听器**
<table>
<thead>
<tr>
<th width="15%">监听器基本配置</th>
<th width="70%">说明</th>
<th width="15%">示例</th>
</tr>
</thead>
<tbody><tr>
<td>名称</td>
<td>监听器的名称。</td>
<td><span>test-https-443</span></td>
</tr>
<tr>
<td>监听协议端口</td>
<td>
<ul><li>监听协议：本示例选择 HTTPS。</li><li>监听端口：用来接收请求并向后端服务器转发请求的端口，端口范围为1 - 65535。其中，843、1020、1433、1434、3306、3389、6006、20000、36000、42222、48369、56000、65010端口为系统保留端口，暂不对外开放。</li><li>同一个负载均衡实例内，监听端口不可重复。</li></ul></td>
<td>HTTPS:443</td>
</tr>
<tr>
<td>启用长连接</td>
<td>开启后，CLB 与后端服务之间使用长连接，CLB 不再透传源 IP，请从 XFF 中获取源 IP。为保证正常转发，请在 CLB 上打开安全组默认放通或者在 CVM 的安全组上放通100.127.0.0/16。
<dx-alert infotype="explain" title="">
开启后，CLB 与后端服务的连接数范围在请求[QPS，QPS*60]区间波动，具体数值取决于连接复用率。若后端服务对连接数上限有限制，则建议谨慎开启。此功能目前处于内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/tsodp6qm21)。
</dx-alert></td>
<td><span>选择已有证书</span></td>
</tr>
<tr>
<td>启用 SNI</td>
<td>启用 SNI 表示一个监听器下可为不同的域名配置不同的证书，不启用 SNI 表示该监听器下多个域名使用同一个证书。</td>
<td><span>不启用</span></td>
</tr>
<tr>
<td>SSL 解析方式</td>
<td>支持单向认证和双向认证。负载均衡器代理了 SSL 加解密的开销，保证访问安全。</td>
<td><span>单向认证</span></td>
</tr>
<tr>
<td>服务器证书</td>
<td>可以选择 <a href="https://console.cloud.tencent.com/ssl">SSL 证书平台</a> 中已有的证书，或上传证书。</td>
<td><span>选择已有</span></td>
</tr>
</tbody>
</table>
<b>2. 创建转发规则</b>
 <table>
<tr>
<th>转发规则基本配置</th>
<th>说明</th>
<th>示例</th>
</tr>
<tr>
<td>域名</td>
<td>转发域名：<ul style="margin-bottom:0px;"><li>长度限制：1 - 80个字符。</li><li>不能以 `_` 开头。</li><li>支持精准域名和通配域名。</li><li>支持正则表达式。</li></ul>具体配置规则，详情请参见 <a href="https://cloud.tencent.com/document/product/214/9032#.E8.BD.AC.E5.8F.91.E5.9F.9F.E5.90.8D.E9.85.8D.E7.BD.AE.E8.A7.84.E5.88.99">转发域名配置规则</a>。</td>
<td>www.example.com</td>
</tr>
<tr>
<td>默认域名</td>
<td><ul><li>当监听器中所有域名均没有匹配成功时，系统会将请求指向默认访问域名，让默认访问可控。</li><li>一个监听器下仅能配置一个默认域名。</li></ul></td>
<td>开启</td>
</tr>
<tr>
<td>HTTP 2.0</td>
<td>启用 HTTP2.0 后，CLB 可以接收 HTTP 2.0 的请求，无论客户端请求 CLB 时使用哪种 HTTP 版本，CLB 访问后端服务器的 HTTP 版本都是 HTTP 1.1。</td>
<td>开启</td>
</tr>
<tr>
<td>QUIC</td>
<td>启用 QUIC 后，客户端可以和 CLB 之间建立 QUIC 连接，当二者协商无法建立 QUIC 连接时自动降级到 HTTPS 或 HTTP/2，但 CLB 和后端服务器之间仍然使用 HTTP1.x 协议。详情请参见 <a href="https://cloud.tencent.com/document/product/214/46008">CLB 支持 QUIC 协议</a>。</td>
<td>开启</td>
</tr>
<tr>
<td>URL 路径</td>
<td>转发 URL 路径：<ul style="margin-bottom:0px;"><li>长度限制：1 - 200个字符。</li><li>支持正则表达式。</li><li>具体配置规则，详情请参见 <a href="https://cloud.tencent.com/document/product/214/9032#.E8.BD.AC.E5.8F.91-url-.E8.B7.AF.E5.BE.84.E9.85.8D.E7.BD.AE.E8.A7.84.E5.88.99">转发 URL 路径配置规则</a>。</li></ul></td>
<td>/index</td>
</tr>
<tr>
<td>均衡方式</td>
<td>HTTPS 监听器中，负载均衡支持加权轮询（WRR）、加权最小连接数（WLC）和 IP Hash 三种调度算法：<ul style="margin-bottom:0px;"><li>加权轮询算法：根据后端服务器的权重，按依次将请求分发给不同的服务器。加权轮询算法根据<b>新建连接数</b>来调度，权值高的服务器被轮询到的次数（概率）越高，相同权值的服务器处理相同数目的连接数。</li><li>加权最小连接数：根据服务器当前活跃的连接数来估计服务器的负载情况，加权最小连接数根据服务器负载和权重来综合调度，当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。</li><li>IP Hash：根据请求的源 IP 地址，使用散列键（Hash Key）从静态分配的散列表找出对应的服务器，若该服务器为可用且未超载状态，则请求发送到该服务器，反之则返回空。</li></ul></td>
<td>加权轮询</td>
</tr>
<tr>
<td>后端协议</td>
<td>后端协议是指 CLB 与后端服务之间的协议：<ul style="margin-bottom:0px;"> <li>后端协议选择 HTTP 时，后端服务需部署 HTTP 服务。</li><li>后端协议选中 HTTPS 时，后端服务需部署 HTTPS 服务，HTTPS 服务的加解密会让后端服务消耗更多资源。</li><li>后端协议选中 gRPC 时，后端服务需部署 gRPC 服务。仅 HTTP2.0 开启且 QUIC 关闭的情况下，后端转发协议支持选择 gRPC。</li></ul></td>
<td>gRPC</td>
</tr>
<tr>
<td>获取客户端 IP</td>
<td>默认启用。</td>
<td>已开启</td>
</tr>
<tr>
<td>Gzip 压缩</td>
<td> 默认启用。</td>
<td>已开启</td>
</tr>
</table>
<b>3. <a href="https://cloud.tencent.com/document/product/214/50011#https">HTTPS 健康检查</a></b>。</br> 
<b>4. 会话保持</b>
<table>
<tr>
<th>会话保持配置</th>
<th>说明</th>
<th>示例</th>
</tr>
<tr>
<td>会话保持开关</td>
<td><ul><li>开启会话保持后，负载均衡监听会把来自同一客户端的访问请求分发到同一台后端服务器上。</li><li>TCP 协议是基于客户端 IP 地址的会话保持，即来自同一 IP 地址的访问请求转发到同一台后端服务器上。</li><li>加权轮询调度支持会话保持，加权最小连接数调度不支持开启会话保持功能。</li></ul></td>
<td>开启</td>
</tr>
<tr>
<td>会话保持时间</td>
<td><ul><li>当超过保持时间，连接内无新的请求，将会自动断开会话保持。</li><li>可配置范围30s - 3600s。</li></ul></td>
<td>30s</td>
</tr>
</table>


### 步骤二：绑定后端云服务器
1. 在**监听器管理**页面，单击刚才创建的监听器，如上述 `HTTPS:443` 监听器，单击左侧的 **+** 展开域名和 URL 路径，选中具体的 URL 路径，即可在监听器右侧查看该路径上已绑定的后端服务。
2. 单击**绑定**，在弹出框中选择需绑定的后端服务器，并配置服务端口和权重。
>? 默认端口功能：先填写“默认端口”，再选择云服务器后，每台云服务器的端口均为默认端口。
>

### 步骤三：安全组（可选）
您可以配置负载均衡的安全组来进行公网流量的隔离，详情请参见 [配置负载均衡安全组](https://cloud.tencent.com/document/product/214/14733)。

### 步骤四：修改/删除监听器（可选）
如果您需要修改或删除已创建的监听器，请在**监听器管理**页面，单击已创建完毕的监听器，单击![](https://qcloudimg.tencent-cloud.cn/raw/4ab10b98316964812832043bbfd99df6.svg)图标修改或![](https://qcloudimg.tencent-cloud.cn/raw/e863cc51c29790d665d53feba800fd90.svg)图标删除。

