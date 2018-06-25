Tencent Cloud provides Cloud Monitor feature for all users by default, so you don't need to enable it manually. When you use cloud load balancer, Cloud Monitor will help you collect relevant monitoring data.

You can view the monitoring data of cloud load balancer in the following ways:

## Cloud Load Balance Console

1) Log in to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click corresponding cloud load balancer instance ID to enter the details page of cloud load balancer.

2) Click "Listener Monitor" tab to check the monitoring data of current cloud load balancer instance.

> Note: Tencent Cloud Monitor supports collecting monitor data every minute or every 5 minutes. Default is every 5 minutes. In different display modes, the metrics are displayed differently. For example, in the "past hour" display mode, the monitor data is displayed in their original 5-minute granularity. In the "past month" display mode, the monitor data is displayed in 1-day granularity (average data for each day).

## Cloud Monitor Console

Log in to [Cloud Monitor Console](https://console.cloud.tencent.com/monitor/overview), click "Cloud Product Monitoring" -> "Cloud Load Balance", click the ID of **public network application/public network (with static IP)/private network** cloud load balancer instance to enter the details page of monitor to check the monitoring data of the cloud load balancer instance.

## API Method

Please refer to [API GetMonitorData](https://cloud.tencent.com/doc/api/405/4667#5.3-.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1).

