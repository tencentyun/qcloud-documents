## Application Creation
Log in to the [Tencent TKE Console](https://console.cloud.tencent.com/ccs). In [Application Page"][1], click **New**.

![Create Application-006.png][2]

## Basic Configurations

In the **Application Configuration** page, complete all required items.

1. Enter application name and description.

2. Select the region and cluster where you want to deploy the application.

3. Select an application template. Here we choose the template `nginxapp` created previously. For more information on how to create a template, please see [Creating Application Template][3].

4. Select the config file type. You can use the default configurations in the template or use the specific configuration item as needed. Here we choose the default configuration item in the template. For more information on how to create a configuration file, please see [Creating Configuration Item][4].

![Create Application-007.png][5]

>**Note:**
> When you create an application using a template, you're using a duplicate of the template. Modifications you make to the template are not updated to the original one.

## Custom Configurations

In the **Custom Configurations** page, you can modify template and configurations. For more information about operations on template content, please see [Application Template Operation Instructions][6].

![Create Application-008.png][7]


After editing, click **Finish** to complete the application creation.

![Create Application-009.png][8]

## Deploying Service in the Application

When an application is created, you can view the new application in [Application List][9]. Click application name to go to the application details page, where you can view the status of services in the application, and deploy them.

![Create Application-009.png][10]

In the application details page, you can view the information of specific service in the application. The status of the service is **Not Deployed**. Click **Deploy** button to deploy the service.

![Create Application-010.png][11]

Now, the service has been deployed, and its **Deployment Status** is changed from **Not Deployed** to **Deployed**. The **Service Status** becomes **Running**.

![Create Application-013.png][12]

>**Note:**
>For more information about the operations and status of services in the application, please see [Management of Service in Application][13]

## Accessing Deployed Application

After the application deployment is completed, you can access the application from the public network on which the service in the application is exposed. For the `nginx` service, you can access services through the load balancer IP and port of the exposed public network.

![Create Application-014.png][14]

  [1]: https://console.cloud.tencent.com/ccs/application
  [2]: https://mc.qcloudimg.com/static/img/199851213de9bf5c5295f1ac1f3043f0/image.png
  [3]: https://cloud.tencent.com/document/product/457/11949
  [4]: https://cloud.tencent.com/document/product/457/10173#.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6.E7.9A.84.E5.88.9B.E5.BB.BA
  [5]: https://mc.qcloudimg.com/static/img/f43beba1efb27a873bc7d996e0fc434e/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199
  [7]: https://mc.qcloudimg.com/static/img/3f2eab515f5924841ae6d6ed68c07890/image.png
  [8]: https://mc.qcloudimg.com/static/img/917a3462aab79c532dcdbb224be2e8cd/image.png
  [9]: https://console.cloud.tencent.com/ccs/application
  [10]: https://mc.qcloudimg.com/static/img/1a511542b19efa088704b7b5b799bc5b/image.png
  [11]: https://mc.qcloudimg.com/static/img/db475d88ad163b8730a4b072f2a83522/image.png
  [12]: https://mc.qcloudimg.com/static/img/be0aa85ebf756ea5ee78ca1b123a7305/image.png
  [13]: https://cloud.tencent.com/document/product/457/11989
  [14]: https://mc.qcloudimg.com/static/img/dbed8cb87251ea9d338e0dd3de2f8db5/image.png
