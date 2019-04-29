The CVM instance described below also refers to dedicated CVM.

In order to maintain high reliability, high availability and high performance for Tencent Cloud CVMs, it is important to provide a good monitoring environment. Users can collect monitor data at different dimensions for different resources, in order to obtain resource usage information and quickly locate errors.

Collecting monitor data allows users to establish normal standards regarding CVM instance performance. By testing the performance of a CVM and collecting historical monitoring data at different times and under different load conditions, users can better understand the normal performance of a running CVM, and quickly determine whether the running instance is exceptional based on the current monitoring data, in order to find out solutions in time. For example, users can monitor the CPU utilization, memory utilization and disk I/O of an instance. If the performance of an instance falls below normal, users may need be alarmed to upgrade instance specifications or add more instances to lower the load of each instance, and thus maintain the stability of the whole system.

To establish normal performance standard for CVM instances, the following metrics should be monitored:

| Monitoring Item      | Monitoring Metric           |
| -------- | -------------- |
| CPU utilization   | cpu_usage      |
| Memory utilization    | mem_usage      |
| Outbound bandwidth of private network    | lan_outtraffic |
| Inbound bandwidth of private network    | lan_intraffic  |
| Outbound bandwidth of public network    | wan_outtraffic |
| Inbound bandwidth of public network    | wan_intraffic  |
| Disk utilization    | disk_usage     |
| Disk IO waiting time | disk_io_await  |

For more information about monitoring metrics, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).

Cloud Monitoring collects original data from a running CVM instance and displays the data in the form of readable icon. Statistics are retained for a month by default so that you can observe the running status of your instances during the month, and have a better understanding of the running status of your applications and services. By default, cloud monitor collects the status data of running instances every 5 minutes. Some Tencent Cloud products also support more detailed monitor which collects data at a granularity of 1 minute.

The console pages of different products may show a series of tables and diagrams based on raw data from cloud monitor. The cloud monitor console summarizes the monitor data from all products to give users an overall view of the running status. Users can acquire instances' status data from different channels based on their specific needs.

Furthermore, you can setup alarms for instance metrics of your concern. When the CVM instances' running statuses meet specific conditions, alarm messages will be sent to relevant users in time. With this mechanism, you can detect abnormality in time and take appropriate measures to ensure the stability and reliability for the system. For more information, please see [Create Alarm](/doc/product/248/6126).
