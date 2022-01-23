您可以在负载均衡实例上添加一个 QUIC 监听器，转发来自客户端加密的 QUIC 协议请求。QUIC 协议的监听器，后端服务器可直接获取客户端的真实 IP。

## 使用场景
QUIC 监听器支持连接迁移，当您的网络发生变化时，例如 4G 网络与 Wi-Fi 网络频繁切换，能够平滑迁移连接无中断，适用于音视频业务、游戏业务等。

## 限制说明
- QUIC 监听器目前处于内测阶段，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/55frjei1y18)。
- 仅负载均衡实例支持 QUIC 监听器，传统型负载均衡不支持。
- 仅 VPC 网络类型的负载均衡实例支持 QUIC 监听器，基础网络类型不支持。
- 仅 IPv4、IPv6 NAT64 版本的负载均衡实例支持 QUIC 监听器，IPv6 版本不支持。

## 前提条件
您需要 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。

## 操作步骤
### 步骤一：配置监听器
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏单击**实例管理**。
2. 在 CLB 实例列表页面左上角选择地域，在实例列表右侧的操作列中单击**配置监听器**。
![](https://qcloudimg.tencent-cloud.cn/raw/2c0b7f73cd81582c7ace11dbfe7d6c18.png)
3. 在 TCP/UDP/TCP SSL/QUIC 监听器下，单击**新建**，在弹出的**创建监听器**对话框中配置 QUIC 监听器。
  **a. 基本配置**
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
<td><span>test-quic-443</span></td>
</tr>
<tr>
<td>监听协议端口</td>
<td>
<ul><li>监听协议：本示例选择 QUIC。选择 QUIC 后，CLB可 接收客户端发起的 QUIC 请求，CLB 和后端服务器之间仍然使用 TCP 协议。</li><li>监听端口：用来接收请求并向后端服务器转发请求的端口，端口范围为1 - 65535。</li><li>同一个负载均衡实例内，监听端口不可重复。</li></ul></td>
<td>QUIC:443</td>
</tr>
<tr>
<td>SSL 解析方式</td>
<td>支持单向认证和双向认证。</td>
<td>单向认证</td>
</tr>
<tr>
<td>服务器证书</td>
<td>可以选择 <a href="https://console.cloud.tencent.com/ssl">SSL 证书平台</a> 中已有的证书，或上传证书。</td>
<td>选择已有证书</td>
</tr>
<tr>
<td>均衡方式</td>
<td>TCP SSL 监听器中，负载均衡支持加权轮询（WRR）和加权最小连接数（WLC）两种调度算法 <br><ul><li>加权轮询算法：根据后端服务器的权重，按依次将请求分发给不同的服务器。加权轮询算法根据<strong>新建连接数</strong>来调度，权值高的服务器被轮询到的次数（概率）越高，相同权值的服务器处理相同数目的连接数。</li><li>加权最小连接数：根据服务器当前活跃的连接数来估计服务器的负载情况，加权最小连接数根据服务器负载和权重来综合调度，当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。</li></ul></td>
<td>加权轮询</td>
</tr>
</tbody></table>
 <b>b. 健康检查</b></br>
健康检查详情请参见<a href="https://cloud.tencent.com/document/product/214/50011#tcp-ssl"> TCP SSL 健康检查</a>。</br>
<b>c. 会话保持</b>
</br>QUIC 监听器暂不支持会话保持。

### 步骤二：绑定后端云服务器
1. 在**监听器管理**页面，单击刚才创建的监听器，如上述 `QUIC:443` 监听器，即可在监听器右侧查看已绑定的后端服务。
2. 单击**绑定**，在弹出框中选择需绑定的后端服务器，并配置服务端口和权重。
>? 默认端口功能：先填写**默认端口**，再选择云服务器后，每台云服务器的端口均为默认端口。
>

### 步骤三：配置安全组
您需配置负载均衡的安全组来进行公网流量的隔离，详情请参见 [配置负载均衡安全组](https://cloud.tencent.com/document/product/214/14733)。

### 步骤四：修改/删除监听器（可选）
如果您需要修改或删除已创建的监听器，请在“监听器管理”页面，单击已创建完毕的监听器，单击![](https://qcloudimg.tencent-cloud.cn/raw/4ab10b98316964812832043bbfd99df6.svg)图标修改或![](https://qcloudimg.tencent-cloud.cn/raw/e863cc51c29790d665d53feba800fd90.svg)图标删除。


## 相关文档
[CLB 支持 QUIC 协议](https://cloud.tencent.com/document/product/214/46008)
