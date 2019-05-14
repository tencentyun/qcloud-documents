Cloud Monitor of Tencent Cloud provides the following monitoring metrics for Cloud Virtual Machine:

| Metric Name | Description | Meaning in Linux | Meaning in Windows | Unit | Dimension |
|---------|---------|
| CPU_usage | cpu_usage | Percentage of CPU in non-idle status, which is calculated by obtaining data /proc/stat | Percentage of CPU in non-idle status | % | unInstanceId |
| Average CPU load | cpu_loadavg | Take the first column data of /proc/loadavg \*100 within 1 minute. The Cloud Monitor data with the granularity of 5 minutes is the maximum value of the data within 1 minute | None | - | unInstanceId |
| Memory usage	 | mem_used | Difference value between Memtotal and MemFree of /proc/meminfo | Same as Linux | MB | unInstanceId |
| Memory utilization	 | mem_usage | The ratio of actual memory used by users to the total memory after subtracting the cache, buffer and remaining memory from the total memory | The ratio of actual memory used by users to the total memory after subtracting the cache, buffer and remaining memory from the total memory | % | unInstanceId |
| Private network outbound bandwidth | lan_outtraffic | Outbound traffic per second of private network NIC | Outbound traffic per second of private network NIC | Mbps | unInstanceId |
| Private network inbound bandwidth | lan_intraffic | Inbound traffic per second of private network NIC | Inbound traffic per second of private network NIC | Mbps | unInstanceId |
| Private network outbound packets | lan_outpkg | Outbound packets per second of private network NIC | Outbound packets per second of private network NIC | Count/s | unInstanceId |
| Private network inbound packets | lan_inpkg | Inbound packets per second of private network NIC | Outbound packets per second of private network NIC | Count/s | unInstanceId |
| Public network outbound bandwidth | wan_outtraffic | Outbound traffic per second of public network NIC | Outbound traffic per second of public network NIC | Mbps | unInstanceId |
| Public network inbound bandwidth | wan_intraffic | Inbound traffic per second of public network NIC | Inbound traffic per second of public network NIC | Mbps | unInstanceId |
| Public network outbound packets | wan_outpkg | Outbound packets per second of public network NIC | Outbound packets per second of public network NIC | Count/s | unInstanceId |
| Public network inbound packets | wan_outpkg | Inbound packets per second of public network NIC | Inbound packets per second of public network NIC | Count/s | unInstanceId |
| Disk read traffic | disk_read_traffic | Average data volume read from a disk to a memory per second, take the maximum value among all partitions | Average data volume read from a disk to a memory per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk write traffic | disk_write_traffic | Average data volume written from a memory to a disk per second, take the maximum value among all partitions | Average data volume written from a memory to a disk per second, take the maximum value among all partitions | KB/s | unInstanceId |
| Disk usage | disk_usage | Percentage of used disk space, displayed by partitions | 	Percentage of used disk space, displayed by partitions | % | unInstanceId |
| Disk I/O wait | disk_io_await | Average waiting time for each I/O operation of a device, take the maximum value among all partitions | Average waiting time for I/O operation of a device, take the maximum value among all partitions | ms | unInstanceId |

For more information about the monitoring metrics of Cloud Virtual Machine, please see [Read Monitoring Data API](https://cloud.tencent.com/doc/api/405/4667) in the Cloud Monitor API.
