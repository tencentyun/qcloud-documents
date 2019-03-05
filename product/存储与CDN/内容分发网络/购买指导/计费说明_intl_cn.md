CDN 为您提供了两种计费方式： **带宽计费** 和 **流量计费** 。均为**后付费按日结算**，前一天 00:00:00 - 23:59:59 产生的总消耗，会在第二天进行计算扣费。

## 带宽计费
### 阶梯价格
CDN 带宽计费采用阶梯到达模式，价格阶梯如下所示：
<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width: 145px;">计费模式</th>
			<th scope="col" style="width: 154px;">带宽阶梯</th>
			<th scope="col" style="width: 180px;">单价（美元/Mbps/月）</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="4" style="text-align: center; width: 145px;">带宽峰值</td>
			<td style="text-align: center; width: 154px;">0-500Mbps</td>
			<td style="text-align: center; width: 180px;">4.80</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">500Mbps-5Gbps</td>
			<td style="text-align: center; width: 180px;">4.20</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">5Gbps-50Gbps</td>
			<td style="text-align: center; width: 180px;">3.90</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">大于等于 50Gbps</td>
			<td style="text-align: center; width: 180px;">低于 3.30，线下谈判，以合同价为准</td>
		</tr>
	</tbody>
</table>

### 计算方式
假设前一日 CDN 的峰值带宽为 X，阶梯计算方式如下：
1. 若 X < 500 Mbps，则账单费用为 X \* 4.80。
2. 若 500 Mbps <= X < 5000 Mbps，则账单费用为 X \* 4.20。
3. 若 5000 Mbps <= X < 50000Mbps，则账单费用为 X \* 3.90。
4. 若 X >= 50000Mbps，请联系我们进行线下签约，更多优惠方式供您选择。

您可以使用 [价格计算器](https://buy.cloud.tencent.com/calculator/cdn) 进行费用估算。

## 流量计费
### 阶梯价格
CDN 流量计费采用月度阶梯累进结算，计费阶梯如表所示：
<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width:98px">计费模式</th>
			<th scope="col" style="width: 170px;">流量阶梯</th>
			<th scope="col" style="width: 189px;">单价（美元/GB）</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="5" style="text-align:center; width:98px">月流量</td>
			<td style="text-align: center; width: 170px;">0GB-2TB</td>
			<td style="text-align: center; width: 189px;">0.055</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">2TB-10TB</td>
			<td style="text-align: center; width: 189px;">0.053</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">10TB-50TB</td>
			<td style="text-align: center; width: 189px;">0.049</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">50TB-100TB</td>
			<td style="text-align: center; width: 189px;">0.046</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">大于等于 100TB</td>
			<td style="text-align: center; width: 189px;">低于 0.040，线下谈判，以合同价为准</td>
		</tr>
	</tbody>
</table>

### 计算方式
流量计费与带宽计费不同，按照月度流量进行阶梯累进，计算方式示例如下：
+ 若 1 月 1 日产生流量为 3TB，如下图所示。图中灰色为实际计费阶梯，绿色为 1 月 1 日产生的流量，其中 2TB 落入 0TB-2TB 的计费阶梯，1TB 落入 2TB-10TB 的计费阶梯，因此 1 月 1 日这一天的实际费用为：2 \* 1000 \* 0.34 + 1 \* 1000 \* 0.32。
  ![](https://mc.qcloudimg.com/static/img/bfdae242f6cca57421a65e46a96b0c67/image.png)

+ 若 1 月 2 日这一天也产生了 3TB 的流量，如下图所示。流量计费采用月度累计，因此 1 月 2 日产生的流量均落入 2TB-10TB 的计费阶梯，因此 1 月 2 日这一天的实际费用为：3 \* 1000 \* 0.32。
  ![](https://mc.qcloudimg.com/static/img/f62d1056c1c2cab249cec62ad6e74ddc/image.png)

+ 若 1 月 3 日这一天产生了 7TB 的流量，如下图所示。此时 3 号的 7TB 中，有 4TB 落入 2TB-10TB 的计费阶梯，3TB 落入 10TB-50TB 的计费阶梯，因此 1 月 3 日这一天的实际费用为：4 \* 1000 \* 0.32 + 3 \* 1000 \* 0.3。
  ![](https://mc.qcloudimg.com/static/img/954e2d483e31afd411f9a91ebd7f66c8/image.png)

以此类推，计算出当月每一天的费用，当 2 月 1 日开始计费时，一切从 0 开始重新阶梯累进。此外，您可以使用 [价格计算器](https://buy.cloud.tencent.com/calculator/cdn) 进行成本估算。

## 大客户计费说明
若您已经在腾讯云，或未来预期在腾讯云的月消耗金额大于 2 万美元，您可以通过商务洽谈的方式获得更优惠的价格及月结等更加灵活的计费方式。

+ **日峰带宽取月均**：CDN 每日带宽统计点共 288 个，对每一个有效天的峰值取平均，得到计费带宽，再根据商务签订的合同价格计算费用。
> 计算示例：
> 客户从 2017 年 2 月 1 日 正式开始计费，签订的合同价格为：P 美元/Mbps/月
> 有效天：产生的消耗 大于 1 Kbps，则记为有效天
> 假设客户 2 月份有 14 天产生的消耗大于 1 Kbps，这 14 天每一天的 288 个统计点最大值为：Max_1、Max_2、Max_3... Max_14，计费带宽为 Average(Max_1, Max_2, ..., Max_14)，2月的费用为：Average(Max_1, Max_2, ..., Max_14)  x  P  x  14 / 28

+ **月 95 带宽**：CDN 每日带宽统计点共 288 个，从当月 1 号起，每一个有效日（产生消耗）的所有统计点进行排序，去掉前 5% 的统计点，剩下的最大的统计点，即为计费带宽，再根据合同价格计算费用。
> 计算示例：
> 客户从 2017 年 2 月 1 日正式开始计费，签订的合同价格为：P 美元/Mbps/月
> 有效天：产生的消耗 大于  1 Kbps，则记为有效天
> 假设客户 2 月份有 14 天产生的消耗大于 1 Kbps，则计费带宽为这 14 天的所有统计点 14 \* 288个，去掉最高的 5% 的点，剩余统计点中最高的为 Max95，Max95 即为计费带宽，2 月的费用为：Max95 x P x 14 / 28

+ **月流量**：月度累计使用的所有流量和，根据合同价格计算费用。

欢迎[提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=83&level2_id=85&level1_name=%E5%AD%98%E5%82%A8%E4%B8%8ECDN&level2_name=%E5%86%85%E5%AE%B9%E5%88%86%E5%8F%91%E7%BD%91%E7%BB%9C%20%20CDN) 咨询更多详情。

## 计费模式选择
CDN 为您提供了两种计费模式：**流量计费** 和 **带宽计费**，您可以根据自身业务形态选择合适的计费模式。您可以通过计算带宽利用率来选择适用的计费模式，带宽利用率计算方式示例如下：
假设用户昨日 00:00 - 24:00 的消耗流量为 200GB，曲线图如下所示，此时流量消耗可以理解为图中曲线所占面积：
![](https://mc.qcloudimg.com/static/img/3ecfe86a031782ebeaf0b1f7595cc69f/image.png)
假设用户昨日 00:00 - 24:00 的带宽峰值为 40Mbps，一天为 86400 秒，此时一天的流量为 40 \* 1000 \* 86400，将单位折算为 GB，为 432GB，此时可以理解为图中矩形所占面积：
![](https://mc.qcloudimg.com/static/img/b80d043b6e7f461d62fd2d87abf67005/image.png)
此时带宽利用率为：200GB / 432GB * 100% = 46%。

**选择方式：**
+ 若您的带宽利用率超过 30%，表明您业务的曲线较为平稳，建议您采用带宽计费方式。
+ 若您的带宽利用率小于 30%，表明您业务的曲线波动较大，建议您采用流量计费方式。
