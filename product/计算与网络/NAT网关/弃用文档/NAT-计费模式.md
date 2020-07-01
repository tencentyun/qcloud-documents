<style rel="stylesheet">
table th:nth-of-type(1){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(2){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(3){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(4){
width:200px;
}</style>
<style rel="stylesheet">
table tr:hover {
background: #efefef; 
</style>
## 计费方式
NAT 网关设备共收取两项服务费用：网关租用费（按小时计费）和访问 Internet 产生的流量费用。流量部分的费用可以参考云服务器网络费用中的按流量计费。NAT 网关租用计费模式如下表：

| 类型 | 国内 |中国香港 |新加坡、硅谷|  多伦多 |
|:---------:|:---------:|:---------:|:---------:|
| 小型 | 0.5 元/h | 0.75 元/h | 0.75 元/h |0.8 元/h |
| 中型 | 1.5 元/h| 2.25 元/h | 2.25 元/h |2.4 元/h |
| 大型 | 5 元/h | 7.5 元/h | 7.5 元/h |8 元/h |

 ><b>注意：</b>
 >1. 如果用户账号开通了带宽包共享带宽功能，则 NAT 网关产生的出流量按照带宽包整体结算（不再重复收取 0.8 元/GB 的网络流量费），建议您限制 NAT 网关的出带宽，以避免因为 NAT 网关出带宽过高产生高额的带宽包费用。单击查看 <a href="https://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD#.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9" target="_blank">带宽包计费详情</a>
 >
 >2. 欠费逻辑：与按量计费主机保持一致。<a href="https://cloud.tencent.com/doc/product/215/3079" target="_blank">单击查看私有网络价格总览</a>
>
>3. 由于 NAT 网关具备双机热备的特性，系统每 3 秒会分别给 NAT 网关的主备服务器发送一个 5 KB 的探测包，因此每天会产生 0.2747 GB 的流量，对应大陆、中国香港、北美会分别产生 0.2197 元、0.2747 元、0.1373 元的费用。


## 到期提醒
当您购买的腾讯云 NAT 服务到期后且账户余额不足，需要注意以下几点：

- 从余额为 0 的时刻开始，**2** 小时内 NAT 网关可继续使用且继续扣费。

- 2 小时后，若您的账户仍未充值到大于 0，NAT 网关将自动停止服务并停止扣费。

- NAT 网关停止服务后的 24 小时内，若您的账户余额仍未充值到大于 0，则保持为不可用状态；若充值到余额大于 0，则网关重新可用，且计费重新开始。

- NAT 网关停止服务后，余额小于 0 的时间达到 24 小时，NAT 网关将被立即回收。

- NAT 网关回收时，我们将通过邮件及短信的方式通知到腾讯云账号的创建者以及所有协作者。
