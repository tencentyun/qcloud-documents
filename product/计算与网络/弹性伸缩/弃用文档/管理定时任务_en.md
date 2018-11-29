## Scheduled Task

Scheduled task means to scale based on a schedule. It allows you to scale the number of CVM instances in response to predictable load changes.

For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can schedule the scaling activities based on the predictable traffic pattern of your Web application.

To create a scheduled scaling action, you specify the start time when the scaling action is expected to take effect, as well as the new minimum (minimum number of instances), maximum (maximum number of instances) and required size (expected number of instances) for the scaling action. AS will update the number of instances in the scaling group based on these values at the specified time.

You can create scheduled actions for scaling one time only or for scaling on a recurring schedule.


## Scheduled Task Management
1. Open the [Console](https://console.cloud.tencent.com/autoscaling/config), and select **Scaling Group** in the navigation bar.

2. Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](http://mccdn.qcloud.com/static/img/bae3ec563534769d6c38143b60299d74/image.png)

3. Select **Scheduled Task** in the top navigation bar, and manage the scheduled task associated with the scaling group on the page:
![](http://mccdn.qcloud.com/static/img/606fc6dc7e5a3e27584f58755e7bca53/image.png)

	- Click **New** to add a scheduled task;

	- Select a scheduled task and click **Modify**. On the pop-up page, you can modify the task name, the execution time and the activities to be executed, and choose whether to execute periodically;

	- Click **Delete** to delete the scheduled task.

If you want to create a scheduled task on a recurring schedule, you can specify a start time. AS performs the action at the specified time, and then performs the action based on the recurring schedule. If you specify an end time, AS does not perform the action after the specified time.



