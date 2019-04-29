After using the custom image, you can delete it. When you delete a custom image, you will not be able to use this image to [start a new CVM instance](/doc/product/213/4855), but any instances that are already started will not affected. If you want to remove all instances that were purchased and started from this image, you can refer to [Expiration of Prepaid Instances](/doc/product/213/4931) or [Terminate Postpaid Instances](/doc/product/213/4930).

> - If you have already shared a custom image to others ([see here](/doc/product/213/4944)), you cannot delete it. You need to cancel all of its sharing before deleting a custom image.
> - You can only delete the custom image, but neither the common image nor the shared image.

## Deleting custom images on Console

1) Open [Tencent Cloud Console](https://console.cloud.tencent.com).

2) Click **CVM – Image** in the navigation pane.

3) Click the "Custom Images" tab, and select the custom image you want to share in the list.

4) Click the "Delete" button and confirm the operation, to delete all selected custom images. In case of failed deletion, the reasons will be prompted above the image. 

## Deleting custom images via API
You can use the [DeleteImages API](https://cloud.tencent.com/doc/api/229/1274) to delete images. For details, refer to 