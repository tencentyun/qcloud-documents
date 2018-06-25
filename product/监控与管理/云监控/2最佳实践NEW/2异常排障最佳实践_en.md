Cloud Monitor provides various methods to help you judge resource exceptions, and informs you of the exception information in real time through multiple channels.

![](http://mc.qcloudimg.com/static/img/3486dc34300abd096c209c69ab4a73b1/image.png)

## Locating Exceptions

### Detecting Exceptions Through Monitoring and Alarming

Monitoring and alarming is a service in which Tencent Cloud can detect exceptions timely and remind users of this initiatively and users detect exceptions passively. This ensures that users can detect exception information in real time in any scenarios. You can log in to the Tencent Cloud Console, and go to [Cloud Monitor Console](https://console.cloud.tencent.com/monitor/overview) to configure corresponding alarm policies for resources of your concern. For more information, please see [Configure Alarm Policy](https://cloud.tencent.com/document/product/248/6215).

If you have configured important performance metrics and events as alarm rules, when an exception occurs, you and your system are informed of this exception immediately in multiple ways through the alarm channel.

Alarm policies configured with an alarm receiving group will reach you via SMS message/email. Besides, features such as repetitive alarm and alarm convergence are also supported, to avoid missing important alarms while preventing you from being badly disturbed by alarms.

You can also make exception alarm information reach your system by configuring the callback API feature in the alarm channel, so as to further aggregate and process the exception alarm information.

### Detecting Exceptions Through Monitoring Views

To locate an exception through monitoring views, you need to initiatively locate the exception according to the average trend and historical data of performance metrics, which requires you to take initiative to detect the exception. Those exceptions for which alarms are not configured or that are difficult to locate using alarm rules can be discovered through monitoring views during daily check. Compared with alarms, monitoring views can help you locate the exception influence surface of resources globally. You can highlight resource exception information under various scenarios by subscribing important resources to dashboard and properly setting charts. For more information, please see [Configure Monitoring Views](https://cloud.tencent.com/document/product/248/13119).

For some instances, you can subscribe instance details views to compare the trends of instance performance data conveniently on the dashboard.

For resource clusters, you can subscribe the aggregated data under the same cluster to view the overall monitoring view of the cluster on the dashboard and compare its trend against that in the view of single instance under this cluster. For more information, please see [Best Practice for Massive Resources Monitoring Scenarios](https://cloud.tencent.com/document/product/248/13521).

Any exception point detected through a view can be located to a specific resource and exception influence surface through the list sorting feature of the view for further exception locating and troubleshooting.

## Exception Troubleshooting

### Locating Exception Objects Through Monitoring Overview Page

When you are conducting daily check or have received an alarm message, you can log in to the Tencent Cloud console, and then go to [Monitoring Overview Page](https://console.cloud.tencent.com/monitor/overview).

1. View the overview page -> cloud service health status module, to find out the resource exceptions in each region and project.
   You can browse through recent exceptions using the exception information overview feature.

   ![](http://mc.qcloudimg.com/static/img/1491420e1cce11a90a57ef3f602ae9f3/image.png)

2. Click the number of exception objects and jump to the cloud product monitoring page.

   ![](http://mc.qcloudimg.com/static/img/a9a643f0d24d5f3c999c36f2f3d81e2d/image.png)

   Specific exceptional resource objects are automatically filtered out on the list page of Cloud Product Monitoring. You can also uncheck the filter option and go back to the list of all objects.

   ![](http://mc.qcloudimg.com/static/img/2198d27636069a35a476d458d770b040/image.png)

3. Click the ID of the specific object to jump to the monitoring details page of the object, where details of rewinding historical statistics and assisting location of exception are provided.

   - Exception timeline, which enables you to view the current and historical information of the exception object. It helps you to troubleshoot current exceptions through historical alarms and status change information.
   - Resource performance monitoring data, which provides you with the most comprehensive resource performance data. It can compare the current data and historical data of the same metric on a year-on-year/month-on-month basis, or compare data changes of different metrics within the same period for troubleshooting.

   ![](http://mc.qcloudimg.com/static/img/d80ab68f3bad08e9f6166f18e5ded136/image.png)


### Locating Exception Objects Through dashboard

1. When an exception trend is found in the monitoring view, click the time period during which exceptions occur, and a sorted list of corresponding instances is displayed below the chart. You can locate the specific exceptional objects through the sorted list.

   ![](http://mc.qcloudimg.com/static/img/a69fec87b521bc3417740a8f3af07dae/image.png)

2. Click the object name in the sorted list to jump to the monitoring details page of the object, where details of rewinding historical statistics and assisting location of exception are provided.

   - Exception timeline, which enables you to view the current and historical information of the exception object. It helps you to troubleshoot current exceptions through historical alarms and status change information.
   - Resource performance monitoring data, which provides you with the most comprehensive resource performance data. It can compare the current data and historical data of the same metric on a year-on-year/month-on-month basis, or compare data changes of different metrics within the same period for troubleshooting.

   ![](http://mc.qcloudimg.com/static/img/d80ab68f3bad08e9f6166f18e5ded136/image.png)

