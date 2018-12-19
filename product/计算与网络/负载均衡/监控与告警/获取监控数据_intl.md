Tencent Cloud provides Cloud Monitor feature for all users by default, so you do not need to enable it manually. When you use CLB, Cloud Monitor can help you collect relevant monitoring data.

You can view the monitoring data of your load balancers in the following ways:

## CLB Console

1) Log in to the [CLB Console](https://console.cloud.tencent.com/loadbalance) and click the ID of a load balancer instance to enter its details page.

2) Click the **Listener Monitoring** tab to check the monitoring data of the current load balancer instance.

> Note: Tencent Cloud Monitor supports collecting monitoring data every minute or every 5 minutes. Default is every 5 minutes. In different display modes, the metrics are displayed differently. For example, in the "past hour" display mode, the monitoring data is displayed in their original 5-minute granularity. In the "past month" display mode, the monitoring data is displayed in 1-day granularity (average data for each day).

## Cloud Monitor Console

Log in to the [Cloud Monitor console](https://console.cloud.tencent.com/monitor/overview), click **Cloud Product Monitoring** -> **Cloud Load Balance**, click the ID of **public network application-based/public network (with static IP)/private network-based** load balancer instance to enter the monitoring details page to check its monitoring data.

## API Method

Please see the [API GetMonitorData](https://cloud.tencent.com/doc/api/405/4667#5.3-.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1).

