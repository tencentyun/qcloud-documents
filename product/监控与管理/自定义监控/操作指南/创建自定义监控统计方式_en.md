1) Log in to Tencent Cloud Console, select "Cloud Monitor" -> "CCM", and click "Monitor Configuration" tab. In the page of monitor configuration list, click "Manage" button at the end of the line of a created metric to enter the metric configuration details page:
![](//mccdn.qcloud.com/static/img/7a006801eb63d6a8e03f4b8fb1ab49ee/image.png)

2) Original dimensions are the default dimensions added during creation. You can also choose dimension aggregation data for analysis. Click "Metric Configuration" button, and select statistical method and statistical period in the pop-up window. Here, we take calculating CPU utilization by taking the maximum value within 5 minutes as an example:
> Note: Please properly configure the statistical type (including statistical method and statistical period) of the metric, otherwise the reported data may not be correctly recorded. Cloud Monitor Platform will calculate the data based on the statistical type of the metric and store the data. It will then display the data and trigger the alarm in the console.

![](//mccdn.qcloud.com/static/img/e727f69b913c14335bd42f0d62d58d45/image.png)

![](//mccdn.qcloud.com/static/img/1bad0b345a09df8b2bfc106bbcad4dbe/image.png)
