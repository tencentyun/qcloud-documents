
## General

You can launch an CVM using a public image or a service market image, and install and configure the software environment as needed. Then you can create an image to quickly launch more new instances with the same configurations. 

It's recommended to shut down the CVM before creating the image.

If you want to reserve the data on the original instance data disk when starting a new instance, then you can first take a snapshot of the data disk. When starting the new instance, you can use this disk snapshot to create a new CBS disk.

## Creating Images on Console

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Select the CVM instance from which you want to create an image, and click **Operation** -> **More** -> **Create Image**.

3) When the image is created successfully, the result is displayed near the operation log in the upper right corner. With the image ID, you can jump to the image list.

## Creating Images via API
You can use the [CreateImage](https://cloud.tencent.com/doc/api/229/1273) API to create custom images.