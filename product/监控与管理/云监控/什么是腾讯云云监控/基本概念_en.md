This document describes the key terms and concepts that make it easy for you to understand and use Tencent Cloud Cloud Monitor.

## Metric

Metrics are the core concept of Cloud Monitoring and represent a collection of chronological data points sent to Cloud Monitoring that allows you to retrieve statistics about these data points in chronological order. Think of a metric as a variable to monitor, and the data points represent the values of that variable over time. For example, the CPU utilization of CVM is a metric, and the space usage of cloud database is another metric.

Metric data can come from any products, applications, or services. For example, the metric can be the CPU utilization of CVM or the process latency of users' services. Metrics are uniquely defined by a name, a namespace, and one or more dimensions. Each data point has a time stamp, and (optionally) a unit of measure. When you request the metric data stored by Cloud Monitor, the returned data stream is identified by the namespace, metric name, and dimension.


## Namespace
A namespace is a container for metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated.


## Dimension
Dimension is a Key/Value pair for uniquely identifying the monitoring object. The metric is only meaningful when the dimension value is determined. Dimensions help you design a structure for your statistics plan. For example， When the values of machine IP and proc_name are determined, you can determine a monitoring object: monitoring object A (IP = 1.1.1.1 & proc_name = test). You need to specify the appropriate dimensions when you put the Cloud Product metric data into the Cloud Monitor (the appropriate dimension metrics are preset by the system). There will be an error in using a dimension that is not defined when retrieving.

## Timestamp

In the Cloud Monitor, each metric data point must be marked with a time stamp, indicating the time of original data acquisition. Time stamps are dateTime objects, with the complete date plus hours, minutes, and seconds, such as 2000-01-31 23:59:59. It is recommended to provide timestamps based on Beijing time (UTC+08:00).


## Unit

The unit is the unit of measure of original data, and the application gets useful syntax based on the unit of data. For example, the unit of CVM's outbound bandwidth is Mbps because the network bandwidth often measures the current network speed in Mbps. The list below provides some common units supported by Cloud Monitor:

- Second (unit of time)
- Byte (often indicating the data size. 1 Byte = 8 bit)
- bit (the minimum unit of data.)
- % (percent)
- Count (count unit)
- Bps (Bytes per second)
- bps (bits per second)

## Periods

A period is the interval length of Cloud Monitor statistics. Each statistic represents an aggregation of the metrics data collected for a specified period of time. Although periods are expressed in seconds, the minimum granularity for a period is one minute. Accordingly, you specify period values as multiples of 60. For example, to specify a period of six minutes, you would use the value 360.

When you call Cloud Monitor API, you can specify the length of time with the period parameter. When you call the [GetMonitorData API](https://cloud.tencent.com/doc/api/405/4667#5.1-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8) to obtain the monitoring data, the values that you specify for the period, start time and end time parameters determine the amount of data which will return. For example, retrieving statistics using the default values of all parameters returns the statistics for each five minutes of the previous hour, i.e. a total of 12 data points. If you prefer statistics aggregated in ten-minute blocks, specify a period of 600. For statistics aggregated over the entire hour, specify a period of 3600.

Periods are also important for Alarm function. When you create an alarm trigger condition, you need to compare the metrics with the thresholds that you specified. You can specify that the monitoring data must meet multiple consecutive periods before sending an alarm.

## Alarm
Alarm management is a function provided in the monitoring and alarm service by Tencent Cloud. It will give alarms when there is an abnormal situation in the cloud resources, and also provides users with alarm information, alarm custom threshold and alarm subscription. An alarm watches a custom threshold over a specified time period. If the alarm trigger conditions are met, you will be notified immediately.

## Alarm Policy
The alarm policy is a set of alarm trigger conditions. The alarm policy is associated with projects and policy types. For each policy type, fifteen alarm policies can be created for each project.

The alarm policy includes alarm trigger condition, alarm object, and alarm receiver group. When the configuration is completed, an alarm will be triggered immediately if an alarm is detected. After the configuration is completed, the alarm policy will be sent to users via SMS, or email, etc according to the alarm set by the user after the alarm is detected. 

## Alarm Receiver Group
Alarm receiver group can contain one or more users. In the alarm configuration, the alarm notifications are sent through the "alarm receiver group". Each alarm policy will send a notification to the users of preset alarm receiver group when the alarm threshold is reached. User information and alarm reception methods can be added in the "User Center" - "Permission Setting".

## Alarm Reception Methods
The way users are notified when an exception occurs includes SMS, email and so on.



