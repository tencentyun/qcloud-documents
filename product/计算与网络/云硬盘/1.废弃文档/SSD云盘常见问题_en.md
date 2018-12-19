### 1. When is SSD cloud storage needed?
If you encounter one of the following situations:

- Your local disk cannot be expanded, disk capacity is limited; 
- The local disk is unable to be mounted or unmounted flexibly; 
- Data has SPOF risk, SAL is only 99.95, or local disk data is lost or corrupted, resulting in irreversible loss; 
- Cannot support Hadoop big data business with massive data, high IO concurrency.

SSD cloud storage is just the tool to solve the above problems! SSD cloud storage can satisfy the following business scenarios:

- High performance, high data reliability:  Suitable for high-load, critical core business systems. Provides three copies of redundant data, with excellent data backup, snapshot capability and can recover data within seconds 
- Elastic scaling: Cloud disks can be mounted or unmounted flexibly within the region, without the need to shut down/reboot the server; the capacity of cloud storage can be configured in an elastic manner, and upgraded as required; up to 10 cloud disks can be mounted on a single virtual machine, with a capacity of up to 40 TB 
- Medium and large database: able to support medium and large relational database applications such as MySQL, Oracle, SQL Server, MongoDB which have table with millions of rows 
- Core business system: I/O-intensive applications and other core business systems with high data reliability requirements 
- Big data analysis:  Provides distributed processing capabilities for data calculated in TB or PB, suitable for data analysis, digging, business intelligence and other fields

### 2. Can I purchase SSD cloud storage separately?

SSD cloud storage can be purchased separately. Beijing Zone 1, Singapore Zone 1 and Guangzhou Zone 3 are supported synchronously.

### 3. Can I add SSD cloud storage to the original CVM or replace original HDD cloud storage with SSD cloud storage?

The SSD cloud storage is implemented using full SSD storage media, so it is not supported to replace original HDD cloud storage with SSD cloud storage. Currently, mounting/unmounting purchased SSD storage on or from CVMs are not supported either.

### 4. Can I upgrade it after purchasing?

You may adjust SSD cloud storage and expand disk capacity
### 5. My business is located in Guangzhou or Shanghai, when can I use SSD cloud storage?

Tencent cloud has launched SSD cloud storage service in Beijing, plans for Guangzhou and Shanghai are under preparation.

### 6. Does SSD cloud storage need prefetch?

After purchasing, the block storage provided by some service providers needs prefetch (Pre-Warm, such as using dd command to activate the disk) in order to reach its peak performance. Tencent cloud SSD cloud storage does not need prefetch to achieve its peak performance.
