The scaling group can adjust the number of CVMs based on the scaling policy:
- Create a **scheduled task** to perform scaling activities as scheduled, and you can also set to execute the scheduled task periodically;
- Create an **alarm trigger policy** to perform scaling activities according to cloud monitoring indicators (such as CPU utilization and memory usage).

## Create a Scheduled Task
If your load changes are predictable, you can set a scheduled task to plan your scaling activities. You can use this feature to automatically increase or decrease CVM instances on a scheduled and periodical basis to flexibly deal with traffic load changes and improve device utilization while saving deployment and instance costs.

**Steps:** 

In the **Scaling Group** page, click the scaling group ID to enter the scaling group management page.
![](https://mc.qcloudimg.com/static/img/cebad1b79ccba9fb9548c2bd2c30a210/31.jpg)

Select the **Timing Task** tab, and click **New**.
![](https://mc.qcloudimg.com/static/img/4f1f4aefc3b5bb73ecf758014a05fee3/32.jpg)

Specify information such as the scheduled task name, execution time, and activities to be executed in the New page. You can also check **Duplicate** to define the interval for the execution of a scheduled task.
![](https://mc.qcloudimg.com/static/img/7de4f1afee9e267d023be26b61143b11/33.jpg)

After setting, the scheduled task will be displayed in the list on the page, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/d63deed2755236fc4ecfa3b5d5225936/34.jpg)

## Create an Alarm Trigger Policy
If you wish to adjust business deployment based on CVM metrics, you can customize the alarm trigger policy, which will automatically increase or decrease the number of CVM instances when business load pushes the metrics to the threshold. This flexibly deals with traffic load changes, improves device utilization, and saves deployment and instance costs.


**Steps:** 

> - When a scaling group is created, a ping unreachable alarm trigger policy is created by default to replace the unhealthy sub-machine.
> - Before using the alarm trigger policy, you need to install a new version of Cloud Monitor Agent in the CVM image. For the installation method, refer to [Install Monitoring Components](/doc/product/248/安装监控组件)

In the **Scaling Group** page, click the scaling group ID to enter the scaling group management page.
![](https://mc.qcloudimg.com/static/img/cebad1b79ccba9fb9548c2bd2c30a210/31.jpg)

Select the **Alarm Trigger Policy** tab, and click **New**.
![](https://mc.qcloudimg.com/static/img/c5e08feff6bf4015c7503a9061af5e07/35.jpg)

Set the alarm policy in the New page to automatically increase or decrease CVM instances by a specified number or percentage for the scaling group based on cloud monitoring performance metrics (such as CPU, memory, and bandwidth).

You can also copy the existing policy of an existing scaling group to the current scaling group by setting in the **Copy Policy (Optional)**.
![](https://mc.qcloudimg.com/static/img/314ebc50386cfcbcd570d4c6224d7c02/36.jpg)

After setting, the alarm trigger policy will be displayed in the list on the page, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/f832ab241eb32864a87839da77f9b9d1/37.jpg)



