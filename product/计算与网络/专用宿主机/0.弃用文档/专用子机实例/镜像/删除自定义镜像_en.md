The CVM instance described below also refers to dedicated CVM.

You can delete the customs images after use. You cannot [start new CVM instances](/doc/product/213/4855) with a deleted image. However, any existing instances won't be affected. If you need to delete all the instances purchased and launched from this image, please see the API [When a Prepaid Instance Expires](/doc/product/213/4931) or API [Terminate Postpaid Instances](/doc/product/213/4930).

> - You cannot delete an image if it has been [shared with other users](/doc/product/213/4944). You need to cancel sharing images with all users before deleting this image.
> - Users can only delete the custom images, rather than public and shared images.

## Deleting Custom Images in the Console

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com).

2) Click "CVM" -> "Image" in the navigation pane.

3) Click the "Custom Image" tab, and select the custom images you want to share from the list.

4) Click the "Delete" button and confirm the operation to delete all the selected custom images. If the operation fails, you will be prompted with the reason.

## Deleting Custom Images through API
Users can share images using the API DeleteImages. For more information, please see the API [Delete Images](https://cloud.tencent.com/doc/api/229/1274).
