## Overview of Creation
### Common Steps
You can start an instance with a public image or service marketplace image, and then connect to the instance and deploy your software environment. If the instance runs normally, you can create a new custom image based on this instance as needed, so that you can use this image to start more new instances that have the same custom items with the original one.

### Best Practice
 - **Shut down instance:**
Shut down the instance before you can create the custom image to ensure that the image has exactly the same the deployment environment as that of the current instance.
 - **Data migration:**
If you want to keep the data in the original instance data disk while starting a new instance, you can first take a [Snapshot](/doc/product/362/2455) of the data disk, and then create a new CBS disk with this data disk snapshot when the new instance is started. For more information, please see [Create Cloud Disk from Snapshot](/doc/product/362/2455#6.-.E4.BD.BF.E7.94.A8.E5.BF.AB.E7.85.A7.E5.88.9B.E5.BB.BA.E7.A3.81.E7.9B.98).

### Limit on Creation
 - Each region supports a maximum of 10 custom images.
 
## Creation Method
### Creating Image from Instance via Console

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. Select the instance to be shut down, and then click **Shut Down** on the top.
 3. Click "More" on the right side of the instance used to create image, and click **Create Image**.
 4. Enter **Image Name** and **Image Description** in the pop-up box, and click **OK** to submit the creation application.
 5. Move your mouse to "Recent Operations (clock icon)" on the upper right corner to view the progress of creation.
 6. After the image is created, click "Image" in the left navigation bar, or click on the image ID in "Recent Operations (clock icon)", and then you are redirected to the image list to view details.
 7. To purchase a server with the same image as the previous one, click **Create CVM** on the right side of the image in the image list.
![](//mc.qcloudimg.com/static/img/b44502e4494247574d23da9e09a20a19/image.png)

### Creating Image Using API
Users can use the API CreateImage to create a custom image. For more information, please see the [API for Creating Image](/doc/api/229/1273).

