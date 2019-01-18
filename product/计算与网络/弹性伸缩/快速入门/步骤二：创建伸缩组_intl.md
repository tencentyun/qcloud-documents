A scaling group is a collection of CVM instances following the same rules and serving the same scenario.

## Create a Scaling Group
Enter the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Group** in the navigation bar. Click ![](https://mc.qcloudimg.com/static/img/60fa242cdf5488626d6968f2c174222c/12.jpg), and fill in the basic information on scaling group in the pop-up page. Items with ![](//mccdn.qcloud.com/static/img/f9df27a1d1e0d42a7ff08dd884bfa34c/image.png) are required.

- The current number of CVM instances in the scaling group will be kept between the minimum and the maximum scaling group sizes.
- The initial number of instances defines the number of CVM instances in the scaling group when created;
	- If the current number of CVM instances is less than the minimum scaling group size, the Auto Scaling service will automatically add instances to make it equal to the minimum scaling group size;
	- If the current number of CVM instances is greater than the maximum scaling group size, the Auto Scaling service will automatically decrease instances to make it equal to the maximum scaling group size;
- You can select the existing scaling configuration, or create a scaling configuration.
- Select a network, availability zone and Removal policy.
- **(Optional) You can choose to associate with an existing cloud load balance policy or create a load balancer.**

![](https://mc.qcloudimg.com/static/img/e82f2ce171a0cff61f075b0cd7bd17f0/23.jpg)
![](https://mc.qcloudimg.com/static/img/f3ab676105c79c61ce877b92e4e6ca7c/24.jpg)

After configuration, this entry will be displayed in the scaling group list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/7c9974b283c4299d37e482b5a745979a/25.jpg)

## Add a CVM (Optional)
Now, let's bind a CVM.

Add the CVM instance to be bound in the CVM list. After configuration, this entry will be displayed in the scaling configuration list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/6e12d2e111f550ced48277017dbc131a/26.jpg)
> Note: If you cannot add or remove a CVM, please check the maximum and minimum scaling group sizes you set.

