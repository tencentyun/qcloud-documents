Cloud Block Storage is a low-cost, highly available, highly reliable and customizable network block device, which can be used as a standalone scalable hard disk for CVM. It provides data storage at data block level and employs a 3-copy distributed mechanism, thus ensuring the data reliability for CVM. CBS provides three types of cloud storages, and different types of storages have different performance characteristics and prices. Users can choose storage performance and corresponding cost based on the application requirements of deployment:

## HDD Cloud Storage
### Introduction

All the HDD cloud storages (including system disks and data disks) purchased along with CVMs on the official website are (non-elastic) cloud storages. Non-elastic cloud storages do not support mounting or unmounting, and can be purchased with CVMs based on an annual/monthly plan or pay-by-usage model, and cannot be purchased separately.

### Specification

System disk: A fee-free capacity of 20 GB is provided. You can choose to buy disks with a larger capacity. It supports a maximum of 50 GB.
Data disk: A capacity from 10 GB up to 16,000 GB (in 10GB increments) is provided, and its maximum capacity to be selected varies with the specific hardware configuration.

### Performance

An IO throughput of 40-100 MB/s and a random IOPS of hundreds - one thousand are provided.

### Price

Prepaid: 0.3 CNY/GB/month
Postpaid: 0.042 CNY/100 G/hour

### Usage Scenarios

- High data reliability: HDD cloud storage uses HDD as storage media, and employs a distributed 3-copy mechanism to achieve highly reliable data storage
- Applicable to low-load business: It is ideal for application scenarios where data is not frequently accessed or the I/O load is low

## SSD Cloud Storage
### Introduction

Based on the full SSD storage media, SSD cloud storages can provide I/O capabilities featured by low latency, high random IOPS and high throughput, and high-performance storage with 99.999999% data security by leveraging the 3-copy distributed storage technology of Tencent Cloud CBS. SSD cloud storage can be used as a standalone scalable hard disk for CVM. Currently, SSD cloud storages can only be purchased along with high-IO CVM instances.

### Specification

A capacity from 250 GB up to 4 TB (in 10 GB increments) is provided

### Performance

A single SSD cloud storage can provide a random read/write IOPS of 24,000, and a throughput of 260 MB/sec. Specific performance values depend on the purchased capacity:

| Performance Indicator | Computing |
|---------|---------|
| IOPS | {min 24\*capacity, max 24,000}<br>24 IOPS are provided per GB, and the upper limit is 24,000; the minimum IOPS value is 6,000; |
| Throughput | {min 150+0.147\*(Purchased capacity-250GB), max 260} MB/s<br>The minimum throughput value is 150 MB/s with an increment of 0.147 MB/s per GB and the upper limit is 260 MB/s; |
| Latency | 0.5-2 ms |

Compared with HDD cloud storages, the performance of SSD cloud storages increases 20+ times for the random IOPS and 8-16 times for the throughput; also, it is normal for IOPS performance of SSD cloud storages to have a fluctuation of about 10% in general;

### Price

Prepaid: 1.1 CNY/GB/month
Postpaid: 0.332 CNY/hour/100 GB

### Usage Scenarios

- High performance, high data reliability:  Suitable for high-load, critical core business systems. Provides three copies of redundant data, with excellent data backup, snapshot capability and can recover data within seconds 
- Medium and large database: able to support medium and large relational database applications such as MySQL, Oracle, SQL Server, MongoDB which have table with millions of rows 
- Core business system: I/O-intensive applications and other core business systems with high data reliability requirements 
- Big data analysis:  Provides distributed processing capabilities for data calculated in TB or PB, suitable for data analysis, digging, business intelligence and other fields

## Premium Cloud Storage

### Specification

A capacity from 50 GB up to 4 TB is provided

### Performance

| Performance Indicator | Computing |
|---------|---------|
| IOPS | {min 1,500, max 4,500}<br>Formula: 1,500 + disk capacity\*8; |
| Throughput | {min 75, max 130} MB/s<br>Formula: 75 MB/s + CBS capacity\*0.147;<br>The minimum throughput value is 75 MB/s, and the upper limit is 130 MB/s; |
| Latency | 0.5-2 ms |

### Price

Annual or monthly plan: RMB 0.35/GB/month

Pay by usage: RMB 0.0009/GB/hour

### Usage Scenarios

You can purchase premium cloud storages to meet the following requirements:

- Suitable for 90% of the I/O scenarios. Best choice if you want a storage with both high quality and lost cost
- Suitable for medium to small sized databases, web servers and so on. Can provide long-term and stable IO performance
- It can satisfy the IO demands for testing core businesses and developing integrated testing environment


## Comparison of Various Block Storage Devices
<table class="cvmMonth">
        <tbody><tr>
            <th style="width: 10%;" rowspan="2">Item</th>
            <th style="width: 40%;" colspan="2">Local disk</th>
            <th style="width: 50%;" colspan="3">Cloud disk</th>
        </tr>
        <tr>
            <th>Local HDD</th>
            <th>SSD local disk</th>
			<th>HDD cloud storage</th>
			<th>SSD cloud storage</th>
            <th>Premium cloud storage</th>
        </tr>
        <tr>
            <td>Capacity of a single disk (used as a data disk)</td>
            <td>10GB - 1,000 GB</td>
            <td>10GB - 250 GB</td>
						<td>10 GB - 16,000 GB</td>
            <td>250GB - 4,000 GB</td>
            <td>50GB - 4,000 GB</td>
        </tr>
        <tr>
            <td>Maximum throughput</td>
            <td>40-hundreds MB/s</td>
            <td>300 MB/s</td>
						<td>40-100 MB/s</td>
            <td>150-260 MB/s</td>
            <td>75-130 MB/s</td>
        </tr>
					<tr>
            <td>Formula for calculating throughput performance</td>
            <td>N/A</td>
            <td>N/A</td>
						<td>N/A</td>
            <td>Throughput={min 150+0.147*(purchased capacity-250GB), max 260} MB/s<br>
The minimum throughput value is 150 MB/s with an increment of 0.147 MB/s per GB and the upper limit is 260 MB/s;</td>
            <td>Throughput={min 75+disk capacity*0.147, max 130} MB/s<br>The minimum throughput value is 75 MB/s, and the upper limit is 130 MB/s;
</td>
        </tr>
        <tr>
            <td>Maximum IOPS</td>
            <td>Hundreds-2,000</td>
            <td>30,000</td>
						<td>Hundreds-1,000</td>
            <td>6,000-24,000</td>
            <td>1,500-4,500</td>
        </tr>
				<tr>
            <td>Formula for calculating IOPS performance</td>
            <td>N/A</td>
            <td>N/A</td>
						<td>N/A</td>
            <td>IOPS={min 6,000+24*capacity, max 24,000}<br>
24 IOPS are provided per GB, and the upper limit is 24,000; the minimum IOPS value is 6,000;</td>
            <td>IOPS={min 1,500+8*capacity, max 4,500}<br>
8 IOPS are provided per GB, and the upper limit is 4,500; the minimum IOPS value is 1,500;
</td>
        </tr>
								<tr>
            <td>Price</td>
            <td>Annual or monthly plan: RMB 0.3/GB/month<br>
Pay by usage: RMB 0.042/100G/hour</td>
            <td>Annual or monthly plan: RMB 0.8/GB/month<br>
Pay by usage: RMB 0.33/hour/100GB</td>
            <td>Annual or monthly plan: RMB 0.3/GB/month<br>
Pay by usage: RMB 0.042/hour/100GB</td>
						<td>Annual or monthly plan: RMB 1.1/GB/month<br>
Pay by usage: RMB 0.332/hour/100GB</td>
            <td>Annual or monthly plan: RMB 0.35/GB/month<br>
Pay by usage: RMB 0.09/hour/100GB</td>
        </tr>
        
    </tbody></table>
    


