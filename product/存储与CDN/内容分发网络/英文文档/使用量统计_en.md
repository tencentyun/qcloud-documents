Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and click "Usage" page under "Statistics" to review the curve graph of detailed real-time bandwidth and traffic consumption as well as other data including the analysis of ISPs, provinces and popular URLs. You can also query for historical data. Details will be described below.

## Query Criteria

The usage statistics page includes the following query criteria:
![](https://mc.qcloudimg.com/static/img/cfe4dc604956845bdacbe46566081978/1.png)

**Note:**

+ Time range: The earliest selectable time is 2015-01-01, you can select a query time span of up to 90 days;
+ Project: Query for usage data based on project is supported;
+ Domain: Query for usage data based on specified domain is supported;
+ Region: Query for usage data based on specified region is supported. Currently you cannot select both "Region" and "Carrier", when you select regions, the carrier will need to be "All carriers";
+ Carrier: Query for usage data based on specified carrier is supported. Currently you cannot select both "Region" and "Carrier", when you select a carrier, the region will need to be "All regions";
+ Network layer: Query for usage data of edge nodes or intermediate nodes is supported;
+ Temporal granularity: This refers to the temporal granularity with which bandwidth and traffic data will be presented. This is related to the selected time span:
  > If the selected time span is 1 day, you can query data with a temporal granularity of 5 minutes, 15 minutes, 30 minutes, 2 hours or 4 hours;
  > If the selected time span is 2-3 days, you can query data with a temporal granularity of 15 minutes, 30 minutes, 2 hours or 4 hours;
  > If the selected time span is 4-7 days, you can query data with a temporal granularity of 2 hours, 4 hours or 1 day;
  > If the selected time span is more than 30 days, you can only query data with a temporal granularity of 4 hours or 1 day;

## Data Result Description
### Statistics of Traffic and Bandwidth
Displays the curve graph of traffic and bandwidth statistical data:
![](https://mc.qcloudimg.com/static/img/223e2d6ab037740b68175291ca124940/2.png)


**Note:**

+ The minimum granularity for traffic and bandwidth statistics is five minutes, that is, the statistical data from 2016-10-25 15:00:00 to 15:04:59 will be shown at the statistical point of 2016-10-25 15:05:00;
+ The latency of real-time data is about five minutes, that is, the statistical point of 2016-10-25 15:05:00 will appear around 2016-10-25 15:10:00;
+ Accelerated domains that were once connected and then deleted will be displayed in gray in the "All domains" drop-down box;
+ Note about statistics:
  > If the domain has not been connected to CDN for the specified time range, it will not be covered in statistics even if it is checked;
  > If the domain has been deleted for the specified time range, it will not be covered in statistics even if it is checked;
  > If the domain experienced three stages (not connected, connected and deleted) for the specified time range, the statistical data for unconnected and deleted time period will be filled by 0.

### Carrier and Province Analysis
The usage statistics are ranked and analyzed based on provinces and carriers:
![](https://mc.qcloudimg.com/static/img/31dc248c29ed74cf371ccc2e27fb0778/3.png)

**Note:**

+ Carrier and province data is analyzed through logs, thus the data belongs to application layer. There will be deviations between this data and the statistics of traffic and bandwidth NIC data in the previous figure;
+ Latency of data statistics during peak hours is less than 30 minutes;
+ The record of carrier and province data will only be kept for 90 days, if the query time range exceeds the limit of 90 days, the data will not be displayed.

### Domain Bandwidth/Traffic Usage Details
Domains and their detailed traffic and bandwidth are displayed according to selected query criteria (sorted from high to low). You can click "Download all data" to download detailed data:
![](https://mc.qcloudimg.com/static/img/9d2d4baf4b79049289de2bfa01e55085/4.png)


**Note:**

+ The details of domain bandwidth and traffic are statistics of NIC data;
+ The record of detailed bandwidth and traffic data will only be kept for 90 days, if the query time range exceeds the limit of 90 days, the data will not be displayed.

### TOP100 URL
TOP100 analysis for traffic usage and bandwidth usage towards individual URL resources is carried out according to the selected query criteria, to help you locate popular resources:
![](https://mc.qcloudimg.com/static/img/5ff67be62cace40eee945ee8775b3f42/5.png)


**Note:**

+ TOP100 URL analysis is done through logs, there will be a latency of 1-2 hours;
+ The record of TOP100 data will only be kept for 90 days, if the query time range exceeds the limit of 90 days, the data will not be displayed.


