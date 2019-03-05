The scaling configuration defines the configuration information of CVM instances used for auto scaling, including the image, storage, network, security group, login method of the CVM.
> Note: The creation of a scaling configuration is free of charge.

Log in to [Auto Scaling Console](https://console.cloud.tencent.com/autoscaling/config), and click **Scaling Configuration** in the navigation bar.

## Select a Region
![](https://mc.qcloudimg.com/static/img/653ebf516d940a90fd79728e5d319cdc/image.png)
Please note that you must select the region where the CVM to which the scaling group needs to bind locates.

The CVMs which can be added manually and the cloud load balancers which can be bound are restricted by your selected region. For example, if you select Guangzhou as the region of the scaling configuration, the CVM of Guangzhou is automatically added to the scaling group. In a scaling group of Guangzhou region, you cannot add CVMs in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.) manually, nor bind load balancers in other regions (Shanghai, Beijing, Hong Kong, Toronto, etc.)

## Select a Model
Click ![](//mccdn.qcloud.com/static/img/9d38f7bfbe02a922370765f3adfa58bf/image.png), and fill in the basic scaling configuration information in the pop-up page.

![](https://mc.qcloudimg.com/static/img/4cecf25e8ad9caa67271159c67d0b770/image.png)


## Select an Image
![](https://mc.qcloudimg.com/static/img/c9a614fedaccf6a5ab2c1a16634989cc/image.png)
Public images and custom images are available.

If you select a public image, it should be consistent with the operating system of the CVM to which the scaling group is going to bind. If you select a custom image, you need to create the custom image through the CVM's image creation feature.

The difference is that, if you select a public image, the scaled CVM instance is not activated and cannot be used directly, and you need to manually deploy the application environment; if you select a custom image, by creating an image for the CVM instance of which the environment has been deployed, and using the image as the operating system when batch creating CVM instances, the CVM instances will have the same software environment as the original CVM instance after created successfully, and thus the batch deployment of software environments is achieved.

Therefore, it is recommended to select a custom image here. Bind the image of the "CVM to which the scaling group is going to bind".

> Note: [How to create the image for the "CVM to which the scaling group is going to bind"?](https://cloud.tencent.com/doc/product/213/4942)

## Select a Storage and a Network
![](https://mc.qcloudimg.com/static/img/8e9c2fc896959e14364a2e17ce277e28/image.png)
Set the disk and network in the **Select Storage and Network** page.

Please note that if you select the cloud disk as the system disk, then you can select the data disk snapshot for the data disk.

For users with large amount of data, they often use data disks to store data. When a data disk creates a snapshot file, users can use it to quickly clone multiple disks, achieving a fast server deployment.

When the auto scaling automatically adds a new CVM instance, if the data disk snapshot is specified in scaling configuration, Tencent Cloud's cloud disk can allow the automatic mounting of the data disk containing the set data after the CVM instance is activated, so as to meet the needs of automatic data copy.

If the data disk snapshot is specified in the scaling configuration, you need to ensure that the data disk can be mounted automatically and correctly for the successful automatic scale-up of the scaling group. You need to perform some operations on the original instance of the data disk snapshot before setting the auto scaling, so as to realize the automatic mounting of data disk when activating a new CVM instance. For instructions on how to do this, refer to [How to Mount Data Disk Automatically When Activating New Instance Using Custom Image and Data Disk Snapshot](https://cloud.tencent.com/doc/product/362/5564)
> Note:
-  Auto Scaling service is free of charge, and newly added servers, hard disks and networks will be charged by the traffic of CVM instances, hard disks and networks. This page will display prices based on your settings.

## Set Information
Select the login method and security group in the **Set Information** page.
![](https://mc.qcloudimg.com/static/img/bd8a3a728126fc866ccf0c17d15a5d27/image.png)

> Note: The CVM instances added via the Auto Scaling service use Cloud Security and Cloud Monitor services for free by default.

After configuration, this entry will be displayed in the scaling configuration list, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/67ba31fd6c1f12485bb8f96220aaf6af/image.png)
