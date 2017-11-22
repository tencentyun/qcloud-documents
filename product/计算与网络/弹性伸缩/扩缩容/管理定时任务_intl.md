切换至1.0对外运营
欢迎您，v_yunyxiao
增效工具
Markdown编辑器
资源上传工具
产品介绍页模板管理
文档中心(新)
官网运营> 增效工具 > Markdown编辑器
|||||

Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mc.qcloudimg.com/static/img/06a1ca079f41a7cd825b47c68304f6f5/1.jpg)

Users may view the list of CVMs bound to the scaling group in this page.
- To manually add CVM instances to the scaling group, click **Add CVM**, select the instance to be added (hold Shift key to select multiple instances) and click **OK**;
- To unbind a certain CVM, click **Remove** behind the corresponding CVM entry.
![](https://mc.qcloudimg.com/static/img/32296300304a228286b919c41ab30613/2.jpg)

Automatically created machines will be terminated when removed.
Manually added machines will not be terminated upon removal. They will only be removed from the scaling group, and the load balancer will be unbound.



## Scheduled Task
​
Scheduled task means to scale based on a schedule. It allows you to scale the number of CVM instances in response to predictable load changes.
​
For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can schedule the scaling activities based on the predictable traffic pattern of your Web application.
​
To create a scheduled scaling action, you specify the start time when the scaling action is expected to take effect, as well as the new minimum (minimum number of instances), maximum (maximum number of instances) and required size (expected number of instances) for the scaling action. AS will update the number of instances in the scaling group based on these values at the specified time.
​
You can create scheduled actions for scaling one time only or for scaling on a recurring schedule.
​
​
## Scheduled Task Management
1. Open the [Console](https://console.cloud.tencent.com/autoscaling/config), and select **Scaling Group** in the navigation bar.
​
2. Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mc.qcloudimg.com/static/img/cebad1b79ccba9fb9548c2bd2c30a210/31.jpg)
​
3. Select **Timing Task** in the top navigation bar, and manage the scheduled task associated with the scaling group on the page:
![](https://mc.qcloudimg.com/static/img/a649a9205c2b994db09c4b79583a3827/32.jpg)
​
  - Click **New** to add a scheduled task;
​
  - Select a scheduled task and click **Modify**. On the pop-up page, you can modify the task name, the execution time and the activities to be executed, and choose whether to execute periodically;
​
  - Click **Delete** to delete the scheduled task.
​
If you want to create a scheduled task on a recurring schedule, you can specify a start time. AS performs the action at the specified time, and then performs the action based on the recurring schedule. If you specify an end time, AS does not perform the action after the specified time.
​
Scheduled Task
Scheduled Task Management
Scheduled Task

Scheduled task means to scale based on a schedule. It allows you to scale the number of CVM instances in response to predictable load changes.

For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can schedule the scaling activities based on the predictable traffic pattern of your Web application.

To create a scheduled scaling action, you specify the start time when the scaling action is expected to take effect, as well as the new minimum (minimum number of instances), maximum (maximum number of instances) and required size (expected number of instances) for the scaling action. AS will update the number of instances in the scaling group based on these values at the specified time.

You can create scheduled actions for scaling one time only or for scaling on a recurring schedule.

Scheduled Task Management

Open the Console, and select Scaling Group in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.


Select Timing Task in the top navigation bar, and manage the scheduled task associated with the scaling group on the page:


Click New to add a scheduled task;

Select a scheduled task and click Modify. On the pop-up page, you can modify the task name, the execution time and the activities to be executed, and choose whether to execute periodically;

Click Delete to delete the scheduled task.

If you want to create a scheduled task on a recurring schedule, you can specify a start time. AS performs the action at the specified time, and then performs the action based on the recurring schedule. If you specify an end time, AS does not perform the action after the specified time.
