## Overview of Creation
### Common steps
You can launch an instance with a public image or a service marketplace image, and then connect to the instance and deploy your software environment. If the instance runs normally, you can create a new custom image based on this instance as needed, so that you can use this image to launch more new instances that have the same custom configurations with the original one.

### Best practice
 - **Shut down instance:**
Shut down the instance before you can create a custom image to ensure that the image has exactly the same deployment environment as that of the current instance.
 - **Data migration:**
To keep the data in the original instance data disk when you lunch a new instance, you can first take a [Snapshot](/doc/product/362/2455) of the data disk, and then create a new CBS data disk with this snapshot when launching the new instance. For more information, please see [Create Cloud Disk from Snapshot](/doc/product/362/2455#6.-.E4.BD.BF.E7.94.A8.E5.BF.AB.E7.85.A7.E5.88.9B.E5.BB.BA.E7.A3.81.E7.9B.98).

### Limit
 - Each region supports a maximum of 10 custom images.

### Notes
1. The following directory and files will be removed.
- /var/log/  
- /root/.bash_history, /home/ubuntu/.bash_history (Ubuntu system)

2. /etc/fstab will reset to avoid launch failure due to no data disk found.
 
## Creation Method
### Create an image from an instance via the console

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. Shut down the instance. Select the instance to be shut down, and then click **Shutdown** on the top.
 3. Click **More** on the right side of the instance used to create an image, and click **Create Image**.
 4. Enter **Image Name** and **Image Description** in the pop-up box, and click **OK** to submit the creation application.
 5. Move your mouse to **Recent Operations (clock icon)** on the upper right corner to view the progress of creation.
 6. After the image is created, click **Image** in the left navigation bar, or click on the image ID in **Recent Operations (clock icon)**, and then you are redirected to the image list to view details.
 7. To purchase a server with the same image as the previous one, click **Create CVM** on the right side of the image in the image list.
![](//mc.qcloudimg.com/static/img/b44502e4494247574d23da9e09a20a19/image.png)

### Create an image using API
You can use the API CreateImage to create a custom image. For more information, please see the API [Create Image](/doc/api/229/1273).

