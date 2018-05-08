
## Deployment Architecture
We can create a WeChat Lite App with the following architecture. Auto Scaling is required for business server cluster and session server cluster.
![](https://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/solution/css/img/wx/fw-pic.png)

## Why Is the Auto Scaling Configuration Required?

Auto Scaling in the following two scenarios may reduce costs and improve business continuity:

1. Lite Apps visits with obvious peak and idle hours: According to the prediction, if more than 1 set of CVM for business server cluster and session server cluster with less than 8 peak hours are required, 30% of the cost shall be saved if the method of **fixed servers only for idle hours + temporary servers added for peak hours** is used. With AS's scheduled scaling capability, Tencent Cloud allows you to add temporary servers in peak hours and reclaim and terminate the surplus servers in idle hours.

2. Constant lite Apps visits: You can configure monitoring and alarm based scaling policy to deal with unexpected high load, maintain continuous service and earn time for troubleshooting. Abnormally high load includes [CC attack](http://baike.baidu.com/link?url=aSNcL5Q_xzDxPvFYRU3qbS11NIQXD5vwvI5yxtJTVlL0xhjAaLntwmDHVW8buUlH4bbNJqMzCPp8b1N2LX-OnwAUR3MnE9GhH-F7fomUac3) and unexpected traffic (for example, superfast spreading speed of "MYOTee" upon its launch, or burst visits brought by a certain event). Refer to the cases at the public welfare website [baobeihuijia](https://cloud.tencent.com/community/article/651089001483090830).

> Note: Auto Scaling is free, but the scaled CVM will be charged by seconds.

## What Will Auto Scaling Do?

It will:
1. Increase or decrease CVMs on a scheduled basis;
2. Automatically increase or decrease CVMs based on the load of the cluster server;
3. Automatically register the additional CVMs into the cloud load balancer to achieve fully automatic scaling.


## Preconditions of Configuration
Your WeChat Lite App should support auto scaling. To enable auto scaling for your WeChat Lite App, refer to [Detailed Steps](https://console.cloud.tencent.com/la/guide).

## Configuring Auto Scaling Policy for Session Servers

### 1. Create Scaling Configuration

As **scaling configuration** is the template for CVMs creation when scaling, we specify the region, model, image through scaling configuration in advance.

1. Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click "Scaling Configuration" in the navigation bar.

2. Choose the project and region. Note that you must select the project and region of your WeChat Lite App.
![](https://mc.qcloudimg.com/static/img/653ebf516d940a90fd79728e5d319cdc/image.png)

3. The following procedure is similar to purchasing CVMs. You can follow the guidelines to complete the creation of scaling configuration.
![](https://mc.qcloudimg.com/static/img/4cecf25e8ad9caa67271159c67d0b770/image.png)

> Note:
> You need to create an image in advance, and ensure that the application of the image can be activated with the operating system. In such case, the scaled CVM can work directly without manual intervention.
![](https://camo.githubusercontent.com/c58d92b133f44b3d70a0936cf4d6f087e7e0d3ee/68747470733a2f2f6d632e71636c6f7564696d672e636f6d2f7374617469632f696d672f33663363343433316137353637656261323565383633356537383865353962612f392e706e67)

### 2. Create a Scaling Group

In the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling), click "New" and fill in the cluster management information as follows:

- **Name**: Fill in an appropriate name, such as "Session Server Cluster".
- **Minimum group size**: Lower limit of the number of cluster servers, such as "0".
- **Initial number of instances**: Number of CVMs automatically created upon the creation of the scaling group, such as "0".
- **Maximum group size**: Upper limit of the number of cluster servers. Fill as needed.
- **Scaling Configuration**: Select the scaling configuration you have just created.
- **Supported network**: The network environment of the session server. Select "Basic Network" generally.
- **Supported availability zone**: Select an availability zone for the CVM to be scaled. Check the availability zone of the session server.
- **Removal policy**: Select the default.
- **Cloud load balancer**: Select the cloud load balancer of the session server.

![](https://mc.qcloudimg.com/static/img/f665314e51db863d3f57cd75534f69f6/932.jpg)

Click **OK** to finish the creation.

### 3. Add Existing CVMs to the Scaling Group

1. In the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling), click on the scaling group name to enter the management page, and click "Add CVM" at the bottom of the page.
![](https://mc.qcloudimg.com/static/img/8ed547b6d545cff5b6e22cd71a75402c/08.jpg)

2. Select the existing session server to add to the scaling group in the pop-up dialog box.
![](https://mc.qcloudimg.com/static/img/5c91d826a3aab5bbb478a1c0524302e8/08113043.jpg)

3. Set the added server as "Scale-down exemption", so as to protect it from being removed for scale-down by the scaling group.
![](https://mc.qcloudimg.com/static/img/62319473a1a05e98d51c64c22ca24424/0308113553.jpg)

### 4. Set the Scaling Policy
You can select scheduled scaling, or dynamic scaling based on the alarm (usually scaling up and scaling down tasks are provided in pairs).

![](https://mc.qcloudimg.com/static/img/41763806c8d05ae89128b5a87e772974/08121006.jpg)

**a. Scheduled scaling**:

For example, a WeChat Lite App that orders lunches is expected to see higher load during the lunch time. So you can add two extra servers during 11: 00-13: 00 for such load.

- First, set a scheduled scale-up task:
![](https://mc.qcloudimg.com/static/img/d276c8d6924b4126a1532ddcefae8f0c/0170308120453.jpg)

- Then set a scheduled scale-down task:
![](https://mc.qcloudimg.com/static/img/ae7b0f21529d9f483a455e6148594926/20170308120822.jpg)

**b. Scale-up based on the alarm**:

Predict the uncertain scale-up while keep watch on the unexpected traffic/attacks:

- First, set a scale-up policy based on the alarm which deals with abnormal traffic:
![](https://mc.qcloudimg.com/static/img/d23dde14b8e12241d3315286682c2d8d/455.jpg)

- Then set a scale-down policy based on the alarm which removes surplus servers:
![](https://mc.qcloudimg.com/static/img/92b7fccdfb2b863e4798574e0cb06bde/22630.jpg)


## Configuring the Auto Scaling Policy for Business Servers

This process is similar to that of configuring the session servers:

- Create a scaling configuration for the business server;
- Create a scaling group "business server cluster" for the business server, directed to the load balance of the business server;
- Configure the auto scaling policy for the business server.

## Verifying the Scalability and Viewing the Scaling Activities
Add 1 to the expected instance number of the scaling group and the group shall automatically scale up one server to the cluster. If the newly scale-up machine can handle requests normally, it indicates that the scaling group is working properly.
![](https://mc.qcloudimg.com/static/img/665e029c6abfa6a7ef3f9063c88df486/05.jpg)

The scaling group also supports [View Scaling Activity History](https://cloud.tencent.com/document/product/377/3804), ensuring your complete grasp of the scaling activity.

Now, your WeChat Lite App is capable of intelligent capacity scaling. You no longer need to worry about the scale-up and scale-down. Just pay attention to the scaling group notification or check from time to time the history of scaling activities.

