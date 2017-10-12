A scaling group is a collection of CVM instances following the same rules and serving the same scenario.

## Create a Scaling Group
Enter the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Group** in the navigation bar. Click ![](//mccdn.qcloud.com/static/img/9d38f7bfbe02a922370765f3adfa58bf/image.png), and fill in the basic information on scaling group in the pop-up page. Items with ![](//mccdn.qcloud.com/static/img/f9df27a1d1e0d42a7ff08dd884bfa34c/image.png) are required.

- The current number of CVM instances in the scaling group will be kept between the minimum and the maximum scaling group sizes.
- The initial number of instances defines the number of CVM instances in the scaling group when created;
	- If the current number of CVM instances is less than the minimum scaling group size, the Auto Scaling service will automatically add instances to make it equal to the minimum scaling group size;
	- If the current number of CVM instances is greater than the maximum scaling group size, the Auto Scaling service will automatically decrease instances to make it equal to the maximum scaling group size;
- You can select the existing scaling configuration, or create a scaling configuration.
- Select a network, availability zone and Removal policy.
- **(Optional) You can choose to associate with an existing cloud load balance policy or create a load balancer.**

![](https://mc.qcloudimg.com/static/img/2fb365611291fb8917637dba46f398f4/image.png)

After configuration, this entry will be displayed in the scaling group list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/c1c64cdb16c11aaa6d31bc4781db62c4/image.png)

## Add a CVM (Optional)
Now, let's bind a CVM.

Add the CVM instance to be bound in the CVM list. After configuration, this entry will be displayed in the scaling configuration list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/e3232872ad5fe19e89c9eb7306418a3d/image.png)
> Note: If you cannot add or remove a CVM, please check the maximum and minimum scaling group sizes you set.


