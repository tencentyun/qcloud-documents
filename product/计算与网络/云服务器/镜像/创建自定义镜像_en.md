You can create a new custom image as needed after you have started an instance, and use it to start more new instances which have the same custom items as the existing instance.

## General idea to create images

You can first start an instance using a common image or a service market image, and connect to your instance to install and configure the software environment. You can create a custom image when the instance is the ***running*** status, but you may not save some data that is being read and written. It is, therefore, recommended that you first shut down the instance first to ensure that all contents on the instance are consistent during image creation.

If you want to reserve the data on the original instance data disk when starting a new instance, then you can first take a [snapshot](https://www.qcloud.com/doc/product/362/2455) of the data disk . When starting the new instance, you can use this disk snapshot to create a new CBS disk. For more information, see [Create Cloud Disks with Snapshots](https://www.qcloud.com/doc/product/362/2455#6.-.E4.BD.BF.E7.94.A8.E5.BF.AB.E7.85.A7.E5.88.9B.E5.BB.BA.E7.A3.81.E7.9B.98).

## Use console to create images from instances

1) Open [CVM Console](https://console.qcloud.com/cvm/).

2) Right-click the CVM instance from which you want to create an image, or click "Operation" -> "More", and then click "Create Image".

3) When the image is created successfully, the result is displayed near the operation log in the upper right corner. With the image ID, you can jump to the image list.

## Use API to create images
You can use the CreateImage API to create custom images. For details, see [API for Creating Image](https://www.qcloud.com/doc/api/229/1273).