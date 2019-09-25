In the global settings page of Tencent Cloud VOD console, you can configure the transcoding format type of the video file, set the domain name, mange the video categories, and perform the callback configuration etc.
## Transcoding Setting
With the transcoding settings, you can configure the default transcoding formats and resolutions for all the videos you have uploaded. You can set the transcoding bitrate for output here. The history files that have been transcoded will not be transcoded again. If needed, you can select individual videos for transcoding in the **Video Management** page. When transcoding is enabled, click the desired bitrate format. It takes about 5 minutes for the change to take effect.
Log in to Tencent Cloud [VOD Console](https://console.cloud.tencent.com/vod), click "Global Settings" -> "Transcoding Settings" -> "Edit", select the transcoding format type, and click "OK".
![](https://mc.qcloudimg.com/static/img/09f2bcad15557a2f9d35b5f745d7f66b/image.png)
>Among the transcoding formats, mp4 SD is the default format, which cannot be disabled. You are recommended to select HLS format preferably for a better platform compatibility and experience, and to choose other formats based on actual needs. Transcoding to other mp4 files or Ultra HD resolutions may significantly increase the time taken for transcoding.

## Domain Name Settings
You can go to "Global Settings" -> "Domain Name Settings" to add or manage the domain name for video playback.
![](https://mc.qcloudimg.com/static/img/e9bedf2ce72d12d827d47a3b201ecd80/image.png)
### Adding Domain
Click "Add Domain Name", enter the domain name information in the pop-up box, and click "OK" after confirmation. It takes a few minutes to deploy the added domain name, please wait. After the deployment is completed, you can disable or delete the domain name, download the certificate, and configure the hotlink protection.
>Only licensed domain names can be added. For more information on domain name licensing, please see [Licensing Process Diagram](https://cloud.tencent.com/document/product/243/655).

![](https://mc.qcloudimg.com/static/img/f80011e5f8f67b09d593f37ee6088734/image.png)

### Hotlink Protection
You can go to "Global Settings" -> "Domain Name Settings", click "Hotlink Protection Configuration" on the right side of the corresponding domain name to go to its details page, and then click "Edit" to enable the hotlink protection feature. Because the original URL will become unavailable after the hotlink protection is enabled, be sure to read Tencent Cloud [URL Hotlink Protection](http://video.qcloud.com/download/docs/QVOD_HotLink_Protection_User_Guide.pdf?_ga=1.9461937.586497180.1511491691) carefully and perform a test.
![](https://mc.qcloudimg.com/static/img/c8b886e335846fef8efd646653b86c10/image.png)

## Category Management
You can go to "Global Settings" -> "Category Management" to manage file categories, including category creation, deletion, and renaming. In the meanwhile, Category Management allows you to view, modify, delete, and associate files via APIs.
![](https://mc.qcloudimg.com/static/img/6c3675e5426e3d5261e906ddbbc8b7ec/image.png)
After categories are created, you can also mange the file categories in the file information management page and the video management page.
-  **Add First Level Category: **Click "Add Category", and a first level category will be added with the default name "New First Level Category". If you need to modify the category name, select the category to be renamed, and click the Edit icon in front of the Number of Files column, and then input the new name, and click "OK".
-  **Add Sub-category: **Click "Add Sub-category" on the right side of the category list to add sub-categories under the corresponding category. The current system supports the 4-level category structure, so the fourth level category cannot have sub-categories added. If you need to modify the category name, select the category to be renamed, and click the Edit icon in front of the Number of Files column, and then input the new name, and click "OK".
-  **Delete Category: **You can click "Delete" on the right side of the corresponding category to delete it. After a category is deleted, the corresponding files will be grouped into the **Other** category.


## Callback Configuration
Go to "Global Settings" -> "Callback Configuration" page, set **Callback URL** to be the address used for the APP backend to receive the callback, select "Normal Callback" in the **Callback Model**, and select the desired event callback type. For more information, please see [Task Management and Event Notification](https://cloud.tencent.com/document/product/266/7829).
![](https://mc.qcloudimg.com/static/img/5ae3c74660be7c531f61bd3e849a4c1b/image.png)



