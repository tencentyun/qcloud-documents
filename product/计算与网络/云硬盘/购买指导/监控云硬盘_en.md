In order to maintain high reliability of data, it is important to provide a good monitoring environment for a cloud disk. You can use Cloud Monitoring to monitor the cloud disk ***that has been mounted on an instance***. When you need to collect cloud disk statistics, please first perform [Connect Cloud Block Storage to CVM Instance](/doc/product/362/5745). Through Cloud Monitoring, you can view metric data of a cloud disk, and analyze and set the alarm about the cloud disk. Currently, Cloud Monitoring provides a cloud disk with the following monitoring metrics:


| Monitoring Items | Monitoring Metrics | Meaning in Linux | 	Meaning in Windows| 	Unit| 	Dimension
|---------|---------|--|--|--|--|
| Disk read traffic	 | disk_read_traffic	 | Average data volume read from a disk to a memory per second, take the maximum value among all partitions	 | Average data volume read from a disk to a memory per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk write traffic	 | disk_write_traffic	 | Average data volume written from a memory to a disk per second, take the maximum value among all partitions	 | Average data volume written from a memory to a disk per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk usage	 | disk_usage	 | Percentage of used disk space, displayed by partitions | 	Percentage of used disk space, displayed by partitions | % | unInstanceId |
| Disk I/O wait	 | disk_io_await	 | Average waiting time for each I/O operation of a device, take the maximum value among all partitions | 	Average waiting time for I/O operation of a device, take the maximum value among all partitions | ms | unInstanceId |

For details about monitoring metrics, please refer to [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).

Cloud Monitoring collects original data of a cloud disk from a running CVM instance and displays the data in the form of readable icon. Statistics can be retained for a month by default so that you can observe the cloud disk situation during the month, and have a better understanding of data on such aspects as usage, read and write.

You can get the data from [Cloud Monitor Console](https://console.cloud.tencent.com/monitor/cvm) entry or [Cloud Monitor API](https://cloud.tencent.com/doc/api/405/4667). The console also provides visualized icons of corresponding metrics. For more information, refer to [Obtaining Monitoring Data of Specific Metrics](/doc/product/248/6141) and [Viewing Monitoring Diagram](/doc/product/248/6142).
