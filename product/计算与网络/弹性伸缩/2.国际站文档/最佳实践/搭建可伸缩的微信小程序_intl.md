## Deployment Architecture
We can create a WeChat Lite App with the following architecture. Auto Scaling is required for business server cluster and session server cluster.
![](https://mc.qcloudimg.com/static/img/e2de0c6b3a406e867c26d2310f2cf228/AS-Best+Practise-WeChat.png)

## Why Is the Auto Scaling Configuration Required?

Auto Scaling in the following two scenarios may reduce costs and improve business continuity:

1. Lite Apps visits with obvious peak and idle hours: According to the prediction, if more than 1 set of CVM for business server cluster and session server cluster with less than 8 peak hours are required, 30% of the cost shall be saved if the method of **fixed servers only for idle hours + temporary servers added for peak hours** is used. With AS's scheduled scaling capability, Tencent Cloud allows you to add temporary servers in peak hours and reclaim and terminate the surplus servers in idle hours.

2. Constant lite Apps visits: You can configure monitoring and alarm based scaling policy to deal with unexpected high load, maintain continuous service and earn time for troubleshooting. Abnormally high load includes CC attack and unexpected traffic (for example, superfast spreading speed of "MYOTee" upon its launch, or burst visits brought by a certain event).

> Note: Auto Scaling is free, but the scaled CVM will be charged by seconds.

## What Will Auto Scaling Do?

It will:
1. Increase or decrease CVMs on a scheduled basis;
2. Automatically increase or decrease CVMs based on the load of the cluster server;
3. Automatically register the additional CVMs into the cloud load balancer to achieve fully automatic scaling.


## Preconditions of Configuration
Your WeChat Lite App should support auto scaling.

## Configuring Auto Scaling Policy for Session Servers

### 1. Create Scaling Configuration

As **scaling configuration** is the template for CVMs creation when scaling, we specify the region, model, image through scaling configuration in advance.

1. Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click "Scaling Configuration" in the navigation bar.

2. Choose the project and region. Note that you must select the project and region of your WeChat Lite App.
![](https://mc.qcloudimg.com/static/img/9a39d87fa90f3ae5995073a6077b1057/1.jpg)

3. The following procedure is similar to purchasing CVMs. You can follow the guidelines to complete the creation of scaling configuration.
![](https://mc.qcloudimg.com/static/img/02220977468b12ef47c9aeb30a26b06d/2.jpg)

> Note:
> You need to create an image in advance, and ensure that the application of the image can be activated with the operating system. In such case, the scaled CVM can work directly without manual intervention.
![](https://mc.qcloudimg.com/static/img/087be62002126d98981743246c14f85f/cvm.jpg)

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

![](https://mc.qcloudimg.com/static/img/e82f2ce171a0cff61f075b0cd7bd17f0/23.jpg)
![](https://mc.qcloudimg.com/static/img/f3ab676105c79c61ce877b92e4e6ca7c/24.jpg)

Click **Done** to finish the creation.

### 3. Add Existing CVMs to the Scaling Group

1. In the [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling), click on the scaling group name to enter the management page, and click "Add CVM" at the bottom of the page.
![](https://mc.qcloudimg.com/static/img/3ff1beba2621d68ef939d7fd0df2de11/5.jpg)

2. Select the existing session server to add to the scaling group in the pop-up dialog box.
![](https://mc.qcloudimg.com/static/img/be11ceec587195b7cf39f9183a051769/6.jpg)

3. Set the added server as "Scale-down exemption", so as to protect it from being removed for scale-down by the scaling group.
![](https://mc.qcloudimg.com/static/img/2c19119e95beb4eb820757939578c656/7.jpg)

### 4. Set the Scaling Policy
You can select scheduled scaling, or dynamic scaling based on the alarm (usually scaling up and scaling down tasks are provided in pairs).

![](https://mc.qcloudimg.com/static/img/f348d96c002cdf79ac2033abcd7e6e4c/8.jpg)

**a. Scheduled scaling**:

For example, a WeChat Lite App that orders lunches is expected to see higher load during the lunch time. So you can add two extra servers during 11: 00-13: 00 for such load.

- First, set a scheduled scale-up task:
![](https://mc.qcloudimg.com/static/img/4cb5f7533c0f8645033298fe69e413c4/t1.jpg)

- Then set a scheduled scale-down task:
![](https://mc.qcloudimg.com/static/img/c8fdf2ca0a47b59863501c0a088af13c/t2.jpg)

**b. Scale-up based on the alarm**:

Predict the uncertain scale-up while keep watch on the unexpected traffic/attacks:

- First, set a scale-up policy based on the alarm which deals with abnormal traffic:
![](https://mc.qcloudimg.com/static/img/5ca400f8d1d9eb5af8e5542deccf39f6/t3.jpg)


- Then set a scale-down policy based on the alarm which removes surplus servers:
![](https://mc.qcloudimg.com/static/img/87b0a1b2cc236c3a586e5b03bec478ad/t4.jpg)

## Configuring the Auto Scaling Policy for Business Servers

This process is similar to that of configuring the session servers:

- Create a scaling configuration for the business server;
- Create a scaling group "business server cluster" for the business server, directed to the load balance of the business server;
- Configure the auto scaling policy for the business server.

## Verifying the Scalability and Viewing the Scaling Activities
Add 1 to the expected instance number of the scaling group and the group shall automatically scale up one server to the cluster. If the newly scale-up machine can handle requests normally, it indicates that the scaling group is working properly.
![](https://mc.qcloudimg.com/static/img/9f3d937afcad32a79febaea107d558db/12.jpg)

The scaling group also supports [View Scaling Activity History](https://cloud.tencent.com/document/product/377/3804), ensuring your complete grasp of the scaling activity.

Now, your WeChat Lite App is capable of intelligent capacity scaling. You no longer need to worry about the scale-up and scale-down. Just pay attention to the scaling group notification or check from time to time the history of scaling activities.
