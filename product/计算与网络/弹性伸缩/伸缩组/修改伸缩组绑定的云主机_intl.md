Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](https://mc.qcloudimg.com/static/img/06a1ca079f41a7cd825b47c68304f6f5/1.jpg)

Users may view the list of CVMs bound to the scaling group in this page.
- To manually add CVM instances to the scaling group, click **Add CVM**, select the instance to be added (hold Shift key to select multiple instances) and click **OK**;
- To unbind a certain CVM, click **Remove** behind the corresponding CVM entry.
![](https://mc.qcloudimg.com/static/img/32296300304a228286b919c41ab30613/2.jpg)

Automatically created machines will be terminated when removed.
Manually added machines will not be terminated upon removal. They will only be removed from the scaling group, and the load balancer will be unbound.


