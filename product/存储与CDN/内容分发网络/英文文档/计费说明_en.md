CDN provides two billing methods: **Bill-by-Bandwidth** and **Bill-by-Traffic**. Both methods are **postpaid on a daily basis**. The charge for total consumption generated during 00:00:00 - 23:59:59 on the current date is billed on the next day.

## Bill-by-Bandwidth
### Tier Prices
CDN's "Bill-by-Bandwidth" method uses a tiered pricing model, with the tier prices shown as below:
<table  style="width:494px">
```
<thead>
	<tr>
		<th scope="col" style="width: 145px;">Billing Method</th>
		<th scope="col" style="width: 154px;">Bandwidth Tiers</th>
		<th scope="col" style="width: 180px;">Unit Price (CNY/Mbps/day)</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td colspan="1" rowspan="4" style="text-align: center; width: 145px;">Peak Bandwidth</td>
		<td style="text-align: center; width: 154px;">0-500Mbps</td>
		<td style="text-align: center; width: 180px;">0.58</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 154px;">500Mbps-5Gbps</td>
		<td style="text-align: center; width: 180px;">0.56</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 154px;">5Gbps-50Gbps</td>
		<td style="text-align: center; width: 180px;">0.54</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 154px;">≥ 50 Gbps</td>
		<td style="text-align: center; width: 180px;">< 0.53, off-line negotiation, subject to the contract price</td>
	</tr>
</tbody>
```
</table>

### Calculation Method
Assume that the CDN peak bandwidth for the previous day is X, the tiered calculation is performed as follows:
1. If X < 500 Mbps, the charge billed is X \* 0.58.
2. If 500 Mbps <= X < 5,000 Mbps, the charge billed is X \* 0.56.
3. If 5,000 Mbps <= X < 50,000 Mbps, the charge billed is X \* 0.54.
4. If X >= 50,000 Mbps, contact us for off-line contracting. We have more discount options available for you.

You can use [Price Calculator](https://buy.cloud.tencent.com/calculator/cdn) for a price estimation.

## Bill-by-Traffic
### Tier Prices
CDN's "Bill-by-Traffic" method takes a monthly tiered progressive approach, with the tier prices shown as below:
<table  style="width:494px">
```
<thead>
	<tr>
		<th scope="col" style="width:98px">Billing Method</th>
		<th scope="col" style="width: 170px;">Traffic Tiers</th>
		<th scope="col" style="width: 189px;">Unit Price (CNY/GB)</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td colspan="1" rowspan="5" style="text-align:center; width:98px">Monthly Traffic</td>
		<td style="text-align: center; width: 170px;">0GB-2TB</td>
		<td style="text-align: center; width: 189px;">0.23</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 170px;">2TB-10TB</td>
		<td style="text-align: center; width: 189px;">0.22</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 170px;">10TB-50TB</td>
		<td style="text-align: center; width: 189px;">0.21</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 170px;">50TB-100TB</td>
		<td style="text-align: center; width: 189px;">0.19</td>
	</tr>
	<tr>
		<td style="text-align: center; width: 170px;">≥ 100 TB</td>
		<td style="text-align: center; width: 189px;">< 0.14, off-line negotiation, subject to the contract price</td>
	</tr>
</tbody>
```
</table>

### Calculation Method
Unlike "Bill-by-Bandwidth", "Bill-by-Traffic" method takes a tiered progressive approach based on monthly traffic. Examples on how to calculate the charge are illustrated as shown below:
+ If the traffic consumed on January 1 is 3 TB, as shown in the figure below. The gray bar in the figure is the actual billing tier, and green bar is the traffic consumed on January 1, out of which 2 TB falls into 0 TB - 2 TB billing tier and the remaining 1 TB into 2 TB - 10 TB billing tier. Thus the actual charge billed for January 1 equals 2 \* 1000 \* 0.23 + 1 \* 1000 \* 0.22.
  ![](https://mc.qcloudimg.com/static/img/bfdae242f6cca57421a65e46a96b0c67/image.png)

+ If the traffic consumed on January 2 is also 3 TB, as shown in the figure below. The traffic is billed by traffic on a monthly basis. In this way, the total traffic consumed on January 2 falls into 2 TB - 10 TB billing tier, and the actual charge billed for January 2 equals 3 \* 1000 \* 0.22.
  ![](https://mc.qcloudimg.com/static/img/f62d1056c1c2cab249cec62ad6e74ddc/image.png)

+ If the traffic consumed on January 2 is 7 TB, as shown in the figure below. Among the 7 TB, 4 TB falls into 2 TB - 10 TB billing tier and 3 TB into 10 TB - 50 TB billing tier, so the actual charge billed for January 3 equals 4 \* 1000 \* 0.22 + 3 \* 1000 \* 0.21.
  ![](https://mc.qcloudimg.com/static/img/954e2d483e31afd411f9a91ebd7f66c8/image.png)

By such a way, the charge for each day in January can be calculated. From February 1, a new progressive billing process is started from scratch. You can also use [Price Calculator](https://buy.cloud.tencent.com/calculator/cdn) for a price estimation.

## Traffic Package
If you select "Bill-by-Traffic", you can purchase a traffic package from which the traffic consumed is deducted. Traffic consumed is deducted preferably from the traffic package, and the traffic beyond the package quota is billed based on tiered prices.

Special offer campaign for traffic package is underway. Click [Buy Now](https://buy.cloud.tencent.com/cdn_package).

### Note on Traffic Package Deduction
The traffic package takes effect on the day of purchase. The validity period of ordinary traffic package is 6 months from the date of purchase. The validity period of special traffic package provided during special offer campaign varies with campaign policies, which is generally one month. Your traffic package is only valid during the validity period. Any unused traffic expires as the traffic package expires.

## Billing for Key Customers
If your monthly consumption amount in Tencent Cloud is or will be more than 100k CNY, you can be granted more favorable prices and more flexible billing options (such as payment on a monthly basis) through negotiations.

+ **Bill by monthly average value of daily bandwidth peaks**: There are 288 CDN bandwidth statistical points each day. Calculate the billing bandwidth by taking the average of peaks on each effective day. Then calculate the charge based on contract price.
> Computing Examples
> The billing process starts on February 1, 2017. The contract price is P CNY/Mbps/month.
> Effective day: It is a day on which the consumption generated is greater than 1 Kbps.
> Assume that the traffic consumption generated is more than 1 Kbps for 14 days in February, the maximum of 288 statistical points per day is Max_1, Max_2, Max_3 ... Max_14, and the billing bandwidth is Average (Max_1, Max_2, ..., Max_14), so the charge billed in February is: Average (Max_1, Max_2, ..., Max_14) x P x 14/28.

+ **Monthly 95th Percentile**: There are 288 CDN bandwidth statistical points each day. Sort all statistical points for all effective days from the first day of current month (generating consumption) by bandwidth value and eliminate the first 5% statistical points. Then take the largest bandwidth among the remaining 95% of statistical points as the billing bandwidth. Then calculate the charge based on contract price.
> Computing Examples
> The billing process starts on February 1, 2017. The contract price is P CNY/Mbps/month.
> Effective day: It is a day on which the consumption generated is greater than 1 Kbps.
> Assume that the traffic consumption generated is more than 1 Kbps for 14 days in February, calculate all statistical points for these 14 days (14 \* 288) and eliminate the first 5% statistical points. Then take the largest value among the remaining statistical points as the billing bandwidth, which is Max95. The charge billed in February is: Max95 x P x 14 / 28.

+ **Bill by monthly traffic**: Calculate the total traffic consumed on a monthly basis. Then calculate the charge based on contract price.

For more information, please call 4009-100-100 or [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=83&level2_id=85&level1_name=%E5%AD%98%E5%82%A8%E4%B8%8ECDN&level2_name=%E5%86%85%E5%AE%B9%E5%88%86%E5%8F%91%E7%BD%91%E7%BB%9C%20%20CDN).

## Billing Methods
CDN provides two billing methods: **Bill-by-Traffic** and **Bill-by-Bandwidth**. You can choose one that is best suitable for your business type. You can also choose the proper method by calculating the bandwidth utilization, which is calculated as shown in the example below:
Assume that a user consumed 200 GB traffic from 00:00 am to 11:59 pm yesterday, as shown in the figure below. The consumed traffic during this time period can be illustrated as the area defined by the curve in the figure:
![](https://mc.qcloudimg.com/static/img/3ecfe86a031782ebeaf0b1f7595cc69f/image.png)
If the user has a bandwidth peak of 40 Mbps from 00:00 am to 11:59 pm yesterday, the traffic of the day is 40 \* 1000 \* 86400 (There are 86,400 seconds a day). After converted to the unit of GB, the result is 432 GB. In this case, the consumed traffic is illustrated as the area defined by the rectangle in the figure:
![](https://mc.qcloudimg.com/static/img/b80d043b6e7f461d62fd2d87abf67005/image.png)
The bandwidth utilization during this time period is: 200 GB/432 GB*100%=46%.

**Guidelines on how to select the billing method:**
+ If your bandwidth utilization is more than 30%, which means your business curve is flat, you're recommended to select "Bill-by-Bandwidth".
+ If your bandwidth utilization is less than 30%, which means your business curve has substantial fluctuations, you're recommended to select "Bill-by-Traffic".
