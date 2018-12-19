## Creating a Task Template

For more information on the task template, please see "Task Template" in the [Glossary](https://cloud.tencent.com/document/product/599/10396). You can create a task template in the [BatchCompute Console](https://console.cloud.tencent.com/batch/task). The steps are as follows:
1. Log in to the [BatchCompute Console](https://console.cloud.tencent.com/batch/task). If you have not activated the BatchCompute service, activate it according to the prompts on the BatchCompute Console page.

2. Click the **Task Template** option in the left navigation bar, select the target region, and then click the **New** button.
![](https://mc.qcloudimg.com/static/img/b6d89f6a4b4e0c8cc0469606948b8e41/image.jpg)

3. Configure the basic information.
   - Resource configuration: Click the **CVM Configuration** option to complete the configuration. For more information on the configuration, please see [CVM product documentation](https://cloud.tencent.com/document/product/213).
   - Number of resources: The number of resources that determines the tasks executed in parallel. For more information, please see "Task Instance" in the [Glossary](https://cloud.tencent.com/document/product/599/10396).
   - Image: For more information, please see "Image" in the [Glossary](https://cloud.tencent.com/document/product/599/10396).
   ![](https://mc.qcloudimg.com/static/img/2e4c9a7879539ae70b907f669e4a8b78/image.jpg)

4. Configure the program configuration information.
   - Execution method: When **Package** is selected, **Package Address** is required. **Package Address** is saved in the [Cloud Object Storage](https://cloud.tencent.com/document/product/436).
   - Package address/Stdout log/Stderr log should be in the fixed format. For more information, please see [How to Enter COS and CFS Paths](https://cloud.tencent.com/document/product/599/13996).
![](https://mc.qcloudimg.com/static/img/ed418b2351814d567c0beceb3183ec9d/image.jpg)

5. Configure storage mapping.
   - Input path mapping: [COS](https://cloud.tencent.com/document/product/436) and [CFS](https://cloud.tencent.com/document/product/582) are supported on LINUX, and only [CFS](https://cloud.tencent.com/document/product/582) is supported on Windows. For more information on the requirements of COS and CFS formats, please see [How to enter COS and CFS Paths](https://cloud.tencent.com/document/product/599/13996). Note that the formats of local paths on different operating systems may vary.
   - Output path mapping: [COS](https://cloud.tencent.com/document/product/436) is supported. For more information on the COS format, please see [How to enter COS and CFS Paths](https://cloud.tencent.com/document/product/599/13996).
   ![](https://mc.qcloudimg.com/static/img/b86945c2ee04dcb89d1ce9aa2a62955c/image.jpg)

6. After you confirm the task template in JSON file, click **Save** to complete the creation of the task template.
![](https://mc.qcloudimg.com/static/img/779bfc1f07af787612d2fb1db5ce70d1/image.jpg)

## Deleting a Task Template
When you no longer need a task template, you can delete it from the task template list.
![](https://mc.qcloudimg.com/static/img/9d207da685ef89b75a93818851f5050f/image.jpg)

## Modifying a Task Template
To edit an existing task template, you can click on the task template ID to enter the task template configuration page, and then edit the task template accordingly.
![](https://mc.qcloudimg.com/static/img/bab3f74591f80db4022716f897d57893/image.jpg)

