Log in to [CDN Console](https://console.qcloud.com/cdn), and click "Access" page under "Statistics" to review real-time statistics of request quantity, number of IP visits, hit rates. You can check the historical record within 90 days.

## Query Criteria Instruction
The following criteria are supported when querying access statistics:
![](https://mc.qcloudimg.com/static/img/9e835338bd4d7de2adb3d93e2da44cc1/request_query_condition.png)

**Note:**

+ Time selection: The query for access statistics for the last 90 days is supported with a query span of up to 90 days.
+ Project: Query for usage data based on project is supported;
+ Domain: Query for usage data based on specified domain is supported;
+ Region: Query for usage data based on specified region is supported. Currently you cannot select both "Region" and "Carrier", when you select regions, the carrier will need to be "All carriers";
+ Carrier: Query for usage data based on specified carrier is supported. Currently you cannot select both "Region" and "Carrier", when you select a carrier, the region will need to be "All regions";
+ Temporal granularity: This refers to the temporal granularity with which bandwidth and traffic data will be presented. This is related to the selected time span:
	> If the selected time span is 1 day, you can query data with a temporal granularity of 5 minutes, 15 minutes, 30 minutes, 2 hours or 4 hours;
	> If the selected time span is 2-3 days, you can query data with a temporal granularity of 15 minutes, 30 minutes, 2 hours or 4 hours;
	> If the selected time span is 4-7 days, you can query data with a temporal granularity of 2 hours, 4 hours or 1 day;
	> If the selected time span is more than 30 days, you can only query data with a temporal granularity of 4 hours or 1 day;

## Data Result Description
### Access Statistics
The figure shows the data under the specified query criteria:
![](https://mc.qcloudimg.com/static/img/a8f0a7d04f6541a3e2ecf7f170d711ab/requests.png)

+ Network-wide statistics for number of requests of OC nodes;
+ Statistics for number of IP visits: This statistic is obtained by calculating all request IPs within 5 minutes after removing duplicates;
+ Hit rate: Hit rate (%) = (number of requests - number of back-to-origin requests) / number of requests.

**Note:**

+ For access statistics, there is a statistical point every five minutes, that is, the statistical data from 2016-10-25 15:00:00 to 15:04:59 will be presented at the statistical point of 2016-10-25 15:05:00;
+ The latency of real-time data is about five minutes, that is, the statistical point of 2016-10-25 15:05:00 will appear around 2016-10-25 15:10:00;
+ All domains connected within 90 days will be covered in the "All Domains" drop-down box, including those that have been deleted;
+ Note about statistics:
	> If the domain has not been connected to CDN for the specified time range, it will not be covered in statistics even if it is checked;
	> If the domain has been deleted for the specified time range, it will not be covered in statistics even if it is checked;
	> If the domain experienced three stages (not connected, connected and deleted) for the specified time range, the statistical data for unconnected and deleted time period will be filled by 0.

### Carrier and Province Analysis
The number of requests are ranked and analyzed based on provinces and carriers:
![](https://mc.qcloudimg.com/static/img/35beb0fcc742eefdf82ae11f6864db46/request_province.png)

**Note:**

+ Carrier and province data is analyzed through logs, thus the data belongs to application layer. There will be deviations between this data and the statistics of traffic and bandwidth NIC data in the previous figure;
+ Latency of data statistics during peak hours is less than 30 minutes;
+ The record of carrier and province data will only be kept for 90 days, if the query time range exceeds the limit of 90 days, the data will not be displayed.

### Domain Access Status Statistics
You can click "Download all data" to download detailed data about the domain, number of requests, number of IP visits, hit rate according to the selected query criteria:
![](https://mc.qcloudimg.com/static/img/612284e7768e4157502e8552d93ad96b/request_donmain_detail.png)


### TOP100 URL
TOP100 analysis for requests towards individual URL resources is carried out according to the selected query criteria to help you locate popular resources:
![](https://mc.qcloudimg.com/static/img/946aa1e57beaf37dd904aebe26a601a0/request_top100.png)


**Note:**

+ TOP100 URL analysis is done through logs, there will be a latency of 1-2 hours;
+ The record of TOP100 data will only be kept for 90 days, if the query time range exceeds the limit of 90 days, the data will not be displayed.


