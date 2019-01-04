## How to Use Image Registry Trigger
You can use a registry trigger by following the three steps below:
1. Select a specific image registry to create a trigger, and configure the trigger expression and service update parameters.
2. Push an image to the image registry via Tencent Cloud CI or docker, and confirm whether the submitted image meets the condition of the trigger expression.
3. View the trigger log to check whether the triggered action is performed successfully.

## Creating Image Registry Trigger
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list. On "My Image Registries" page, click the **name** of an image (e.g. "test" in the figure).
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. Click "Trigger" -> "Add Trigger".
![](//mc.qcloudimg.com/static/img/c63426ed0398fc08aa28e81ddf7be8aa/image.png)
4. Configure the attributes of trigger.
 - **Trigger Name**: The name of the created trigger. It starts with a letter with a length limited to 2-64 characters.
 - **Trigger Condition**: There are three types of trigger conditions.
 i: **All**: Action is triggered when a Tag (image version) is created or updated in image registry.
 ii: **Specified Tag**: Action is triggered when a specified Tag is created or updated in image registry.
 iii: **Regular Expression**: Action is triggered when a matching Tag is created or updated in image registry.
 - **Trigger Action**: Update images of a container.
 - **Select Service/Image**: Click "Please select a container image", and then select attributes in the drop-down list, including "Region", "Cluster", "Namespace", "Service", and "Container Image".
![](//mc.qcloudimg.com/static/img/6e2200e24d13e873354bb38ade55e14d/image.png)
5. Click "Save"  to complete the creation of a trigger.

## Modifying Image Registry Trigger
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list. On "My Image Registries" page, click the **name** of an image (e.g. "test" in the figure).
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. Click "Trigger" to go to the trigger list page, and click the modification icon on the right side of the trigger display bar.
![](//mc.qcloudimg.com/static/img/77b87f6ba86db13caa0bc6d9fb623499/image.png)

## Deleting Image Registry Trigger
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list. On "My Image Registries" page, click the **name** of an image (e.g. "test" in the figure).
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. Click "Trigger" to go to the trigger list page, and click the deletion icon on the right side of the trigger display bar.
![](//mc.qcloudimg.com/static/img/a453712626e6cf47f591e5142010f842/image.png)

## Viewing Trigger Log
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list. On "My Image Registries" page, click the **name** of an image (e.g. "test" in the figure).
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. Click "Trigger" to go to the trigger list page, and you can view the trigger logs.
![](//mc.qcloudimg.com/static/img/f5751a02e2a899d97b2d46c2866e218e/image.png)

