In case of scale-up, AS needs to know beforehand what kind of configuration is required to produce CVMs, and you need to specify related resources in advance, such as image, data for data disk, instance configuration, key pair, security group, block storage device, etc.

Please note that scaling configuration is just a template based on which CVMs are produced during auto-scaling. **The creation of scaling configuration is free of charge since it will not lead to the production of CVM, please don't worry about the cost.**

Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Configuration** in the navigation bar.

### Step 1. Selecting a Region

In the menu on the top of the screen, select a region you need for the scaling group.

> Note:
> Please note that you need to select the region of the CVM to which the scaling group will be bind. Both scaling configuration and scaling group are region-sensitive. For example, if you select Guangzhou as the region for the scaling configuration, it can only be bound to the scaling group in Guangzhou, and all the automatically added CVMs belong to Guangzhou.

![](https://mc.qcloudimg.com/static/img/9a39d87fa90f3ae5995073a6077b1057/1.jpg)

### Step 2. Specifying Parameters

Click **Create**, and create scaling configuration as instructed using the same steps as those for purchasing CVM.

1. Enter **Configuration Name**, e.g. "Frontend Server Cluster Configuration A";

2. Select model, for example, 1 core 1 G (1-core CPU, 1 G memory);

3. Select an image. You can select a clean "public image", or a "custom image" on which the service has been deployed.
To make CVM become available directly after its creation, it is strongly recommended to deploy the business application into the custom image.** At the same time, the business application inside the image needs to be set to be started upon the boot-up of operating system**. Only by this way can the CVMs scaled up by AS be automated.

4. Select sizes of system and data disks.
If you want the data disk to come with data after the CVMs are activated, you can specify a data disk snapshot so that the CVMs produced will come with the data in the snapshot.
> Note:
> - Generally, the CVMs in the scaling group are stateless. You're recommended to place the data native to CVMs into the custom image. If the system disk has not enough space, you can submit a ticket for a larger one.
> - If you want to store the data in the data disk, you need to set auto mount for the data disk to eliminate the need of manual intervention.

5. Select the bandwidth by following the procedure similar to that for purchasing CVM.

6. Set user name, password and security group.

7. Click **Finish**.

8. Create a scaling group based on this scaling configuration. Scaling configuration determines what kind of CVM is created, and scaling group determines when to perform scale-up.
