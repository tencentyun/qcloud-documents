## 内容分发网络 CDN 定价

CDN 提供流量计费和带宽计费两种计费模式，您可以根据自身业务形态选择合适的计费模式。

若后续您在使用中，发现您所选的计费模式不适用您的业务状态，您也可以变更计费模式，有关变更详情，请参见 [变更计费]()。

### 计费模式选择

您可以通过计算带宽利用率来选择适用的计费模式。

示例：

- 假设用户昨日 00:00 - 24:00 的消耗流量为 200GB，曲线图如下所示，此时流量消耗可以理解为图中曲线所占面积：
   ![](https://mc.qcloudimg.com/static/img/3ecfe86a031782ebeaf0b1f7595cc69f/image.png)

- 假设用户昨日 00:00 - 24:00 的带宽峰值为 40Mbps，一天为 86400 秒，此时一天的流量为 40 \* 1000 \* 86400，将单位折算为GB，为 432GB，此时可以理解为图中矩形所占面积：
   ![](https://mc.qcloudimg.com/static/img/b80d043b6e7f461d62fd2d87abf67005/image.png)

- 此时带宽利用率为：200GB / 432GB * 100% = 46%。

**选择方式：**
+ 若您的带宽利用率超过30%，表明您业务的曲线较为平稳，建议您采用带宽计费方式；
+ 若您的带宽利用率小于30%，表明您业务的曲线波动较大，建议您采用流量计费方式。

#### 大客户计费模式

若您已经在腾讯云，或未来预期在腾讯云的月消耗金额大于10万元，您可以通过商务洽谈的方式获得更优惠的价格及月结等更加灵活的计费方式。

CDN 为您提供以下几种月结计费方式，月结计费在每月5号时统一生成账单并执行扣费，并按照上月费用的120%进行费用冻结，下个月结算时，会对本次冻结的费用先解冻，再进行扣除。

+ **日峰带宽取月均**：CDN 每日带宽统计点共288个，取每一个有效日（产生消耗）的峰值和，除以有效天数，则得到日峰值带宽的月平均数据，为计费带宽，再根据合同价格计算费用；
+ **月95带宽**：CDN 每日带宽统计点共288个，从当月1号起，每一个有效日（产生消耗）的所有统计点进行排序，去掉前5%的统计点，剩下的最大的统计点，即为计费带宽，再根据合同价格计算费用；
+ **月流量**：月度累计使用的所有流量和，根据合同价格计算费用。

大客户默认的计费方式为月95带宽，其他方式需要与您的腾讯云商务经理进行约定确定，您也可以联系腾讯云获取更多价格信息。

### 带宽计费

带宽计费采用一日一结算方式，CDN 的带宽统计数据为每5分钟一个，即每天 288 个统计点，在此288个点中取最大值作为计费带宽。带宽计费采用阶梯到达结算，计费阶梯如表所示：

<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width: 145px;">计费模式</th>
			<th scope="col" style="width: 154px;">带宽阶梯</th>
			<th scope="col" style="width: 180px;">单价（元/Mbps/天）</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="4" style="text-align: center; width: 145px;">带宽峰值</td>
			<td style="text-align: center; width: 154px;">0-500 Mbps</td>
			<td style="text-align: center; width: 180px;">1.1</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">500 Mbps-5 Gbps</td>
			<td style="text-align: center; width: 180px;">1</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">5 Gbps-50 Gbps</td>
			<td style="text-align: center; width: 180px;">0.9</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">大于等于50 Gbps</td>
			<td style="text-align: center; width: 180px;">低于0.74，线下谈判，以合同价为准</td>
		</tr>
	</tbody>
</table>

#### 结算方式

带宽计费结算时，采用阶梯到达计费模式，统计时间为自然日 00:00 - 24:00，扣费时间为第二天早上8:00。

假设前一日CDN的峰值带宽为 X，阶梯计算方式如下：

+ 若 X < 500 Mbps，则账单费用为 X \* 1.1；
+ 若 500 Mbps <= X < 5000 Mbps，则账单费用为 X \* 1.0；
+ 若 5000 Mbps <= X < 50000Mbps，则账单费用为 X \* 0.9；
+ 若 X >= 50000Mbps，请联系我们进行线下签约，更多优惠方式供您选择。

【注意事项】

- 带宽计费模式为先使用后扣费，即后付费模式；
- 为了防止恶意流量给您带来不必要的损失，默认的带宽上限为10Gbps；
- 带宽进制为1000进制，其中 1Gbps = 1000 Mbps，1 Mbps = 1000 Kbps， 1 Kbps = 1000 bps。

###  流量计费

流量计费采用一日一结算方式，CDN 的流量统计数据为每5分钟一个，即每天 288 个统计点，将此288个点进行累加得到当日的计费流量。流量计费采用月度阶梯到达结算，计费阶梯如表所示：

<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width:98px">计费模式</th>
			<th scope="col" style="width: 170px;">流量阶梯</th>
			<th scope="col" style="width: 189px;">单价（元/GB）</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="5" style="text-align:center; width:98px">月流量</td>
			<td style="text-align: center; width: 170px;">0GB-2TB</td>
			<td style="text-align: center; width: 189px;">0.34</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">2TB-10TB</td>
			<td style="text-align: center; width: 189px;">0.32</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">10TB-50TB</td>
			<td style="text-align: center; width: 189px;">0.3</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">50TB-100TB</td>
			<td style="text-align: center; width: 189px;">0.28</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">大于等于100TB</td>
			<td style="text-align: center; width: 189px;">低于0.25，，线下谈判，以合同价为准</td>
		</tr>
	</tbody>
</table>

#### 结算方式

流量计费与带宽计费不同，按照月度流量进行阶梯累计，而后按日进行结算。统计时间为自然日 00:00 - 24:00，扣费时间为第二天早上8:00。

计算方式如下：

+ 若为1月1日，产生流量为3TB，如下图所示。图中灰色为实际计费阶梯，绿色为1月1日产生的流量，其中2TB落入 0TB-2TB的计费阶梯，1TB落入2TB-10TB的计费阶梯，因此1月1日这一天的实际费用为：2 \* 1000 \* 0.34 + 1 \* 1000 \* 0.32；![](https://mc.qcloudimg.com/static/img/bfdae242f6cca57421a65e46a96b0c67/image.png)

+ 若1月2日这一天也产生了3TB的流量，如下图所示。流量计费采用月度累计，因此1月2日产生的流量均落入 2TB-10TB的计费阶梯，因此1月2日这一天的实际费用为：3 \* 1000 \* 0.32；![](https://mc.qcloudimg.com/static/img/f62d1056c1c2cab249cec62ad6e74ddc/image.png)

+ 若1月3日这一天产生了7TB的流量，如下图所示。此时3号的7TB中，有5TB落入2TB-10TB的计费阶梯，2TB落入10TB-50TB的计费阶梯，因此1月3日这一天的实际费用为：5 \* 1000 \* 0.32 + 2 \* 1000 \* 0.3；![](https://mc.qcloudimg.com/static/img/954e2d483e31afd411f9a91ebd7f66c8/image.png)

以此类推，计算出当月每一天的费用，当2月1日开始计费时，一切从0开始重新阶梯累进。

【注意事项】

- 流量计费为先使用后付费，因此为后付费模式；
- 流量进制为1000，1 TB = 1000 GB， 1 GB = 1000 MB， 1 MB = 1000 KB， 1KB = 1000 B。

#### 流量包抵扣

当您的计费方式为流量计费时，您可以通过购买预付费的流量包来进行抵扣，[前往购买](http://manage.qcloud.com/shoppingcart/shop.php?tab=cdn)。

【注意事项】

- 流量包购买当日生效，普通流量包的有效期为自购买日起6个月，活动派发的特殊流量包有效期视具体活动而定，一般为1个月，流量一旦过期则无法进行抵扣；
- 若您已经购买流量包，则在第二日进行费用结算时，会优先抵扣流量包，超出部分再继续按照阶梯价格进行计费。

## 购买指导

### 直接使用

在您开通了CDN服务时（如何开通？点击[开通CDN](https://www.qcloud.com/doc/product/228/3156)），您需要选择 **流量计费** 或是 **带宽计费**， 以上两种计费方式均为<font color="red">后付费模式</font>，即您可以先使用，在第二天才会进行扣费，此时您只需要保证您的腾讯云账户中拥有充足的金额，不会被扣至欠费状态。

### 购买流量包

若您在开通CDN服务时选择的是**流量计费**， 则您可以通过购买流量包来进行抵扣。点击[流量包购买](http://manage.qcloud.com/shoppingcart/shop.php?tab=cdn)页面，即可看到如下各种大小的流量包：

![](https://mccdn.qcloud.com/static/img/faf8fafeda54bf592203884e4de3bb13/image.png)

您可以根据需要选择所需大小的流量包，点击**立即购买**即可，流量包使用规则可以参考[计费模型](https://www.qcloud.com/doc/product/228/2949)中流量包抵扣部分说明

## 到期提醒

### 通过资质认证的用户

- 若您是已经通过个人/企业资质认证，而后开通CDN服务的用户，当您的腾讯云账户处于欠费状态时，同时会通过短信、邮件等多种方式提醒您欠费状态，并考虑到节假日等因素，为您保留7天的缓冲时间，在第8天会停止您的CDN 加速服务；
- 您的 CDN 相关域名、配置信息会为您保留12个月，停服后，您的**所有域名全部下线，访问全部回源处理，CDN 控制台仅支持查询操作，不能进行配置修改等操作。**

### 未认证用户

- 若您未通过个人/企业资质认证，仅为试用用户，一旦您的流量包试用完毕，会立即停止您的CDN加速服务。若您想要继续使用，需要通过CDN资质认证（如何认证？参考[开通CDN](https://www.qcloud.com/doc/product/228/3156) 或者购买流量包，才能继续试用。

## 账单查询

### 查询入口

您可以在腾讯云官网**个人中心**中**消耗明细**菜单，查看您CDN账单详情，若您具备权限，可按照以下步骤查看明细数据：

1. 登录腾讯云官方网站中[个人中心](https://console.qcloud.com/developer)，在左侧**费用中心**中选择**收支明细**菜单： 
	![](https://mc.qcloudimg.com/static/img/8256b1289ebd5e9947b71465fa48d485/image.png)

2. 选择要查询的日期或时间区间： 
	![](https://mc.qcloudimg.com/static/img/30aaf40e3eac1d897008bea5c6e114e7/image.png)

3. 您可以在**交易类型**栏对费用类型进行筛选，CDN属于**按量计费扣费**： 
	![](https://mc.qcloudimg.com/static/img/503c94689aedc121151afe8790bbaced/1.png) 

### 日结账单

通过选择按量计费扣费进行过滤，您可以在结果中找到日结扣费情况：
![](https://mc.qcloudimg.com/static/img/d64c068d95a852b448191035f61e52dd/image.png)

点击详情，可查看详细的统计明细：
![](https://mc.qcloudimg.com/static/img/3e84112921f1e3d2669343e1f2830174/image.png) 

### 月结账单

CDN月收入超过10W的客户，可以选择使用按月结算计费方式。通过选择按量计费扣费过滤，可以看到CDN账单。使用了海外CDN的客户，也可以查询到对应的扣费情况。
![](https://mc.qcloudimg.com/static/img/81a53f2ea6f468dd86214252d66f07b6/image.png) 

<font color="red">海外CDN火热邀请内测中，敬请期待全量开放！</font>









