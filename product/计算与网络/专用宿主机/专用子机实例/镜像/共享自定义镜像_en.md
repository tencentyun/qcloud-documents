The CVM instance described below also refers to dedicated CVM.

Image sharing feature allows users to share their created custom images with other users. Users can obtain shared images from other users conveniently, get desired components and add custom contents on them.

Please note that Tencent Cloud can't guarantee that the images shared by other users are intact or secure. It's recommended to use only the shared images from reliable sources.

## Sharing Images
### Sharing Images in the Console

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com).

2) Click "CVM" -> "Image" in the navigation pane.

3) Click the "Custom Image" tab, and select the custom images you want to share from the list.

4) Click the "Share" button, enter the Tencent Cloud account with whom you want to share the images, and click "OK".

5) Notify the user in the previous step to log in to [Tencent Cloud Console](https://console.cloud.tencent.com). The shared images could be found in "CVM" -> "Image" -> "Shared Image".

6) To share an image with multiple users, repeat the above steps until all users get the shared image.

### Sharing Images through API
Users can share images using the API ShareImage. For more information, please see the API [Share Images](https://cloud.tencent.com/doc/api/229/2361).

## Using Shared Images
Shared images can only be used to launch CVM instances. For more information, please see the API [Purchase and Start Instances](/doc/product/213/4855).
