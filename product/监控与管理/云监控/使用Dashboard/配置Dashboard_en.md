## Monitoring Dashboard Configuration

You can gain an quick insight into the running status of various cloud resources by viewing different monitoring dashboards.

- All monitoring views are created on the monitoring dashboard, so a monitoring dashboard can be interpreted as a collection of monitoring views.
- Cloud resources in various groups can be distinguished by creating different monitoring dashboards.

A maximum of 20 monitoring dashboards can be created by each developer.

### Creating a Monitoring Dashboard

1. Log in to [Dashboard](https://console.cloud.tencent.com/monitor/dashboard) page of Tencent cloud monitor console.
2. Click "+" icon, the button used to create a monitoring dashboard.
3. Enter the monitoring dashboard name, and click "OK" to complete the dashboard creation.
   ![3](http://mc.qcloudimg.com/static/img/389f555ee1ffb844fb00f8c61822c38b/image.png)

### Renaming and Deleting Dashboards

You can rename or delete a dashboard by clicking "..." icon on the right side of the dashboard.
![](http://mc.qcloudimg.com/static/img/affd539eaf50e0d41a4a4e3dc42573bc/image.png)

### Adjusting Dashboard Sorting Order

You can adjust dashboard sorting order by dragging a dashboard tab to the destination position.
![](http://mc.qcloudimg.com/static/img/87c038ba833c3e612dc5a3ab6d3664aa/image.png)

## Monitoring View Configuration

You can flexibly monitor resource performance in various scenarios by creating different monitoring views on the dashboard. Rich view categories, linkage views, view zooming by dragging, and other features make it easier for you to view monitoring data.

### Viewing Categories

Now, the dashboard service provides three types of monitoring views: line charts, area charts and bar charts.

- Line chart: As the most commonly used view, it can display the vast majority of sequential monitoring data.
- Bar chart: It is applicable to metrics like disk usage, helping you view the current resource consumption rate.

### Creating Line Charts

A line chart contains a details view and an aggregation view.

- Details view: Multiple curves reflecting the same metric for multiple resources are displayed in one view.
- Aggregation view: Curves of aggregated data reflecting the same metric for multiple resources are displayed in one view. Aggregation data of two metrics with the same unit can be displayed at the same time.

![](http://mc.qcloudimg.com/static/img/67c54615dc83ed2bb92b1e4684ed9d44/image.png)

#### Creating Processes

1. Click "Add Monitoring Chart" on the dashboard.
   ![](http://mc.qcloudimg.com/static/img/846763f78af542e795b211cac8d63e61/image.png)

2. Configure the chart in the pop-up window.
   ![](http://mc.qcloudimg.com/static/img/fc99d01f2c0671e40d66b127e8eaf318/image.png)

3. After the configuration is completed, click "OK" to complete the view creation.
   - If there is no view on the dashboard, views are created at positions from the top left to the bottom right on the dashboard by default.
   - If there are views on the dashboard, views are created following the bottom view from the top left to the bottom right on the dashboard.

> **Note:**
> 
> When creating charts, you can create multiple charts with multiple metrics in batches for the same batch of objects to avoid the tedious process of repeatedly selecting monitoring items.
>
> If the number of selected instances exceeds the limit of a single chart, the charts will be created in batches in the order of object list by default to prevent you from repeatedly configuring new charts.
>
> When selecting resources for an instance, you can filter, search, select all with one key, and select multiple with shift key in the resource list. The friendly batch operation facilitate batch selection of resources, thus improving the configuration efficiency.

### Creating Bar Charts

1. The creation process of a bar chart is same as that of a line chart.
2. If the selected metric is "CVM - Disk Usage", the chart is automatically switched to a bar chart.


