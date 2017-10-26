The CVM instance described below also refers to dedicated CVM.

Users do not need to activate cloud monitor feature manually, as it is provided by Tencent Cloud by default. However, monitor data can only be collected and recorded after the users start using a Tencent Cloud product. There are several ways to view these monitor data:

## View Monitor Data on the Standalone Monitor Page of the Cloud Product Console

Some cloud products have standalone monitor tabs in their consoles. Take CVM as an example:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Select "Cloud Virtual Machine".

2) Select the ID of the CVM instance whose monitor data you want to view in the CVM list to enter CVM detail page.

3) Click on "Monitor" tab. In this tab, you can view the monitor data of the CVM instance such as CPU, memory, network bandwidth and storage. You can also view the monitor data in a certain time period.

> Note: Tencent Cloud Monitor supports collecting monitor data every minute or every 5 minutes. Default is every 5 minutes. In different display modes, the metrics are displayed differently. For example, in the "past hour" display mode, the monitor data is displayed in their original 5-minute granularity. In the "past month" display mode, the monitor data is displayed in 1-day granularity (average data for each day).

## View Monitor Data in the Cloud Monitor Console
Cloud monitor console is the centralized hub for all products' monitor data. Here, you can view the monitor data of most cloud products. Take CVM as an example:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Select "Cloud Product" -> "Cloud Monitoring".

2) In the navigation bar to the left, select "Cloud Product Monitoring" -> "Cloud Virtual Machine".

3) Select the ID of the CVM instance whose monitor data you want to view in the CVM list to enter the monitor detail page.

4) In this page, you can view all the monitor data of the CVM instance such as CPU, memory, network bandwidth and storage. You can also view the monitor data in a certain time period.

## Acquire Monitor Data Through API
Users can use API "GetMonitorData" to acquire the monitor data of all products. For more information, please see API [Read Monitor Data](https://cloud.tencent.com/doc/api/405/4667).



