This document describes the key terms and concepts that make it easy for you to understand and use Tencent Cloud Monitor.

## Metric

Metrics are the fundamental concept in Cloud Monitor. A metric represents a time-ordered set of data points that are published to Cloud Monitor. You can retrieve statistics about those data points as an ordered set of time-series data. Think of a metric as a variable to monitor, and the data points represent the values of that variable over time. For example, the CPU utilization of a CVM is a metric, and the space usage of a cloud database is another metric.

Metric data can come from any products, applications, or services. For example, the metric can be the CPU utilization of CVM or the process latency of users' services. Metrics are uniquely defined by a name, a namespace, and one or more dimensions. Each data point has a timestamp, and (optionally) a unit of measure. When you request the metric data stored by Cloud Monitor, the returned data stream is identified by the namespace, metric name, and dimension.


## Namespace
A namespace is a container for metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated.


## Dimension
A dimension is a Key/Value pair that uniquely identifies the monitoring object. The metric can be used only after the dimension value is determined. Dimension is helpful to design the statistical data aggregation structure. For example: When machine IP and proc_name are determined, you can determine a monitoring object: monitoring object A (IP = 1.1.1.1 & proc_name = test). You need to specify the appropriate dimensions when you put the Cloud Product metric data into the Cloud Monitor. The appropriate dimension metrics are preset by the system. An error will occur if you use a dimension that is not defined when retrieving.

## Timestamp

In the Cloud Monitor, each metric data point must be marked with a timestamp, indicating the time of original data acquisition. Timestamps are dateTime objects, with the complete date plus hours, minutes, and seconds, for example: 2000-01-31 23:59:59. The Cloud Monitor console and alarm display data and judge alarms in UTC+08:00 by default.


## Unit

The unit is the unit of measure of original data, and the application gets useful syntax based on the unit of data. For example, the unit of CVM's outbound bandwidth is Mbps because the network bandwidth often measures the current network speed in Mbps. The list below provides some common units supported by Cloud Monitor:

- Second (unit of time)
- Byte (usually representing data size; 1 Byte = 8 bits)
- bit (the minimum unit of data)
- % (percent)
- Count (count unit)
- Bps (Bytes per second)
- bps (bits per second)

## Data granularity

A data granularity is the length of time associated with a specific Cloud Monitor statistics. Each statistic represents an aggregation of the metrics data collected fir a specified granularity. Data granularities are defined in numbers of seconds. Cloud Monitor supports 10d, 60d, 300d and other monitoring data granularities.

When calling Cloud Monitor API, you can specify the data granularity with the period parameter. When you call the [GetMonitorData API](https://cloud.tencent.com/doc/api/405/4667#5.1-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8) to obtain the monitoring data, the values of period, startTime, and endTime determine the amount of data that will return. For example, if you call the API using the default values of all parameters, statistics for each 300 seconds of the previous hour is returned, i.e. a total of 12 data points.

Data granularities are also important for alarms. When creating an alarm triggering condition, you need to set the data granularity and period for an alarm rule. Different granularities and periods indicate different alarm judgment durations.

## Statistical Method

* Time dimension

Time dimension is a statistical method used when Cloud Monitor metric data is aggregated from fine to rough granularities. Generally, it can be Sum, Max, Min, Avg or Last. For example, a metric has data with granularities of 10, 60 and 300. Time dimension determines how to aggregate six 10-second granularities to a 60-second data as well as how to aggregate five 60-second data to a data with a granularity of 300 seconds.

A metric can have at most five levels of computation: 10 seconds → 1 minute → 5 minutes → 1 hour → 1 day, and the same statistical method is used in each level of computation.

* Object dimension

Object dimension is a statistical method used when specific monitoring metric data of multiple instances is aggregated into one data. Generally, it can be Sum, Max, Min or Avg. For example, when you want to compute the data of a metric of all the servers under a cluster, object dimension determines how the data of all the servers under this cluster is aggregated. For the average of cluster CPU utilization, the aggregation method is Avg; or for total bandwidth of a cluster, the aggregation method is Sum.



