## Overview

Tencent Cloud's Cloud Monitor provides data collection and presentation features for the cloud load balancer and backend instances. With Tencent Cloud's Cloud Monitor, you can view the statistical data of cloud load balancer, verify whether the system is running normally and create corresponding alarms. For more information on Cloud Monitor, please refer to [Cloud Monitor](https://cloud.tencent.com/doc/product/248).

Now, **public network application, public network with IP and private network cloud load balancers** support operation status monitoring using Cloud Monitor. You can check the status by clicking the monitor icon on the cloud load balancer instance list page or by clicking "Listener Monitor" on the cloud load balancer instance details page.

## Monitoring

Now, **public network application, public network IP-based and private network cloud load balancers** support monitor view display based on the four dimensions below:
- Cloud load balancer instance
- Listener
- Backend CVM
- Port of backend server

The specific monitoring metrics of different dimensions for cloud load balancer are as follows:

Item | Unit | Description
----|------|----
Number of public network connections | count  | Statistics of established TCP connections 
Public network inbound bandwidth | bps  | Statistics of bandwidth used by the public network accessing cloud load balancer
Public network outbound bandwidth | bps  | Statistics of bandwidth used by the public network accessing from cloud load balancer
Inbound packets of public network | count/s  | Number of request packets received by cloud load balancer per second
Outbound packets of public network | count/s  | Number of request packets sent from cloud load balancer per second
Number of new public network connections | count/s  | Number of TCP connections created per second

For more information on monitor metrics and how to obtain the monitoring data of backend CVMs, please refer to [Monitor Cloud CVM](/doc/product/213/5178).

Cloud Monitor collects original data from a running cloud load balancer instance and displays the data in the form of readable icon. Statistics are retained for a month by default so that you can observe the running status of your instances during the month, and have a better understanding of the running status of your applications and services.

For more detailed monitoring data, cloud load balancers support data monitoring at a shorter granularity period of 1 minute, and support horizontal comparison of monitoring data of the same dimension in different time periods.

The console pages of different products may show a series of tables and diagrams based on raw data from cloud monitor. The cloud monitor console summarizes the monitor data from all products to give users an overall view of the running status. You can acquire instances' status data from different channels based on your specific demands.


## Alarm

You can create alarms for instance metrics of your concern. When the cloud load balancer instances' running statuses meet specific conditions, alarm messages will be sent to relevant users in time. With this mechanism, you can detect abnormality in time and take appropriate measures to ensure the stability and reliability for the system. For more information, please see [Alarm Overview](/doc/product/248/6126).

Now, **public network application, public network IP-based and private network cloud load balancers** support alarm display based on two dimensions below:
- Listener
- Port of backend server

The specific monitoring metrics of cloud load balancer alarm are as follows:

Item | Unit | Description
----|------|----
Public network inbound bandwidth | bps  | Statistics of bandwidth used by the public network accessing cloud load balancer
Public network outbound bandwidth | bps  | Statistics of bandwidth used by the public network accessing from cloud load balancer
Inbound packets of public network | count/s  | Number of request packets received by cloud load balancer per second
Outbound packets of public network | count/s  | Number of request packets sent from cloud load balancer per second

