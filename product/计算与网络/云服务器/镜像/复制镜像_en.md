The image synchronization feature enables users to quickly deploy the same CVM instances in different regions. Deploying the same CVM instance in different regions using image synchronization is a reliable way to improve application robustness.

## Synchronize images to different regions via console
1) Open [CVM Console](https://console.qcloud.com/cvm/).

2) Click "Image" in the navigation pane.

3) Check all images you want to synchronize, click the "Synchronize Image" button at the top.

4) Select the destination region to which you synchronize images, and click OK.

5) After successful synchronization, the image list status in the destination region is updated to 100%.

## Synchronize images to different regions via API
You can use the SyncCvmImage API to synchronize images. For details, refer to [SyncCvmImage API](https://www.qcloud.com/doc/api/229/1336).