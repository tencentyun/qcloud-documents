Tencent Cloud provides cloud monitoring for all users by default, no need for the user to manually turn on. But the user must use Tencent Cloud products before cloud monitoring can begin to collect monitoring data; to view these monitoring data, there are several ways:

## Obtain monitoring data through the cloud product console's individual monitoring page

Some cloud products provide a separate monitoring data reading tab on their own console pages. CVM is used in this example

1) Open [Tencent Cloud Console](https://console.cloud.tencent.com), select "CVM".

2) Click the CVM Instance ID from the list of CVMs to view the monitoring data, and enter the CVM details page.

3) Click the "Monitor" tab; on this page, you can view the CPU, memory, network bandwidth, disk and monitoring data, etc. of the CVM instance. You can also freely adjust the time range.

> Note: Tencent Cloud monitoring provides both 5 minute and 1 minute data acquisition modes; 5 minute data collection is the default. In different display modes, the indicator data displays will be different. For example, when monitoring charts are displayed for nearly an hour, the monitoring data is presented in the original 5-minute interval format. When monitoring charts are displayed for nearly a month, the monitoring data will show daily data averages in days.

## Obtain monitoring data from Console
On Cloud Monitoring console, you can view monitoring data for most of the products used. In this case, CVM is used as an example.

1) Open [Tencent Cloud Console](https://console.cloud.tencent.com), select "Cloud Products - Cloud Monitoring".

2) On the left navigation bar, select "Cloud Product Monitoring - CVM".

3) Click the CVM Instance ID from the list of CVMs displayed to view the monitoring data, and enter the monitoring details page.

4) On this page, you can view the CPU, memory, network bandwidth, disk and all monitoring data of the CVM instance. You can also freely adjust the time range.

## Obtain monitoring data through the API
Users can use the GetMonitorData API to obtain monitoring data for all products. For more information, please see [Reading Monitoring Data API](https://cloud.tencent.com/doc/api/405/4667).


