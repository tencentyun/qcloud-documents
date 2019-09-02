### When is high-performance cloud block storage needed?

According to massive data analysis and research, high-performance cloud block storage can satisfy the demand of IO scenarios for most business. It can provide long-term, stable performance in 99.5% of its service time, to avoid uncertain impact on the business caused by frequent disk IO jitter.

### Which regions are available for purchase for high-performance cloud block storage? Can I purchase one separately?

For Open Beta Test, Beijing Zone 1, Shanghai Zone 1 and Guangzhou Zone 3 will be available for purchase. You can purchase one separately. The time for applying for OBT is to be determined.

### High-performance cloud block storage performance description

The performance of high-performance cloud block storage is proportional to its size. Random IOPS starts from 1500, and increases by 8 IOPS per GB, up to 4500; Throughput starts at 75 MBps, and
increases by 0.147 MBps per GB, up to 130 MBps.

### Can I upgrade it after purchasing?

You can adjust your high-performance cloud block storage and expand its capacity.

### Random and sequential IO

IO is either random or sequential. Random IO means read and write operations are continuous in time, but are discontinuous in access address, which is randomly distributed in the address space of the disk LUN. Major businesses that generate random IO include OLTP service, SQL, instant messaging service and so on.

Sequential IO means read and write operations continuously access data from adjacent addresses one by one, based on logical blocks. In sequential IO access, the track seeking time needed by HDD is significantly reduced because the read/write head can access the next block with minimum movement. Businesses such as data backup and journal log writing are sequential IO businesses.

### Is prefetch needed for high-performance cloud block storage?

After purchasing, the block storage provided by some service providers needs prefetch (Pre-Warm, such as using dd command to activate the disk) in order to reach its peak performance. Tencent Cloud high-performance cloud block storage can achieve its peak performance without performing prefetch.


### What is IOPS?

IOPS (Input/Output Per Second) is the input and output per second (or number of read and write operations), which is one of the main indicators of disk performance.
IOPS is the number of I/O requests that the system can process within a unit time period, typically in the unit of I/O requests per second; I/O requests are usually data read or write requests.

Traditional disks are essentially mechanical devices, such as FC, SAS, SATA disk, usually with different rotational speeds such as 5400/7200/10000/15000 rpm.
The key factor affecting the disk is the disk's service time, that is, the time it takes for the disk to complete an I/O request. Service time consists of track seeking time, rotation delay and data transmission time.

Commonly, a mechanical hard drive with 7200 rpm can provide 75-150 IOPS, a mechanical hard drive with 15000 rpm can provide 175-210 IOPS (specific value depends on access mode, such as sequential and random, as well as other factors like IO size).

### How is high-performance cloud block storage achieved?

Currently, the cost of SDD solid state drives is still much higher than that of HDD mechanical hard drives. In order to allow users to enjoy high-performance, cost-effective block device services, Tencent Cloud introduced a hybrid storage architecture. The principle of achieving high-performance cloud block storage is:
New data written by the user are directly written to cache, and cache algorithm will dynamically calculate the "hotness" of the data based on user data access characteristics. When ssd cache is full, part of the cold data are transferred to cold storage;
When the cold data is accessed again and becomes hot data, it will be scheduled from cold storage to hot storage.


### Test result on the actual performance of high performance cloud block storage


**Random IOPS Test**

![](//mc.qcloudimg.com/static/img/a322edf0a5e0ac98054f0f101fc2b7f9/image.png)


**Throughput Performance Test**

![](//mc.qcloudimg.com/static/img/c6c3ee4fcad0093cb42d268ee04f0150/image.png)


**Access Delay Test**

![](//mc.qcloudimg.com/static/img/c3389c18009904903f83a4325c3bdbc6/image.png)

	
	
