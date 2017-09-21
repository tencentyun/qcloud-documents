移动直播本身不是一项独立的云服务，所以费用全部源自其依赖的如下几项基础云服务，自身不产生额外费用：

### 直播云服务（LVB）
直播可以选择**带宽**计费（默认计费方案，适合直播平台）或者**流量**计费（适合直播活动）两种计费方式。
- 按带宽计费的日结价格如下：

| 带宽阶梯 | 价格 |
|---------|---------|
| 0Mbps-500Mbps(含) | 1.0元Mbps/天 | 
| 500Mbps-5Gbps(含)	 | 0.9元Mbps/天 | 
| >5Gbps | 0.76元Mbps/天 | 

- 按流量计费的日结价格如下：

| 带宽阶梯 | 价格 |
|---------|---------|
| 0-50GB(含)	  | 0.29元/GB/天  |
| 50-500G(含)	| 0.27元/GB/天 |
| 500G-1T(含)	| 0.26元/GB/天 |
| 1T-5T(含)	    | 0.24元/GB/天 |
| >5T(含)	       | 0.23元/GB/天 |

您可以选择月结等其它计费方式，更多信息可以关注 [直播价格总览](https://www.qcloud.com/document/product/267/2818)。


### 点播云服务（VOD）
如果您的希望将直播内容录制并提供回放能力，那么该项服务是必不可少的：
<table class="t" style="text-align: center;">
<tbody><tr>
<th width=150> 功能版本
</th><th width=100> 测试体验版
</th><th width=100> 创业版
</th><th width=100> 企业版
</th><th width=100> 旗舰版-Ⅰ
</th><th width=100> 旗舰版-Ⅱ
</th><th width=100> 旗舰版-Ⅲ
</th></tr>
<tr>
<td> 价格
</td><td> 免费七天
</td><td> 399元/年
</td><td> 3899元/年
</td><td> 7899元/年
</td><td> 28999元/年
</td><td> 38999元/年
</td></tr>
<tr>
<td> 空间
</td><td> 5G
</td><td> 20G
</td><td> 100G
</td><td> 500G
</td><td> 1.5T
</td><td> 3T
</td></tr>
<tr>
<td> 流量
</td><td> 1G
</td><td> 60G/月
</td><td> 500G/月
</td><td> 1000G/月
</td><td> 3000G/月
</td><td> 5000G/月
</td></tr>
</tbody></table>

### 云通讯服务（IM）
主要用于构建高并发和无人数限制的聊天室功能，同时也能够用来做可靠的 1V1 私信消息：
<table class="t" style="text-align: center;">
<tbody><tr>
<th width=150> 日活用户数
</th><th width=200> X &lt; 10万
</th><th width=200> 10万 ≤ X &lt; 80万
</th><th width=200> X ≥ 80万
</th></tr>
<tr>
<td> 收费标准
</td><td> 免费
</td><td> 10000元/月/10万DAU
</td><td> 咨询客服
</td></tr>
</tbody></table>

### 对象存储服务（COS）
对象存储 COS 主要用于文件的上传、存储和下载，如果您现有的服务体系中已经很完善，则不需要开通。

在收费方面，COS采用后付费方式，即每月 3-5 日生成上个月的账单并进行结算。所有用户拥有50G的免费存储空间，10G 的免费 IDC 流量，10G 的免费 CDN 回源流量，10万次PUT请求数和100万次GET请求数。

超出部分按量计费，阶梯累进，更多内容，[请点击查看文档>>](https://www.qcloud.com/document/product/430/5871)




