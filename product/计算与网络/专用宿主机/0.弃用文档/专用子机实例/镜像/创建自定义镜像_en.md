The CVM instance described below also refers to dedicated CVM.

## Common Practices of Creating Images

You can start an instance with a public image or service marketplace image, and then connect to the instance and deploy your software environment. If the instance works normally, you can create new custom images based on it as needed. With these images, you can later start more new instances with same customization with the original instances.

It's highly recommended to shut down the instances before creating custom images, so that the images would be completely identical to the current deployed environment.
>Note: You can also create custom images when the instances are still running. However, the data on which the read and write operations are performed may not be saved.

To preserve the data on original instances' data disks when starting new instances, first create [Snapshots](https://cloud.tencent.com/doc/product/362/2455) of the data disks and create new CBS data disks with the snapshots when starting the new instances. For more information, please see [Create CBS from Snapshot](https://cloud.tencent.com/doc/product/362/2455#6.-.E4.BD.BF.E7.94.A8.E5.BF.AB.E7.85.A7.E5.88.9B.E5.BB.BA.E7.A3.81.E7.9B.98).

## Create Images from Instances in the Console

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Right click on the CVM instance from which you want to create an image, or click "Action" -> "More" -> "Create Image".

3) After an image is successfully created, the operation log at the upper right corner will display the completion status. You can use the ID of the created image to redirect to the image list.

## Create Images with API
Users can create custom images with the API CreateImage. For more information, please see the API [Create Image](https://cloud.tencent.com/doc/api/229/1273).

