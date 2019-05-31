In addition to monitoring data collection, Cloud Monitor also provides an intuitive way to view the changes of metric data for a certain period of time in charts, allowing you to stay on top of the changes and take appropriate actions.

## Viewing the Monitoring Charts of a Single Resource

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" - "Cloud Product Monitoring", and then select the type of the product you wish to view.
> Note: If there is no desired product, you can check whether there is a monitoring tab in the corresponding product console and obtain relevant data there.

2) Select a specific object to be monitored, and click object ID to enter the details page of monitor.

3) You will see specific monitoring metrics of current product on the left of Overview page and the charts containing the data of each metric for a certain period of time on the right. You can click a specific metric on the left to enter the chart views of a single metric.

## Viewing the Monitoring Chart of Multiple Resources
You can view the metric data of multiple resources in a chart by setting in "Custom Monitoring View" in "Monitor Overview". For more information, please see [Custom Monitoring View](/doc/product/248/6214).

## Modifying the Time Period to Display in a Chart
You may need to view the monitoring data for a different time period. Please note that the interval of data collection varies with different time period selected to display.

<table><tbody>
<tr><th>Time Period to Display</th><th>Default Interval of Data Collection</th></tr>
<tr><td>≤ 1 hour</td><td>1 minute (only for CVM)<br>5 minutes (default value as a legend in the chart)</td></tr>
<tr><td>≤ 24 hours</td><td>5 minutes</td></tr>
<tr><td>≤ 7 days</td><td>1 hour</td></tr>
<tr><td>> 7 days</td><td>1 day</td></tr>
</tbody></table>

You can click in the upper right corner to select the time period to display. There are several time periods preset by Cloud Monitor: "Last hour", "Today", "Yesterday", "Last 7 days" and "Last 14 days". You can also specify a time period using the date picker.

You can also view the data in a day for recent half year, and also the data in one minute, five minutes and one hour for the recent thirty-one days. 

 The data can be displayed for up to thirty one days. 

