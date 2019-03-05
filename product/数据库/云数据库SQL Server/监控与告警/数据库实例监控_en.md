CDB for SQL Server system monitor supports 25 common parameters of SQLSever. You can monitor other parameters by configuring SSMS counter.
#### Currently, the following parameters are supported:
![](//mccdn.qcloud.com/static/img/17c5e9848b7b6df37bee706488dc45ee/image.png)

> SQL Server's memory is used on a "fully occupied" basis, so there is no need to monitor the memory capacity metric. You can check the memory usage using cache hit rate.

#### Metrics Supporting Alarm
Currently, alarm is available only for the key performance metrics. For other metrics, alarm is not supported in Cloud Monitor. You can configure the alarm feature in Tencent Cloud's "Console" -> "Cloud Monitor" -> "My Alarm" -> "Alarm Policy"
![](//mccdn.qcloud.com/static/img/b5912eec83886f728ea2dadf596551d5/image.png)
Currently, alarm is available for the following monitor metrics. Recommended alarm thresholds are provided in this chapter (Figure 1).
- CPU Utilization
- Number of Connections
- Inbound Traffic
- Outbound Traffic
- IOPS
- Storage Space

