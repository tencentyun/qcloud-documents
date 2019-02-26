## Overview
Local disk is a storage device located on the same physical server as the CVM instance and features high read/write IO and low latency.
It is a local storage reserved on the physical machine where the CVM resides in. You can choose local disks as system disks and data disks for most of Tencent instances.

- **Lifecycle**: Local disk is created with the creation of CVM instance, so its life cycle is same as that of CVM.
- **Purchase**: Local disk can only be enabled with the enabling of CVM, which means you can specify a local disk only when purchasing a CVM instance. For more information about purchasing a CVM, please see [Purchase and Enable an Instance](/doc/product/213/4855).

>**Note:**
>For a CVM with local disk, you cannot upgrade hardware (CPU and memory), and can only upgrade bandwidth.

## Type
Local disk is a local storages on the physical machine where the CVM resides in, and can be classified into local HDDs and SSDs according to their media.
### Local HDD
<table class="typical">
	<tbody>
	<tr>
		<th>Type</th>
		<th>Available specification</th>
		<th>Performance</th>
		<th>Price</th>
	</tr>
	<tr>
		<td>System disk</td>
		<td>Always 50 GB and unchangeable</td>
		<td rowspan="2">Peak throughput: 40 - 100 MB/s. IOPS: hundreds - 1000.</td>
		<td rowspan="2">Prepaid: 0.3 CNY/GB/month<br>Postpaid: 0.00042 CNY/GB/hour</td>
	</tr>
	
	<tr>
		<td>Data disk</td>
		<td>A capacity ranging from 10 GB to 1600 GB (in 10 GB increments) is supported. The maximum capacity supported varies with hardware configuration.</td>
	</tr>
</tbody></table>

### Local SSD
Local SSD is a local storage on the physical machine where the CVM resides in. It provides instances with full SSD block-level data access capability with a low latency, high random IOPS, and high I/O throughput.
<table class="SSD">
	<tbody>
	<tr>
		<th>Type</th>
		<th>Available specification</th>
		<th>Performance</th>
		<th>Price</th>
	</tr>
	<tr>
		<td >System disk</td>
		<td>Always 50 GB and unchangeable</td>
		<td rowspan="2">Peak throughput: 250 MB/s<br>Its IOPS for random write reaches up to 10000 (blocksize = 4k, iodepth = 32)<br>Its IOPS for random read reaches up to 75000 (blocksize = 4k, iodepth = 32)<br>Access latency is less than 3 ms.
</td>
		<td rowspan="2">Prepaid: 0.8 CNY/GB/month<br/>Postpaid: 0.0033 CNY/GB/hour</td>
	</tr>
	<tr>
		<td>Data disk</td>
		<td>A capacity ranging from 10 GB to 7000 GB (in 10 GB increments) is supported. The maximum capacity supported varies with hardware configuration.</td>
	</tr>
</tbody></table>

Local SSD is suitable for the following scenarios:

- Low latency: Access latency within microseconds. 
- Distributed application: NoSQL, MPP data warehouse, distributed file system and other I/O intensive applications. These applications themselves have distributed data redundancy. 
- Logs for large online applications: Large online applications produce a large amount of log data, which require high-performance storage with less demand on storage reliability. 
- Single point of failure (SPOF) risk: If SPOF risk exists, it is recommended to implement data redundancy at the application layer to ensure data availability.

