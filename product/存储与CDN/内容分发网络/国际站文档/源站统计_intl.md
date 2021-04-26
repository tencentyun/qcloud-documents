Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and click "Origin" page under "Statistics" to review statistical data such as back-to-origin bandwidth, back-to-origin traffic and back-to-origin speed.

## Query Criteria Instruction
The following query criteria are supported when querying back-to-origin statistic data:
![](https://mc.qcloudimg.com/static/img/c40e3e69331742bd187f7f394ebab739/1.png)

**Note:**

+ Project: Query for usage data based on project is supported;

+ Domain: Query for usage data based on specified domain is supported;

+ Temporal granularity: This refers to the temporal granularity with which bandwidth and traffic data will be presented. This is related to the selected time span:
  > If the selected time span is 1 day, you can query data with a temporal granularity of 5 minutes, 15 minutes, 30 minutes, 2 hours or 4 hours;
  > If the selected time span is 2-3 days, you can query data with a temporal granularity of 15 minutes, 30 minutes, 2 hours or 4 hours;
  > If the selected time span is 4-7 days, you can query data with a temporal granularity of 2 hours, 4 hours or 1 day;
  > If the selected time span is more than 30 days, you can only query data with a temporal granularity of 4 hours or 1 day;

+ The minimum granularity of back-to-origin statistics is five minutes, that is, the statistical data from 2016-10-25 15:00:00 to 15:04:59 will be shown at the statistical point of 2016-10-25 15:05:00;
+ The latency of real-time data is about five minutes, that is, the statistical point of 2016-10-25 15:05:00 will appear around 2016-10-25 15:10:00;

+ All domains that have been connected by the user will be displayed in the "All domains" drop-down box; deleted domains are grayed out:
  > If the domain has not been connected to CDN for the specified time range, it will not be covered in statistics even if it is checked;
  > If the domain has been deleted for the specified time range, it will not be covered in statistics even if it is checked;
  > If the domain experienced three stages (not connected, connected and deleted) for the specified time range, the statistical data for unconnected and deleted time period will be filled by 0.

## Data Result Description
**Note about statistics:**

Back-to-origin failure rate statistics, back-to-origin failure analysis, and 404 status code are obtained from the statistical analysis of logs, thus such data are collected from the hosting source dimension:

> Connect the accelerated domain "www.a.com"  and set its hosting source to "www.c.com";
> Connect the accelerated domain "www.b.com", and set its hosting source to "www.c.com";

In this situation, the query results regarding relevant information of "www.a.com" or "www.b.com" are the same, which will be the statistics of the origin server "www.c.com".

The statistics of back-to-origin bandwidth and back-to-origin speed are collected independently without following the above logic.
### Back-to-origin Traffic and Bandwidth
Displays statistical curve graph of back-to-origin traffic and back-to-origin bandwidth:
![](https://mc.qcloudimg.com/static/img/08ba22338ee731ec7d036f30c5000c86/2.png)


### Back-to-origin Speed
CDN provides back-to-origin speed monitoring to give you a better understanding of the quality of back-to-origin links. Back-to-origin speed is calculated by dividing the total traffic of all back-to-origin requests with the time spent by all back-to-origin requests, during the statistical cycle.
![](https://mc.qcloudimg.com/static/img/fe77f762a89dd9130b0e8e3acf7a1dd3/3.png)

### Back-to-origin Failure Rate
Displays the statistical curve graph of real-time back-to-origin failure rate:

![](https://mc.qcloudimg.com/static/img/6c7d1031c571eb1a1a1c41a0704fbf0c/4.png)

**Note:**

+ Back-to-origin failure rate = number of failed back-to-origin requests / total number of back-to-origin requests. Situations when a request is considered failed include TCP connection timeout, origin server disconnection, incompatible HTTP protocols and 5XX server error. For more details, please refer to the following "Details of Back-to-origin Failure";
+ Statistical data regarding back-to-origin failure rate is provided starting from 2016-10-15. Currently you cannot query for data before this date;
+ You can configure real-time alarms against back-to-origin failure rate for CDN domains and projects in [Cloud Monitoring](https://console.cloud.tencent.com/monitor/policylist).


### Details of Back-to-origin Failure Types
In correspondence with back-to-origin failure rate, real-time statistics and proportions of various types of back-to-origin failures are displayed:
![](https://mc.qcloudimg.com/static/img/708035e68b9a3ebf948256ad190526b9/5.png)

### 404 Status Code Statistics
Provides statistics of 404 status codes that are generated for back-to-origin requests:
![](https://mc.qcloudimg.com/static/img/73500636cbce3c8368faff0d9de0f43a/6.png)

**Note:**

+ Statistical data regarding 404 status codes is provided starting from 2016-10-15. Currently you cannot query for data before this date;

  ​

