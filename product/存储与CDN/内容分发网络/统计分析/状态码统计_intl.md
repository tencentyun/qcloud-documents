Log in to [CDN Console](https://console.cloud.tencent.com/cdn), and click "Status Code" under "Statistics" to review statistics of 2XX, 3XX, 4XX, 5XX status codes.



## Query Criteria Instruction

The following query criteria are supported when querying status code statistics:

![](https://mc.qcloudimg.com/static/img/3f2027ec9927755a4d24d0165c683f13/1.png)



**Note:**



+ Time selection: The query for statistical data for the last 90 days is supported with a query span of up to 90 days.

+ Project: Query for usage data based on project is supported;

+ Domain: Query for usage data based on specified domain is supported;

+ Network layer: Query for status code statistics of edge nodes or intermediate nodes is supported;

+ Temporal granularity: This refers to the temporal granularity with which bandwidth and traffic data will be presented. This is related to the selected time span:

  > If the selected time span is 1 day, you can query data with a temporal granularity of 5 minutes, 15 minutes, 30 minutes, 2 hours or 4 hours;

  > If the selected time span is 2-3 days, you can query data with a temporal granularity of 15 minutes, 30 minutes, 2 hours or 4 hours;

  > If the selected time span is 4-7 days, you can query data with a temporal granularity of 2 hours, 4 hours or 1 day;

  > If the selected time span is more than 30 days, you can only query data with a temporal granularity of 4 hours or 1 day;



## Data Result Description

### Status Code Statistics

Displays the statistical data curve graph of 2XX, 3XX, 4XX, 5XX status codes:

![](https://mc.qcloudimg.com/static/img/126f0bb583fb06ec38649789324b4348/2.png)



**Statistics Instruction:**



+ 2XX: Statistics of status code 200 and 206;

+ 3XX: Statistics of status code 304;

+ 4XX: Statistics of status code 404 and 416;

+ 5XX: Statistics of status code 500.



**Note:**



+ The minimum granularity of status code statistics is five minutes, that is, the statistical data from 2016-10-25 15:00:00 to 15:04:59 will be shown at the statistical point of 2016-10-25 15:05:00;

+ The latency of real-time data is about five minutes, that is, the statistical point of 2016-10-25 15:05:00 will appear around 2016-10-25 15:10:00;

+ Domains added within 90 days by the user, including deleted domains, will be displayed in the "All domains" drop-down box;

+ Note about statistics:

  > If the domain has not been connected to CDN for the specified time range, it will not be covered in statistics even if it is checked;

  > If the domain has been deleted for the specified time range, it will not be covered in statistics even if it is checked;

  > If the domain experienced three stages (not connected, connected and deleted) for the specified time range, the statistical data for unconnected and deleted time period will be filled by 0.



### Status Code Distribution

Detailed statistics regarding the number and proportion of status codes:

![](https://mc.qcloudimg.com/static/img/a54907bfa41bab8b3bb97ea97446e2fa/3.png)


