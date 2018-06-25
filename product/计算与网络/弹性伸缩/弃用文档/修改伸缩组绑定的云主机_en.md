Open the [Console](https://console.cloud.tencent.com/autoscaling), and select **Scaling Group** in the navigation bar.

Select the scaling group to be modified, and click the scaling group ID to enter the basic information page.
![](http://mccdn.qcloud.com/static/img/bae3ec563534769d6c38143b60299d74/image.png)

Users may view the list of CVMs bound to the scaling group in this page.
- To manually add CVM instances to the scaling group, click **Add CVM**, select the instance to be added (hold Shift key to select multiple instances) and click **OK**;
- To unbind a certain CVM, click **Remove** behind the corresponding CVM entry.
![](//mccdn.qcloud.com/static/img/ac4e495a20c3aa69836f3eefb6fdb609/image.png)

Automatically created machines will be terminated when removed.
Manually added machines will not be terminated upon removal. They will only be removed from the scaling group, and the load balancer will be unbound.
