## GN2 Instance Overview
**GCC computing GN2 instance** is suitable for generic GPU computing applications. It is a rapid, stable and flexible computing service based on GPU, and is applicable to many GPU computing scenarios, such as deep learning, scientific computing, etc. It is managed in the same way as with standard CVM.

>**Note:**
>GCC computing GN2 instance is based on SSD local storage. In this case, the system and data disks of GN2 instance only exist within the life cycle of the instance. When the instance expires or is terminated by users, the applications and data in the instance storage will be erased. We suggest that you back up or copy the data in the instance storage regularly.

## Applicable Scenario
GN2 Instance is especially suitable for server GPU computing workloads requiring high-performance computing capacity.
 - Deep learning;
 - Graphic database;
 - High-performance database;
 - Computational fluid dynamics;
 - Computational finance;
 - Earthquake analysis;
 - Molecular modeling;
 - Genomics and others.

## Hardware Specification
- **CPU:** High-frequency Intel Xeon E5-2680 (Broadwell).
- **GPU:** NVIDIA Tesla M40 GPU.
- **Memory:** DDR4.
- **Storage:** Both system disk and data disk are local SSD. You can [Purchase Elastic Cloud Disk](/doc/product/362/2732) and mount it if you need to expand the capacity.	 
- **Network:** Network enhancement is available by default (free).

	
**GN2 instance is provided in two configurations:**
<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=11%>GPU<br>(Tesla M40)</th>
			<th width=11%>GPU Memory <br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>Memory<br>(DDR4)</th>
			<th>Data disk <br>(local SSD)</th>
			<th>Performance Metric</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>GN2.7xlarge56</td>
					<td>&nbsp;1</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;28 cores</td>
					<td>&nbsp;&nbsp;&nbsp;56 GB</td>
					<td>&nbsp;1,650 GB</td>
					<td>Peak computing capacity for single machine:<br/>&nbsp;&nbsp;&nbsp;&nbsp;7T Flops for single-precision floating point arithmetic<br/>&nbsp;&nbsp;0.2T Flops for double-precision floating point arithmetic.</td>
					</tr>
				<tr>
				<td>GN2.14xlarge112</td>
				<td>&nbsp;2</td>
				<td>&nbsp;48 GB</td>
				<td>&nbsp;56 cores</td>
				<td>&nbsp;112 GB</td>
				<td>&nbsp;3,300 GB</td>
				<td>Peak computing capacity for single machine:<br/>&nbsp;&nbsp;&nbsp;&nbsp;14T Flops for single-precision floating point arithmetic<br/>&nbsp;&nbsp;0.4T Flops for double-precision floating point arithmetic.</td>
				</tr>
			</tbody>
</table>

## Service Options
- It supports [Prepaid](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) and [Postpaid](/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9).
- It can be launched in basic network and [VPC](/doc/product/213/5227).
- It can be interfaced with [Load Balance](/doc/product/214/524) and other businesses, without additional management and OPS costs. Private network traffic is free of charge.













