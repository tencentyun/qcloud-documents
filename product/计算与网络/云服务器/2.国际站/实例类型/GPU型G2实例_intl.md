## GPU G2 Overview
**GPU G2 instance** is applicable for general GPU computing applications. It is a rapid, stable and flexible computing service based on GPU, and is applicable to video encoding/decoding, deep learning, scientific computing, and other scenarios. You can managed G2 instances in the same way as with standard CVMs.

## Application Scenarios
GN2 Instance is the best choice for server-side GPU computing workloads, which require excellent graphic processing and high-performance computing capacities.
 - Deep Learning
 - Graphic database
 - High-performance database
 - Computational fluid dynamics
 - Computational finance
 - Earthquake analysis
 - Molecular modeling
 - Genomics and others

## Hardware Specification
- **CPU:** High-frequency Intel Xeon E5-2680 (Broadwell).
- **GPU:** NVIDIA Tesla M40 GPU.
- **Memory:** (DDR4).
- **Storage:** Both system disk and data disk are local SSD.	 
- **Network:** Network enhancement is available by default (free).

	
**G2 instances are provided in two configurations:**
<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=11%>GPU<br>(Tesla M40)</th>
			<th width=11%>GPU Memory<br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>Memory<br>(DDR4)</th>
			<th>Data disk<br>(local SSD)</th>
			<th>Performance Metric</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>G2.large</td>
					<td>&nbsp;1</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;28 cores</td>
					<td>&nbsp;&nbsp;&nbsp;60 GB</td>
					<td>&nbsp;1,650 GB</td>
					<td>Peak computing capacity for single machine:<br/>&nbsp;&nbsp;&nbsp;&nbsp;7T Flops for single-precision floating point arithmetic.<br/>&nbsp;&nbsp;0.2T Flops for double-precision floating point arithmetic.</td>
					</tr>
				<tr>
				<td>G2.2xlarge</td>
				<td>&nbsp;2</td>
				<td>&nbsp;48 GB</td>
				<td>&nbsp;56 cores</td>
				<td>&nbsp;120 GB</td>
				<td>&nbsp;3,300 GB</td>
				<td>Peak computing capacity for single machine:<br/>&nbsp;&nbsp;&nbsp;&nbsp;14 T Flops for single-precision floating point arithmetic.<br/>&nbsp;&nbsp;&nbsp;0.4 T Flops for double-precision floating point arithmetic.</td>
				</tr>
			</tbody>
</table>

## Service Options
- It supports one billing methods: [Postpaid](/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9).
- It can be launched in basic network and [VPC](/doc/product/213/5227).
- It can be accessed with [Load Balance](/doc/product/214/524) and other Tencent Cloud services, without additional management and OPS costs. Private network traffic is free of charge.

