In order to maintain high reliability of data, it is important to provide a good monitoring environment for cloud disks. You can use Cloud Monitor to monitor the cloud disk that ***has been mounted to an instance***. When you need to collect cloud disk statistics, perform [Mounting Cloud Disks to CVM Instances](/doc/product/362/5745). With Cloud Monitor, you can view metric data of a cloud disk, and analyze and set the alarm for the cloud disk. Now, Cloud Monitor provides cloud disks with the following monitoring metrics:


| Monitoring Item | Monitoring Metric | Meaning in Linux | Meaning in Windows | Unit | Dimension
|---------|---------|--|--|--|--|
| Disk read traffic | disk_read_traffic | Average data volume read from a disk to a memory per second, take the maximum value among all partitions | Average data volume read from a disk to a memory per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk write traffic | disk_write_traffic | Average data volume written from a memory to a disk per second, take the maximum value among all partitions | Average data volume written from a memory to a disk per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk usage | disk_usage | Percentage of used disk space, displayed by partitions | Percentage of used disk space, displayed by partitions | % | unInstanceId |
| Disk I/O wait	| disk_io_await	| Average waiting time for each I/O operation of a device, take the maximum value among all partitions | Average waiting time for I/O operation of a device, take the maximum value among all partitions | ms | unInstanceId |

For more information on monitoring metrics, please see [Cloud Monitor Product Documentation](https://intl.cloud.tencent.com/doc/product/248).

Cloud Monitor collects raw data of a disk from a running CVM instance and displays the data in easy-to-read charts. Statistics can be retained for a month by default so that you can observe the cloud disk situation during the month, and have a better understanding of usage and reading/writing data.

You can get the data via the [Cloud Monitor Console](https://console.cloud.tencent.com/monitor/cvm) or [Cloud Monitor API](https://intl.cloud.tencent.com/doc/api/405/4667). The console also provides visualized charts of corresponding metrics. For more information, please see [Obtaining Monitoring Data of Specific Metrics](/doc/product/248/6141) and [Viewing Monitoring Charts](/doc/product/248/6142).
