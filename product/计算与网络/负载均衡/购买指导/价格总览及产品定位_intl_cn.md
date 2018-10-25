## 负载均衡实例费用及产品定位

## 负载均衡产品定位

应用型负载均衡及传统型负载均衡的产品定位如下，供您选择时参考：

<table>
        <tbody>
                <tr>
            <th style="width: 10%;" rowspan="2">产品类型</th>
            <th style="width: 45%;" colspan="2" >应用型负载均衡</th>
            <th style="width: 45%;" colspan="2">传统型负载均衡</th>
        </tr>
        <tr>
            <th>公网</th>
            <th>内网</th>
            <th>公网</th>
            <th>内网</th>
        </tr>
        <tr>
            <td>七层转发(HTTP/HTTPS)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
        </tr>
        <tr>
            <td>四层转发(TCP/UDP)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>    
                <tr>
            <td>支持HTTP/2及websocket(secure)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
        </tr>
        <tr>
            <td>负载均衡策略</td>
                        <td>ip hash(七层)<br>加权轮询<br>加权最小连接数 </td>
                        <td>ip hash(七层)<br>加权轮询<br>加权最小连接数</td>
                        <td>ip hash(七层)<br>加权轮询<br>加权最小连接数</td>
                        <td>加权轮询</td>
        </tr>   
         <tr>
            <td>会话保持</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>   
        <tr>
            <td>健康检查</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>   
         <tr>
            <td>自定义转发规则(域名/URL)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
            <tr>
            <td>转发到不同的后端端口</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
         <tr>
            <td>支持重定向功能(rewrite)</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
             <tr>
            <td>支持跨地域绑定功能</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
        <tr>
            <td>支持日志存储到COS功能</td>
                        <td>✔（七层）</td>
                        <td>即将支持</td>
                        <td>✔（七层）</td>
                        <td>✖</td>
        </tr>   
</tbody></table>

> Note: When a user cancels cloud load balance service in advance, the corresponding charges will be deducted from blocked balance in the user account according to the actual usage period. The remaining balance will be returned to the account.

## 负载均衡带宽费用

### 带宽费用付费场景
1) 云服务器按带宽计费：带宽消耗使用的是云服务器已包含的公网带宽，不另外收取带宽费用；
2) 云服务器按流量计费：用户使用公网负载均衡会产生出流量，需支付对应的流量费用。 

### 带宽费用付费标准
在上述场景2) 下CLB负载均衡器的带宽费用，收取的是后端CVM云主机产生的网络费用。具体计费模式参见[网络计费](http://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD)。
