## 内容分发网络 CDN 定价

CDN 提供流量计费和带宽计费两种计费模式，均为 后付费按日结算，前一天 00:00:00 - 23:59:59 产生的总消耗，会在第二天进行计算扣费

若后续您在使用中，发现您所选的计费模式不适用您的业务状态，您也可以变更计费模式，有关变更详情，请参见 [变更计费](/doc/product/439/6802)。

### 带宽计费

CDN 带宽计费采用阶梯到达模式，价格阶梯如下所示：

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

假设前一日CDN的峰值带宽为 X，阶梯计算方式如下：

+ 若 X < 500 Mbps，则账单费用为 X \* 1.1；
+ 若 500 Mbps <= X < 5000 Mbps，则账单费用为 X \* 1.0；
+ 若 5000 Mbps <= X < 50000Mbps，则账单费用为 X \* 0.9；
+ 若 X >= 50000Mbps，请联系我们进行线下签约，更多优惠方式供您选择。

您可以使用 价格计算器 进行费用估算

###  流量计费

CDN 流量计费采用月度阶梯累进结算，计费阶梯如表所示：

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

### 流量包计费

采用 **流量计费** 模式的客户，可以购买流量包进行抵扣。系统在计费时会优先抵扣流量包，超出部分再继续按照阶梯价格进行计费。

#### 流量包价格

| 流量包大小 | 价格（元/个） | 有效时间 |
|--------|--------| --------| 
| 100 GB | 34 | 6个月 |
| 200 GB | 68 | 6个月 |
| 500 GB | 170 | 6个月 |
| 1 TB | 348 | 6个月 |
| 2 TB | 696 | 6个月 |
| 5 TB | 1679 | 6个月 |

流量包优惠活动正在进行中，点击[立即购买](http://manage.qcloud.com/shoppingcart/shop.php?tab=cdn)。

#### 抵扣说明

+ 流量包购买当日生效，普通流量包的有效期为自购买日起6个月，活动派发的特殊流量包有效期视具体活动而定，一般为1个月，流量一旦过期则无法进行抵扣

### 大客户计费

若您已经在腾讯云，或未来预期在腾讯云的月消耗金额大于10万元，您可以通过商务洽谈的方式获得更优惠的价格及月结等更加灵活的计费方式。

CDN 为您提供以下几种月结计费方式，月结计费在每月5号时统一生成账单并执行扣费，并按照上月费用的120%进行费用冻结，下个月结算时，会对本次冻结的费用先解冻，再进行扣除。

+ **日峰带宽取月均**：CDN 每日带宽统计点共288个，取每一个有效日（产生消耗）的峰值和，除以有效天数，则得到日峰值带宽的月平均数据，为计费带宽，再根据合同价格计算费用；
+ **月95带宽**：CDN 每日带宽统计点共288个，从当月1号起，每一个有效日（产生消耗）的所有统计点进行排序，去掉前5%的统计点，剩下的最大的统计点，即为计费带宽，再根据合同价格计算费用；
+ **月流量**：月度累计使用的所有流量和，根据合同价格计算费用。

大客户默认的计费方式为月95带宽，其他方式需要与您的腾讯云商务经理进行约定确定，您也可以联系腾讯云获取更多价格信息。

### 计费模式选择

CDN为您提供了两种计费模式：流量计费 和 带宽计费，您可以根据自身业务形态选择合适的计费模式。您可以通过计算带宽利用率来选择适用的计费模式，带宽利用率计算方式示例如下：

示例：

- 假设用户昨日 00:00 - 24:00 的消耗流量为 200GB，曲线图如下所示，此时流量消耗可以理解为图中曲线所占面积：
   ![](https://mc.qcloudimg.com/static/img/3ecfe86a031782ebeaf0b1f7595cc69f/image.png)

- 假设用户昨日 00:00 - 24:00 的带宽峰值为 40Mbps，一天为 86400 秒，此时一天的流量为 40 \* 1000 \* 86400，将单位折算为GB，为 432GB，此时可以理解为图中矩形所占面积：
   ![](https://mc.qcloudimg.com/static/img/b80d043b6e7f461d62fd2d87abf67005/image.png)

- 此时带宽利用率为：200GB / 432GB * 100% = 46%。

**选择方式：**
+ 若您的带宽利用率超过30%，表明您业务的曲线较为平稳，建议您采用带宽计费方式；
+ 若您的带宽利用率小于30%，表明您业务的曲线波动较大，建议您采用流量计费方式。

## 购买指导

CDN 为<font color="red">后付费产品</font>，先使用后付费，无需提前付费购买，即可直接使用。

登陆 [腾讯云CDN官方页面](https://cloud.tencent.com/product/cdn.html)，点击 【立即使用】：
![](https://mc.qcloudimg.com/static/img/37e78fb6baeade5c4d83e0554e909b24/image.png)

CDN 为后付费产品，需要先经过实名认证：
![](https://mc.qcloudimg.com/static/img/e207ea6d36bb48898844cdb8878f5620/image.png)
若您已经通过实名认证，则跳过此步骤。

完成认证后，选择计费方式，即可开通 CDN 服务：
![](https://mccdn.qcloud.com/static/img/f5d3235f86db2992ad6d01d1e3d07d04/image.png)

若您选择使用流量计费，可以购买流量包进行抵扣，[点击购买](http://manage.qcloud.com/shoppingcart/shop.php?tab=cdn)。

## 到期提醒

### 通过资质认证的用户

- 若您是已经通过个人/企业资质认证，而后开通CDN服务的用户，当您的腾讯云账户处于欠费状态时，同时会通过短信、邮件等多种方式提醒您欠费状态，并考虑到节假日等因素，为您保留7天的缓冲时间，在第8天会停止您的CDN 加速服务；
- 您的 CDN 相关域名、配置信息会为您保留12个月，停服后，您的**所有域名全部下线，访问全部回源处理，CDN 控制台仅支持查询操作，不能进行配置修改等操作。**

### 未认证用户

- 若您未通过个人/企业资质认证，仅为试用用户，一旦您的流量包试用完毕，会立即停止您的CDN加速服务。若您想要继续使用，需要通过CDN资质认证（如何认证？参考[开通CDN](/doc/product/439/6803) 或者购买流量包，才能继续试用。





