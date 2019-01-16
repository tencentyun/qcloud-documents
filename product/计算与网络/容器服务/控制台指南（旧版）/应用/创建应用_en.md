Log in to the [Tencent Cloud CCS Console](https://console.cloud.tencent.com/ccs), and click **New** on the **Application Management** -> **[Application][1]** page.

![][create]

## Application Configuration

After an application is created, go to the Application Configuration page, where you can make configurations as follows:

1. Enter application name and description.
2. Select the region and cluster to which the application needs to be deployed.

![][create2]

>**Note:**
>When you create an application, a duplicate is copied from the application template. When you update the template content in the application, the modified content cannot be synced to the original application template.

## Application Editing

After the configuration is completed, go to the application editing page where you can modify template and configurations. Click **Save** after modification is completed. For more information about operations on template content, please see [Application Template Operation Instructions][6].

![][7]

After editing, click **Finish** to complete the application creation.

## Deploying Service in the Application

After an application is created, you can view it in [Application List][9]. Click an application name to go to the application details page where you can view the status of services in the application, and deploy them.

![][10]

On the application details page, you can see the information on specific services in the application. At this point, the status of the service is **Not Deployed**. Click the **Deploy** button to deploy the service.

Now, the service has been deployed, and its status is changed from **Not Deployed** to **Deployed** on the details page. The status of the service is **Running**.

![][12]

>**Note:**
>For more information about the operations and status of services in the application, please see [Management of Service in Application][13]

## Accessing Deployed Application

After the application is deployed, it can be accessed using the open public network address in the application service. `nginx` service can be accessed via open public network load balancer IP and ports.

![][14]

  [1]: https://console.cloud.tencent.com/ccs/application
  [create]: https://mc.qcloudimg.com/static/img/193ee99a7ccaff383b87ef2491a4468c/image.png
  [3]: https://cloud.tencent.com/document/product/457/11949
  [create2]: https://mc.qcloudimg.com/static/img/9bef862af44c4b1acc3a571589ebf71f/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199
  [7]: https://mc.qcloudimg.com/static/img/68364f4d1cc623615e0ddc01b9f302ac/image.png
  [9]: https://console.cloud.tencent.com/ccs/application
  [10]: https://mc.qcloudimg.com/static/img/0bb4b714e791dc5c8ade33e2b1dea3d7/image.png
  [12]: https://mc.qcloudimg.com/static/img/189cb4d6c49b3f9605c641045894b101/image.png
  [13]: https://cloud.tencent.com/document/product/457/11989
  [14]: https://mc.qcloudimg.com/static/img/dbed8cb87251ea9d338e0dd3de2f8db5/image.png
