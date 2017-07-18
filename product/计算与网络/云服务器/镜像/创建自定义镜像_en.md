
## General

You can launch an CVM using a public image or a service market image, and install and configure the software environment as needed. Then you can create an image to quickly launch more new instances with the same configurations. 

It's recommended to shut down the CVM before creating the image. 
>Note: you can creating custom image while the instance is runing, but data reading/writing during the creation may not be saved properly. 

If you want to reserve the data on the original instance data disk when starting a new instance, then you can first take a [snapshot](https://www.qcloud.com/doc/product/362/2455) of the data disk. When starting the new instance, you can use this disk snapshot to create a new CBS disk. For more information, see [Create Cloud Disks with Snapshots](https://www.qcloud.com/doc/product/362/2455#6.-.E4.BD.BF.E7.94.A8.E5.BF.AB.E7.85.A7.E5.88.9B.E5.BB.BA.E7.A3.81.E7.9B.98).

## Creating Images on Console

1) Log in to [CVM Console](https://console.qcloud.com/cvm/).

2) Select the CVM instance from which you want to create an image, and click **Operation** -> **More** -> **Create Image**.

3) When the image is created successfully, the result is displayed near the operation log in the upper right corner. With the image ID, you can jump to the image list.

## Creating Images via API
You can use the [CreateImage](https://www.qcloud.com/doc/api/229/1273) API to create custom images.