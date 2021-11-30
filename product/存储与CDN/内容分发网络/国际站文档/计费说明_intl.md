
CDN provides two billing methods:  **Pay by Bandwidth** and **Pay by Traffic**. Both methods use a <font color="red">post-payment policy and charged on a daily basis</font>. The charge for total consumption generated during 00:00:00 - 23:59:59 on the current date will be billed the next day.

## Pay by Bandwidth
### Tiered Prices
CDN's "Pay by Bandwidth" method uses a tiered pricing model, with the tiered prices shown as below:
<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width: 145px;">Billing Model</th>
			<th scope="col" style="width: 154px;">Bandwidth Tiers</th>
			<th scope="col" style="width: 180px;">Unit Price (USD/Mbps/Day)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="4" style="text-align: center; width: 145px;">Bandwidth Peak</td>
			<td style="text-align: center; width: 154px;">0 - 500Mbps</td>
			<td style="text-align: center; width: 180px;">0.094</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">500Mbps - 5Gbps</td>
			<td style="text-align: center; width: 180px;">0.092</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">5Gbps - 50Gbps</td>
			<td style="text-align: center; width: 180px;">0.086</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 154px;">>= 50Gbps</td>
			<td style="text-align: center; width: 180px;">0.084, or subject to the contract price</td>
		</tr>
	</tbody>
</table>


### Calculation Method
Assume that the CDN peak bandwidth for the previous day is X, the tiered calculation is performed as follows:

> If X < 500 Mbps, the charge billed is X  &times; 0.094;
> If 500Mbps <= X < 5000Mbps, the charge billed is X  &times; 0.092;
> If 5000Mbps <= X < 50000Mbps, the charge billed is X &times; 0.086;
> If X >= 50000Mbps, the charge billed is X &times; 0.084. You may also contact us for off-line contracting. We have more discount options available for you.



## Pay by Traffic

### Tiered Prices
CDN's "Pay by Traffic" method takes a monthly tiered progressive approach, with the tiered prices shown as below:
<table  style="width:494px">
	<thead>
		<tr>
			<th scope="col" style="width:98px">Billing Model</th>
			<th scope="col" style="width: 170px;">Traffic Tiers</th>
			<th scope="col" style="width: 189px;">Unit Price (USD/GB)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="1" rowspan="5" style="text-align:center; width:98px">Monthly Tiered Traffic</td>
			<td style="text-align: center; width: 170px;">0GB - 2TB</td>
			<td style="text-align: center; width: 189px;">0.037</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">2TB - 10TB</td>
			<td style="text-align: center; width: 189px;">0.035</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">10TB - 50TB</td>
			<td style="text-align: center; width: 189px;">0.032</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">50TB - 100TB</td>
			<td style="text-align: center; width: 189px;">0.026</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 170px;">>= 100TB</td>
			<td style="text-align: center; width: 189px;"> 0.02, or subject to the contract price</td>
		</tr>
	</tbody>
</table>


### Calculation Method

Unlike "Pay by Bandwidth", "Pay by Traffic" method takes a tiered progressive approach based on monthly traffic. Examples on how to calculate the charge are illustrated as shown below:

+ If the traffic consumed on January 1 is 3TB, as shown in the figure below: The gray bar in the figure is the actual billing tier, and green bar is the traffic consumed on January 1, out of which 2TB falls into 0TB - 2TB billing tier and the remaining 1TB into 2TB - 10TB billing tier, so the actual charge billed for January 1 equals 2\* 1000 \* 0.34 + 1\* 1000\* 0.32;
  ![](https://mc.qcloudimg.com/static/img/bfdae242f6cca57421a65e46a96b0c67/image.png)

+ If the traffic consumed on January 2 is also 3TB, as shown in the figure below: The traffic will be accumulated on a monthly basis for "Pay by Traffic" method. In this way, the total traffic consumed on January 2 falls into 2TB - 10TB billing tier, and the actual charge billed for January 2 equals 3\* 1000\* 0.32;
  ![](https://mc.qcloudimg.com/static/img/f62d1056c1c2cab249cec62ad6e74ddc/image.png)

+ If the traffic consumed on January 3 is 7TB, as shown below: Among the 7TB, 4TB falls into 2TB - 10TB billing tier and 3TB into 10TB - 50TB billing tier, so the actual charge charged for January 3 equals 4\* 1000\* 0.32 + 3\* 1000\* 0.3;
  ![](https://mc.qcloudimg.com/static/img/954e2d483e31afd411f9a91ebd7f66c8/image.png)

By such a way, the charge for each day in January can be calculated. From February 1, a new progressive billing process will be started from scratch.

## Billing for Key Account Customers
If your monthly consumption amount in Tencent Cloud is or will be more than USD 20,000, you can be granted more favorable prices and more flexible billing options (such as payment on a monthly basis) through negotiations.

+ **Pay by monthly average value of daily bandwidth peaks**: There are 288 CDN bandwidth statistical points each day. Divide the sum of peaks on each effective day (generating consumption) by the number of effective days to get the monthly average value of daily bandwidth peaks to use as billing bandwidth. Then calculate the charge based on contract price;
+ **Pay by 95% of bandwidths in a month**: There are 288 CDN bandwidth statistical points each day. Sort all statistical points for all effective days from the first day of current month (generating consumption) by bandwidth value and eliminate the first 5% statistical points. Then take the largest bandwidth among the remaining 95% of statistical points as the billing bandwidth. Then calculate the charge based on contract price;
+ **Pay by monthly traffic**: Calculate the total traffic consumed on a monthly basis. Then calculate the charge based on contract price.

For more details, please submit a ticket.


## Billing Model Options
CDN provides two billing models - **Pay by Bandwidth** and **Pay by Traffic**. You can choose the billing model that is best suitable for your business type. You can select the right billing model by calculating the bandwidth utilization, which is calculated as shown in the example below:

Assume that the user consumed 200GB traffic from 00:00 am to 11:59 pm yesterday, as shown in the figure below. The consumed traffic during this time period can be illustrated as the area defined by the curve in the figure:
   ![](https://mc.qcloudimg.com/static/img/3ecfe86a031782ebeaf0b1f7595cc69f/image.png)

If the user has a bandwidth peak of 40Mbps from 00:00 am to 11:59 pm yesterday, the traffic of the day is 40\* 1000\* 86400 (There are 86,400 seconds a day). After converted to the unit of GB, the result will be 432GB. In this case, the consumed traffic is illustrated as the area defined by the rectangle in the figure:
   ![](https://mc.qcloudimg.com/static/img/b80d043b6e7f461d62fd2d87abf67005/image.png)

The bandwidth utilization during this time period is: 200GB/432GB * 100% = 46%.

**Guidelines on how to select the billing method:**
+ If your bandwidth utilization is more than 30%, which means your business curve is flat, you're recommended to select "Pay by Bandwidth"; 
+ If your bandwidth utilization is less than 30%, which means your business curve has substantial fluctuations, you're recommended to select "Pay by Traffic".


