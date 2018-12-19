## 1. API Description

Domain name: monitor.api.qcloud.com


Tencent Cloud's Cloud Virtual Machine (CVM) is the server running at Tencent Cloud IDC. For more information, please see<a href="https://cloud.tencent.com/document/api/213/568" title="CVM Overview">CVM Overview</a> page.

This API (GetMonitorData) is used to query the monitoring data of CVM. The values for input parameter are as follows:
Namespace: qce/cvm
dimensions.0.name=unInstanceId
Dimensions.0.value is CVM ID. Obtain the unInstanceId field by calling the API [DescribeInstances](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8).

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content         | Description                                       |
| ------------------ | ---- | -------- | ------------ | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm      | Namespace. Every cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name      | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | uInstanceId | Input parameter is the server ID                                 |
| dimensions.0.value | Yes    | String   | Specific CVM ID    | Obtain the unInstanceId field by calling the API [DescribeInstances](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8) |
| period             | No    | Int      | 60/300       | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time         | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time         | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name

#### 2.2.1 Data Monitoring Metrics Obtained Without Installation of Monitor Agent

| Metric Name           | Description    | Unit   | Statistical Granularity (period) |
| -------------- | ----- | ---- | ------------ |
| lan_outtraffic | Private network outbound bandwidth | Mbps | 60s, 300s     |
| lan_intraffic  | Private network inbound bandwidth | Mbps | 60s, 300s     |
| lan_outpkg     | Private network outbound packets | pck/sec  | 60s, 300s     |
| lan_inpkg      | Private network inbound packets | pck/sec  | 60s, 300s     |
| wan_outtraffic | Public network outbound bandwidth | Mbps | 60s, 300s     |
| wan_outtraffic  | Public network inbound bandwidth | Mbps | 60s, 300s     |
| acc_outtraffic | Public network outbound traffic | MB   | 60s, 300s     |
| wan_outpkg     | Public network outbound packets | pck/sec  | 60s, 300s     |
| wan_inpkg      | Public network inbound packets | pck/sec  | 60s, 300s     |

#### 2.2.2 Data Monitoring Metrics Obtained After Installation of Monitor Agent

| Metric               | Name  | Calculation Method                                     | Description                        | Unit   | Statistical Granularity (period) |
| ------------------ | ------- | ---------------------------------------- | --------------------------- | ---- | ------------ |
| cpu_usage          | CPU utilization  | Percentage of CPU's "user+nice+system+irq+softirq+idle+iowait" time in total time | Percentage of time during which CPU is occupied in real time when CVM is running           | %    | 10s, 60s, 300s |
| cpu_loadavg        | CPU average load | Analyze data in /proc/loadavg, and collect the average load of the system in the last 1 minute every 10s<br>(This metric is not available to the CVM in Windows) | Average number of tasks of CPU in use and to be used over a period of time     | -    | 10s, 60s, 300s |
| mem_used           | Memory usage    | Windows: Call GlobalMemoryStatusEx<br>Linux: Call psutil.virtual_memory()<br>Calculate the value of memory usage (excluding buffers and cached) by subtracting the available memory (including buffers and cached) from the total memory | Actual memory used by users, excluding the memory occupied by buffers and system cache | MB   | 10s, 60s, 300s |
| mem_usage          | Memory utilization   | The ratio of actual memory used by users to the total memory after the cache, buffer and remaining memory are subtracted            | Actual memory used by users, excluding the memory occupied by buffers and system cache | %    | 10s, 60s, 300s |
| disk_read_traffic  | Disk read traffic   | Windows: Send IOCTL_DISK_PERFORMANCE to obtain the disk read bytes by calling ioctrl<br>Linux: Obtain the disk read bytes by calling psutil.disk_io_counters<br>Calculate the disk read traffic by dividing the value difference between two calls by the time difference between two calls | Number of bytes per second read from disk partition                | KB/sec | 10s, 60s, 300s |
| disk_write_traffic  | Disk write traffic   | Windows: Send IOCTL_DISK_PERFORMANCE to obtain the disk write bytes by calling ioctrl<br>Linux: Obtain the disk write bytes by calling psutil.disk_io_counters<br>Calculate the disk write traffic by dividing the value difference between two calls by the time difference between two calls | Number of bytes per second written into disk partition                | KB/sec | 10s, 60s, 300s |
| disk_io_await      | Disk IO wait  | Windows: Send IOCTL_DISK_PERFORMANCE to obtain the number of disk reads and writes by calling ioctrl<br>Linux: Obtain the number of disk reads and writes by calling psutil.disk_io_counters<br>Calculate the IOWait value by dividing the total time spent on reads and writes by the total number of reads and writes | Average time spent on each I/O operation in disk partition            | ms   | 10s, 60s, 300s |

Note: The time when metrics are reported/displayed and the alarm time obtained only by installing agent are the local time of user's CVM. If the local time on the CVM is not UTC+08:00, then the time when the monitoring data is collected from the CVM is the local time (non-UTC+08:00) on the sub-server.

## 3. Output Parameters

| Parameter Name       | Type       | Description                  |
| ---------- | -------- | ------------------- |
| code       | Int      | Error code. 0: Successful; other values: Failed |
| message    | String   | Error message                |
| startTime  | Datetime | Start time                |
| endTime    | Datetime | End time                |
| metricName | String   | Metric name                |
| period     | Int      | Interval for collecting monitoring data              |
| dataPoints | Array    | Monitoring data list              |


## 4. Error Codes

| Error Code | Error Description    | Error Message                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit is exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |

## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cvm
&metricName=cpu_usage
&dimensions.0.name=unInstanceId
&dimensions.0.value=ins-e24d4dzf
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cpu_usage",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5.6,
		6.7,
		7.7
	]
}
```

