Open the [Console](https://console.cloud.tencent.com/autoscaling/config), and select **Scaling Group** in the navigation bar.

### a. Select a Region

Select the region above the console where the scaling group shall be established. The CVMs which can be added manually and the cloud load balancers which can be bound are restricted by your selected region. For example, if you select Guangzhou as the region of the scaling configuration, the CVM of Guangzhou is automatically added to the scaling group. In a scaling group of Guangzhou region, you cannot add CVMs in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc) manually, nor bind load balancers in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.)

![](https://mc.qcloudimg.com/static/img/9a39d87fa90f3ae5995073a6077b1057/1.jpg)

### b. Define Information
Click the "New" button and define attributes of the scaling group:

  - **Name of Scaling Group**: labels the scaling group. For example, "Website Logical Layer"
  - **Minimum scaling group size**: defines the minimum number of instances in the scaling group
  - **Initial number of instances**: defines the number of **automatically** created instances at the startup of the scaling group. The corresponding number of instances will be created upon the establishment of the scaling group.
  - **Maximum scaling group size**: defines the maximum number of instances in the scaling group
  - **Scaling configuration**: defines the scaling configuration. Machines will be created according to this configuration when performing scaling operations
  - **Supported network**: the network attribute of the scale-up machines, i.e., whether the scale-up machines are in the basic network or a VPC. Choose "Basic Network", unless your cluster has already been using VPC
  - **Supported availability zone**: defines in which availability zone the machine will be automatically created during scaling operations. You can select multiple availability zones. The scale-up machines will be automatically created randomly in the selected availability zones, allowing cross-availability zone disaster recovery
  - **Remove policy**: when removing instances from the scaling group and there are multiple choices, which CVMs shall be removed will be based on this policy. Usually, you can select "Remove Oldest Machine". Check the [Details](https://www.cloud.tencent.com/document/product/377/4166#13.-.E4.BC.B8.E7.BC.A9.E7.BB.84.E7.A7.BB.E5.87.BA.E7.AD.96.E7.95.A5.E7.9A.84.E5.85.B7.E4.BD.93.E8.A7.84.E5.88.99.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F) of the two policies.
  - **Load balancer**: specifies a load balancer. Created scale-up machines will be automatically mounted to this load balancer.

The scaling group is now created. Currently the scaling group can accommodate machines, but cannot perform intelligent capacity scaling. We strongly recommend you to proceed with the following 3 operations:
 - Add existing CVMs
 - Create scaling policy
 - Create notification
