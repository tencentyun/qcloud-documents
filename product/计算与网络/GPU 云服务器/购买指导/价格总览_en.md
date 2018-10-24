## Billing

**Prepaid**: Service fee for one or several months is paid in advance. You have the permission to use and manage GCC instances.
**Postpaid**: The time granularity is accurate to seconds. All fees are charged on an hourly basis with no need to pay in advance.
A GCC instance includes network, storage (system disk, data disk), hardware (CPU, memory, GPU). For more information on the network price, please see [Network Price Overview](/doc/product/213/509). For more information on the disk price, please see [Disk Price Overview](/doc/product/213/2255).
GCC instances support two types of instances: computing GN2,GN8 and rendering GA2. You can purchase an GCC instance based on your actual needs after learning about the configurations and prices.
### Computing GN2 Instance
<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=20%>GPU<br>(Tesla M40)</th>
			<th width=11%>GPU Memory<br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>Memory<br>(DDR4)</th>
			<th>Data disk<br>(local SSD)</th>
			<th>Prepaid</th>
			<th>Postpaid</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>GN2.large</td>
					<td>&nbsp;1</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;28 cores</td>
					<td>&nbsp;&nbsp;&nbsp;56 GB</td>
					<td>&nbsp;1,650 GB</td>
					<td><b>4,288 CNY/month</b></td>
					<td><b>From 13.86 CNY/hour</b></td>
					</tr>
				<tr>
				<td>GN2.2xlarge</td>
				<td>&nbsp;2</td>
				<td>&nbsp;48 GB</td> 
				<td>&nbsp;56 cores</td>
				<td>&nbsp;112 GB</td>
				<td>&nbsp;3,300 GB</td>
				<td><b>8,576 CNY/month</b></td>
				<td><b>From 27.71 CNY/hour</b></td>
				</tr>
			</tbody>
</table>

Computing performance:
- Peak computing capacity for single GN2.large machine: 7T Flops for single-precision floating point arithmetic and 0.2T Flops for double-precision floating point arithmetic.
- Peak computing capacity for single GN2.2xlarge machine: 14T Flops for single-precision floating point arithmetic and 0.4T Flops for double-precision floating point arithmetic.

### Computing GN8 Instance
<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=20%>GPU<br>(Tesla P40)</th>
			<th width=11%>GPU Memory<br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>Memory<br>(DDR4)</th>
			<th>Prepaid</th>
			<th>Postpaid</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>GN8.LARGE56</td>
					<td>&nbsp;1</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;6 cores</td>
					<td>&nbsp;&nbsp;&nbsp;56 GB</td>
					<td><b>4,400 CNY/month</b></td>
					<td><b>From 15.09 CNY/hour</b></td>
					</tr>
				<tr>
				<td>GN8.7XLARGE224</td>
				<td>&nbsp;4</td>
				<td>&nbsp;96 GB</td> 
				<td>&nbsp;28 cores</td>
				<td>&nbsp;224 GB</td>
				<td><b>18,000 CNY/month</b></td>
				<td><b>From 61.76 CNY/hour</b></td>
				</tr>
				<tr>
				<td>GN8.14XLARGE448</td>
				<td>&nbsp;8</td>
				<td>&nbsp;192 GB</td> 
				<td>&nbsp;56 cores</td>
				<td>&nbsp;448 GB</td>
				<td><b>36,000 CNY/month</b></td>
				<td><b>From 123.52 CNY/hour</b></td>
				</tr>				
			</tbody>
</table>

Computing performance:
- Peak computing capacity for single GN8.LARGE56 machine: 12 TFLOPS for single-precision floating point arithmetic and 47 TOPS integer arithmetic(INT8).
- Peak computing capacity for single GN8.7XLARGE224 machine: 48 TFLOPS for single-precision floating point arithmetic and 188 TOPS integer arithmetic(INT8) .
- Peak computing capacity for single GN8.14XLARGE448 machine: 96 TFLOPS for single-precision floating point arithmetic and 376 TOPS integer arithmetic(INT8).

### Rendering GA2 Instance
> Note:
>GPU rendering GA2 instance is under internal trial. You can click [here](https://cloud.tencent.com/act/apply/ga2) to apply for it.

<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=20%>GPU<br>(AMD S7150)</th>
			<th width=12%>vCPU</th>
			<th>Memory<br>(DDR4)</th>
			<th>Data Disk</th>
			<th>Prepaid</th>
			<th>Postpaid</th>
		</tr>
		</thead>
		<tbody>
			<tr>
				<td>GA2.2xlarge</td>
				<td>&nbsp;1/4</td> 
				<td>&nbsp;8 cores</td>
				<td>&nbsp;16 GB</td>
				<td>&nbsp;<a href="/doc/product/362/2345">Cloud Block Storage</td>
				<td><b>1,500 CNY/month</b></td>
				<td><b>From 5.21 CNY/hour</b></td>
			</tr>
		</tbody>
</table>

Computing performance:
- Peak computing capacity for a single GCC instance is up to 3.77T Flops for single-precision floating point arithmetic.

## Renewing
 Prepaid GCC instances can not be terminated by users, but automatically terminated by the system within 7 days upon its expiration.
- GCC instance is shut down on the expiry date and put into the recycle bin automatically. It will be retained for 7 calendar days during which you can choose to renew it. The instance is terminated if it is not renewed within 7 calendar days.
- You can set auto renewal when buying an instance.

You are recommended to renew an instance before its expiration to avoid service interruption caused by a shutdown when it expires. For more information on renewal, please see [How to Renew](https://cloud.tencent.com/document/product/560/8052).
## Reclaiming
 GCC instances are reclaimed in the same way as with CVM instances. For more information, please see CVM [Instance Reclaim](/doc/product/213/4931#.E5.AE.9E.E4.BE.8B.E5.9B.9E.E6.94.B6).



