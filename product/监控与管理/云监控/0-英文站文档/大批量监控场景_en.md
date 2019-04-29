As the continuous development of customer businesses, demands for underlying resources also increase. With more and more basic resources in place, the efficiency of daily monitoring becomes a bottleneck for OPS. Tencent Cloud's Cloud Monitor provides customers who have a large number of resources with a solution for massive resources monitoring scenarios.

## Performance View for Monitoring Massive Resources

With a large quantity of resources in place, it is unpractical to view the metric data of all the cloud resources one by one. Even if you have done so, you still cannot compare these data with the global data, and it is difficult to find out where the exceptions are. Therefore, the following two key points should be noted when you monitor massive resources:

* Aggregation: This refers to the aggregation of the performance data for a batch of resources. With these aggregated data, you can easily understand the overall performance of resource operation.
* Sorting: Data is sorted by different metrics of a batch of resources. So you can quickly find exceptional data and corresponding resource object.

### Creating Aggregation Monitoring View for Massive Resources

Here we take CVM as an example:

1. Classify and manage CVMs by businesses/clusters through the project. Resources of different businesses/clusters reside in different projects.
2. Go to [Dashboard](https://console.cloud.tencent.com/monitor/dashboard) on the Cloud Monitor console, create a new monitoring dashboard, and then name it with the name of a business/cluster.
3. Click "Add Monitoring Chart" on Dashboard.
   ![](http://mc.qcloudimg.com/static/img/846763f78af542e795b211cac8d63e61/image.png)

4. Configure the chart in the pop-up window.
   ![](http://mc.qcloudimg.com/static/img/fc99d01f2c0671e40d66b127e8eaf318/image.png)

5. After the configuration is completed, click "OK" to complete the view creation.
   * You can create multiple charts with multiple metrics in batches to avoid the tedious process of repeatedly selecting monitoring items.
   * You can create charts in batches in the order of object list to prevent you from repeatedly configuring new charts because the number of resources to be monitored exceeds the limit of a chart.
   * In a resource list, you can filter and search resources, select all resources with one key, or select multiple resources by pressing Shift. The friendly batch operation facilitates batch selection of resources, thus improving the configuration efficiency.

6. Bandwidth-based metrics: You can sum up the data of all the servers to obtain the total bandwidth used by a business/cluster.
   Performance-based metrics (such as CPU utilization): You can take the avg, max and min of the monitoring data of all the servers and display them in the same chart. In this case, you can obtain the average, maximum and minimum CPU utilization of a business/cluster. Through the trend comparison of these three curves, you can locate the slopes or peaks of exceptions in an intuitive manner.

   ![](http://mc.qcloudimg.com/static/img/54a195ab0efa737d5675651ee258d297/image.png)

7. **Detect exceptional data in an aggregation view**: Through the overall aggregation curve trend of resources and the comparison among curves, you can understand the overall trend and exceptions of performance data of the resources.

   For example, for bandwidth data, you can determine whether the current bandwidth is exceptional through the comparison between inbound and outbound bandwidth curves as well as the overall trend of bandwidth. For CPU utilization, you can determine the overall condition of resources and whether some of the resources are exceptional through the comparison between the average CPU utilization and the maximum/minimum CPU utilization.

8. **Locate specific exception object**

   8.1 Click a time point on the chart to unfold the sorted list of corresponding instances. You can modify the sorting order and metrics, or modify the data displayed in the sorted list by clicking different points in the chart.

   ![](http://mc.qcloudimg.com/static/img/ccb381ae8e0adb6d39958141617fc082/image.png)

   8.2 When you hover the cursor over an instance in the sorted list, the monitoring data curve corresponding to this instance is highlighted in the above chart. By comparing and analyzing the monitoring curve data of this instance and the overall aggregated data, you can further determine the current and historical exceptions of the instance.

   ![](http://mc.qcloudimg.com/static/img/211946d1b2db8ef3e41cf7847265fca2/image.png)

   8.3 After confirming the specific exception object in the previous two steps, click the name of the exception object in the list to jump to its monitoring details page for further troubleshooting.

Now, you have finished the process of creating a monitoring view -> viewing a monitoring view -> detecting an exception -> locating the specific exception. Through the combination of the chart and the sorted list, you can get an intuitive overview of the operation status of global resources, locate specific exception objects, and analyze the exceptional trend, thus solving the problems of low massive resources monitoring efficiency and difficult exception detection.

> Note:
> A maximum of 12 cloud service instances can be added to each chart in Dashboard. If this cannot meet your needs, you can submit a ticket to raise the limit.

### Creating Details Monitoring View of Massive Resources

Apart from aggregation views, you can also choose a details view to help you detect and locate exceptions for massive resources.

Details view: The curves of all instances are displayed in the same chart.
Aggregation view: The curves of all instances are computed and aggregated into one or more curves using a user-defined statistical method.

1. **Create a details view**
   A details view is created in the same way as with an aggregation view. When creating a details view, you do not need to select the statistical method. For the specific process, please see [Configure Monitoring View](https://cloud.tencent.com/document/product/248/13119) in Configuration of Dashboard document.

2. **Detect exceptional data in a details view**
* The more the resources in the same business/cluster, the denser the curves in the chart. The overall trend and the density of curves in the chart indicate the overall trend and distribution of the performance data of resources.
* If some of the curves are away from the dense area, this indicates that the performance data of this instance is exceptional.

3. **Locate specific exception object**
   A details view can also be combined with a chart and a sorted list to locate a specific exception object. The overall process is similar to that of an aggregation view. You can refer to the point 6 of aggregation view above.

> Note:
> A maximum of 12 cloud service instances can be added to each chart in Dashboard. If this cannot meet your needs, you can submit a ticket to raise the limit.

## Configuring Alarm Policies for Massive Resources

1. Classify and manage cloud service resources by businesses/clusters through the project. Resources of different businesses/clusters reside in different projects.
2. Go to "My Alarms" module in the Cloud Monitor console to create alarm policies for resources. Since the resources have been grouped by projects, you can create default [Alarm Policy](https://cloud.tencent.com/document/product/248/6215) for different projects.
   The default alarm policy is automatically bound with all the resources under the project. If resource changes such as new resource, project change or termination upon expiry occur, the resource objects bound to the default policy by default will change synchronously, avoiding the cost of tedious manual maintenance.


