## 1. Viewing Scaling Group List

1. Open the [Console](https://console.cloud.tencent.com/autoscaling), and click **Scaling Group** in the navigation bar to view the list.
![](https://mccdn.qcloud.com/static/img/ff713a0ff792e49e5e8e099e59251b5a/image.png)

## 2. Creating a Scaling Group

Open the [Console](https://console.cloud.tencent.com/autoscaling/config), and select **Scaling Group** in the navigation bar.

### 2.1. Select a Region

Select the region above the console where the scaling group shall be established. The CVMs which can be added manually and the cloud load balancers which can be bound are restricted by your selected region. For example, if you select Guangzhou as the region of the scaling configuration, the CVM of Guangzhou is automatically added to the scaling group. In a scaling group of Guangzhou region, you cannot add CVMs in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc) manually, nor bind load balancers in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.)

![](https://mc.qcloudimg.com/static/img/fc2af25ac2023adb97f427aa68b72ff4/image.jpg)

### 2.2. Define Information
Click the **New** button and define attributes of the scaling group:

  - **Name of Scaling Group**: labels the scaling group. For example, "Website Logical Layer"
  - **Minimum scaling group size**: defines the minimum number of instances in the scaling group
  - **Initial number of instances**: defines the number of **automatically** created instances at the startup of the scaling group. The corresponding number of instances will be created upon the establishment of the scaling group.
  - **Maximum scaling group size**: defines the maximum number of instances in the scaling group
  - **Scaling configuration**: defines the scaling configuration. Machines will be created according to this configuration when performing scaling operations
  - **Supported network**: the network attribute of the scale-up machines, i.e., whether the scale-up machines are in the basic network or a VPC. Choose "Basic Network", unless your cluster has already been using VPC
  - **Supported availability zone**: defines in which availability zone the machine will be automatically created during scaling operations. You can select multiple availability zones. The scale-up machines will be automatically created randomly in the selected availability zones, allowing cross-availability zone disaster recovery
  - **Remove policy**: when removing instances from the scaling group and there are multiple choices, which CVMs shall be removed will be based on this policy. Usually, you can select "Remove Oldest Machine". Check the [Details](https://cloud.tencent.com/document/product/377/4166#13.-.E4.BC.B8.E7.BC.A9.E7.BB.84.E7.A7.BB.E5.87.BA.E7.AD.96.E7.95.A5.E7.9A.84.E5.85.B7.E4.BD.93.E8.A7.84.E5.88.99.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F) of the two policies.
  - **Load balancer**: specifies a load balancer. Created scale-up machines will be automatically mounted to this load balancer.

The scaling group is now created. Currently the scaling group can accommodate machines, but cannot perform intelligent capacity scaling. We strongly recommend you to proceed with the following 3 operations:
 - Add existing CVMs
 - Create scaling policy
 - Create notification


## 3. Modifying CVMs Bound to the Scaling Group
Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page of the scaling group.
![](https://mccdn.qcloud.com/static/img/bae3ec563534769d6c38143b60299d74/image.png)

Users may view the list of CVMs bound to the scaling group in this page.
- To manually add CVM instances to the scaling group, click **Add CVM**, select the instance to be added (hold Shift key to select multiple instances) and click **OK**;
- To unbind a certain CVM, click **Remove** behind the corresponding CVM entry.
![](https://mccdn.qcloud.com/static/img/ac4e495a20c3aa69836f3eefb6fdb609/image.png)

Automatically created machines will be terminated when removed.
Manually added machines will not be terminated upon removal. They will only be removed from the scaling group, and the load balancer will be unbound.

## 4. Defining the Availability Zone Where Scale-up Machine will be Automatically Created
Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mccdn.qcloud.com/static/img/bae3ec563534769d6c38143b60299d74/image.png)

Click "Edit" to increase or decrease availability zones.


## 5. Modifying Scaling Group
Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mccdn.qcloud.com/static/img/bae3ec563534769d6c38143b60299d74/image.png)

Click **Edit** to modify the scaling group name, adjust the minimum and maximum scaling group sizes, and modify CVM instance remove policy, etc.
![](https://mccdn.qcloud.com/static/img/19a6f7cc708a4288974a98d8a78263bd/image.png)

## 6. Deleting Scaling Group
Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

There is a **Delete** button behind each scaling group in the scaling group list. Note: you need to delete the instances in the scaling group before your can delete the scaling group itself.


## 7. Integrating Load Balancer and Scaling Group
When adding and deleting CVM instances in an AS, you need to ensure that the traffic of applications is allocated across all CVM instances. If you want the created scale-up machines to be under a certain load balancer and receive the traffic forwarded by the load balancer without your intervention, you can specify a load balancer for your machine. The load balancer will be the single point of contact for all incoming traffic towards the instances in your Auto Scaling group.

### Adding Load Balancer to Scaling Group

Integrate scaling group and CLB so that you can attach the CLB to the existing scaling group. Once the CLB is attached, it will automatically register the instances in the group and distribute inbound traffic to these instances.

In the AS [Console](https://console.cloud.tencent.com/autoscaling), click "New" and select the load balancer you need from the "Load Balance" option at the bottom of the page. If you did not create it in advance, click the "New" link below the option to create a new load balancer.

> Note:
> The load balancer instance associated with the scaling group must be in the same network environment (VPC or the basic network of the same region) as the scaling group.


### Removing Load Balancer from Scaling Group
Click to enter the detail page of the scaling group, and click "Modify" below the details to delete the corresponding LB.

Once the LB is deleted, the machines in the scaling group will also be automatically unbound from the deleted load balancer.
