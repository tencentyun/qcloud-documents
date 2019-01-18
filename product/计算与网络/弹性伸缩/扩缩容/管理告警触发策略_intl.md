## Introduction

AS supports dynamic scaling of the number of instances in the scaling group based on the monitoring metrics, provided that you define the alarm trigger policy, including the status of the monitoring metrics that trigger the scaling, and how you want to scale in response to changing demand.

You need to specify the conditions and actions when creating an alarm policy:
- Condition format: A metric + threshold + period + number of periods during which the threshold is reached. That is, the value of the metric breaches the threshold that you defined, for the number of periods that you specified.
- Actions: Sending notification + increasing/decreasing a specified number of CVMs.

It is recommended that you create two policies for each scaling change: one policy to scale out and another policy to scale in. Once your business volume breaches the threshold of the alarm policy, AS executes the associated policy to scale your group in (by terminating instances) or out (by launching instances).

As shown in the figure below:

![](https://mc.qcloudimg.com/static/img/83557f69f860be57cf464b2b45ab31c5/1.jpg)

## Scenario Example

For example, you have an e-commerce web application that currently runs on five instances. You carry out an operating activity, and worry about that the number of visits is much greater than you've expected. You can launch two new instances when the load on the current instance increases to 70%, and terminate these instances when the load decreases to 40%. You can configure the scaling group to scale automatically based on these conditions.

![](https://mc.qcloudimg.com/static/img/92435c4281be33320200ce3f69bbc36c/AS-Expanding+and+Reducing-Managing+Alarm+Triggering+Policies.jpg)

## Steps

1. Open the [Console](https://console.cloud.tencent.com/autoscaling/config), and select **Scaling Group** in the navigation bar.

2. Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mc.qcloudimg.com/static/img/cebad1b79ccba9fb9548c2bd2c30a210/2.jpg)

3. Select **Alarm Trigger Policy** in the top navigation bar, and manage the alarm trigger policy associated with the scaling group on this page.
	- Click **New** to add a new alarm trigger policy;
	- Click **Delete** to delete the alarm trigger policy.

![](https://mc.qcloudimg.com/static/img/570e5bd24b8975c65dd939bc9052d5a3/3.jpg)


## Exclude a Server from the Alarm Scaling Policy
Before using auto scaling, your system may have a server that is regularly used. Given the following considerations, you may not want the server to be removed by the alarm scaling policy:

- **One server for multiple uses**: Apart from the tasks specified by the cluster, a server in the cluster is also used for other purposes. For example, in the early stage of website construction, one of your servers is used as both a cache server and a file server. You don't want the server to be removed by the alarm scaling policy when placing the cluster of cache servers into a scaling group.

- **Data storage**: The server is in service or stores data that other servers do not have. For example, the server stores the incremental data of other running servers in a cluster.

- **Image/Snapshot updates**: The server is used to update the image and snapshot regularly.


**How to configure:**


**Step 1**: In the [Scaling Group List](https://console.cloud.tencent.com/autoscaling), click the scaling group in which the server resides to enter the management page;

**Step 2**: In the **CVM List** at the bottom of the management page, click **Set Removal Protection** for the appropriate CVM.
