### 为什么要升级公网无固定 IP 型负载均衡？
升级的目的是为了给您提供更优质的服务。公网无固定 IP 型负载均衡为腾讯云早期的负载均衡版本，现在腾讯云已推出性能更强、特性更多、服务更健壮的负载均衡服务，支持四层（TCP/UDP）和七层（HTTP/HTTPS）转发规则，并且具备监控告警、安全组、日志管理等功能。

### 升级对我有什么影响？我需要做什么？
- 此次升级为平滑升级，业务无感知，相关域名、转发规则、实例名称等均会保留，升级后价格为 0.02 元/小时，负载均衡实例 ID 会改变。
- 用户无需做任何操作，腾讯云会将有服务的公网无固定 IP 型负载均衡升级。

### 判断升级或回收的标准是什么？
公网无固定 IP 型负载均衡一直是免费资源，有服务的将被升级，无服务的则被回收。
- 升级对象为有服务（有转发规则且绑定云服务器）的公网无固定 IP 型负载均衡。
- 回收对象为全网无服务（没有转发规则或者未绑定云服务器）的公网无固定 IP 型负载均衡。

### 我能不能迁到应用型 CLB，而不是传统型 CLB？
如果您需要保留公网无固定 IP 型 CLB 的域名，则必须使用传统型 CLB；如果您想使用应用型 CLB，可以直接在购买页购买并配置。

### 为什么公网无固定 IP 型 CLB 转发协议是 HTTP，升级后的传统型公网 CLB 是 TCP？
公网无固定 IP 型 CLB 的 HTTP 监听器实现机制，与传统型公网 CLB 的 HTTP 监听器不完全一致。为了能够平滑地将无固定 IP 型负载均衡升级为传统型公网负载均衡，升级后的监听器协议采用 TCP。在功能上，升级后的 TCP 协议能覆盖老版本的能力，同时您也可以启用功能更完备的 HTTP/HTTPS 协议。

### 升级前后详细对比

<table>
        <tbody>
        <tr>
            <th style="width: 10%;">特性</th>
            <th style="width: 45%;">升级前</th>
            <th style="width: 45%;">升级后</th>
        </tr>
        <tr>
          <td>产品类型</td>
          <td>公网无固定 IP 型 CLB</td>
          <td>传统型公网 CLB</td>
        </tr>
        <tr>
          <td>域名</td>
          <td>✔</td>
          <td>✔</td>
        </tr>
        <tr>
          <td>vip</td>
          <td>✖</td>
          <td>✔</td>
        </tr>
        <tr>
          <td>协议</td>
          <td>HTTP</td>
          <td>四层（TCP/UDP）<br>七层（HTTP/HTTPS）</td>
        </tr>
        <tr>
            <td>负载均衡策略</td>
            <td>加权轮询</td>
            <td>加权轮询<br>加权最小连接数<br>IP hash（七层）</td>
        </tr>    
        <tr>
          <td>WebSocket（Secure）</td>
          <td>✖</td>
          <td>✔</td>
        </tr>
        <tr>
          <td>HTTP/2</td>
          <td>✖</td>
          <td>✔</td>
        </tr>
        <tr>
            <td>安全组</td>
            <td>✖</td>
            <td>✔</td>    
        </tr>   
        <tr>
            <td>监控告警</td>
            <td>✖</td>
            <td>✔</td>    
        </tr>
        <tr>
            <td>日志存储到 COS</td>
            <td>✖</td>
            <td>✔（七层）</td>
        </tr>   
        <tr>
            <td>价格</td>
            <td>暂时免费</td>
            <td>0.02 元/小时<br>详情请参见 <a href=(https://cloud.tencent.com/document/product/214/8848)>计费说明</a>。</td>    
        </tr>
</tbody></table>

>**注意：**
>若您有任何问题，请在 [工单系统](https://console.cloud.tencent.com/workorder/category) 提交工单与我们联系。
