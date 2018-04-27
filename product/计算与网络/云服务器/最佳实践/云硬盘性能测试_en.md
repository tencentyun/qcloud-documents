The block storage devices provided by Tencent Cloud has different performance and prices according to its types. For more information, refer to [Cloud Block Storage Classification](/doc/product/362/2353). It should be noted that due to different work load of different applications, if enough I/O requests are not provided to take full advantage of Cloud Block Storage, it is probable that maximum performance of the Cloud Block Storage cannot be achieved.

How to measure the performance of Cloud Block Storage? The performance of the storage device is generally justified by the following indicators:

- IOPS: read/write times per second, in units of times (count). Different types of underlying driver in storage device result in different IOPS.
- Throughput: The amount of reading/writing data per second, in MB/s.
- Delay: The time elapsed from the transmission time of the IO operation to the reception confirmation, in seconds.


FIO is an appropriate tool for testing disk performance and is used for stress testing and verification of hardware. It is recommended to use libaio's I/O engine to test the disk. Please install FIO and Libaio.

Test formulas in different scenes are basically the same, with only three different parameters (read and write mode, iodepth, and blocksize). The following example illustrates the use of block size as 4k and iodepth as 1 to test the performance of read in order.

Commands are as follows:

```
fio --bs=4k --ioengine=libaio --iodepth=1 --direct=1 --rw=read --time_based --runtime=600  --refill_buffers --norandommap --randrepeat=0 --group_reporting --name=fio-read --size=100G --filename=/dev/sdb
```
Each workload is suitable for different iodepth at best, depending on how sensitive your application is to IOPS and delay.



Parameter Description:
![](//mccdn.qcloud.com/static/img/44b8577054f94a8920d57f23945b3289/image.jpg)

Common examples are as follows:
- Block = 4k iodepth = 1 Random read test. Reflecting delay performance of the disk;
- Block = 128K iodepth = 32 Reflecting throughput performance at the peak; 
- Block = 4K iodepth = 32 Reflecting IOPS performance at the peak;

The figure below shows test performance screenshots of the SSD cloud disk:
![](//mccdn.qcloud.com/static/img/1609e6314d25fe8c60d2b41fb680d93a/image.png)
![](//mccdn.qcloud.com/static/img/ead7220181d8491752899b195e8bc15c/image.png)
![](//mccdn.qcloud.com/static/img/9a9621f1eaec3f630fbad75f8d3820ee/image.png)
