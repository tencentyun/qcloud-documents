The CVM instance described below also refers to dedicated CVM.

Image replication feature allows users to quickly deploy identical CVM instances across regions. Deploying identical CVM instances under different regions through cross-region image replication is a reliable method to improve your applications' robustness.

## Copying Images Across Regions in the Console
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Image" in the navigation pane.

3) Check all the images you want to copy, and click "Copy Image" button at the top.

4) In the pop-up box, select the region to which you want to copy the images, and click "OK".

5) After the images are successfully copied, the status of the image list of the destination region will be updated to 100%.

## Copying Images Across Regions through API
Users can copy images using the API SyncCvmImage. For more information, please see the API [Copy Images](https://cloud.tencent.com/doc/api/229/1336).
