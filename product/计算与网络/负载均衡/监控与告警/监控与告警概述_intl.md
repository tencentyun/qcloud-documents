## Overview

Tencent Cloud's Cloud Monitor provides data collection and presentation features for load balancer and backend instances. With Tencent Cloud's Cloud Monitor, you can view the statistical data of a load balancer, verify whether the system is running normally and create relevant alarms. For more information on Cloud Monitor, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).

Monitoring the running status of **public network application-based, public network IP-based and private network-based load balancers** with Cloud Monitor is supported. You can also check the status by clicking the monitoring icon on the load balancer instance list page or by clicking **Listener Monitoring** on the load balancer instance details page.

## Monitoring

**Public network application-based, public network IP-based and private network-based load balancers** support displaying monitoring views from the following four dimensions:
- Load balancer instance
- Listener
- RS
- RS port

The specific monitoring metrics of different dimensions for load balancer are as follows:

Item | Unit | Description
----|------|----
Number of public network connections | count | Statistics of TCP connections established
Public network inbound bandwidth | bps | Statistics of bandwidth used by the public network access to load balancer
Public network outbound bandwidth | bps | Statistics of bandwidth used by the public network access from load balancer
Inbound packets of public network | count/sec | Number of request packets received by load balancer per second
Outbound packets of public network | count/sec | Number of request packets sent from load balancer per second
Number of new public network connections | count/sec | Number of TCP connections created per second

For more information on monitoring metrics and how to obtain the monitoring data of RS, please see [Monitor CVM](/doc/product/213/5178).

Cloud Monitor collects original data from a running load balancer instance and displays the data in the form of readable icon. Statistics are retained for a month by default so that you can observe the running status of your instances during the month, and have a better understanding of the running status of your applications and services.

For more detailed monitoring data, CLB product supports data monitoring at a shorter granularity period of 1 minute, and horizontal comparison of monitoring data of the same dimension in different time periods.

The console pages of different products may show a series of tables and diagrams based on raw data from Cloud Monitor. The Cloud Monitor console summarizes the monitoring data from all products to give you an overall view of the running status. You can obtain instances' status data from different entries based on your specific needs.


## Alarm

You can create alarms for instance metrics of your concern. When a load balancer instance's running status meets a specific condition, an alarm message is sent to relevant users in time. By this way, you can detect exceptions in real time and take appropriate measures to ensure the stability and reliability for the system. For more information, please see [Create Alarm](/doc/product/248/6126).

**Public network application-based, public network IP-based and private network-based load balancers** support displaying alarms from the following two dimensions:
- Listener
- RS port

The specific monitoring metrics of a load balancer alarm are as follows:

Item | Unit | Description
----|------|----
Public network inbound bandwidth | bps | Statistics of bandwidth used by the public network access to load balancer
Public network outbound bandwidth | bps | Statistics of bandwidth used by the public network access from load balancer
Inbound packets of public network | count/sec | Number of request packets received by load balancer per second
Outbound packets of public network | count/sec | Number of request packets sent from load balancer per second

