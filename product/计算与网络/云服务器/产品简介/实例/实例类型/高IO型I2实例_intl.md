
High IO I2 instances are optimized to provide tens of thousands of low-latency random I/O operations per second (IOPS) to applications, and are the ideal choice for high disk IO. They are well suited for the following situations:

- NoSQL database (e.g. MongoDB)
- Clustered database
- Online Transaction Processing (OLTP) System

and other I/O intensive applications that require low latency.

A high IO I2 machine features 2.4 GHz Intel E5-Xeon Broadwell (v4) CPU and DDR4 memory, and SSD local disks are adopted for all its system disks. It runs on a network boost mode and supports up to 300,000 packets per second (PPS).

For the available configurations when you purchase a high IO I2 instance, refer to [CVM Instance Configurations](https://cloud.tencent.com/doc/product/213/2177). 
## Hardware Specification
The hardware specification for a high IO I2 instance is as follows:

- 2.4 GHz Intel Xeon  E5-2680 Broadwell (v4) processor, DDR4 memory
- CPU performance is 20% higher than Series 1 High IO I1
- SSD is used for instance storage
	- High random IOPS, with up to 40,000 random read IOPS in typical scenarios (blocksize =4k, iodepth =32);
	- High throughput, with up to 300MB/s random read throughput in typical scenarios (blocksize =4k, iodepth =32);
- Network Enhanced type is used by default (up to 300k pps)


## Features of high IO I2 instance
Here is a summary of I2 instance features:

- The storage of I2 instance data is based on SSD instance storage. The system and data disks of I2 instance only exist within the life cycle of the instance. When the instance expires or is terminated by you, the applications and data in the instance storage will be wiped out. We suggest that you back up or copy the data in the instance storage regularly.
- I2 instance is network boosted by default, which leads to significant increase in packets per second (PPS) and decrease in network jittering and latency.

## Requirements for high IO I2 instance
Here are the requirements for I2 instance:

- An I2 instance can be used on the basis of  [postpaid](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9), or as the production instance of high IO host in dedicated hosts;
- Support I2 instance startup in basic network and [Virtual Private Cloud](https://cloud.tencent.com/doc/product/215/535#.E8.85.BE.E8.AE.AF.E4.BA.91.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F);
- For the available configurations when you purchase a high IO I2 instance, refer to [CVM Instance Configurations](https://cloud.tencent.com/doc/product/213/2177).


