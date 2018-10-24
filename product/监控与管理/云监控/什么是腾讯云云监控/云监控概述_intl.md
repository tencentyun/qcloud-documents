 As a general monitoring and management system, Tencent Cloud Monitor monitors all your Tencent cloud products and resources in real time to provide the most complete and detailed monitoring data. When monitoring [Cloud Virtual Machine](https://cloud.tencent.com/product/cvm.html), [Cloud Database](https://cloud.tencent.com/product/cdb-overview.html), [Cloud Load Balance](https://cloud.tencent.com/product/clb.html), and other Cloud products, Cloud Monitor extracts their key metrics and displays the monitored results in chart, which allows you to have a clear understanding of your resource usage, application performance and cloud product health, set custom alarm threshold, and send notifications based on your custom rules.

Cloud Monitor uses monitoring charts to demonstrate the health and performance of your cloud products. If any exceptions are monitored, an alarm message will be pushed to you, enabling you to know the product usage and health without developing a new application. You can get the monitoring data using [Cloud Monitoring Console](https://console.cloud.tencent.com/monitor/overview), [Cloud Monitoring API](https://cloud.tencent.com/doc/api/405) or Tencent Cloud CLI.

## Functions of Cloud Monitor
You can get the following functions in the Cloud Monitoring Console:

| Module | Feature |Function |
|---------|---------|---------|
| Monitor Overview | Cloud Monitoring overview | Provide general monitoring results and health check, so you can view the monitoring data at a glance |
| My Alarms | User-defined alarm threshold | Support Alarm Settings for CVMs, Cloud Databases, CDN, VPN, etc. |
| Cloud Product Monitoring | Visualized cloud products monitoring | Cloud monitor console provides monitoring views for Cloud Databases, CVMs, memcached and other cloud products |
| Custom Monitoring | User-defined monitoring metrics | Check user-defined custom monitoring metrics and reported data |
| Data Usage Monitoring | Traffic monitoring | Check the user's overall traffic |

## Supported Services
Cloud Monitor can automatically monitor the following services. Once you start using any of these services, it will automatically send metric data to the Cloud Monitor.

> Two monitoring modes are available: basic monitoring and detailed monitoring. For basic monitoring, the metric data is collected every 5 minutes; for detailed monitoring, the metric data is collected every minute. Some cloud products (such as CVM) supports both basic and detailed monitoring, while others only support basic monitoring.

- [Cloud Virtual Machine](https://cloud.tencent.com/doc/product/213)
- [Cloud Block Storage](https://cloud.tencent.com/doc/product/362) (only when mounted on a running CVM)
- [Cloud Load Balance](https://cloud.tencent.com/doc/product/214)
- [Direct Connect](https://cloud.tencent.com/doc/product/216)
- [Content Delivery Network](https://cloud.tencent.com/doc/product/228)
- [Cloud Object Storage](https://cloud.tencent.com/document/product/436)
- [Cloud Database for MySQL](https://cloud.tencent.com/doc/product/236)
- [Cloud Database for TDSQL](https://cloud.tencent.com/doc/product/237)
- [Cloud Database for SQL Server](https://cloud.tencent.com/doc/product/238)
- [Cloud Redis](https://cloud.tencent.com/doc/product/239)
- [Cloud Memcached](https://cloud.tencent.com/doc/product/241)

## Architecture of Cloud Monitor
Cloud Monitor provides basic metrics monitoring and data storage. You can view the metric data via console or specific API. If the basic metric monitoring cannot meet your demand, you can use [Custom Monitoring](https://cloud.tencent.com/doc/product/397) to report metric data, and view corresponding monitoring charts in the Cloud Monitoring Console.

Cloud Monitor stores metric data of all the cloud products. You can search the cloud products (such as CVM) based on these metrics. The Cloud Monitoring Console collects the metric data of cloud products and displays them in chart.

![](https://mc.qcloudimg.com/static/img/93517fe56fa0222615d9f73cba5bd494/image.png)
