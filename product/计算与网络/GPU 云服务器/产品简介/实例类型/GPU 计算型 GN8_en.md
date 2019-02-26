## GN8 Instance Overview
**GPU computing GN8 instance** is suitable for generic GPU computing applications. It is a rapid, stable and flexible computing service based on GPU, and is applicable to many GPU computing scenarios, such as deep learning, scientific computing, etc. It is managed in the same way as with standard CVM.

>**Note:**
>GPU computing GN8 instance can be chose to base on SSD local storage. In this case, the system and data disks of GN8 instance only exist within the life cycle of the instance. When the instance expires or is terminated by users, the applications and data in the instance storage will be erased. We suggest that you back up or copy the data in the instance storage regularly.

## Applicable Scenario
GN8 Instance is especially suitable for server GPU computing workloads requiring high-performance computing capacity.
 - Deep learning;
 - Graphic database;
 - High-performance database;
 - Computational fluid dynamics;
 - Computational finance;
 - Earthquake analysis;
 - Molecular modeling;
 - Genomics and others.

## Hardware Specification
- **CPU:** High-frequency Intel Xeon E5-2680v4 (Broadwell).
- **GPU:** NVIDIA Tesla P40 GPU.
- **Memory:** DDR4.
- **Storage:** System Disk: Cloud Block Storage/SSD Cloud Storage/Local SSD Disk
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data Disk: Cloud Block Storage/Premium Cloud Storage(white list)/SSD Cloud Storage/Local SSD Disk	 
- **Network:** Network enhancement is available by default (free).

	
**GN2 instance is provided in two configurations:**
<table>
		<thead>
		<tr>
			<th width=10%>Model</th>
			<th width=11%>GPU<br>(Tesla P40)</th>
			<th width=11%>GPU Memory <br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>Memory<br>(DDR4)</th>		
			<th>Performance Metric</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>GN8.LARGE56</td>
					<td>&nbsp;1</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;6 cores</td>
					<td>&nbsp;&nbsp;&nbsp;56 GB</td>				
					<td>&nbsp;&nbsp;12 TFLOPS for single-precision floating point arithmetic<br/>&nbsp;&nbsp;47 TOPS integer arithmetic(INT8).</td>
					</tr>
				<tr>
				<td>GN8.7XLARGE224</td>
				<td>&nbsp;4</td>
				<td>&nbsp;96 GB</td>
				<td>&nbsp;28 cores</td>
				<td>&nbsp;224 GB</td>			
				<td>&nbsp;&nbsp;48 TFLOPS for single-precision floating point arithmetic<br/>&nbsp;&nbsp;188 TOPS integer arithmetic(INT8).</td>
				</tr>
				<tr>
				<td>GN8.14XLARGE448</td>
				<td>&nbsp;8</td>
				<td>&nbsp;192GB</td>
				<td>&nbsp;56 cores</td>
				<td>&nbsp;448 GB</td>				
				<td>&nbsp;&nbsp;96 TFLOPS for single-precision floating point arithmetic<br/>&nbsp;&nbsp;376 TOPS integer arithmetic(INT8).</td>
				</tr>
			</tbody>
</table>

## Service Options
- It supports [Prepaid](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) and [Postpaid](/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9).
- It can be launched in basic network and [VPC](/doc/product/213/5227).
- It can be interfaced with [Load Balance](/doc/product/214/524) and other businesses, without additional management and OPS costs. Private network traffic is free of charge.













