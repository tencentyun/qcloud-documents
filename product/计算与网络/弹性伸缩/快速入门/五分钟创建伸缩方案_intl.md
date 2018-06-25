You can create a complete auto scaling solution by performing the following three steps:
![](https://mc.qcloudimg.com/static/img/cfca5d454509e38558e458cca5efecc4/AS-Creating+a+Scaling+Solution.png)

> Note: The example below are performed in the console. If you want to use API, refer to [API Usage Examples](https://cloud.tencent.com/document/product/377/4232).

## Step 1: Create a Scaling Configuration
The scaling configuration defines the configuration information of CVM instances used for auto scaling, including the image, storage, network, security group, login method of the CVM.

> Note: The scaling configuration is created **completely free of charge**.

Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Configuration** in the navigation bar.

### Select a Region

The CVMs which can be added manually and the cloud load balancers which can be bound are restricted by your selected region. For example, if you select Guangzhou as the region of the scaling configuration, the CVM of Guangzhou is automatically added to the scaling group. In a scaling group of Guangzhou region, you cannot add CVMs in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.) manually, nor bind load balancers in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.).

![](https://mc.qcloudimg.com/static/img/9a39d87fa90f3ae5995073a6077b1057/11.jpg)


Click ![](https://mc.qcloudimg.com/static/img/60fa242cdf5488626d6968f2c174222c/12.jpg), and fill in the basic scaling configuration information in the pop-up page.

## Select a Model
- Name the configuration.
- Select the same CVM model to which the scaling group is going to bind.

![](https://mc.qcloudimg.com/static/img/02220977468b12ef47c9aeb30a26b06d/13.jpg)


### Select an Image
You can use a public image or a custom image to create the scaling configuration.

It is strongly recommended that you use the custom image of which the environment has been deployed. The reasons include the following:

- If you select a public image, the scaled CVM instance is a clear OS, and you need to manually deploy the application environment;
- If you select a custom image, by creating an image for the CVM instance of which the environment has been deployed, and using the image to create CVM instances in batches, the CVM instances will have the same software environment as the original CVM instance after created successfully, and thus the batch deployment is achieved.

Therefore, it is recommended to select a custom image here.
Bind the image of the **CVM to which the scaling group is going to bind**.
[How to create the image for the "CVM to which the scaling group is going to bind"?](https://intl.cloud.tencent.com/document/product/213/4940)
![](https://mc.qcloudimg.com/static/img/4a199eb83c1a38c47d9d545e44acea62/14.jpg)


### Select a Storage and a Network

Set storage and network in this page.

![](https://mc.qcloudimg.com/static/img/4d39abc1fd4ed12927aa80591518328d/15.jpg)

Please note that if you select the cloud disk as the system disk, then you can select the data disk snapshot for the data disk.

For users with large amount of data, they often use data disks to store data. When data disk A creates a snapshot file, users can use it to quickly clone multiple disks, achieving a fast server deployment.

When the auto scaling automatically adds a new CVM instance, if the data disk snapshot is specified in scaling configuration, Tencent Cloud's cloud disk can allow the automatic mounting of the data disk containing the set data after the CVM instance is activated, so as to meet the needs of automatic data copy.

If the data disk snapshot is specified in the scaling configuration, you need to ensure that the data disk can be mounted automatically and correctly for the successful automatic scale-up of the scaling group. You need to perform some operations on the original instance of the data disk snapshot before setting the auto scaling, so as to realize the automatic mounting of data disk when activating a new CVM instance. For instructions on how to do this, refer to [How to Mount Data Disk Automatically When Activating New Instance Using Custom Image and Data Disk Snapshot](https://intl.cloud.tencent.com/document/product/362/7871)

> Note:
>-  Auto Scaling service is free of charge, and newly added servers, hard disks and networks will be charged by the traffic of CVM instances, hard disks and networks. This page will display prices based on your settings.

### Set Information
![](https://mc.qcloudimg.com/static/img/5738fa58c6990e7428c83e6d20ebd80c/as_revise_1.jpg)
Select the login method and security group in the **Set Information** page. The CVM instances added via the Auto Scaling service use Cloud Security and Cloud Monitor services for free by default.

After configuration, this entry will be displayed in the scaling configuration list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/c968ea622f06c8cfdd19f96b04fd5bb8/17.jpg)


## Step 2: Create a Scaling Group
A scaling group is a collection of CVM instances following the same rules and serving the same scenario.
Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Group** in the navigation bar.

### Create a Scaling Group
Click ![](https://mc.qcloudimg.com/static/img/60fa242cdf5488626d6968f2c174222c/12.jpg), and fill in the basic information on scaling group in the pop-up page. Items with ![](//mccdn.qcloud.com/static/img/f9df27a1d1e0d42a7ff08dd884bfa34c/image.png) are required.

- The current number of CVM instances in the scaling group will be kept between the minimum and the maximum scaling group sizes.
	- The initial number of instances defines the number of CVM instances in the scaling group when created;
	- If the current number of CVM instances is less than the minimum scaling group size, the Auto Scaling service will automatically add instances to make it equal to the minimum scaling group size;
	- If the current number of CVM instances is greater than the maximum scaling group size, the Auto Scaling service will automatically decrease instances to make it equal to the maximum scaling group size;
- You can select the existing scaling configuration, or create a new scaling configuration.
- Select a network, availability zone, and remove policy.
- (Optional) You can choose to associate with an existing cloud load balance policy or create a new load balancer.

![](https://mc.qcloudimg.com/static/img/e82f2ce171a0cff61f075b0cd7bd17f0/23.jpg)
![](https://mc.qcloudimg.com/static/img/f3ab676105c79c61ce877b92e4e6ca7c/24.jpg)

After configuration, this entry will be displayed in the scaling group list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/7c9974b283c4299d37e482b5a745979a/25.jpg)

### Add a CVM (Optional) 
Now, let's bind a CVM.

Add the CVM instance to be bound in the CVM list. After configuration, this entry will be displayed in the scaling configuration list, as shown in the figure below:

![](https://mc.qcloudimg.com/static/img/6e12d2e111f550ced48277017dbc131a/26.jpg)

> Note: If you cannot add or remove a CVM, please check the maximum and minimum scaling group sizes you set.

## Step 3: Create a Scaling Policy
The scaling group can adjust the number of CVMs based on the scaling policy:
- Create a **scheduled task** to perform scaling activities as scheduled, and you can also set to execute the scheduled task periodically;
- Create an **alarm trigger policy** to perform scaling activities according to cloud monitoring indicators (such as CPU utilization and memory usage).

### Create a Scheduled Task
If your load changes are predictable, you can set a scheduled task to plan your scaling activities. You can use this feature to automatically increase or decrease CVM instances on a scheduled and periodical basis to flexibly deal with traffic load changes and improve device utilization while saving deployment and instance costs.

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

> - When a scaling group is created, a ping unreachable alarm trigger policy is created by default to replace the unhealthy machine.
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


